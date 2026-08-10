import json, os, re

save_path = r"C:\Users\yanshijie\AppData\Roaming\SmartSteamEmu\650760\remote\Save19.Save"

with open(save_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Try to parse as JSON
try:
    data = json.loads(content)
    print("Parsed as JSON successfully")
except:
    print("Not valid JSON, trying manual extraction")
    data = None

if data:
    # Look for character/team data
    def find_chars(obj, path=""):
        results = []
        if isinstance(obj, dict):
            # Check if this dict has both name and talent list
            name = obj.get('strName', '')
            talent = obj.get('TalentList', None)
            npc_id = obj.get('m_iNPCID', None)
            if name and talent is not None:
                results.append({
                    'name': name,
                    'npc_id': npc_id,
                    'talents': talent,
                    'path': path
                })
            for k, v in obj.items():
                results.extend(find_chars(v, f"{path}.{k}"))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                results.extend(find_chars(v, f"{path}[{i}]"))
        return results
    
    chars = find_chars(data)
    print(f"\nFound {len(chars)} characters with talent lists:")
    for c in chars:
        print(f"  NPC ID: {c['npc_id']}, Name: {c['name']}, Talents: {c['talents']}")
else:
    # Manual regex extraction
    # Find all character blocks with name and talent list
    pattern = r'"strName":\s*"([^"]*)"[^}]*?"TalentList":\s*\[([^\]]*)\]'
    matches = re.findall(pattern, content)
    print(f"\nFound {len(matches)} character-talent pairs:")
    for name, talents in matches:
        print(f"  Name: {name}, Talents: [{talents}]")
    
    # Also find NPC IDs near talent lists
    pattern2 = r'"m_iNPCID":\s*(\d+)[^}]*?"TalentList":\s*\[([^\]]*)\]'
    matches2 = re.findall(pattern2, content)
    print(f"\nFound {len(matches2)} NPC-talent pairs:")
    for npc_id, talents in matches2:
        print(f"  NPC ID: {npc_id}, Talents: [{talents}]")
