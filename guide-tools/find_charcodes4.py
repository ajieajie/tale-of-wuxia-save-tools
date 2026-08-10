import json

save_path = r"C:\Users\yanshijie\AppData\Roaming\SmartSteamEmu\650760\remote\Save19.Save"

with open(save_path, 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

# m_NpcList has all NPCs - find ones with talent 305 or 339
npc_list = data.get('m_NpcList', [])
print(f"Total NPCs in save: {len(npc_list)}")

# Also check m_TeammateList for teammate IDs
teammates = data.get('m_TeammateList', [])
print(f"Teammates: {teammates}")

# Find NPCs with talent 305 or 339
for i, npc in enumerate(npc_list):
    talents = npc.get('TalentList', [])
    if 305 in talents or 339 in talents:
        npc_id = npc.get('iNpcID', 'N/A')
        change_id = npc.get('iChangeNPCID', 'N/A')
        npc_type = npc.get('NpcType', 'N/A')
        now_practice = npc.get('NowPractice', 'N/A')
        weapon = npc.get('WeaponTypeList', [])
        routine = npc.get('RoutineList', [])
        neigong = npc.get('NeigongList', [])
        items = npc.get('Itemlist', [])
        
        print(f"\n=== NPC at index {i} ===")
        print(f"  iNpcID: {npc_id}")
        print(f"  iChangeNPCID: {change_id}")
        print(f"  NpcType: {npc_type}")
        print(f"  NowPractice: {now_practice}")
        print(f"  TalentList: {talents}")
        print(f"  WeaponTypeList: {weapon}")
        print(f"  RoutineList: {routine}")
        print(f"  NeigongList: {neigong}")
        print(f"  Itemlist: {items}")
        print(f"  iStr/iInt/iDex/iCon: {npc.get('iStr')}/{npc.get('iInt')}/{npc.get('iDex')}/{npc.get('iCon')}")

# Also print first few NPCs to understand the ID mapping
print("\n\n=== First 10 NPCs (ID mapping) ===")
for i, npc in enumerate(npc_list[:10]):
    print(f"  Index {i}: iNpcID={npc.get('iNpcID')}, NpcType={npc.get('NpcType')}, Talents={npc.get('TalentList')}, NowPractice={npc.get('NowPractice')}")
