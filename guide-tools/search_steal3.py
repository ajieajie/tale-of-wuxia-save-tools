import re

# Read both DLLs
for dll_name in ['Assembly-CSharp.dll', 'Assembly-CSharp-firstpass.dll']:
    path = f'F:/SteamLibrary/steamapps/common/Tale of WuxiaThe Pre-Sequel/YoungHero_Data/Managed/{dll_name}'
    with open(path, 'rb') as f:
        data = f.read()
    
    print(f'\n{"="*60}')
    print(f'DLL: {dll_name} ({len(data)} bytes)')
    print(f'{"="*60}')
    
    # Extract all ASCII strings of length >= 4
    strings = re.findall(b'[\x20-\x7e]{4,}', data)
    
    # Filter for potentially interesting strings
    steal_related = []
    for s in strings:
        s_decoded = s.decode('ascii', errors='ignore').lower()
        if any(kw in s_decoded for kw in ['steal', 'thief', 'rob', 'pick', 'loot', 'snatch', 'pilfer', 'swipe', 'grab', 'miao', 'kong', 'empty', 'hand', 'qiang', 'tou', 'qie', 'shou']):
            steal_related.append(s.decode('ascii', errors='ignore'))
    
    if steal_related:
        print(f'Found {len(steal_related)} potentially steal-related strings:')
        for s in sorted(set(steal_related))[:30]:
            print(f'  {s}')
    else:
        print('No steal-related strings found')
    
    # Also look for method/class names containing "Item" or "Battle" 
    item_strings = [s.decode('ascii', errors='ignore') for s in strings 
                    if any(kw in s.decode('ascii', errors='ignore').lower() for kw in ['getitem', 'battle', 'fight', 'combat', 'skill', 'ability'])]
    if item_strings:
        print(f'\nFound {len(item_strings)} item/battle-related strings (first 20):')
        for s in sorted(set(item_strings))[:20]:
            print(f'  {s}')

    # Search for UTF-16LE encoded Chinese characters (common in .NET)
    # 偷 = 0x5072, 窃 = 0x7A7A, 妙 = 0x592D, 手 = 0x523B
    # Actually in Unicode: 偷=U+5077, 窃=U+7A83, 妙=U+5999, 手=U+624B
    cn_patterns = [
        ('偷', b'\x77\x50'),  # U+5077 in UTF-16LE
        ('窃', b'\x83\x7a'),  # U+7A83
        ('妙', b'\x99\x59'),  # U+5999
    ]
    for cn_char, pattern in cn_patterns:
        count = data.count(pattern)
        if count > 0 and count < 100:
            print(f'\nChinese char "{cn_char}" (U+{ord(cn_char):04X}) found {count} times in UTF-16LE')
            positions = [m.start() for m in re.finditer(re.escape(pattern), data)]
            for pos in positions[:5]:
                # Get surrounding UTF-16LE text
                start = max(0, pos - 20)
                end = min(len(data), pos + 20)
                chunk = data[start:end]
                try:
                    text = chunk.decode('utf-16-le', errors='replace')
                    print(f'  offset {pos}: {text}')
                except:
                    pass
