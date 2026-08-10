"""只 dump ItemData 行(F[2] in 4/6) 中 F[0] 命中目标的，存文件。"""
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
    anchor = b'121034\t'
    h = kernel32.OpenProcess(0x0410, False, pid)
    si = SI(); kernel32.GetSystemInfo(ctypes.byref(si))
    start=int(si.min); end=int(si.max); ps=si.ps
    mbi=MBI(); addr=start; full=None
    while addr<end:
        if not kernel32.VirtualQueryEx(h,ctypes.c_void_p(addr),ctypes.byref(mbi),ctypes.sizeof(mbi)):
            addr+=ps; continue
        sz=int(mbi.RegionSize)
        if mbi.State==MEM_COMMIT and (mbi.Protect&PAGE_READABLE) and 0<sz<200*1024*1024:
            buf=ctypes.create_string_buffer(sz); nr=ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h,ctypes.c_void_p(addr),buf,sz,ctypes.byref(nr)):
                d=buf.raw[:nr.value]
                if anchor in d: full=d; break
        addr+=sz
    if full is None:
        print("anchor not found"); return
    want={b'100010',b'140087',b'121010',b'121034',b'120004'}
    out=[]
    for line in re.split(b'\r\n|\n', full):
        f=line.split(b'\t')
        if f and f[0] in want and len(f)>2 and f[2] in (b'4',b'6'):
            out.append("ROW F[0]=%s type=%s fields=%d" % (f[0].decode(), f[2].decode(), len(f)))
            for i,v in enumerate(f):
                out.append("  [%d]= %s" % (i, v.decode('utf-8','ignore')))
            out.append("")
    open("dump_items_out.txt","w",encoding="utf-8").write("\n".join(out))
    print("written", len(out), "lines")

if __name__=="__main__":
    main()
