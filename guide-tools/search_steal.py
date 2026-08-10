import re

# Search for steal-related strings in the main game DLL
with open('F:/SteamLibrary/steamapps/common/Tale of WuxiaThe Pre-Sequel/YoungHero_Data/Managed/Assembly-CSharp.dll', 'rb') as f:
    data = f.read()

# Search for steal-related keywords
keywords = [
    b'Steal', b'steal', b'StealRate', b'stealRate', b'StealSuccess',
    b'TouQie', b'touqie', b'Tou', b'Qie', b'PickPocket', b'pickpocket',
    b'Snatch', b'snatch', b'Rob', b'rob', b'StealItem', b'stealItem',
    '偷'.encode('utf-8'), '窃'.encode('utf-8'), b'StealProbability', b'StealChance'
]

for kw in keywords:
    positions = [m.start() for m in re.finditer(re.escape(kw), data)]
    if positions:
        print(f'\n=== "{kw.decode('utf-8', errors='replace')}" found {len(positions)} times ===')
        for pos in positions[:8]:
            context = data[max(0, pos-30):pos+50]
            printable = ''.join(chr(b) if 32 <= b < 127 else '.' for b in context)
            print(f'  offset {pos}: ...{printable}...')
