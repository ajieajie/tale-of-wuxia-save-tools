import ctypes
kernel32=ctypes.windll.kernel32
PAGE_READABLE=0x04|0x02|0x10; MEM_COMMIT=0x1000
class SI(ctypes.Structure):
    _fields_=[('a',ctypes.c_ushort),('b',ctypes.c_ushort),('ps',ctypes.c_ulong),('min',ctypes.c_void_p),('max',ctypes.c_void_p),('m',ctypes.c_ulong),('n',ctypes.c_ulong),('t',ctypes.c_ulong),('ag',ctypes.c_ulong),('l',ctypes.c_ushort),('r',ctypes.c_ushort)]
class MBI(ctypes.Structure):
    _fields_=[('ba',ctypes.c_void_p),('ab',ctypes.c_void_p),('ap',ctypes.c_ulong),('rs',ctypes.c_size_t),('st',ctypes.c_ulong),('pr',ctypes.c_ulong),('ty',ctypes.c_ulong)]
h=kernel32.OpenProcess(0x0410,False,38528)
si=SI(); kernel32.GetSystemInfo(ctypes.byref(si))
addr=int(si.min); end=int(si.max); ps=si.ps; mbi=MBI()
targets=[b'\t70069\t',b'\t60036\t']
for t in targets:
    cnt=0; a=addr
    while a<end and cnt<3:
        if not kernel32.VirtualQueryEx(h,ctypes.c_void_p(a),ctypes.byref(mbi),ctypes.sizeof(mbi)):
            a+=ps; continue
        sz=int(mbi.rs)
        if mbi.st==MEM_COMMIT and (mbi.pr&PAGE_READABLE) and 0<sz<200*1024*1024:
            buf=ctypes.create_string_buffer(sz); nr=ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h,ctypes.c_void_p(a),buf,sz,ctypes.byref(nr)):
                d=buf.raw[:nr.value]
                i=0
                while True:
                    i=d.find(t,i)
                    if i==-1: break
                    s=d.rfind(b' ',0,i); e=d.find(b' ',i)
                    if s==-1: s=max(0,i-120)
                    if e==-1: e=min(len(d),i+300)
                    row=d[s+1:e].decode('utf-8','ignore')
                    f=row.split('\t')
                    # find which field equals skill
                    sk=t.decode().strip()
                    idxs=[k for k,v in enumerate(f) if v==sk]
                    print(t.decode(),'match: f0=',f[0] if f else '?','f2=',f[2] if len(f)>2 else '?','skill_idx=',idxs,'len=',len(f))
                    print('   head:',row[:200])
                    cnt+=1
                    if cnt>=3: break
                    i+=1
        a+=sz
print('done')
