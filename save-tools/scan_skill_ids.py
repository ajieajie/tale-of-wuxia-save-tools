"""全内存扫描 100010 / 140087 的所有出现，dump 上下文，判断其 book 行格式。"""
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
    pid = int(sys.argv[1]) if len(sys.argv) > 1 else 38528
    targets = [b'100010', b'140087']
    h = kernel32.OpenProcess(0x0410, False, pid)
    si = SYSTEM_INFO()
    kernel32.GetSystemInfo(ctypes.byref(si))
    start = int(si.lpMinimumApplicationAddress)
    end = int(si.lpMaximumApplicationAddress)
    pagesize = si.dwPageSize
    mbi = MEMORY_BASIC_INFORMATION()
    addr = start
    per_t = {t: [] for t in targets}
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
                for t in targets:
                    idx = 0
                    while True:
                        i = data.find(t, idx)
                        if i == -1: break
                        ctx = data[max(0, i-200): i+600]
                        per_t[t].append((addr + i, ctx))
                        idx = i + 1
                        if len(per_t[t]) > 15: break
        addr += size
    for t in targets:
        print("="*70)
        print("TARGET", t.decode(), "hits:", len(per_t[t]))
        for off, ctx in per_t[t][:4]:
            print("  @", hex(off))
            print("   ", ctx.decode('utf-8', 'ignore')[:400].replace("\r", " ").replace("\n", " "))

if __name__ == "__main__":
    main()
