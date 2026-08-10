"""精确 dump 指定物品ID的 ItemData 行，带字段索引，看清结构。"""
import sys, re, ctypes

kernel32 = ctypes.windll.kernel32
PAGE_READABLE = 0x04 | 0x02 | 0x10
MEM_COMMIT = 0x1000

class SI(ctypes.Structure):
    _fields_ = [
        ("w", ctypes.c_ushort),("w2", ctypes.c_ushort),("ps", ctypes.c_ulong),
        ("min", ctypes.c_void_p),("max", ctypes.c_void_p),("m", ctypes.c_ulong),
        ("n", ctypes.c_ulong),("t", ctypes.c_ulong),("ag", ctypes.c_ulong),
        ("l", ctypes.c_ushort),("r", ctypes.c_ushort),
    ]
class MBI(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_void_p),("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", ctypes.c_ulong),("RegionSize", ctypes.c_size_t),
        ("State", ctypes.c_ulong),("Protect", ctypes.c_ulong),("Type", ctypes.c_ulong),
    ]

def main():
    pid = int(sys.argv[1]) if len(sys.argv) > 1 else 38528
    anchor = b'121034\t'
    h = kernel32.OpenProcess(0x0410, False, pid)
    si = SI(); kernel32.GetSystemInfo(ctypes.byref(si))
    start = int(si.min); end = int(si.max); ps = si.ps
    mbi = MBI(); addr = start; full = None
    while addr < end:
        if not kernel32.VirtualQueryEx(h, ctypes.c_void_p(addr), ctypes.byref(mbi), ctypes.sizeof(mbi)):
            addr += ps; continue
        sz = int(mbi.RegionSize)
        if mbi.State == MEM_COMMIT and (mbi.Protect & PAGE_READABLE) and 0 < sz < 200*1024*1024:
            buf = ctypes.create_string_buffer(sz); nr = ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h, ctypes.c_void_p(addr), buf, sz, ctypes.byref(nr)):
                d = buf.raw[:nr.value]
                if anchor in d:
                    full = d; break
        addr += sz
    if full is None:
        print("anchor not found"); return

    want = {b'100010', b'140087', b'121010', b'121034', b'120004'}
    lines = re.split(b'\r\n|\n', full)
    for line in lines:
        f = line.split(b'\t')
        if f and f[0] in want:
            print("="*72)
            print("ROW F[0]=", f[0].decode('utf-8','ignore'), " FIELDCOUNT=", len(f))
            for i, v in enumerate(f):
                print("  [%d]= %s" % (i, v.decode('utf-8','ignore')))

if __name__ == "__main__":
    main()
