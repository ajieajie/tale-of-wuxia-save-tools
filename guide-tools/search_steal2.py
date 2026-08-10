import re

# Read the DLL
with open('F:/SteamLibrary/steamapps/common/Tale of WuxiaThe Pre-Sequel/YoungHero_Data/Managed/Assembly-CSharp.dll', 'rb') as f:
    data = f.read()

# Search for broader steal-related terms
keywords = [
    b'MiaoShou', b'miaoshou', b'Pick', b'pick', b'Grab', b'grab',
    b'Loot', b'loot', b'Snatch', b'snatch', b'Swift', b'swift',
    b'Qinggong', b'qinggong', b'QingGong', b'Thief', b'thief',
    b'Bandit', b'bandit', b'Pilfer', b'pilfer',
    b'ItemRate', b'itemRate', b'DropRate', b'dropRate',
    b'GetItem', b'getItem', b'TakeItem', b'takeItem',
    b'SuccessRate', b'successRate', b'Success', b'success',
    b'Probability', b'probability', b'Chance', b'chance',
    b'Random', b'random', b'Rate', b'rate',
    b'Miao', b'miao', b'Kong', b'kong',
]

found = set()
for kw in keywords:
    positions = [m.start() for m in re.finditer(re.escape(kw), data)]
    if positions:
        for pos in positions[:3]:
            context = data[max(0, pos-20):pos+60]
            printable = ''.join(chr(b) if 32 <= b < 127 else '.' for b in context)
            key = f'{kw.decode()}: {printable}'
            if key not in found:
                found.add(key)
                print(f'[{kw.decode()}] offset {pos}: ...{printable}...')

# Also search for Chinese terms related to stealing
cn_keywords = ['妙手空空', '偷窃', '偷取', '窃取', '摸尸', '搜身', '顺手牵羊', '空空妙手']
for kw in cn_keywords:
    encoded = kw.encode('utf-8')
    positions = [m.start() for m in re.finditer(re.escape(encoded), data)]
    if positions:
        print(f'\n=== "{kw}" found {len(positions)} times ===')
        for pos in positions[:5]:
            context = data[max(0, pos-20):pos+60]
            printable = ''.join(chr(b) if 32 <= b < 127 else '.' for b in context)
            print(f'  offset {pos}: ...{printable}...')
