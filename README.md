# 侠客风云传前传 · 攻略与改存档工具包

本仓库收录《侠客风云传前传》（Tale of Wuxia: The Pre-Sequel，Steam 版，内部版本 **1.0.2.2**）的两类成果：

1. **通关攻略**（`guide/`，多个版本）
2. **改存档 / 数据分析工具**（`save-tools/`、`guide-tools/`），用于在本地离线修改游戏存档、逆向游戏内部数据

> ⚠️ 所有工具均为**单机离线操作**，直接读写本地存档与游戏文件，不涉及联网或第三方服务。修改存档前请务必备份原文件。

---

## 目录结构

```
tale-of-wuxia-save-tools/
├── README.md              # 本文件
├── EXPERIENCE.md          # 存档修改核心经验（血泪踩坑提炼，优先读这个）
├── .gitignore
├── guide/                 # 攻略 HTML（每个版本一份）
├── save-tools/            # 存档修改脚本（内存扫描 / 退还武功 / 校验等）
├── guide-tools/           # 攻略 HTML 生成 / 游戏数据逆向脚本
├── data/                  # 游戏原始数据备份（MOD 修改前）
└── experience/            # 原始每日工作日志（md，按日期），记录完整排查过程
```

---

## 一、攻略版本（`guide/`）

| 文件 | 说明 | 时间 |
|------|------|------|
| `侠客风云传前传_终极全攻略.html` | **最新完整版**（角色培养、物品获取、全支线、主线时间线、全地点等 7+ 标签页） | 2026-08-10 |
| `侠客风云传前传_终极全攻略_backup.html` | 终极全攻略的中间备份版本（内容较旧，保留供对照） | 2026-08-04 |
| `侠客风云传前传_全奖励时间线攻略.html` | 早期「全奖励时间线」专项攻略 | 2026-07-31 |

直接用浏览器打开 `.html` 即可阅读。

---

## 二、存档修改脚本（`save-tools/`）

存档路径（本机默认）：`D:\steam_jie\userdata\1187465257\650760\remote\SaveN.Save`
真实存档目录以 `SaveTitle.SaveTitle` 索引确认（第 i 项 ↔ `Save{i}.Save`）。

| 脚本 | 作用 |
|------|------|
| `refund_skill.py` | **通用「退还武功/内功为秘籍」工具**：从角色 `NeigongList`/`RoutineList` 移除指定 `iSkillID`，并把对应秘籍物品加入 `m_BackpackList`。参数化 `REFUND_PLAN`，强校验，自动备份。**最常用、可直接改路径复用。** |
| `scan_mem_utf8.py` | 遍历游戏进程（YoungHero.exe）全部可读内存区，按 **UTF-8** 搜关键字，dump 上下文。用于抠出被加密的 `.pk` 配置表明文。 |
| `collect_books.py` | 从内存中的 ItemData 表收集「技能 ID → 秘籍物品 ID」映射（type-6 行，`col14` = 所教技能）。 |
| `scan_skill_ids.py` / `scan_book_region.py` / `full_scan_items.py` | 全内存扫描技能/物品 ID 的出现位置与上下文，确认结构与数据缺口。 |
| `inspect_save.py` | 读存档，打印各角色 `NeigongList`/`RoutineList`、背包，确认现状。 |
| `verify_save.py` | 对比「修改后存档 vs 备份」，确认仅目标改变、其余零改动。 |
| `crack_pk.py` / `extract_config.py` / `dump_config.py` | 尝试静态破解加密 `.pk`（结论：强加密、静态无解，必须靠运行时内存）。保留作排查记录。 |
| `find_book*.py` / `diag_*.py` / `inspect_bytes.py` / `scan_*.py` | 迭代过程中的调试/诊断脚本，记录探索路径。 |

### `refund_skill.py` 用法

```python
# 改 SAVE 路径 + REFUND_PLAN 即可复用
SAVE = r'D:/steam_jie/userdata/1187465257/650760/remote/Save19.Save'
# (npc_id, list_name, skill_id, book_item_id_or_None)
REFUND_PLAN = [
    (210002, 'NeigongList', 60036, 121010),   # 荆棘 血刀经 -> 血刀经秘籍
    (200017, 'NeigongList', 70069, 121034),   # 龙墨 正气决 -> 正气诀秘籍
    (210001, 'RoutineList', 100010, 100010),  # 谷月轩 水浒英雄掌 -> 套路物品
    (210001, 'RoutineList', 140087, None),    # 林冲策马鞭 -> 仅移除(无对应秘籍)
]
```
`book=None` 表示只移除、不放背包（用于游戏里压根没有对应秘籍物品的招式）。

---

## 三、攻略生成 / 数据逆向工具（`guide-tools/`）

| 脚本 | 作用 |
|------|------|
| `decrypt_pk.py` | 尝试解密游戏加密 `.pk`（记录用，结论同上）。 |
| `find_charcodes*.py` | 在游戏数据/DLL 中定位「中文名 ↔ 内部 ID」映射。 |
| `search_steal*.py` | 在 `Assembly-CSharp.dll` 中检索偷窃机制相关字符串。 |
| `rebuild_tabs.py` / `rebuild_builds*.py` / `rebuild_flow.py` / `rebuild_locations.py` | 重建/重写攻略 HTML 各标签页（人物培养、物品获取、支线、主线、地点）。 |
| `restore_save.bat` | Windows 批处理：从备份恢复指定 `SaveN.Save`。 |

---

## 四、原始数据备份（`data/`）

- `TalentNewData_ORIGINAL.txt` — 天赋数据 MOD 修改前的原始明文备份。

---

## 五、修改存档的通用方法（速览）

完整版见 `EXPERIENCE.md`。要点：

1. **备份**原档 → 2. 用 `SaveTitle.SaveTitle` 定位目标 `SaveN` → 3. 确认目标角色/技能/物品的真实 `iNpcID`（靠运行内存 UTF-8 扫描，别猜编号）→ 4. 按 `iNpcID` 改 `m_NpcList` 条目 / 改顶层 `m_TeammateList` 增减队员 → 5. **UTF-8 无 BOM 字节级写回** → 6. 校验（首字节非 `EF BB BF` + `json.loads` 通过）→ 7. **重启游戏读档**生效（运行中会自动存档覆盖）。

### 已知角色 ID 映射（内存实证）

| 角色 | iNpcID |
|------|--------|
| 卫紫绫 | 200000 |
| 蓝婷 | 100058 |
| 史燕 | 100059 |
| 水盼盼 | 200016 |
| 荆棘 | 210002 |
| 龙墨 | 200017 |
| 谷月轩 | 210001 |

---

## 免责声明

本仓库仅用于个人单机游戏的离线研究与备份，不附带任何游戏本体或受版权保护资源，亦不涉及联机作弊。请遵守相关平台与软件的使用条款。
