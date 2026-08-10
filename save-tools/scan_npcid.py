import ctypes, sys

pid = int(sys.argv[1]) if len(sys.argv) > 1 else 38552
names = ['荆棘', '龙墨', '谷月轩']
targets = []
for n in names:
    for enc in (n.encode('utf-16-le'), n.encode('utf-8')):
        targets.append((n, enc))

kernel32 = ctypes.windll.kernel32
PROCESS_VM_READ = 0x10
PROCESS_QUERY_INFORMATION = 0x400
h = kernel32.OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, False, pid)
if not h:
    print('OpenProcess failed', ctypes.GetLastError())
    sys.exit(1)

class MBI(ctypes.Structure):
    _fields_ = [('BaseAddress', ctypes.c_void_p), ('AllocationBase', ctypes.c_void_p),
                ('AllocationProtect', ctypes.c_ulong), ('RegionSize', ctypes.c_size_t),
                ('State', ctypes.c_ulong), ('Protect', ctypes.c_ulong), ('Type', ctypes.c_ulong)]

mbi = MBI()
MAX_ADDR = 0xFFFFFFFF
addr = 0
hits = {n: [] for n in names}
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
                for n, t in targets:
                    pos = 0
                    while True:
                        idx = b.find(t, pos)
                        if idx == -1:
                            break
                        pos = idx + len(t)
                        start = max(0, idx - 80)
                        end = min(len(b), idx + len(t) + 80)
                        ctx = b[start:end]
                        asc = ''.join(chr(c) if 32 <= c < 127 else '.' for c in ctx)
                        hits[n].append((base + off + idx, asc))
            off += chunk
    addr = base + size

for n in names:
    print('==== %s : %d hits ====' % (n, len(hits[n])))
    for a, asc in hits[n][:10]:
        print('  @', hex(a), '|', asc)
print('DONE')
