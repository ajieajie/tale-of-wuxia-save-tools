#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
侠客风云传前传 Save19 内功/武功 退还为秘籍工具
- 从角色 NeigongList(内功) 或 RoutineList(武功) 移除指定 iSkillID，并把对应秘籍物品加入 m_BackpackList
- book=None 表示仅移除、不放背包
- 整体 json 加载->修改->回写(UTF-8 无 BOM)，强校验：除目标外所有角色技能列表与背包原条目均不变
- 自动备份到 _save_backups
"""
import json, shutil, os, datetime

SAVE = r'D:/steam_jie/userdata/1187465257/650760/remote/Save19.Save'

# (npc_id, list_name, skill_id, book_item_id_or_None)
REFUND_PLAN = [
    (210002, 'NeigongList', 60036, 121010),   # 荆棘 血刀经 -> 血刀经秘籍
    (200017, 'NeigongList', 70069, 121034),   # 龙墨 正气决 -> 正气诀秘籍
    (210001, 'RoutineList', 100010, 100010),  # 谷月轩 水浒英雄掌 -> 水浒英雄掌套路
    (210001, 'RoutineList', 140087, None),    # 林冲策马鞭 -> 仅移除(无对应秘籍物品)
]

def snapshot_skills(d0):
    """记录所有 npc 的 NeigongList/RoutineList 的 (iSkillID 多重集, 长度)。"""
    snap = {}
    for e in d0['m_NpcList']:
        if isinstance(e, dict) and 'iNpcID' in e:
            for ln in ('NeigongList', 'RoutineList'):
                lst = e.get(ln)
                if isinstance(lst, list):
                    ids = [x.get('iSkillID') for x in lst if isinstance(x, dict)]
                    snap[(e['iNpcID'], ln)] = (ids, len(lst))
    return snap

def snapshot_backpack(d0):
    return [dict(it) for it in d0['m_BackpackList'] if isinstance(it, dict)]

def main():
    raw = open(SAVE, 'rb').read()
    assert raw[:3] != b'\xef\xbb\xbf', 'BOM detected - abort to avoid corrupting save'
    d0 = json.loads(raw.decode('utf-8-sig'))

    # backup
    bak_dir = os.path.join(os.path.dirname(SAVE), '_save_backups')
    os.makedirs(bak_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    bak = os.path.join(bak_dir, 'Save19.Save.bak_refund_%s' % ts)
    shutil.copy2(SAVE, bak)
    print('backup ->', bak)

    idx = {e['iNpcID']: e for e in d0['m_NpcList'] if isinstance(e, dict) and 'iNpcID' in e}

    # 校验计划合法性 + 记录原背包
    bp_before = snapshot_backpack(d0)
    sk_before = snapshot_skills(d0)
    books_to_add = []

    print('\n--- plan check ---')
    for npc_id, ln, sid, book in REFUND_PLAN:
        e = idx.get(npc_id)
        assert e, 'npc %s not found' % npc_id
        lst = e.get(ln)
        assert isinstance(lst, list), '%s.%s not list' % (npc_id, ln)
        assert any(x.get('iSkillID') == sid for x in lst), '%s not in %s.%s' % (sid, npc_id, ln)
        print('  npc %s %s remove iSkillID %s%s' % (npc_id, ln, sid, (' -> book %s' % book) if book else ' (no book)'))
        if book is not None:
            books_to_add.append(book)

    # 执行修改
    report = []
    for npc_id, ln, sid, book in REFUND_PLAN:
        e = idx[npc_id]
        lst = e[ln]
        before = len(lst)
        new_lst = [x for x in lst if x.get('iSkillID') != sid]
        assert len(new_lst) == before - 1, 'removal failed for %s %s %s' % (npc_id, ln, sid)
        e[ln] = new_lst
        if book is not None:
            d0['m_BackpackList'].append({'m_ItemID': book, 'm_iAmount': 1, 'm_bNew': True})
            report.append('npc %s: removed %s from %s; added book item %s' % (npc_id, sid, ln, book))
        else:
            report.append('npc %s: removed %s from %s (no book added)' % (npc_id, sid, ln))

    # 回写
    out = json.dumps(d0, ensure_ascii=False, separators=(',', ':'))
    out_bytes = out.encode('utf-8')
    assert out_bytes[:3] != b'\xef\xbb\xbf'
    open(SAVE, 'wb').write(out_bytes)

    # 强校验
    d1 = json.loads(out_bytes.decode('utf-8'))
    sk_after = snapshot_skills(d1)
    bp_after = snapshot_backpack(d1)
    errors = []

    # 1) 所有非目标角色技能列表不变
    for key, (ids_before, n_before) in sk_before.items():
        ids_after, n_after = sk_after.get(key, ([], 0))
        if ids_before != ids_after:
            errors.append('skill list changed for %s: %s -> %s' % (key, ids_before, ids_after))

    # 2) 目标角色：被移除技能确实消失，且长度恰好减少计划中的移除次数
    planned_remove = {}
    for npc_id, ln, sid, book in REFUND_PLAN:
        planned_remove[(npc_id, ln)] = planned_remove.get((npc_id, ln), 0) + 1
        ids_after, n_after = sk_after[(npc_id, ln)]
        assert sid not in ids_after, 'skill %s still present in %s.%s' % (sid, npc_id, ln)
    for (npc_id, ln), cnt in planned_remove.items():
        n_after = sk_after[(npc_id, ln)][1]
        assert n_after == sk_before[(npc_id, ln)][1] - cnt, 'length mismatch for %s.%s' % (npc_id, ln)

    # 3) 背包：原条目完全保留，且仅尾部追加了 books_to_add
    assert len(bp_after) == len(bp_before) + len(books_to_add), 'backpack length wrong'
    assert bp_after[:len(bp_before)] == bp_before, 'original backpack entries changed!'
    appended = bp_after[len(bp_before):]
    got_ids = [it.get('m_ItemID') for it in appended]
    assert got_ids == books_to_add, 'appended books mismatch: %s vs %s' % (got_ids, books_to_add)
    for it in appended:
        assert it.get('m_iAmount') == 1 and it.get('m_bNew') is True, 'book entry malformed: %s' % it

    print('\n'.join(report))
    print('backpack: %d -> %d (+%d books: %s)' % (len(bp_before), len(bp_after), len(books_to_add), books_to_add))
    print('written', len(out_bytes), 'bytes (old', len(raw), ')')
    assert not errors, 'UNEXPECTED CHANGES: %s' % errors
    print('VERIFIED OK (only target skills removed + books appended; all else unchanged). backup at', bak)

if __name__ == '__main__':
    main()
