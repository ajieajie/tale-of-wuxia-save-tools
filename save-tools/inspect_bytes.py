import ctypes, sys
kernel32=ctypes.windll.kernel32
PAGE_READABLE=0x04|0x02|0x10; MEM_COMMIT=0x1000
class SI(ctypes.Structure):
    _fields_=[('a',ctypes.c_ushort),('b',ctypes.c_ushort),('ps',ctypes.c_ulong),('min',ctypes.c_void_p),('max',ctypes.c_void_p),('m',ctypes.c_ulong),('n',ctypes.c_ulong),('t',ctypes.c_ulong),('ag',ctypes.c_ulong),('l',ctypes.c_ushort),('r',ctypes.c_ushort)]
class MBI(ctypes.Structure):
    _fields_=[('ba',ctypes.c_void_p),('ab',ctypes.c_void_p),('ap',ctypes.c_ulong),('rs',ctypes.c_size_t),('st',ctypes.c_ulong),('pr',ctypes.c_ulong),('ty',ctypes.c_ulong)]
h=kernel32.OpenProcess(0x0410,False,38528)
si=SI(); kernel32.GetSystemInfo(ctypes.byref(si))
addr=int(si.min); end=int(si.max); ps=si.ps; mbi=MBI()
# targets as utf-8 bytes
targets=[s.encode('utf-8') for s in ['血刀经','正气','水浒英雄掌','林冲策马鞭']]
found=0
a=addr
while a<end and found<8:
    if not kernel32.VirtualQueryEx(h,ctypes.c_void_p(a),ctypes.byref(mbi),ctypes.sizeof(mbi)):
        a+=ps; continue
    sz=int(mbi.rs)
    if mbi.st==MEM_COMMIT and (mbi.pr&PAGE_READABLE) and 0<sz<200*1024*1024:
        buf=ctypes.create_string_buffer(sz); nr=ctypes.c_size_t(0)
        if kernel32.ReadProcessMemory(h,ctypes.c_void_p(a),buf,sz,ctypes.byref(nr)):
            d=buf.raw[:nr.value]
            for t in targets:
                i=d.find(t)
                if i!=-1:
                    print('###',t.decode('utf-8'),'@',hex(a+i))
                    print('  hex before(50):',d[max(0,i-50):i].hex())
                    print('  ascii before  :',repr(d[max(0,i-50):i].decode('latin1','ignore')))
                    print('  after(24)     :',d[i:i+24].hex(),'->',repr(d[i:i+24].decode('utf-8','ignore')))
                    found+=1
                    if found>=8: break
    a+=sz
print('done, found',found)
