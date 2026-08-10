"""扫描游戏进程内存，定位配置表 UTF-8 明文（NpcData/SkillData/ItemData）。"""
import sys, ctypes

kernel32 = ctypes.windll.kernel32
PAGE_READABLE = 0x04 | 0x02 | 0x10
MEM_COMMIT = 0x1000

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

def main():
    pid = int(sys.argv[1])
    kws = sys.argv[2:]
    PROCESS_VM_READ = 0x0010
    PROCESS_QUERY_INFORMATION = 0x0400
    h = kernel32.OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, False, pid)
    if not h:
        print("OpenProcess failed", kernel32.GetLastError()); return
    si = SYSTEM_INFO()
    kernel32.GetSystemInfo(ctypes.byref(si))
    start = int(si.lpMinimumApplicationAddress)
    end = int(si.lpMaximumApplicationAddress)
    pagesize = si.dwPageSize
    print("mem range", hex(start), "-", hex(end))
    mbi = MEMORY_BASIC_INFORMATION()
    addr = start
    hits = {k: [] for k in kws}
    pats = {k: k.encode("utf-8") for k in kws}
    scanned = 0
    while addr < end:
        ret = kernel32.VirtualQueryEx(h, ctypes.c_void_p(addr), ctypes.byref(mbi), ctypes.sizeof(mbi))
        if not ret:
            addr += pagesize; continue
        size = int(mbi.RegionSize)
        if mbi.State == MEM_COMMIT and (mbi.Protect & PAGE_READABLE) and 0 < size < 200 * 1024 * 1024:
            buf = ctypes.create_string_buffer(size)
            nread = ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h, ctypes.c_void_p(addr), buf, size, ctypes.byref(nread)):
                data = buf.raw[:nread.value]
                for k in kws:
                    p = pats[k]
                    idx = 0
                    while True:
                        i = data.find(p, idx)
                        if i == -1: break
                        ctx = data[max(0, i-150): i+450]
                        hits[k].append((addr + i, ctx))
                        idx = i + 1
                        if len(hits[k]) > 20: break
        addr += size
        scanned += 1
        if scanned % 4000 == 0:
            print("scanned", scanned, hex(addr))
    for k in kws:
        print("="*70)
        print("KEYWORD", k, "hits:", len(hits[k]))
        for off, ctx in hits[k][:3]:
            t = ctx.decode("utf-8", "ignore")
            print("  @", hex(off))
            print("   ", t[:300].replace("\r"," ").replace("\n"," "))

if __name__ == "__main__":
    main()
