"""全内存确认：是否存在教 100010/140087 的 type-6 秘籍，或 140087 的 type-4 物品。"""
import sys, re, ctypes

kernel32 = ctypes.windll.kernel32
PAGE_READABLE = 0x04 | 0x02 | 0x10
MEM_COMMIT = 0x1000

class SI(ctypes.Structure):
    _fields_ = [("w",ctypes.c_ushort),("w2",ctypes.c_ushort),("ps",ctypes.c_ulong),
        ("min",ctypes.c_void_p),("max",ctypes.c_void_p),("m",ctypes.c_ulong),
        ("n",ctypes.c_ulong),("t",ctypes.c_ulong),("ag",ctypes.c_ulong),
        ("l",ctypes.c_ushort),("r",ctypes.c_ushort)]
class MBI(ctypes.Structure):
    _fields_ = [("BaseAddress",ctypes.c_void_p),("AllocationBase",ctypes.c_void_p),
        ("AllocationProtect",ctypes.c_ulong),("RegionSize",ctypes.c_size_t),
        ("State",ctypes.c_ulong),("Protect",ctypes.c_ulong),("Type",ctypes.c_ulong)]

def main():
    pid = int(sys.argv[1]) if len(sys.argv)>1 else 38528
    h = kernel32.OpenProcess(0x0410, False, pid)
    si = SI(); kernel32.GetSystemInfo(ctypes.byref(si))
    start=int(si.min); end=int(si.max); ps=si.ps
    mbi=MBI(); addr=start
    hits6=[]   # type-6 秘籍 teaching 100010/140087
    hits_item=[]  # F[0] in {100010,140087} and F[2] in {4,6}
    scanned=0
    while addr<end:
        if not kernel32.VirtualQueryEx(h,ctypes.c_void_p(addr),ctypes.byref(mbi),ctypes.sizeof(mbi)):
            addr+=ps; continue
        sz=int(mbi.RegionSize)
        if mbi.State==MEM_COMMIT and (mbi.Protect&PAGE_READABLE) and 0<sz<200*1024*1024:
            buf=ctypes.create_string_buffer(sz); nr=ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h,ctypes.c_void_p(addr),buf,sz,ctypes.byref(nr)):
                data=buf.raw[:nr.value]
                for line in re.split(b'\r\n|\n', data):
                    f=line.split(b'\t')
                    if len(f)<3: continue
                    if f[2]==b'6' and len(f)>14 and f[14] in (b'100010',b'140087'):
                        hits6.append((hex(addr), f[0].decode(), f[1].decode(), f[14].decode()))
                    if f[0] in (b'100010',b'140087') and f[2] in (b'4',b'6'):
                        hits_item.append((hex(addr), f[0].decode(), f[2].decode(), len(f)))
        addr+=sz
        scanned+=1
    print("scanned regions", scanned)
    print("type-6 秘籍 teaching 100010/140087:", len(hits6))
    for x in hits6[:10]: print("  ", x)
    print("ItemData rows F[0] in {100010,140087} & type 4/6:", len(hits_item))
    for x in hits_item[:10]: print("  ", x)

if __name__=="__main__":
    main()
