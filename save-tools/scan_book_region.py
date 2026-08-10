"""在包含锚点 121034 的内存区里，深挖 内功/武功 秘籍行结构。
1) 打印所有 type==6 行中 field[14] 属于"武功段"(1xxxxx/14xxxx) 的样本
2) 搜索含 '水浒'/'林冲'/'策马' 的行
3) 把命中 100010 / 140087 出现过的行(任意字段)也打印
"""
import sys, re, ctypes

kernel32 = ctypes.windll.kernel32
PAGE_READABLE = 0x04 | 0x02 | 0x10
MEM_COMMIT = 0x1000

class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [
        ("wProcessorArchitecture", ctypes.c_ushort),("wReserved", ctypes.c_ushort),
        ("dwPageSize", ctypes.c_ulong),("lpMinimumApplicationAddress", ctypes.c_void_p),
        ("lpMaximumApplicationAddress", ctypes.c_void_p),("dwActiveProcessorMask", ctypes.c_ulong),
        ("dwNumberOfProcessors", ctypes.c_ulong),("dwProcessorType", ctypes.c_ulong),
        ("dwAllocationGranularity", ctypes.c_ulong),("wProcessorLevel", ctypes.c_ushort),
        ("wProcessorRevision", ctypes.c_ushort),
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
    si = SYSTEM_INFO(); kernel32.GetSystemInfo(ctypes.byref(si))
    start = int(si.lpMinimumApplicationAddress); end = int(si.lpMaximumApplicationAddress); ps = si.dwPageSize
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

    lines = re.split(b'\r\n|\n', full)
    # 1) type-6 行中 field[14] 属武功段的样本
    print("=== sample type-6 rows with field[14] in 武功段 (1xxxxx/14xxxx) ===")
    cnt = 0
    for line in lines:
        f = line.split(b'\t')
        if len(f) > 14 and f[2] == b'6':
            sk = f[14].decode('utf-8','ignore')
            if sk.startswith('1') or sk.startswith('14'):
                print(" book=", f[0].decode('utf-8','ignore'), "name=", f[1].decode('utf-8','ignore'), "skill=", sk)
                cnt += 1
                if cnt >= 30: break
    print("count(武功段秘籍样本上限30):", cnt)

    # 2) 搜含中文名的行
    print("\n=== lines containing 水浒/林冲/策马 ===")
    for line in lines:
        try:
            t = line.decode('utf-8')
        except:
            continue
        if '水浒' in t or '林冲' in t or '策马' in t:
            f = line.split(b'\t')
            print(" F[0]=", f[0].decode('utf-8','ignore'), "F[1]=", f[1].decode('utf-8','ignore'),
                  "F[2]=", f[2].decode('utf-8','ignore'), "F[14]=", f[14].decode('utf-8','ignore') if len(f)>14 else 'NA')
            print("   raw:", t[:200])

    # 3) 命中 100010/140087 出现过的整行(任意字段)
    print("\n=== lines containing 100010 or 140087 (any field) within region ===")
    for line in lines:
        if b'100010' in line or b'140087' in line:
            f = line.split(b'\t')
            print(" F[0]=", f[0].decode('utf-8','ignore'), "F[1]=", f[1].decode('utf-8','ignore'),
                  "F[2]=", f[2].decode('utf-8','ignore'))
            print("   raw:", line.decode('utf-8','ignore')[:220])

if __name__ == "__main__":
    main()
