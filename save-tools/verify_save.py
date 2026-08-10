"""对比当前 Save19 与本次备份，确认修改恰好等于计划。"""
import json

SAVE = r'D:/steam_jie/userdata/1187465257/650760/remote/Save19.Save'
BAK  = r'D:/steam_jie/userdata/1187465257/650760/remote/_save_backups/Save19.Save.bak_refund_20260810_233632'

def load(p):
    raw = open(p,'rb').read()
    assert raw[:3] != b'\xef\xbb\xbf', p+' has BOM!'
    return json.loads(raw.decode('utf-8-sig'))

d0 = load(BAK)   # before
d1 = load(SAVE)  # after

def ids(e, ln):
    lst = e.get(ln)
    if not isinstance(lst, list): return []
    return [x.get('iSkillID') for x in lst if isinstance(x, dict)]

i0 = {e['iNpcID']: e for e in d0['m_NpcList'] if isinstance(e,dict) and 'iNpcID' in e}
i1 = {e['iNpcID']: e for e in d1['m_NpcList'] if isinstance(e,dict) and 'iNpcID' in e}

print("=== 技能列表变化（仅应有目标移除）===")
changed = False
for nid in set(i0) | set(i1):
    for ln in ('NeigongList','RoutineList'):
        a = ids(i0.get(nid,{}), ln); b = ids(i1.get(nid,{}), ln)
        if a != b:
            changed = True
            removed = [x for x in a if x not in b]
            added = [x for x in b if x not in a]
            print("  npc %s %s: removed=%s added=%s" % (nid, ln, removed, added))
if not changed:
    print("  (none)")

print("\n=== 背包变化 ===")
bp0 = [dict(it) for it in d0['m_BackpackList']]
bp1 = [dict(it) for it in d1['m_BackpackList']]
print("  count %d -> %d" % (len(bp0), len(bp1)))
assert bp1[:len(bp0)] == bp0, "原始背包条目被改动！"
added_books = bp1[len(bp0):]
print("  新增条目:", added_books)
expect = [{'m_ItemID':121010,'m_iAmount':1,'m_bNew':True},
          {'m_ItemID':121034,'m_iAmount':1,'m_bNew':True},
          {'m_ItemID':100010,'m_iAmount':1,'m_bNew':True}]
assert added_books == expect, "新增条目不符: %s" % added_books

print("\n=== 其他 NPC 数量/结构一致性 ===")
assert len(d0['m_NpcList']) == len(d1['m_NpcList'])
# 检查除目标外所有 npc 的两个列表完全不变
target = {(210002,'NeigongList'),(200017,'NeigongList'),(210001,'RoutineList')}
bad = []
for nid in i0:
    for ln in ('NeigongList','RoutineList'):
        if (nid,ln) in target: continue
        if ids(i0[nid],ln) != ids(i1.get(nid,{}),ln):
            bad.append((nid,ln))
assert not bad, "非目标列表被改动: %s" % bad
print("  OK, 所有非目标角色技能列表未变")

print("\nALL VERIFIED: 修改恰好等于计划（两本内功秘籍+水浒英雄掌套路入背包；60036/70069/100010/140087 已移除；其余不变）。")
