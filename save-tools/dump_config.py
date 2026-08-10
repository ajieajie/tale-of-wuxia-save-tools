"""抠内存配置：NpcData 角色ID + 各技能行宽上下文，保存到文件供分析。"""
import sys, ctypes

kernel32 = ctypes.windll.kernel32
PAGE_READABLE = 0x04 | 0x02 | 0x10
MEM_COMMIT = 0x1000

class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [("wProcessorArchitecture", ctypes.c_ushort),("wReserved", ctypes.c_ushort),
        ("dwPageSize", ctypes.c_ulong),("lpMinimumApplicationAddress", ctypes.c_void_p),
        ("lpMaximumApplicationAddress", ctypes.c_void_p),("dwActiveProcessorMask", ctypes.c_ulong),
        ("dwNumberOfProcessors", ctypes.c_ulong),("dwProcessorType", ctypes.c_ulong),
        ("dwAllocationGranularity", ctypes.c_ulong),("wProcessorLevel", ctypes.c_ushort),
        ("wProcessorRevision", ctypes.c_ushort)]
class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [("BaseAddress", ctypes.c_void_p),("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", ctypes.c_ulong),("RegionSize", ctypes.c_size_t),
        ("State", ctypes.c_ulong),("Protect", ctypes.c_ulong),("Type", ctypes.c_ulong)]

def scan(pid, kws, ctx=700, out=None):
    h = kernel32.OpenProcess(0x0410, False, pid)
    si = SYSTEM_INFO(); kernel32.GetSystemInfo(ctypes.byref(si))
    start=int(si.lpMinimumApplicationAddress); end=int(si.lpMaximumApplicationAddress)
    mbi=MEMORY_BASIC_INFORMATION(); addr=start
    pats={k:k.encode("utf-8") for k in kws}
    lines=[]
    while addr<end:
        if not kernel32.VirtualQueryEx(h, ctypes.c_void_p(addr), ctypes.byref(mbi), ctypes.sizeof(mbi)):
            addr+=si.dwPageSize; continue
        size=int(mbi.RegionSize)
        if mbi.State==MEM_COMMIT and (mbi.Protect&PAGE_READABLE) and 0<size<200*1024*1024:
            buf=ctypes.create_string_buffer(size); nr=ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(h, ctypes.c_void_p(addr), buf, size, ctypes.byref(nr)):
                data=buf.raw[:nr.value]
                for k in kws:
                    p=pats[k]; idx=0
                    while True:
                        i=data.find(p,idx)
                        if i==-1: break
                        seg=data[max(0,i-ctx):i+ctx]
                        lines.append("==== %s @%s ====\n%s"%(k,hex(addr+i),seg.decode('utf-8','ignore').replace('\r',' ').replace('\n',' ')))
                        idx=i+1
        addr+=size
    if out:
        open(out,"w",encoding="utf-8").write("\n".join(lines))
    return lines

if __name__=="__main__":
    pid=int(sys.argv[1])
    # character names + skill ids of interest
    kws=["谷月轩","荆棘","210002","200017","100010","140087","60036","70069","910067","121034","121043"]
    scan(pid, kws, ctx=600, out="dump_config.txt")
    print("written dump_config.txt lines:", len(open("dump_config.txt",encoding="utf-8").read().splitlines()))
