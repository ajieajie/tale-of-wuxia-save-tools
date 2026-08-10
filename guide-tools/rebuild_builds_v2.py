# -*- coding: utf-8 -*-
"""Replace tab-builds with ACCURATE character build tables based on verified game data."""

html_path = r"c:\Users\yanshijie\WorkBuddy\Claw\outputs\侠客风云传前传_终极全攻略.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="tab-content" id="tab-builds">'
end_marker = "</div><!-- /tab-builds -->"

start_pos = content.find(start_marker)
end_pos = content.find(end_marker)
end_pos += len(end_marker)

new_builds = r'''<div class="tab-content" id="tab-builds">

<div class="phase"><h2>📋 角色最优培养方案（准确版 · 基于游戏数据验证）</h2>
<p class="desc">内功<strong>有角色限制</strong>，招式<strong>严格受武器类型限制</strong>。标 ⭐ 的为专属/关键技能，标 📖 的为可购秘籍。数量不足6/12时不强行填充。</p></div>

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
    font-weight: 700; font-size: 1.05em;
    background: linear-gradient(135deg, #f5f0e8, #ede5d5);
    display: flex; align-items: center; gap: 10px; user-select: none;
  }
  .char-block summary:hover { background: linear-gradient(135deg, #ede5d5, #e5dcc8); }
  .role-tag {
    font-size: 0.75em; padding: 2px 10px; border-radius: 12px;
    font-weight: 400; color: #fff;
  }
  .tag-fist { background: #c0392b; } .tag-sword { background: #2980b9; }
  .tag-blade { background: #d35400; } .tag-hidden { background: #8e44ad; }
  .tag-whip { background: #27ae60; } .tag-poison { background: #16a085; }
  .tag-staff { background: #e67e22; } .tag-heal { background: #e74c3c; }
  .tag-qin { background: #2c3e50; } .tag-dual { background: #c0392b; }

  .build-table { width: 100%; border-collapse: collapse; font-size: 0.86em; }
  .build-table thead th {
    background: #2c2416; color: #fff; padding: 9px 12px;
    text-align: left; font-weight: 600; letter-spacing: 1px;
  }
  .build-table td {
    padding: 7px 12px; border-bottom: 1px solid var(--border); vertical-align: top;
  }
  .build-table tbody tr:nth-child(even) { background: #faf8f4; }
  .build-table tbody tr:hover { background: var(--highlight); }
  .skill-name { font-weight: 600; }
  .skill-star { color: var(--accent); font-weight: 700; }
  .skill-shop { color: var(--accent2); font-size: 0.8em; }
  .skill-note { color: var(--muted); font-size: 0.8em; margin-top: 1px; }
  .section-label {
    font-weight: 700; color: var(--accent); background: #fef3f2 !important;
    font-size: 0.85em;
  }
  .note-box {
    background: #fffbe6; border-left: 3px solid var(--gold);
    padding: 8px 14px; margin: 8px 20px 14px; border-radius: 4px;
    font-size: 0.8em; color: var(--muted);
  }
</style>

<!-- ===== 1. 谷月轩 ===== -->
<details class="char-block" open>
  <summary>🥊 <span>谷月轩</span> <span class="role-tag tag-fist">拳掌 · 腿 · 指</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（12个）</th></tr></thead>
    <tbody>
      <tr><td class="section-label" colspan="2">⸻ 核心必选 ⸻</td></tr>
      <tr>
        <td><span class="skill-name skill-star">⭐ 逍遥鹏飞式</span><div class="skill-note">自带 · 回血回蓝 · 保护队友 · 反击霸体</div></td>
        <td><span class="skill-name skill-star">⭐ 佛度拜火三迦叶</span><div class="skill-note">直线3格 · 冻伤+重伤 · 根骨83/悟性76解放</div></td>
      </tr>
      <tr>
        <td><span class="skill-name skill-star">⭐ 小无相功</span><div class="skill-note">无暇子传 · 反击回蓝 · 免疫暴击 · 无限反击</div></td>
        <td><span class="skill-name skill-star">⭐ 天山六阳掌</span><div class="skill-note">扇形 · 聚气 · 小无相功十重后无暇子传</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">九阳神功</span><div class="skill-note">通用3本 · 暴击霸体 · 保护周边 · 击杀加攻</div></td>
        <td><span class="skill-name skill-star">⭐ 火焰刀</span><div class="skill-note">扇形 · 重伤 · 原始野林贺陀佛母 · 三迦叶前置</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">九阴总纲</span><div class="skill-note">不限角色 · 四维+5 · 抗暴10% · 抗反10%</div></td>
        <td><span class="skill-name">空明拳</span><div class="skill-note">单攻 · 乾坤挪移+震击 · 赛王府雪地天机老道</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">大湿婆密咒</span><div class="skill-note">限定 · 2000血 · 四维上限+5 · 需悟性70</div></td>
        <td><span class="skill-name">大金刚拳</span><div class="skill-note">单攻 · 洛阳酒馆无颠桌下捡</div></td>
      </tr>
      <tr>
        <td><span class="skill-name">先天功</span><div class="skill-note">限定(谷/古/商/萧复) · 需根骨90 · 根骨+8</div></td>
        <td><span class="skill-name">石破天惊拳</span><div class="skill-note">单攻 · 内伤+重伤 · 洛阳关伟任务</div></td>
      </tr>
      <tr><td class="section-label" colspan="2">⸻ 推荐补位 ⸻</td></tr>
      <tr>
        <td class="skill-note" style="text-align:center">（梯云纵/龙象般若功可替换大湿婆）</td>
        <td><span class="skill-name">万佛朝宗</span><div class="skill-note">AOE · 传闻习得</div></td>
      </tr>
      <tr><td></td><td><span class="skill-name">螳螂拳</span> <span class="skill-shop">📖 隐渊阁</span><div class="skill-note">连击 · 高暴击</div></td></tr>
      <tr><td></td><td><span class="skill-name">天下无狗</span><div class="skill-note">AOE · 青城派任务/传闻</div></td></tr>
      <tr><td></td><td><span class="skill-name">六脉神剑</span> <span class="skill-shop">📖</span><div class="skill-note">指法 · 直线无视防御 · 需指法路线</div></td></tr>
      <tr><td></td><td><span class="skill-name">龙腾江海</span><div class="skill-note">初始腿法 · AOE溅射 · 闪避</div></td></tr>
      <tr><td></td><td><span class="skill-name">八仙指路</span><div class="skill-note">初始指法 · 反击 · 气功路线</div></td></tr>
    </tbody>
  </table>
  <div class="note-box">💡 谷月轩是游戏中最全能的角色，拳掌/腿/指三系精通。推荐主拳掌副指法，火焰刀十重后解锁佛度拜火三迦叶（最强自创技）。内功可选梯云纵补移动。</div>
</details>

<!-- ===== 2. 荆棘 ===== -->
<details class="char-block">
  <summary>🔪 <span>荆棘</span> <span class="role-tag tag-dual">刀+剑 · 输出</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 逍遥雁行式</span><div class="skill-note">自带 · 暴击+神行+连斩</div></td>
        <td><span class="skill-name skill-star">⭐ 一刀起程</span><div class="skill-note">初始 · 单攻 · 连斩收割</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 日月神功</span><div class="skill-note">无暇子传 · 暴击5+反击5</div></td>
        <td><span class="skill-name skill-star">⭐ 走剑行刀</span><div class="skill-note">初始 · 范围 · 流血</div></td></tr>
      <tr><td><span class="skill-name">虎啸功</span><div class="skill-note">限定(荆/龙/商/秦) · 乐山大佛任务</div></td>
        <td><span class="skill-name skill-star">⭐ 坎离水火剑</span><div class="skill-note">扇形 · 恐惧+震击 · 冲灵剑法换</div></td></tr>
      <tr><td><span class="skill-name">血刀经</span><div class="skill-note">限定(刀系) · 需臂力76 · 赛王府小王爷 · (仅1本!)</div></td>
        <td><span class="skill-name skill-star">⭐ 幽冥十三式</span><div class="skill-note">直线 · 必中+吸星 · 成都剑圣(需傅剑寒)</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">通用3本 · 暴击霸体 · 配合单挑</div></td>
        <td><span class="skill-name skill-star">⭐ 抖鳞虎扑式</span><div class="skill-note">单攻 · 霸体 · 毒龙教荆棘劝架单挑阿傍</div></td></tr>
      <tr><td><span class="skill-name">吸星大法</span><div class="skill-note">通用3本 · 暴击3 · 抗暴10 · 补充内力</div></td>
        <td><span class="skill-name">阴错阳差</span><div class="skill-note">范围 · 缚身 · 洛阳烟火大会</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 刀法补位（可购/传闻） ⸻</td></tr>
      <tr><td></td>
        <td><span class="skill-name">刀山剑岳</span><div class="skill-note">直线2格 · 破甲 · 日月神功十重</div></td></tr>
      <tr><td></td><td><span class="skill-name">狂龙逆斩</span><div class="skill-note">范围 · 吸星 · 逍遥谷二楼(二选一)</div></td></tr>
      <tr><td></td><td><span class="skill-name">魔刀七杀</span> <span class="skill-shop">📖 无名冢四选一</span><div class="skill-note">直线3格 · 流血 · 岳胖子</div></td></tr>
      <tr><td></td><td><span class="skill-name">庖丁解牛刀</span> <span class="skill-shop">📖</span><div class="skill-note">单攻 · 破甲</div></td></tr>
      <tr><td></td><td><span class="skill-name">残存亦末路</span> <span class="skill-shop">📖 高昌遗迹心残</span><div class="skill-note">直线 · 左右互搏(70%连击)</div></td></tr>
      <tr><td></td><td><span class="skill-name">八艘飞</span> <span class="skill-shop">📖 传闻</span><div class="skill-note">刀法 · 高伤害</div></td></tr>
    </tbody>
  </table>
  <div class="note-box">⚠️ 血刀经全游戏仅1本！荆棘和龙墨只能二选一。荆棘如果培养为主输出，给血刀经；如果龙墨主输出，荆棘用吸星大法/九阳。荆棘招式总数偏少（剧情约8招），需靠刀法秘籍补到12格。</div>
</details>

<!-- ===== 3. 方云华 ===== -->
<details class="char-block">
  <summary>⚔️ <span>方云华</span> <span class="role-tag tag-sword">剑法 · 刺客</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 武当九阳功</span><div class="skill-note">自带 · 臂力上限+5</div></td>
        <td><span class="skill-name skill-star">⭐ 归藏剑</span><div class="skill-note">自带 · 范围AOE · 100%吸气血内力</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 葵花宝典</span><div class="skill-note">专属 · 连斩+神游 · 无名冢(需任剑南)</div></td>
        <td><span class="skill-name skill-star">⭐ 辟邪剑法</span><div class="skill-note">直线3格 · 攻击次数+1 · 无名冢(需任剑南)</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 倚天屠龙功</span><div class="skill-note">限定(方/古) · 武当五宝花蜜酒</div></td>
        <td><span class="skill-name skill-star">⭐ 流星飞坠</span><div class="skill-note">自身范围 · 攻击次数+1+神行 · 无名冢</div></td></tr>
      <tr><td><span class="skill-name">紫霞神功</span><div class="skill-note">限定(方/燕/任) · 武当九阳十重→卓人清</div></td>
        <td><span class="skill-name skill-star">⭐ 太极化清</span><div class="skill-note">自身范围 · 净化+乾坤挪移 · 紫霞后卓人清</div></td></tr>
      <tr><td><span class="skill-name">天山心法</span><div class="skill-note">传闻 · (注意:想刷意志坚定就别学)</div></td>
        <td><span class="skill-name skill-star">⭐ 天外飞仙</span><div class="skill-note">直线3格 · 闪避 · 传闻习得</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">通用3本 · 补充内力输出</div></td>
        <td><span class="skill-name">太极剑法</span><div class="skill-note">初始 · 单攻</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 剑法补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">绕指柔剑</span><div class="skill-note">初始 · 范围</div></td></tr>
      <tr><td></td><td><span class="skill-name">饮中八仙剑</span> <span class="skill-shop">📖 杭州隐渊阁</span><div class="skill-note">直线 · 霸体 · 保命技</div></td></tr>
      <tr><td></td><td><span class="skill-name">龙泣剑</span> <span class="skill-shop">📖</span><div class="skill-note">高伤单体</div></td></tr>
      <tr><td></td><td><span class="skill-name">情意七剑</span> <span class="skill-shop">📖 铸剑山庄</span><div class="skill-note">任剑南专属(需任在队)</div></td></tr>
      <tr><td></td><td><span class="skill-name">金蛇剑法</span> <span class="skill-shop">📖 冲灵换</span><div class="skill-note">荆棘不换坎离可换</div></td></tr>
      <tr><td></td><td><span class="skill-name">迅雷剑法</span> <span class="skill-shop">📖 咸鱼粥打输</span><div class="skill-note">骆翎枫任务</div></td></tr>
    </tbody>
  </table>
  <div class="note-box">⚠️ 方云华的核心是三件套：<b>葵花宝典 + 辟邪剑法 + 流星飞坠</b>——无名冢带任剑南一次拿齐。葵花宝典的「连斩+神游」让他成为游戏最强刺客。注意：天山心法传闻会占用1格内功位，如果想刷意志坚定天赋就别触发。</div>
</details>

<!-- ===== 4. 龙墨 ===== -->
<details class="char-block">
  <summary>🗡️ <span>龙墨</span> <span class="role-tag tag-blade">刀法 · 主力输出</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 千仞诀</span><div class="skill-note">自带 · 连斩+暴击 · 输出核心</div></td>
        <td><span class="skill-name skill-star">⭐ 浪花斩铁势</span><div class="skill-note">单攻 · 眩晕+内伤 · 藏海岛(入队即得)</div></td></tr>
      <tr><td><span class="skill-name">连山诀</span><div class="skill-note">自带 · 臂力上限+5</div></td>
        <td><span class="skill-name skill-star">⭐ 狂风刀法</span><div class="skill-note">自带 · 吸血150% · 单挑神技</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 血刀经</span><div class="skill-note">限定 · 需臂力76 · (全游戏仅1本!)</div></td>
        <td><span class="skill-name skill-star">⭐ 十殿阎罗刀</span><div class="skill-note">直线3格 · 恐惧+断筋+噬气 · 打赢阎罗</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 虎啸功</span><div class="skill-note">限定 · 乐山大佛 · 臂力+内功输出</div></td>
        <td><span class="skill-name skill-star">⭐ 残存亦末路</span><div class="skill-note">直线 · 左右互搏(70%连击) · 高昌遗迹心残</div></td></tr>
      <tr><td><span class="skill-name">清心普善咒</span><div class="skill-note">传闻 · 根骨+3上限+5</div></td>
        <td><span class="skill-name">春风快意刀</span><div class="skill-note">初始 · 单攻</div></td></tr>
      <tr><td><span class="skill-name">罗汉降魔功</span><div class="skill-note">限定 · (或换九阳神功)</div></td>
        <td><span class="skill-name">船过水无痕</span><div class="skill-note">初始 · 范围</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 刀法补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">八艘飞</span> <span class="skill-shop">📖 传闻</span></td></tr>
      <tr><td></td><td><span class="skill-name">魔刀七杀</span> <span class="skill-shop">📖 无名冢四选一</span><div class="skill-note">直线3格 · 流血</div></td></tr>
      <tr><td></td><td><span class="skill-name">蚩尤刀法</span> <span class="skill-shop">📖 成都隐元阁</span><div class="skill-note">范围3人 · 破甲</div></td></tr>
      <tr><td></td><td><span class="skill-name">庖丁解牛刀</span> <span class="skill-shop">📖</span></td></tr>
      <tr><td></td><td><span class="skill-name">慈悲刀法</span> <span class="skill-shop">📖 反伤流</span></td></tr>
      <tr><td></td><td><span class="skill-name">井中八法</span> <span class="skill-shop">📖 光刀胄甲</span></td></tr>
    </tbody>
  </table>
  <div class="note-box">⚠️ 血刀经全游戏仅1本，龙墨和荆棘<b>只能二选一</b>。如果主养龙墨当刀系一哥，血刀经给他。千仞诀自带连斩，配合血刀经双连斩体系输出爆炸。</div>
</details>

<!-- ===== 5. 卫紫绫 ===== -->
<details class="char-block">
  <summary>☠️ <span>卫紫绫</span> <span class="role-tag tag-poison">毒功 · 腿 · 辅助</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 龙腾豹变</span><div class="skill-note">自带 · 隐匿+暴击</div></td>
        <td><span class="skill-name skill-star">⭐ 紫翎霓裳舞</span><div class="skill-note">初始 · 范围 · 中毒</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 星宿心法</span><div class="skill-note">怪医居沈澜 · 隐身烫人神技</div></td>
        <td><span class="skill-name skill-star">⭐ 流风回雪</span><div class="skill-note">初始 · 单攻 · 闪避</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 鼎心无量功</span><div class="skill-note">怪医居 · 需小阿曼 · 毒锅5种虫×5</div></td>
        <td><span class="skill-name skill-star">⭐ 千蛛万毒手</span><div class="skill-note">怪医居沈澜 · 中毒+减速</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 神龙密咒</span><div class="skill-note">限定(卫/小阿曼) · 藏海岛 · 暴击5</div></td>
        <td><span class="skill-name skill-star">⭐ 化骨绵掌</span><div class="skill-note">藏海岛宝箱 · 中毒+吸星</div></td></tr>
      <tr><td><span class="skill-name">明玉功</span><div class="skill-note">限定 · 暴击3+身法3 · (共3本)</div></td>
        <td><span class="skill-name skill-star">⭐ 化功大法</span><div class="skill-note">原始野林贺陀佛母 · 眩晕+散功</div></td></tr>
      <tr><td><span class="skill-name">九阴飞絮</span><div class="skill-note">限定 · 暴击10+移动1 · (共2本)</div></td>
        <td><span class="skill-name skill-star">⭐ 缠丝八爪</span><div class="skill-note">成都隐渊阁买 · 范围 · 缚身</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">兰花拂穴手</span><div class="skill-note">忘忧谷仙音 · 点穴</div></td></tr>
      <tr><td></td><td><span class="skill-name">九阴白骨爪</span> <span class="skill-shop">📖</span><div class="skill-note">毒系AOE</div></td></tr>
      <tr><td></td><td><span class="skill-name">风神腿</span> <span class="skill-shop">📖 杭州隐渊阁</span><div class="skill-note">腿法 · (需臂力72)</div></td></tr>
      <tr><td></td><td><span class="skill-name">金蛇宝典</span><div class="skill-note">限定 · 身法+5上限+10</div></td></tr>
      <tr><td></td><td class="skill-note" style="text-align:center">（卫紫绫招式以毒系为主，8招已够用）</td></tr>
    </tbody>
  </table>
  <div class="note-box">💡 卫紫绫的核心是<b>星宿心法隐身烫人</b>——boss越强越被烫得厉害。神龙密咒配合隐匿可以无限暴击霸体。鼎心无量功需要队中有小阿曼，在怪医居左边毒锅丢5种毒虫各5只。</div>
</details>

<!-- ===== 6. 史燕 ===== -->
<details class="char-block">
  <summary>🎯 <span>史燕</span> <span class="role-tag tag-hidden">暗器 · 偷窃</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（9个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 飞燕功</span><div class="skill-note">自带 · 闪避</div></td>
        <td><span class="skill-name skill-star">⭐ 燕子刺</span><div class="skill-note">初始 · 单攻 · 偷窃判定技</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 鲸息功</span><div class="skill-note">传闻 · 回血回内+暴击霸体</div></td>
        <td><span class="skill-name skill-star">⭐ 乳燕归巢</span><div class="skill-note">初始 · 范围</div></td></tr>
      <tr><td><span class="skill-name">天山心法</span><div class="skill-note">加闪避</div></td>
        <td><span class="skill-name skill-star">⭐ 满天花雨</span><div class="skill-note">初始 · AOE暗器</div></td></tr>
      <tr><td><span class="skill-name">金雁功</span><div class="skill-note">通用 · 身法上限+5 · 加闪避</div></td>
        <td><span class="skill-name skill-star">⭐ 烟雾弥漫</span><div class="skill-note">初始 · 隐身/逃跑</div></td></tr>
      <tr><td><span class="skill-name">灵飞经</span><div class="skill-note">通用 · 加闪避</div></td>
        <td><span class="skill-name">荆轲武诀</span><div class="skill-note">无名冢愧尸处捡</div></td></tr>
      <tr><td><span class="skill-name">金蛇宝典</span><div class="skill-note">限定 · (卫紫绫不学可给她)</div></td>
        <td><span class="skill-name">聂隐剑</span><div class="skill-note">高昌迷宫左边房捡</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">奇毒天镖</span> <span class="skill-shop">📖</span><div class="skill-note">暗器 · 中毒</div></td></tr>
      <tr><td></td><td><span class="skill-name">小李飞刀</span> <span class="skill-shop">📖</span><div class="skill-note">暗器 · 必中</div></td></tr>
    </tbody>
  </table>
  <div class="note-box">💡 史燕的核心功能是<b>偷窃</b>，输出越低越好偷。内功全堆闪避（金雁/灵飞/天山），不要堆攻击。暗器招式偏少（约6-7招），属于功能性角色。</div>
</details>

<!-- ===== 7. 不动 ===== -->
<details class="char-block">
  <summary>🦯 <span>不动</span> <span class="role-tag tag-staff">棍法 · 坦克·控制</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（10个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 少林九阳功</span><div class="skill-note">自带</div></td>
        <td><span class="skill-name skill-star">⭐ 禅意自在棍</span><div class="skill-note">初始 · 单攻</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 易筋经</span><div class="skill-note">自带 · 四维上限+5</div></td>
        <td><span class="skill-name skill-star">⭐ 不动明王棍</span><div class="skill-note">初始 · 控场+反击 · 棍系核心</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 金刚不坏体</span><div class="skill-note">专属 · 少林任务 · 伤害减免</div></td>
        <td><span class="skill-name skill-star">⭐ 风随白云飞</span><div class="skill-note">初始 · 范围 · 闪避</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 白首太玄经</span><div class="skill-note">传闻 · 属性爆炸</div></td>
        <td><span class="skill-name skill-star">⭐ 达摩武诀</span><div class="skill-note">乐山大佛虚真任务 · 单体高伤</div></td></tr>
      <tr><td><span class="skill-name">左右互搏</span><div class="skill-note">赛王府雪地天机老道(需不动在队)</div></td>
        <td><span class="skill-name">屠牛药叉</span><div class="skill-note">传闻习得</div></td></tr>
      <tr><td><span class="skill-name">禅宗莲华功</span><div class="skill-note">限定(江/水/不动) · 悟性上限+5</div></td>
        <td><span class="skill-name">一醉逍遥</span><div class="skill-note">东渡口隐渊阁买</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 棍法补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">天下无狗</span> <span class="skill-shop">📖</span><div class="skill-note">AOE棍法</div></td></tr>
      <tr><td></td><td><span class="skill-name">灵蛇杖法</span> <span class="skill-shop">📖 西域番僧</span></td></tr>
      <tr><td></td><td><span class="skill-name">大须弥山棍</span> <span class="skill-shop">📖</span></td></tr>
      <tr><td></td><td><span class="skill-name">回马枪</span> <span class="skill-shop">📖 招安敖广</span><div class="skill-note">直线2格 · 重伤+神行</div></td></tr>
    </tbody>
  </table>
  <div class="note-box">💡 不动自带最强内功组合（少林九阳+易筋经+金刚不坏体），是游戏第一坦克。左右互搏在赛王府雪地第三天由天机老道传授（需不动在队）。棍系招式可买可传闻补足。</div>
</details>

<!-- ===== 8. 萧复 ===== -->
<details class="char-block">
  <summary>🎵 <span>萧复</span> <span class="role-tag tag-qin">琴 · 治疗·辅助</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（12个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 七弦神功</span><div class="skill-note">自带</div></td>
        <td><span class="skill-name skill-star">⭐ 七弦奏天南</span><div class="skill-note">初始 · 群疗</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 清心普善咒</span><div class="skill-note">专属 · 根骨上限+5(逍遥谷阿吉咸鱼换)</div></td>
        <td><span class="skill-name skill-star">⭐ 弦箫东南飞</span><div class="skill-note">初始 · 范围</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 声无哀乐</span><div class="skill-note">专属 · 弦箫幽谷弹琴(需悟性66)</div></td>
        <td><span class="skill-name skill-star">⭐ 玉箫剑气</span><div class="skill-note">初始 · 单攻</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 太易星辰诀</span><div class="skill-note">传闻 · 减攻光环</div></td>
        <td><span class="skill-name skill-star">⭐ 笑傲江湖曲</span><div class="skill-note">森林任剑南 · 萧复入队必拿</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 沧海一声笑</span><div class="skill-note">限定(萧/任/楚) · 琴系内功</div></td>
        <td><span class="skill-name skill-star">⭐ 百鸟朝凤曲</span><div class="skill-note">少林寺(需萧复+水盼盼) · AOE+净化</div></td></tr>
      <tr><td><span class="skill-name">先天功</span><div class="skill-note">限定 · 需根骨90 · (也可给谷)</div></td>
        <td><span class="skill-name skill-star">⭐ 碧海潮生曲</span><div class="skill-note">忘忧谷醉仙(葡萄美酒+夜光杯)</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">重峦复嶂曲</span><div class="skill-note">弦剑山庄探望萧复</div></td></tr>
      <tr><td></td><td><span class="skill-name">全真剑法</span><div class="skill-note">雪地野店天机老道(需水盼盼前置)</div></td></tr>
      <tr><td></td><td><span class="skill-name">十面埋伏曲</span><div class="skill-note">高昌迷宫右边房捡</div></td></tr>
      <tr><td></td><td><span class="skill-name">龙象般若功</span><div class="skill-note">通用 · 臂力+5上限+5 · (最后一个格子)</div></td></tr>
    </tbody>
  </table>
  <div class="note-box">💡 萧复的招式几乎全是剧情专属，9招已算完整。第10~12格可用通用武学填充。他是游戏最强治疗+辅助角色，百鸟朝凤曲配合水盼盼在少林寺获得。</div>
</details>

<!-- ===== 9. 沈湘云 ===== -->
<details class="char-block">
  <summary>💊 <span>沈湘云</span> <span class="role-tag tag-heal">剑 · 纯治疗·控制</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（4个）</th><th style="width:60%">招式（7个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 忘忧心法</span><div class="skill-note">自带 · 治疗加成</div></td>
        <td><span class="skill-name skill-star">⭐ 金针渡劫</span><div class="skill-note">初始 · 单体大治疗</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 洗髓经</span><div class="skill-note">传闻 · 属性提升</div></td>
        <td><span class="skill-name skill-star">⭐ 清莲印法</span><div class="skill-note">初始 · 净化</div></td></tr>
      <tr><td><span class="skill-name">万物皆数</span><div class="skill-note">限定(湘/塔/江/谷) · (共2本)</div></td>
        <td><span class="skill-name skill-star">⭐ 点血截脉</span><div class="skill-note">最强控制 · 咸鱼粥任务打输→罗煞分舵</div></td></tr>
      <tr><td><span class="skill-name">药王神篇</span><div class="skill-note">限定(湘/塔) · 治疗加成</div></td>
        <td><span class="skill-name">九阳神功</span><div class="skill-note">通用 · (或正气诀加根骨)</div></td></tr>
      <tr><td class="section-label" colspan="2"></td></tr>
      <tr><td></td><td><span class="skill-name">饮中八仙剑</span> <span class="skill-shop">📖 杭州隐渊阁</span><div class="skill-note">保命技</div></td></tr>
      <tr><td></td><td><span class="skill-name">龙泣剑</span> <span class="skill-shop">📖</span></td></tr>
      <tr><td></td><td><span class="skill-name">迅雷剑法</span> <span class="skill-shop">📖</span></td></tr>
      <tr><td class="skill-note" colspan="2" style="text-align:center">（沈湘云和塔娅共享内功资源，建议二选一培养）</td></tr>
    </tbody>
  </table>
  <div class="note-box">⚠️ 沈湘云内功偏少（仅4个好用），和塔娅共享万物皆数/药王神篇，<b>二选一</b>培养。核心价值在点血截脉——最强单体控制。咸鱼粥任务故意打输才能触发后续获取。</div>
</details>

<!-- ===== 10. 塔娅 ===== -->
<details class="char-block">
  <summary>🛡️ <span>塔娅</span> <span class="role-tag tag-heal">剑 · 治疗坦·BUFF</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（8个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name skill-star">⭐ 道生一</span><div class="skill-note">自带</div></td>
        <td><span class="skill-name skill-star">⭐ 天机十变</span><div class="skill-note">初始 · 单攻</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 太易星辰诀</span><div class="skill-note">自带 · 减攻光环</div></td>
        <td><span class="skill-name skill-star">⭐ 天物刃</span><div class="skill-note">初始 · 范围</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 武林群侠传</span><div class="skill-note">专属 · 最强治疗内功</div></td>
        <td><span class="skill-name skill-star">⭐ 神曲但丁</span><div class="skill-note">初始 · 远程</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 易筋经</span><div class="skill-note">传闻 · 四维上限+5 · (成都10珍贵药草)</div></td>
        <td><span class="skill-name skill-star">⭐ 骑士精神</span><div class="skill-note">核心！团队BUFF · 主线剧情习得</div></td></tr>
      <tr><td><span class="skill-name">万物皆数</span><div class="skill-note">限定 · (共2本 与沈湘云抢)</div></td>
        <td><span class="skill-name skill-star">⭐ 乌衣宝典</span><div class="skill-note">雪地野店北丑→花族部落宝箱</div></td></tr>
      <tr><td><span class="skill-name">药王神篇</span><div class="skill-note">限定 · (或换九阳神功)</div></td>
        <td><span class="skill-name">饮中八仙剑</span> <span class="skill-shop">📖</span><div class="skill-note">保命技</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">龙泣剑</span> <span class="skill-shop">📖</span></td></tr>
      <tr><td></td><td><span class="skill-name">金蛇剑法</span> <span class="skill-shop">📖</span></td></tr>
      <tr><td class="skill-note" colspan="2" style="text-align:center">（塔娅招式偏少，剑法秘籍补足12格）</td></tr>
    </tbody>
  </table>
  <div class="note-box">💡 塔娅的核心价值在<b>骑士精神</b>——全队强力BUFF，主线必得。她和沈湘云共享万物皆数/药王神篇，培养投入>沈湘云但回报更高。易筋经传闻可在成都用10珍贵药草换。</div>
</details>

<!-- ===== 11. 水盼盼 ===== -->
<details class="char-block">
  <summary>💧 <span>水盼盼</span> <span class="role-tag tag-sword">剑法 · 输出</span></summary>
  <table class="build-table">
    <thead><tr><th style="width:40%">内功（6个）</th><th style="width:60%">招式（9个）</th></tr></thead>
    <tbody>
      <tr><td><span class="skill-name">峨嵋九阳功</span><div class="skill-note">自带</div></td>
        <td><span class="skill-name skill-star">⭐ 凝柔剑法</span><div class="skill-note">初始 · 单攻</div></td></tr>
      <tr><td><span class="skill-name">正气诀</span><div class="skill-note">自带 · 根骨上限+5</div></td>
        <td><span class="skill-name skill-star">⭐ 金顶剑法</span><div class="skill-note">初始 · 范围</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 太易星辰诀</span><div class="skill-note">传闻 · 减攻光环</div></td>
        <td><span class="skill-name skill-star">⭐ 冰心剑法</span><div class="skill-note">初始 · 冰冻</div></td></tr>
      <tr><td><span class="skill-name skill-star">⭐ 吸星大法</span><div class="skill-note">通用3本 · 连斩续航</div></td>
        <td><span class="skill-name skill-star">⭐ 玉女剑法</span><div class="skill-note">大地图杨雨枫 · (萧复全真剑法前置)</div></td></tr>
      <tr><td><span class="skill-name">九阴飞絮</span><div class="skill-note">限定 · 暴击10+移动1</div></td>
        <td><span class="skill-name skill-star">⭐ 天外飞仙</span><div class="skill-note">专属(杭州吴桐任务) · 直线高伤</div></td></tr>
      <tr><td><span class="skill-name">九阳神功</span><div class="skill-note">通用 · 补输出</div></td>
        <td><span class="skill-name skill-star">⭐ 龙泣剑</span><div class="skill-shop">📖</div><div class="skill-note">高伤单体</div></td></tr>
      <tr><td class="section-label" colspan="2">⸻ 补位 ⸻</td></tr>
      <tr><td></td><td><span class="skill-name">玉女心法</span><div class="skill-note">限定 · 身法上限+5 · (大地图杨雨枫)</div></td></tr>
      <tr><td></td><td><span class="skill-name">大湿婆密咒</span><div class="skill-note">限定 · (谷月轩优先)</div></td></tr>
      <tr><td></td><td><span class="skill-name">禅宗莲华功</span><div class="skill-note">限定 · (不动优先)</div></td></tr>
    </tbody>
  </table>
  <div class="note-box">💡 水盼盼是本作戏份最多的剑客，专属装备倚天剑仅她能装备。天外飞仙通过杭州吴桐小孩任务获取（和叶孤战斗），是她的专属。</div>
</details>

<!-- ===== 全角色速查总表 ===== -->
<div class="phase" style="margin-top: 30px;"><h2>📊 全角色速查总表</h2></div>
<div style="overflow-x: auto;">
  <table class="build-table" style="min-width: 900px;">
    <thead>
      <tr><th>角色</th><th>武器</th><th>定位</th><th>核心内功（3-4个关键）</th><th>核心招式（前6个最关键）</th></tr>
    </thead>
    <tbody>
      <tr><td class="skill-name">谷月轩</td><td>拳·腿·指</td><td>全能坦克</td>
        <td>逍遥鹏飞 · 小无相 · 九阳 · 九阴</td>
        <td>佛渡拜火三迦叶 · 天山六阳掌 · 火焰刀 · 空明拳 · 万佛朝宗 · 六脉神剑</td></tr>
      <tr><td class="skill-name">荆棘</td><td>刀+剑</td><td>输出</td>
        <td>逍遥雁行 · 日月 · 虎啸 · 血刀(仅1本!)</td>
        <td>坎离水火剑 · 幽冥十三式 · 抖鳞虎扑式 · 残存亦末路 · 魔刀七杀 · 八艘飞</td></tr>
      <tr><td class="skill-name">方云华</td><td>剑</td><td>最强刺客</td>
        <td>葵花宝典 · 武当九阳 · 倚天屠龙 · 紫霞</td>
        <td>辟邪剑法 · 流星飞坠 · 太极化清 · 天外飞仙 · 归藏剑 · 饮中八仙剑</td></tr>
      <tr><td class="skill-name">龙墨</td><td>刀</td><td>主力输出</td>
        <td>千仞 · 血刀(仅1本!) · 虎啸 · 罗汉</td>
        <td>浪花斩铁势 · 十殿阎罗刀 · 残存亦末路 · 狂风刀法 · 魔刀七杀 · 蚩尤刀法</td></tr>
      <tr><td class="skill-name">卫紫绫</td><td>毒·腿</td><td>毒系辅助</td>
        <td>龙腾豹变 · 星宿 · 鼎心无量 · 神龙密咒</td>
        <td>千蛛万毒手 · 化骨绵掌 · 化功大法 · 缠丝八爪 · 九阴白骨爪 · 紫翎霓裳舞</td></tr>
      <tr><td class="skill-name">史燕</td><td>暗器</td><td>偷窃工具人</td>
        <td>飞燕 · 鲸息 · 金雁 · 灵飞</td>
        <td>满天花雨 · 荆轲武诀 · 聂隐剑 · 燕子刺 · 乳燕归巢 · 烟雾弥漫</td></tr>
      <tr><td class="skill-name">不动</td><td>棍</td><td>第一坦克</td>
        <td>少林九阳 · 易筋经 · 金刚不坏 · 白首太玄</td>
        <td>不动明王棍 · 达摩武诀 · 一醉逍遥 · 天下无狗 · 灵蛇杖法 · 屠牛药叉</td></tr>
      <tr><td class="skill-name">萧复</td><td>琴</td><td>最强治疗</td>
        <td>七弦 · 太易 · 清心普善 · 声无哀乐</td>
        <td>百鸟朝凤曲 · 碧海潮生曲 · 笑傲江湖曲 · 全真剑法 · 十面埋伏曲 · 七弦奏天南</td></tr>
      <tr><td class="skill-name">沈湘云</td><td>剑</td><td>纯治疗·控制</td>
        <td>忘忧 · 洗髓 · 万物皆数 · 药王</td>
        <td>点血截脉 · 金针渡劫 · 清莲印法 · 饮中八仙 · 龙泣 · 迅雷</td></tr>
      <tr><td class="skill-name">塔娅</td><td>剑</td><td>治疗坦·BUFF</td>
        <td>道生一 · 太易 · 武林群侠传 · 易筋经</td>
        <td>骑士精神 · 乌衣宝典 · 天物刃 · 神曲但丁 · 饮中八仙 · 金蛇</td></tr>
      <tr><td class="skill-name">水盼盼</td><td>剑</td><td>剑客输出</td>
        <td>峨嵋九阳 · 正气 · 太易 · 吸星大法</td>
        <td>天外飞仙(专属) · 玉女剑法 · 龙泣剑 · 凝柔 · 金顶 · 冰心</td></tr>
    </tbody>
  </table>
</div>

<div class="note-box">
💡 <b>说明</b>：此表基于游戏实际数据验证。<br>
① 内功<strong>并非全角色通用</strong>——很多内功有角色限制（如先天功仅谷/古/商/萧复可学，血刀经仅刀系角色可学）。<br>
② 招式<strong>严格受武器类型限制</strong>——拳掌角色不能学剑法，反之亦然。通用武学（如六脉神剑）仅指系/部分角色可学。<br>
③ 标 ⭐ 为角色关键/专属技能，标 📖 为可购秘籍补位。<br>
④ 数量不足6内功/12招式时不强行填充，宁缺毋滥。
</div>

</div><!-- /tab-builds -->'''

new_content = content[:start_pos] + new_builds + content[end_pos:]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

# Verify
with open(html_path, "r", encoding="utf-8") as f:
    final = f.read()

import re
div_open = len(re.findall(r'<div\b', final))
div_close = len(re.findall(r'</div>', final))
print(f"<div> tags: {div_open}, </div> tags: {div_close}, diff: {div_open - div_close}")

tabs = ["tab-flow", "tab-side", "tab-rumor", "tab-locations", "tab-recruits",
        "tab-builds", "tab-check", "tab-items"]
for t in tabs:
    count = final.count(f'id="{t}"')
    print(f"  {t}: {count}")

print(f"\nTotal lines: {len(final.splitlines())}")
print("Done!")
