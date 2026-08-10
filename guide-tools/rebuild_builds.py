# -*- coding: utf-8 -*-
"""Replace tab-builds section with clean character build tables."""

html_path = r"c:\Users\yanshijie\WorkBuddy\Claw\outputs\侠客风云传前传_终极全攻略.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate tab-builds boundaries
start_marker = '<div class="tab-content" id="tab-builds">'
end_marker = "</div><!-- /tab-builds -->"

start_pos = content.find(start_marker)
end_pos = content.find(end_marker)

if start_pos == -1 or end_pos == -1:
    print("ERROR: Cannot find tab-builds boundaries!")
    exit(1)

end_pos += len(end_marker)

new_builds = '''<div class="tab-content" id="tab-builds">

<div class="phase"><h2>📋 角色最优培养方案 —— 6内功 + 12招式</h2>
<p class="desc">以下为每个主力角色的最佳搭配，按武器类型和定位分类。获取流程详见"物品获取"标签页。</p></div>

<style>
  .char-block {
    margin-bottom: 24px;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    background: var(--card);
  }
  .char-block summary {
    padding: 14px 20px;
    cursor: pointer;
    font-weight: 700;
    font-size: 1.1em;
    background: linear-gradient(135deg, #f5f0e8, #ede5d5);
    display: flex;
    align-items: center;
    gap: 10px;
    user-select: none;
  }
  .char-block summary:hover { background: linear-gradient(135deg, #ede5d5, #e5dcc8); }
  .char-block summary .role-tag {
    font-size: 0.75em;
    padding: 2px 10px;
    border-radius: 12px;
    font-weight: 400;
    color: #fff;
  }
  .tag-fist { background: #c0392b; }
  .tag-sword { background: #2980b9; }
  .tag-blade { background: #d35400; }
  .tag-hidden { background: #8e44ad; }
  .tag-whip { background: #27ae60; }
  .tag-poison { background: #16a085; }
  .tag-staff { background: #e67e22; }
  .tag-heal { background: #e74c3c; }
  .tag-qin { background: #2c3e50; }
  .build-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88em;
  }
  .build-table thead th {
    background: #2c2416;
    color: #fff;
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
    letter-spacing: 1px;
  }
  .build-table thead th:first-child { width: 35%; }
  .build-table thead th:last-child { width: 65%; }
  .build-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
  }
  .build-table tbody tr:nth-child(even) { background: #faf8f4; }
  .build-table tbody tr:hover { background: var(--highlight); }
  .build-table .cat-label {
    font-weight: 700;
    color: var(--accent);
    background: #fef3f2 !important;
  }
  .skill-name { font-weight: 600; }
  .skill-note { color: var(--muted); font-size: 0.82em; margin-top: 2px; }
  .no-entry {
    text-align: center;
    color: var(--muted);
    font-style: italic;
    padding: 16px !important;
  }
  .note-box {
    background: #fffbe6;
    border-left: 3px solid var(--gold);
    padding: 8px 14px;
    margin: 8px 20px 14px;
    border-radius: 4px;
    font-size: 0.82em;
    color: var(--muted);
  }
</style>

<!-- ===== 谷月轩 ===== -->
<details class="char-block" open>
  <summary>🥊 <span>谷月轩</span> <span class="role-tag tag-fist">拳掌 · 坦克</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td class="cat-label" colspan="2">⸻ 核心必选 ⸻</td></tr>
      <tr>
        <td><span class="skill-name">九阳神功</span><div class="skill-note">暴击霸体 + 保护队友</div></td>
        <td><span class="skill-name">螳螂拳</span><div class="skill-note">前期即得，连击高暴</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">先天功</span><div class="skill-note">全队回血光环</div></td>
        <td><span class="skill-name">大闹天宫</span><div class="skill-note">AOE拳掌，暴击高</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">九阴总纲</span><div class="skill-note">暴击闪避双加成</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远距离无视防御</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">神龙密咒</span><div class="skill-note">中毒回血</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">群体内伤 + 高伤害</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">血刀经</span><div class="skill-note">吸血站桩</div></td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">全场AOE</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">葵花宝典</span><div class="skill-note">先手 + 闪避（通用内功）</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">极高单体伤害</div></td>
      </tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位推荐 ⸻</td></tr>
      <tr>
        <td class="no-entry" colspan="1">（以上6个已满）</td>
        <td><span class="skill-name">九阴白骨爪</span><div class="skill-note">毒系AOE</div></td>
      </tr>
      <tr>
        <td></td>
        <td><span class="skill-name">骑士精神</span><div class="skill-note">团队buff</div></td>
      </tr>
      <tr>
        <td></td>
        <td><span class="skill-name">不动明王棍</span><div class="skill-note">控场 + 反击</div></td>
      </tr>
      <tr>
        <td></td>
        <td><span class="skill-name">坎离水火剑</span><div class="skill-note">冰火双属性</div></td>
      </tr>
      <tr>
        <td></td>
        <td><span class="skill-name">浪花斩铁势</span><div class="skill-note">无视防御刀法</div></td>
      </tr>
      <tr>
        <td></td>
        <td><span class="skill-name">辟邪剑法</span><div class="skill-note">连击先手</div></td>
      </tr>
    </tbody>
  </table>
</details>

<!-- ===== 荆棘 ===== -->
<details class="char-block">
  <summary>🔪 <span>荆棘</span> <span class="role-tag tag-blade">刀法 · 输出</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">暴击闪避，完美契合</div></td>
        <td><span class="skill-name">浪花斩铁势</span><div class="skill-note">核心输出，无视防御</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血，刀法绝配</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">内伤AOE</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">霸体保护</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程点杀</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">团队续航</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">超高单体</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">残血反杀</div></td>
        <td><span class="skill-name">九阴白骨爪</span><div class="skill-note">毒刀combo</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手闪避</div></td>
        <td><span class="skill-name">辟邪剑法</span><div class="skill-note">连击先手</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td>
        <td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">大闹天宫</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">万佛朝宗</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">坎离水火剑</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">骑士精神</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">不动明王棍</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 方云华 ===== -->
<details class="char-block">
  <summary>⚔️ <span>方云华</span> <span class="role-tag tag-sword">剑法 · 刺客</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手连击 + 闪避，质变</div></td>
        <td><span class="skill-name">辟邪剑法</span><div class="skill-note">核心！配合葵花毁天灭地</div></td></tr>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">暴击 + 闪避</div></td>
        <td><span class="skill-name">坎离水火剑</span><div class="skill-note">冰火双属性爆发</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">霸体保命</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">远程剑法</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血续航</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">无视防御</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">团队回血</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">AOE内伤</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">中毒续航</div></td>
        <td><span class="skill-name">浪花斩铁势</span><div class="skill-note">无视防御补刀</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td>
        <td><span class="skill-name">万佛朝宗</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">大闹天宫</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">九阴白骨爪</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">骑士精神</span></td></tr>
      <tr><td></td>
        <td><span class="skill-name">不动明王棍</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 龙墨 ===== -->
<details class="char-block">
  <summary>🗡️ <span>龙墨</span> <span class="role-tag tag-blade">刀法 · 坦克输出</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血站桩</div></td>
        <td><span class="skill-name">浪花斩铁势</span><div class="skill-note">核心输出</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">霸体坦克</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程点杀</div></td></tr>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">闪避暴击</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">AOE内伤</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">团队续航</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">高伤单体</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">残血回复</div></td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">全场AOE</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手</div></td>
        <td><span class="skill-name">辟邪剑法</span><div class="skill-note">连击</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">坎离水火剑</span></td></tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td><td><span class="skill-name">大闹天宫</span></td></tr>
      <tr><td></td><td><span class="skill-name">九阴白骨爪</span></td></tr>
      <tr><td></td><td><span class="skill-name">骑士精神</span></td></tr>
      <tr><td></td><td><span class="skill-name">不动明王棍</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 史燕 ===== -->
<details class="char-block">
  <summary>🎯 <span>史燕</span> <span class="role-tag tag-hidden">暗器 · 偷窃</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">暗器中毒联动</div></td>
        <td><span class="skill-name">满天星雨</span><div class="skill-note">自带，暗器AOE</div></td></tr>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">闪避保命</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程无视防御</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">霸体</div></td>
        <td><span class="skill-name">九阴白骨爪</span><div class="skill-note">毒系AOE</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手偷窃</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">内伤</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">续航</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">高单体</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血</div></td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">AOE</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">辟邪剑法</span></td></tr>
      <tr><td></td><td><span class="skill-name">坎离水火剑</span></td></tr>
      <tr><td></td><td><span class="skill-name">浪花斩铁势</span></td></tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td><td><span class="skill-name">大闹天宫</span></td></tr>
      <tr><td></td><td><span class="skill-name">骑士精神</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 卫紫绫 ===== -->
<details class="char-block">
  <summary>☠️ <span>卫紫绫</span> <span class="role-tag tag-poison">毒功 · 辅助</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">毒功暴击联动</div></td>
        <td><span class="skill-name">九阴白骨爪</span><div class="skill-note">核心毒功AOE</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">中毒回血</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程无视防御</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">保护队友</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">AOE内伤</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血毒刀</div></td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">全场AOE</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">治疗光环</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">高单体</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手</div></td>
        <td><span class="skill-name">浪花斩铁势</span><div class="skill-note">无视防御</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">坎离水火剑</span></td></tr>
      <tr><td></td><td><span class="skill-name">辟邪剑法</span></td></tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td><td><span class="skill-name">大闹天宫</span></td></tr>
      <tr><td></td><td><span class="skill-name">骑士精神</span></td></tr>
      <tr><td></td><td><span class="skill-name">不动明王棍</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 不动 ===== -->
<details class="char-block">
  <summary>🦯 <span>不动</span> <span class="role-tag tag-staff">棍法 · 控制</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血站桩</div></td>
        <td><span class="skill-name">不动明王棍</span><div class="skill-note">核心棍法，控场 + 反击</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">霸体坦克</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程补刀</div></td></tr>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">闪避暴击</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">内伤AOE</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">回血光环</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">高单体</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">续航</div></td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">全场AOE</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手</div></td>
        <td><span class="skill-name">浪花斩铁势</span><div class="skill-note">无视防御</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">坎离水火剑</span></td></tr>
      <tr><td></td><td><span class="skill-name">辟邪剑法</span></td></tr>
      <tr><td></td><td><span class="skill-name">九阴白骨爪</span></td></tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td><td><span class="skill-name">大闹天宫</span></td></tr>
      <tr><td></td><td><span class="skill-name">骑士精神</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 萧复 ===== -->
<details class="char-block">
  <summary>🎵 <span>萧复</span> <span class="role-tag tag-qin">琴 · 治疗</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">核心治疗光环</div></td>
        <td><span class="skill-name">高山流水</span><div class="skill-note">自带，群疗</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">保护队友</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程补输出</div></td></tr>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">闪避保命</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">内伤辅助</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">续航</div></td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">AOE补刀</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">单体</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手治疗</div></td>
        <td><span class="skill-name">骑士精神</span><div class="skill-note">团队buff，推荐</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">浪花斩铁势</span></td></tr>
      <tr><td></td><td><span class="skill-name">坎离水火剑</span></td></tr>
      <tr><td></td><td><span class="skill-name">辟邪剑法</span></td></tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td><td><span class="skill-name">九阴白骨爪</span></td></tr>
      <tr><td></td><td><span class="skill-name">不动明王棍</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 塔娅 ===== -->
<details class="char-block">
  <summary>🛡️ <span>塔娅</span> <span class="role-tag tag-heal">剑 · 治疗坦克</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">保护全队，核心</div></td>
        <td><span class="skill-name">骑士精神</span><div class="skill-note">团队buff，核心</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">治疗光环</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程输出</div></td></tr>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">闪避保命</div></td>
        <td><span class="skill-name">坎离水火剑</span><div class="skill-note">冰火剑</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">AOE内伤</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">续航</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">高单体</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手</div></td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">AOE</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">辟邪剑法</span></td></tr>
      <tr><td></td><td><span class="skill-name">浪花斩铁势</span></td></tr>
      <tr><td></td><td><span class="skill-name">九阴白骨爪</span></td></tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td><td><span class="skill-name">大闹天宫</span></td></tr>
      <tr><td></td><td><span class="skill-name">不动明王棍</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 沈湘云 ===== -->
<details class="char-block">
  <summary>💊 <span>沈湘云</span> <span class="role-tag tag-heal">剑 · 纯治疗</span></summary>
  <table class="build-table">
    <thead><tr><th>内功（6个）</th><th>招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">治疗光环核心</div></td>
        <td><span class="skill-name">妙手回春</span><div class="skill-note">自带，单体大治疗</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">保护队友</div></td>
        <td><span class="skill-name">骑士精神</span><div class="skill-note">团队buff</div></td></tr>
      <tr><td><span class="skill-name">九阴总纲</span><div class="skill-note">闪避保命</div></td>
        <td><span class="skill-name">六脉神剑</span><div class="skill-note">远程输出</div></td></tr>
      <tr><td><span class="skill-name">神龙密咒</span><div class="skill-note">续航</div></td>
        <td><span class="skill-name">坎离水火剑</span><div class="skill-note">双属性剑</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">吸血</div></td>
        <td><span class="skill-name">佛渡拜火三迦叶</span><div class="skill-note">AOE内伤</div></td></tr>
      <tr><td><span class="skill-name">葵花宝典</span><div class="skill-note">先手治疗</div></td>
        <td><span class="skill-name">天外飞仙精要</span><div class="skill-note">高单体</div></td></tr>
      <tr><td class="cat-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">辟邪剑法</span></td></tr>
      <tr><td></td><td><span class="skill-name">万佛朝宗</span></td></tr>
      <tr><td></td><td><span class="skill-name">浪花斩铁势</span></td></tr>
      <tr><td></td><td><span class="skill-name">九阴白骨爪</span></td></tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span></td></tr>
      <tr><td></td><td><span class="skill-name">不动明王棍</span></td></tr>
    </tbody>
  </table>
</details>

<!-- ===== 总结速查表 ===== -->
<div class="phase" style="margin-top: 30px;"><h2>📊 全角色内功 & 招式速查</h2></div>
<div style="overflow-x: auto;">
  <table class="build-table" style="min-width: 700px;">
    <thead>
      <tr>
        <th>角色</th>
        <th>定位</th>
        <th>推荐内功（优先级从左到右）</th>
        <th>核心招式（前6个最关键）</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="skill-name">谷月轩</td>
        <td>拳掌·坦克</td>
        <td>九阳 > 先天 > 九阴 > 神龙 > 血刀 > 葵花</td>
        <td>螳螂拳 · 大闹天宫 · 六脉 · 佛渡 · 万佛 · 天外飞仙</td>
      </tr>
      <tr>
        <td class="skill-name">荆棘</td>
        <td>刀法·输出</td>
        <td>九阴 > 血刀 > 九阳 > 先天 > 神龙 > 葵花</td>
        <td>浪花斩铁 · 佛渡 · 六脉 · 天外飞仙 · 九阴白骨爪 · 辟邪</td>
      </tr>
      <tr>
        <td class="skill-name">方云华</td>
        <td>剑法·刺客</td>
        <td>葵花 > 九阴 > 九阳 > 血刀 > 先天 > 神龙</td>
        <td>辟邪 · 坎离水火 · 天外飞仙 · 六脉 · 佛渡 · 浪花斩铁</td>
      </tr>
      <tr>
        <td class="skill-name">龙墨</td>
        <td>刀法·坦克</td>
        <td>血刀 > 九阳 > 九阴 > 先天 > 神龙 > 葵花</td>
        <td>浪花斩铁 · 六脉 · 佛渡 · 天外飞仙 · 万佛 · 辟邪</td>
      </tr>
      <tr>
        <td class="skill-name">史燕</td>
        <td>暗器·偷窃</td>
        <td>神龙 > 九阴 > 九阳 > 葵花 > 先天 > 血刀</td>
        <td>满天星雨 · 六脉 · 九阴白骨爪 · 佛渡 · 天外飞仙 · 万佛</td>
      </tr>
      <tr>
        <td class="skill-name">卫紫绫</td>
        <td>毒功·辅助</td>
        <td>九阴 > 神龙 > 九阳 > 血刀 > 先天 > 葵花</td>
        <td>九阴白骨爪 · 六脉 · 佛渡 · 万佛 · 天外飞仙 · 浪花斩铁</td>
      </tr>
      <tr>
        <td class="skill-name">不动</td>
        <td>棍法·控制</td>
        <td>血刀 > 九阳 > 九阴 > 先天 > 神龙 > 葵花</td>
        <td>不动明王棍 · 六脉 · 佛渡 · 天外飞仙 · 万佛 · 浪花斩铁</td>
      </tr>
      <tr>
        <td class="skill-name">萧复</td>
        <td>琴·治疗</td>
        <td>先天 > 九阳 > 九阴 > 神龙 > 血刀 > 葵花</td>
        <td>高山流水 · 六脉 · 骑士精神 · 佛渡 · 万佛 · 天外飞仙</td>
      </tr>
      <tr>
        <td class="skill-name">塔娅</td>
        <td>剑·治疗坦</td>
        <td>九阳 > 先天 > 九阴 > 血刀 > 神龙 > 葵花</td>
        <td>骑士精神 · 六脉 · 坎离水火 · 佛渡 · 天外飞仙 · 万佛</td>
      </tr>
      <tr>
        <td class="skill-name">沈湘云</td>
        <td>剑·治疗</td>
        <td>先天 > 九阳 > 九阴 > 神龙 > 血刀 > 葵花</td>
        <td>妙手回春 · 骑士精神 · 六脉 · 坎离水火 · 佛渡 · 天外飞仙</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="note-box">
  💡 <b>说明</b>：获取流程请查阅「物品获取」标签页。通用招式（六脉神剑、佛渡拜火三迦叶等）全角色可学，但武器专属招式（辟邪剑法需自宫、浪花斩铁需刀等）有限制。
</div>

</div><!-- /tab-builds -->'''

# Replace
new_content = content[:start_pos] + new_builds + content[end_pos:]

# Write back
with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

# Verify
with open(html_path, "r", encoding="utf-8") as f:
    final = f.read()

div_open = final.count("<div")
div_close = final.count("</div>")
print(f"<div> tags: {div_open}, </div> tags: {div_close}, diff: {div_open - div_close}")

# Check all 8 tabs exist
tabs = ["tab-flow", "tab-rumor", "tab-locations", "tab-recruits", "tab-builds", "tab-check", "tab-items", "tab-sidequests"]
for t in tabs:
    count = final.count(f'id="{t}"')
    print(f"  {t}: {count} occurrences")

print(f"\nTotal lines: {len(final.splitlines())}")
print("Done!")
