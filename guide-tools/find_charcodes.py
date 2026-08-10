import json, os, glob

# Find save files
save_paths = [
    r"C:\Users\yanshijie\AppData\Roaming\SmartSteamEmu\650760\remote",
    r"F:\SteamLibrary\steamapps\common\Tale of WuxiaThe Pre-Sequel\Config\SaveData",
]

save_files = []
for sp in save_paths:
    if os.path.exists(sp):
        for f in glob.glob(os.path.join(sp, "*.Save")):
            save_files.append(f)
        for f in glob.glob(os.path.join(sp, "*.SaveTitle")):
            save_files.append(f)

print(f"Found {len(save_files)} save files")
for sf in save_files[:5]:
    print(f"  {sf}")

# Read the most recent save file and look for character data
if save_files:
    # Sort by modification time
    save_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    for sf in save_files[:3]:
        print(f"\n=== Reading {os.path.basename(sf)} ===")
        try:
            with open(sf, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Search for character names
            for name in ['史燕', '岳', '岳胖子', '岳子']:
                if name in content:
                    # Find surrounding context
                    idx = content.find(name)
                    context = content[max(0,idx-100):idx+200]
                    print(f"\nFound '{name}' at position {idx}:")
                    print(context[:300])
                    print("...")
                    
            # Also search for talent codes 305 and 339
            for talent in ['305', '339']:
                # Look in TalentList arrays
                import re
                patterns = re.findall(r'"TalentList":\s*\[([^\]]*)\]', content)
                for p in patterns:
                    if talent in p:
                        idx = content.find(f'"TalentList": [{p}]')
                        context = content[max(0,idx-200):idx+100]
                        # Find character name near this
                        print(f"\nTalent {talent} found in TalentList: [{p}]")
                        # Look for character ID nearby
                        id_match = re.search(r'"m_iNPCID":\s*(\d+)', content[max(0,idx-500):idx+500])
                        if id_match:
                            print(f"  Nearby NPC ID: {id_match.group(1)}")
                        name_match = re.search(r'"strName":\s*"([^"]*)"', content[max(0,idx-500):idx+500])
                        if name_match:
                            print(f"  Nearby Name: {name_match.group(1)}")
        except Exception as e:
            print(f"Error: {e}")
