import ctypes, sys, re

pid = int(sys.argv[1]) if len(sys.argv) > 1 else 38552
ids = ['210001', '210002', '200000', '200022', '100037', '200017', '200038', '200020']
targets = [(i, i.encode('utf-16-le')) for i in ids]
CJK = re.compile(r'[\u4e00-\u9fff]+')

kernel32 = ctypes.windll.kernel32
h = kernel32.OpenProcess(0x10 | 0x400, False, pid)
if not h:
    print('OpenProcess failed', ctypes.GetLastError()); sys.exit(1)

class MBI(ctypes.Structure):
    _fields_ = [('BaseAddress', ctypes.c_void_p), ('AllocationBase', ctypes.c_void_p),
                ('AllocationProtect', ctypes.c_ulong), ('RegionSize', ctypes.c_size_t),
                ('State', ctypes.c_ulong), ('Protect', ctypes.c_ulong), ('Type', ctypes.c_ulong)]

mbi = MBI()
MAX_ADDR = 0xFFFFFFFF
addr = 0
while addr < MAX_ADDR:
    if kernel32.VirtualQueryEx(h, ctypes.c_void_p(addr), ctypes.byref(mbi), ctypes.sizeof(mbi)) == 0:
        break
    base = ctypes.cast(mbi.BaseAddress, ctypes.c_void_p).value
    if base is None:
        addr += 0x1000
        continue
    size = mbi.RegionSize
    if mbi.State == 0x1000 and (mbi.Protect & (0x02 | 0x04 | 0x20 | 0x40)):
        off = 0
        while off < size:
            chunk = min(0x200000, size - off)
            data = ctypes.create_string_buffer(chunk)
            rd = ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h, ctypes.c_void_p(base + off), data, chunk, ctypes.byref(rd)):
                b = data.raw[:rd.value]
                for i, t in targets:
                    pos = 0
                    while True:
                        idx = b.find(t, pos)
                        if idx == -1:
                            break
                        pos = idx + len(t)
                        ctx = b[max(0, idx - 40): idx + 120]
                        # decode as utf-16le, find CJK runs
                        try:
                            s = ctx.decode('utf-16-le', errors='ignore')
                        except Exception:
                            s = ''
                        cjk = CJK.findall(s)
                        if cjk:
                            print('ID %s @%s -> near: %s' % (i, hex(base + off + idx), ' '.join(cjk)[:60]))
            off += chunk
    addr = base + size
print('DONE')
