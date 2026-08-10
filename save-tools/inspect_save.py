"""读 Save19，确认 荆棘/龙墨/谷月轩 的技能列表与背包现状。"""
import json

SAVE = r'D:/steam_jie/userdata/1187465257/650760/remote/Save19.Save'
raw = open(SAVE, 'rb').read()
print("BOM?", raw[:3] == b'\xef\xbb\xbf', "size", len(raw))
d = json.loads(raw.decode('utf-8-sig'))
print("team", d.get('m_Team') or d.get('m_GlobalNpcQuest'))
nl = d['m_NpcList']
idx = {e['iNpcID']: e for e in nl if isinstance(e, dict) and 'iNpcID' in e}
print("NpcList count", len(nl))

def show(nid, label):
    e = idx.get(nid)
    if not e:
        print(label, nid, "NOT FOUND"); return
    ng = e.get('NeigongList'); rt = e.get('RoutineList')
    print("\n=== %s (%d) ===" % (label, nid))
    if isinstance(ng, list):
        print(" NeigongList:", [(x.get('iSkillID'), x.get('iLevel')) for x in ng])
    if isinstance(rt, list):
        print(" RoutineList:", [(x.get('iSkillID'), x.get('iLevel')) for x in rt])

show(210002, "荆棘")
show(200017, "龙墨")
show(210001, "谷月轩")

bp = d.get('m_BackpackList')
print("\nBackpack count:", len(bp))
# show any existing 秘籍-like items (id in 121xxx / 100xxx / 140xxx)
import collections
ids = collections.Counter(it.get('m_ItemID') for it in bp if isinstance(it, dict))
print("distinct item ids:", len(ids))
for iid in [121010, 121034, 121043, 100010, 140087, 130109]:
    print("  item", iid, "in backpack?", iid in ids)
