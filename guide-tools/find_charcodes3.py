import json, os

save_path = r"C:\Users\yanshijie\AppData\Roaming\SmartSteamEmu\650760\remote\Save19.Save"

with open(save_path, 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

# Explore top-level structure
print("Top-level keys:", list(data.keys()) if isinstance(data, dict) else type(data))

if isinstance(data, dict):
    for k, v in data.items():
        if isinstance(v, list):
            print(f"\n{k}: list of {len(v)} items")
            if v and isinstance(v[0], dict):
                print(f"  First item keys: {list(v[0].keys())[:10]}")
        elif isinstance(v, dict):
            print(f"\n{k}: dict with keys {list(v.keys())[:10]}")
        else:
            print(f"\n{k}: {type(v).__name__} = {str(v)[:100]}")

# Search recursively for TalentList
def find_key(obj, target_key, path="", depth=0):
    if depth > 10:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == target_key:
                # Get context - find nearby strName and m_iNPCID
                name = obj.get('strName', 'N/A')
                npc_id = obj.get('m_iNPCID', 'N/A')
                print(f"\nFound {target_key} at {path}.{k}")
                print(f"  strName: {name}")
                print(f"  m_iNPCID: {npc_id}")
                print(f"  {target_key}: {v}")
                # Print all keys in this dict
                print(f"  All keys: {list(obj.keys())}")
            find_key(v, target_key, f"{path}.{k}", depth+1)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            find_key(v, target_key, f"{path}[{i}]", depth+1)

print("\n\n=== Searching for TalentList ===")
find_key(data, "TalentList")

print("\n\n=== Searching for strName with 305 or 339 in nearby talents ===")
def find_talent_chars(obj, path="", depth=0):
    if depth > 10:
        return
    if isinstance(obj, dict):
        if 'TalentList' in obj:
            talents = obj['TalentList']
            if isinstance(talent_str := str(talents), ) and ('305' in str(talents) or '339' in str(talents)):
                name = obj.get('strName', 'N/A')
                npc_id = obj.get('m_iNPCID', 'N/A')
                print(f"  Path: {path}")
                print(f"  Name: {name}, NPC ID: {npc_id}, Talents: {talents}")
        for k, v in obj.items():
            find_talent_chars(v, f"{path}.{k}", depth+1)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            find_talent_chars(v, f"{path}[{i}]", depth+1)

find_talent_chars(data)
