"""扫描游戏进程内存，定位 NpcData / SkillData 配置表的 UTF-16LE 明文条目。
用法: scan_mem_config.py <PID> [keywords...]
"""
import sys, ctypes, re

kernel32 = ctypes.windll.kernel32

PAGE_READABLE = 0x04 | 0x02 | 0x10  # READONLY | READWRITE | COPYONWRITE
MEM_COMMIT = 0x1000

def read_memory(pid, keywords):
    PROCESS_VM_READ = 0x0010
    PROCESS_QUERY_INFORMATION = 0x0400
    h = kernel32.OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, False, pid)
    if not h:
        print("OpenProcess failed, pid", pid, "err", kernel32.GetLastError())
        return

    SYSINFO = ctypes.create_string_buffer(48)
    kernel32.GetSystemInfo(SYSINFO)
    # SYSTEM_INFO: dwPageSize at offset 4 (after 4-byte union + 2x4 pointer on 32-bit)
    # Use ctypes properly
    class SYSTEM_INFO(ctypes.Structure):
        _fields_ = [
            ("wProcessorArchitecture", ctypes.c_ushort),
            ("wReserved", ctypes.c_ushort),
            ("dwPageSize", ctypes.c_ulong),
            ("lpMinimumApplicationAddress", ctypes.c_void_p),
            ("lpMaximumApplicationAddress", ctypes.c_void_p),
            ("dwActiveProcessorMask", ctypes.c_ulong),
            ("dwNumberOfProcessors", ctypes.c_ulong),
            ("dwProcessorType", ctypes.c_ulong),
            ("dwAllocationGranularity", ctypes.c_ulong),
            ("wProcessorLevel", ctypes.c_ushort),
            ("wProcessorRevision", ctypes.c_ushort),
        ]
    si = SYSTEM_INFO()
    kernel32.GetSystemInfo(ctypes.byref(si))
    start = int(si.lpMinimumApplicationAddress)
    end = int(si.lpMaximumApplicationAddress)
    pagesize = si.dwPageSize
    print("mem range", hex(start), "-", hex(end), "pagesize", pagesize)

    class MEMORY_BASIC_INFORMATION(ctypes.Structure):
        _fields_ = [
            ("BaseAddress", ctypes.c_void_p),
            ("AllocationBase", ctypes.c_void_p),
            ("AllocationProtect", ctypes.c_ulong),
            ("RegionSize", ctypes.c_size_t),
            ("State", ctypes.c_ulong),
            ("Protect", ctypes.c_ulong),
            ("Type", ctypes.c_ulong),
        ]

    mbi = MEMORY_BASIC_INFORMATION()
    addr = start
    hits = {k: [] for k in keywords}
    # precompute UTF-16LE byte patterns
    pats = {k: k.encode("utf-16-le") for k in keywords}
    scanned = 0
    while addr < end:
        ret = kernel32.VirtualQueryEx(h, ctypes.c_void_p(addr), ctypes.byref(mbi), ctypes.sizeof(mbi))
        if not ret:
            addr = addr + pagesize
            continue
        size = int(mbi.RegionSize)
        if mbi.State == MEM_COMMIT and (mbi.Protect & PAGE_READABLE) and 0 < size < 100 * 1024 * 1024:
            buf = ctypes.create_string_buffer(size)
            nread = ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h, ctypes.c_void_p(addr), buf, size, ctypes.byref(nread)):
                data = buf.raw[:nread.value]
                for k in keywords:
                    p = pats[k]
                    idx = 0
                    while True:
                        i = data.find(p, idx)
                        if i == -1:
                            break
                        ctx = data[max(0, i-200): i+400]
                        hits[k].append((addr + i, ctx))
                        idx = i + 1
                        if len(hits[k]) > 30:
                            break
        addr = addr + size
        scanned += 1
        if scanned % 2000 == 0:
            print("scanned regions", scanned, "addr", hex(addr))

    for k in keywords:
        print("="*70)
        print("KEYWORD", k, "hits:", len(hits[k]))
        for off, ctx in hits[k][:4]:
            # try decode as utf-16-le for readable context
            try:
                t16 = ctx.decode("utf-16-le", "ignore")
            except Exception:
                t16 = ""
            # find printable ascii
            t8 = "".join(chr(c) if 32 <= c < 127 else "." for c in ctx)
            print("  @", hex(off))
            print("   ascii:", t8[:200])
            print("   utf16:", t16[:120])
    return hits

if __name__ == "__main__":
    pid = int(sys.argv[1])
    kws = sys.argv[2:] or ["荆棘", "谷月轩", "龙墨", "血刀经", "林冲策马鞭", "水浒英雄掌", "正气决"]
    read_memory(pid, kws)
