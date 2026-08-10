"""扫描游戏进程内存，定位 ItemData 明文，提取 skill->book(秘籍) 映射。
找 ItemData 行中 field[2]=='6'(秘籍类型) 且 field[14]==技能ID 的物品ID(field[0])。
"""
import sys, re, ctypes

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
    anchor = b'121034\t'
    h = kernel32.OpenProcess(0x0410, False, pid)
    if not h:
        print("OpenProcess failed", kernel32.GetLastError()); return
    si = SYSTEM_INFO()
    kernel32.GetSystemInfo(ctypes.byref(si))
    start = int(si.lpMinimumApplicationAddress)
    end = int(si.lpMaximumApplicationAddress)
    pagesize = si.dwPageSize
    mbi = MEMORY_BASIC_INFORMATION()
    addr = start
    full = None
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
                if anchor in data:
                    print("FOUND anchor in region base", hex(addr), "size", size)
                    full = data
                    break
        addr += size
        scanned += 1
    if full is None:
        print("anchor not found"); return

    targets = {'70069', '60036', '100010', '140087', '60074'}
    found = {}
    nbook = 0
    nlines = 0
    lines = re.split(b'\r\n|\n', full)
    for line in lines:
        nlines += 1
        f = line.split(b'\t')
        if len(f) > 14 and f[2] == b'6':
            nbook += 1
            sk = f[14].decode('utf-8', 'ignore')
            if sk in targets:
                found[sk] = (f[0].decode(), f[1].decode())
    print("lines", nlines, "books(f2==6)", nbook)
    for sk in ['70069', '60036', '100010', '140087', '60074']:
        if sk in found:
            print("SKILL", sk, "-> BOOK", found[sk][0], found[sk][1])
        else:
            print("SKILL", sk, "-> not in region")

if __name__ == "__main__":
    main()
