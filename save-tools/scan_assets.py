import sys

base = r'F:/SteamLibrary/steamapps/common/Tale of WuxiaThe Pre-Sequel/YoungHero_Data'
files = [
    base + '/resources.assets',
    base + '/sharedassets0.assets',
    base + '/sharedassets1.assets',
]

keywords = ['血刀经', '正气诀', '林冲策马鞭', '水浒英雄掌',
            'NpcData', 'NeigongData', 'SkillData', 'BookData', 'ItemData', 'MartialData']

# build byte patterns
pats = []
for k in keywords:
    pats.append((k, k.encode('utf-8')))
    pats.append((k + '(u16)', k.encode('utf-16-le')))

CHUNK = 20 * 1024 * 1024
OVERLAP = 400

for f in files:
    print('########## FILE', f)
    try:
        fh = open(f, 'rb')
    except Exception as e:
        print('  open fail', e)
        continue
    prev = b''
    offset = 0
    total_hits = 0
    while True:
        block = fh.read(CHUNK)
        if not block:
            break
        buf = prev + block
        for name, pat in pats:
            pos = 0
            while True:
                idx = buf.find(pat, pos)
                if idx == -1:
                    break
                pos = idx + len(pat)
                start = max(0, idx - 200)
                end = min(len(buf), idx + len(pat) + 200)
                ctx = buf[start:end]
                asc = ''.join(chr(c) if 32 <= c < 127 else '.' for c in ctx)
                print('  [%s] @%d' % (name, offset - len(prev) + idx))
                print('     ', asc)
                total_hits += 1
                if total_hits > 120:
                    fh.close()
                    print('LIMIT REACHED')
                    sys.exit(0)
        prev = buf[-OVERLAP:]
        offset += len(block)
    fh.close()
print('DONE')
