"""
Rebuild the flow tab (tab-flow) with a correct chronological timeline,
integrating all item acquisition, recruitment, and quest chains.
"""

import re

html_path = r"c:\Users\yanshijie\WorkBuddy\Claw\outputs\侠客风云传前传_终极全攻略.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find tab-flow boundaries
start_marker = '<div class="tab-content active" id="tab-flow">'
end_marker = '</div><!-- /tab-flow -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    print("ERROR: Cannot find tab-flow boundaries!")
    exit(1)

end_idx += len(end_marker)

new_tab_content = r'''<div class="tab-content active" id="tab-flow">

<div class="priority-box">
  <h3>🔑 十大易错过警告</h3>
  <ul>
    <li><strong>1.</strong> 无名冢杀傀尸前 → <strong>必须先去杭州触发"小孩见僵尸"</strong>（否则楚绘永远无法入队）</li>
    <li><strong>2.</strong> 杭州找龙墨前 → <strong>必须完成洛阳客栈小孟支线（带沈湘云）</strong></li>
    <li><strong>3.</strong> 血色姻缘线路4（东海分舵敖广）→ <strong>必须在赛王府之前完成</strong>（否则渔夫不解锁赛王府）</li>
    <li><strong>4.</strong> 赛王府 → <strong>先天功4张残页先集齐</strong> + <strong>必带史燕</strong>（偷软猬甲/黑玉镯/铁罗汉）</li>
    <li><strong>5.</strong> 山林地堡 → <strong>必带岳胖子+内功满级</strong>（否则坏结局）</li>
    <li><strong>6.</strong> 恶人谷任务 → <strong>尽快清完</strong>（花族拜火大典后可能触发色目人入侵，全部清除！）</li>
    <li><strong>7.</strong> 雪地野店 → <strong>先拿冲灵剑法再进</strong>（华山残页→铸剑山庄墙壁→冲灵剑法→再去雪地）</li>
    <li><strong>8.</strong> 修罗宫开放期间 → <strong>带沈湘云找洛翎枫</strong>（点穴截脉）</li>
    <li><strong>9.</strong> 救阿修罗 → <strong>不杀赵龙</strong>（否则夜叉不入队）</li>
    <li><strong>10.</strong> <strong>燕宇入队后再做支线+传闻</strong>（阅历翻倍甚至更多！）</li>
  </ul>
</div>

<!-- #################### 序章 #################### -->
<div class="phase"><h2>📌 序章 · 逍遥谷 → 弦剑山庄</h2></div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍逍遥谷 — 初始选择</h3>
  <div class="info">
    <strong>选择天龙教</strong>（推荐）→ 谷月轩「并肩作战」+ 荆棘「唯我独尊」100%暴击<br>
    选择酆都 → 谷月轩「惺惺相惜」+ 荆棘「以眼还眼」<br>
    💡 建议打赢，否则缺初始天赋
  </div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍逍遥谷 — 北边上山找老胡</h3>
  <div class="info">荆棘 1v1 老胡（建议打赢）→ <strong>八方藏刀式精要、藤甲、小还丹</strong></div>
</div>

<div class="card">
  <h3><span class="tag i">物品</span> 📍逍遥谷 — 全搜刮</h3>
  <table>
    <tr><th>位置</th><th>内容</th><th>条件</th></tr>
    <tr class="hl"><td>喂猫（老胡旁屋子拿咸鱼）</td><td>选项3「一本破烂的书」= <strong>仙音乐集</strong>（必拿！）<br>其余选项 = 智慧果</td><td>咸鱼</td></tr>
    <tr><td>右侧下方小屋一楼</td><td>肉包子</td><td>—</td></tr>
    <tr><td>右侧下方小屋二楼</td><td>逍遥散、九转还魂丹</td><td>—</td></tr>
    <tr><td>右侧下方小屋二楼床铺</td><td>荆棘秘籍</td><td>—</td></tr>
    <tr><td>左侧下方小屋</td><td>岳胖子掉落 → 武林宝典</td><td>岳胖子在队（后期）</td></tr>
    <tr><td>右侧上方小屋</td><td>看画 → 佛渡拜火三迦叶前置</td><td>根骨85+悟性80（后期）</td></tr>
    <tr><td>左侧上方小屋</td><td>萧复家书</td><td>—</td></tr>
    <tr><td>一楼古琴</td><td>摸琴</td><td>萧复+水盼盼触发少林寺剧情后</td></tr>
    <tr><td>找师父无瑕子切磋</td><td>第一次切磋 → 小无相功+日月神功+刀山剑岳（大/二内功8级）<br>第二次切磋 → 天山六阳掌+天山折梅手（大内功7级+二走剑行刀8级）</td><td>—</td></tr>
  </table>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍弦剑山庄 → 弦箫洞</h3>
  <div class="info">
    多打小怪刷传闻，主角内功到7级再打BOSS<br>
    解密：故意答错得阅历（荆棘听瀑布3次+阅历）。正确答案：<strong>宫→徵→羽→商→角</strong><br>
    出幽谷后河道捡鱼：草鱼×5、神鱼×1、虹鲤×1、咸鱼×7
  </div>
</div>

<div class="card">
  <h3><span class="tag i">物品</span> 📍弦箫幽谷 — 种植</h3>
  <div class="info">
    首次进图收白菜 → 智慧果滚地 → 种出9个（可反复种）<br>
    悟性80+ → 摸棋盘 → <strong>十王走马式</strong><br>
    萧复悟性60+ → 摸琴 → <strong>声无哀乐论</strong>
  </div>
</div>

<div class="card missable">
  <h3><span class="tag x">易错过</span> 回逍遥谷禀报前 → 先解锁大地图</h3>
  <div class="info">建议先去弦箫洞转弦箫幽谷 → <strong>激活大地图</strong> → 再回逍遥谷禀报</div>
</div>

<!-- #################### 第一阶段 #################### -->
<div class="phase"><h2>📌 第一阶段 · 报告三大门派 + 疯狂招队友</h2>
<p class="desc">核心原则：<strong>燕宇必须第一个招！</strong>之后所有支线+传闻奖励翻倍。</p></div>

<div class="priority-box" style="background: linear-gradient(135deg, #e8f5e9, #c8e6c9); border-color: var(--tag-recruit);">
  <h3 style="color: var(--tag-recruit);">🟢 本阶段开始前确认</h3>
  <ul>
    <li><strong>身上物品：</strong>咸鱼（喂猫用，老胡旁屋子）、虹鲤（沈湘云小孟支线用）</li>
    <li><strong>队友状态：</strong>只有主角三人</li>
    <li><strong>目标：</strong>一口气招齐所有早期队友，阵容齐全再推主线</li>
  </ul>
</div>

<div class="card missable">
  <h3>⛩️ 第1站：青城派 — 招燕宇！（阅历翻倍·最优先！）</h3>
  <div class="info">
    <span class="loc">📍 青城派</span><br>
    <strong>操作：</strong>荆棘对战燕宇（输赢不影响）→ 燕宇入队<br>
    右侧门人 → 归还华山玉佩 → <strong>灵飞经</strong>
  </div>
  <div class="reward">⚠️ 燕宇在队 = 所有支线阅历翻倍（1→3、2→4）！之后所有步骤务必带燕宇</div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍少林 → 武当 → 华山 — 报告三大门派</h3>
  <div class="info">
    <span class="loc">📍 少林寺：</span>无因方丈 → 得达摩像<br>
    <span class="loc">📍 武当派：</span>卓人清 → 得三黄宝腊丹×3、梯云踪<br>
    <span class="loc">📍 华山派：</span>曹睿 → 得连山决/正气诀<br>
    <strong>⚠️ 华山派务必做：</strong>左边山道找NPC对话 → 凉亭找曹萼华 → <strong>冲灵残页</strong>（赛王府线前置！）
  </div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> 📍洛阳 — 接���来按顺序高效招人</h3>
  <div class="info">
    <strong>⚠️ 进洛阳城首日务必触发四大事件：</strong>关伟撞人、监狱道人问斩、郊外猎人被鹰啄、菜篮大盗。不触发 = 永久关闭！
  </div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ① 📍忘忧谷 — 沈湘云（第一个治疗）</h3>
  <div class="info">
    <span class="loc">📍 忘忧谷</span> · <span class="action">触发沈湘云剧情</span> → 邀入队<br>
    <span class="teammate">👤 用：沈湘云</span><br>
    <strong>🎁 附带：</strong>沈湘云入队后马上做洛阳小孟支线（见下方）
  </div>
</div>

<div class="card missable">
  <h3><span class="tag s">支线</span> 📍洛阳客栈 — 小孟支线（<strong>龙墨线绝对前置！</strong>）</h3>
  <div class="info">
    <span class="loc">📍 洛阳</span> · <span class="teammate">👤 必须带：沈湘云</span><br>
    <strong>操作：</strong>
    <ol>
      <li>古董店门外跟老奶奶对话 → 需要虹鲤</li>
      <li>去集市鱼贩买虹鲤</li>
      <li>去郊外找鲤鱼王对话 → 选「找其他办法」</li>
      <li>去河洛客栈厨房点击鱼 → 同意快刀小孟请求</li>
      <li>沈湘云 + 快刀小孟 对战 骆翎枫 → <strong>故意战败！</strong></li>
      <li>将虹鲤交给老奶奶</li>
    </ol>
  </div>
  <div class="reward"><strong>🎁</strong> 迅雷剑法 + 2点阅历（燕宇在队4点）+ 沈湘云悟性+3 气血+100</div>
  <div class="warning"><strong>⚠️ 必须在杭州找龙墨之前完成！</strong>否则龙墨线永远无法触发</div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ② 📍成都客栈 — 水盼盼（第二名队友）</h3>
  <div class="info">
    <span class="loc">📍 成都客栈</span><br>
    <strong>操作：</strong>荆棘对战水盼盼（输赢不影响）→ 水盼盼入队<br>
    <span class="teammate">👤 水盼盼入队</span>（剑法输出）
  </div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ③ 📍森林 — 史燕（第三名·最重要偷窃角色！）</h3>
  <div class="info">
    <span class="loc">📍 森林</span><br>
    <strong>操作：</strong>花 <strong>1万钱</strong> 招募史燕入队<br>
    <span class="teammate">👤 史燕入队</span>（暗器/偷窃——游戏中最重要的功能性队友）
  </div>
  <div class="reward"><strong>💡 核心价值：</strong>所有BOSS战都可偷稀有物品。越早招越好！</div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ④ 📍洛阳白马寺 — 江瑜</h3>
  <div class="info">
    <span class="loc">📍 洛阳白马寺</span><br>
    <strong>操作：</strong>跟住持对话 → 答题 → 答案：弃恶从善→放下执着→明心见性 → <strong>禅宗莲华功</strong> + 江瑜入队
  </div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍洛阳 — 姜望答题 + 白马寺答题</h3>
  <div class="info">
    白马寺左上凉亭 → 面摊找姜望 → 答案：<strong>2-1-4-4-3</strong> → 卫紫绫+谷月轩悟性+1
  </div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ⑤ 📍洛阳酒馆 → 杜康村 — 傅剑寒</h3>
  <div class="info">
    <span class="loc">📍 洛阳酒馆</span><br>
    <strong>操作：</strong>右下角找老头对话 → 傅剑寒与无颠斗酒比武 → 卫紫绫掺水 → 荆棘单挑（输赢不影响）→ <strong>不要走！点地上无颠 → 桌下捡大金刚拳精要</strong><br>
    <span class="loc">📍 杜康村</span><br>
    找哭泣的李大娘 → 吃面客人 → 回李大娘 → 傅剑寒出现 → 洛阳衙门→集市(鱼/肉/画/杂货/面贩逐一对话) → 李大娘拿信 → 门口看门人 → 药铺斜对面赵娘子 → 酒馆等傅剑寒 → 夜探钱府(<strong>有史燕顺便拿右边夜明珠</strong>) → 密道打完 → 杜康村李大娘旁找傅剑寒入队<br>
    <span class="teammate">👤 傅剑寒入队 + 史燕(顺路拿夜明珠)</span>
  </div>
  <div class="reward"><strong>🎁</strong> 大金刚拳精要（酒馆桌下）</div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ⑥ 📍森林 → 铸剑山庄 — 任剑南</h3>
  <div class="info">
    <span class="loc">📍 森林</span> · <span class="teammate">👤 需要：萧复在队</span><br>
    <strong>操作：</strong>带萧复去森林找弹琴的任剑南 → 得笑傲江湖曲 → 萧复练到<strong>7重</strong> → 再回森林找任剑南合奏 → 打贺陀 → 铸剑山庄找任剑南入队<br>
    <span class="teammate">👤 任剑南入队</span><br>
    <strong>🎁 附带：</strong>沧海一笑（铸剑山庄，萧复在队）、情义七剑（调查剑冢断剑，根骨64）
  </div>
  <div class="warning">⚠️ 笑傲江湖曲必须练到7重才能触发第二次森林对话</div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ⑦ 📍少林寺 — 史燕偷和尚 + 百鸟朝凤曲</h3>
  <div class="info">
    <span class="loc">📍 少林寺</span> · <span class="teammate">👤 需要：史燕在队</span><br>
    <strong>操作：</strong><strong>水盼盼+萧复入队前</strong>，先带史燕去少林入口最右边找两个和尚对话<br>
    → 再带水盼盼+萧复来少林 → <strong>百鸟朝凤曲</strong> → 铜人开打<br>
    <span class="teammate">👤 史燕 → 水盼盼+萧复</span>
  </div>
  <div class="reward"><strong>🎁</strong> 百鸟朝凤曲 + 罗汉伏魔棍</div>
  <div class="warning"><strong>⚠️ 必须在水盼盼+萧复入队前先带史燕去！</strong>否则永久错过</div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ⑧ 📍忘忧谷 → 弦剑山庄 — 萧复</h3>
  <div class="info">
    <span class="loc">📍 忘忧谷</span> → 弦剑山庄剧情 → 萧复入队<br>
    <span class="teammate">👤 萧复入队</span>（治疗+琴系辅助）
  </div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ⑨ 📍杭州 → 成都破庙 → 武当 — 方云华</h3>
  <div class="info">
    <span class="loc">📍 杭州</span>：自动触发安道煌剧情 → 解决<br>
    <span class="loc">📍 武当</span>：与古实对话 → 方云华失踪<br>
    <span class="loc">📍 成都破庙</span> · <span class="teammate">👤 需要：带史燕</span>：触发剧情（破庙在小摊左手岔路顶头）<br>
    <span class="loc">📍 武当</span>：找方云华入队
  </div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ⑩ 📍武当 — 古实</h3>
  <div class="info">
    完成方云华杭州剧情后 → 武当找古实对话 → 荆棘与古实切磋 → 入队<br>
    <span class="teammate">👤 古实入队</span>（拳掌/太极核心）
  </div>
</div>

<div class="card">
  <h3><span class="tag r">招募</span> ⑪ 📍八卦门 → 成都 → 东渡口 → 八卦门 — 商仲仁</h3>
  <div class="info">
    八卦门剧情 → 成都百草门 → 回八卦门大殿 → 东渡口入口(食物中毒) → 回八卦门打商仲智 → 入队<br>
    <span class="teammate">👤 商仲仁入队</span>（刀法）
  </div>
  <div class="reward"><strong>🎁</strong> 八卦游身掌、鹰爪功（左边书柜）、八卦乱环式（商仲仁在队打商鹤鸣）</div>
</div>

<div class="card">
  <h3>✅ 第一阶段完成确认</h3>
  <div class="info">
    现在队伍里应该有：<strong>燕宇、沈湘云、水盼盼、史燕、江瑜、傅剑寒、任剑南、萧复、方云华、古实、商仲仁</strong><br>
    确认事项：<br>
    ✅ 燕宇始终在队<br>
    ✅ 洛阳小孟支线已完成（沈湘云故意败）<br>
    ✅ 华山冲灵残页已拿到<br>
    ✅ 少林百鸟朝凤前置已做<br>
    ✅ 铸剑山庄已去（任剑南入队）<br>
  </div>
</div>

<!-- #################### 第二阶段 #################### -->
<div class="phase"><h2>📌 第二阶段 · 血色姻缘起始（线路4）+ 杭州前置</h2>
<p class="desc"><strong>⚠️ 血色姻缘线路4必须在赛王府之前完成！</strong>否则东渡口渔夫不解锁赛王府位置。</p></div>

<div class="priority-box" style="background: linear-gradient(135deg, #fff3cd, #ffe69c); border-color: var(--warn);">
  <h3 style="color: var(--warn);">🟡 本阶段总览</h3>
  <ul>
    <li><strong>线路4：</strong>东渡口救东瀛女 → 杭州码头暗号 → 东海分舵打敖广 → 回东渡口遇秦红殇</li>
    <li><strong>同时完成：</strong>杭州楚绘前置（小孩见僵尸）、洛阳丐帮血案前置、先天功传闻刷取</li>
    <li><strong>大地图注意：</strong>此阶段开始出现大量传闻，燕宇在队多走动刷传闻</li>
  </ul>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍洛阳 — 天剑门小师弟（含光剑链起点）</h3>
  <div class="info">
    <span class="loc">📍 洛阳天剑门左下角</span><br>
    <strong>操作：</strong>对话小师弟 → 选「鼓励他」→ 谷月轩对战拖到第6回合 → 对话西门峰选「义正词严」→ 对战西门峰 → 对话小师弟（杜康村后续）<br>
    <span class="teammate">👤 谷月轩</span>
  </div>
  <div class="reward"><strong>🎁</strong> 1点阅历（燕宇3点）+ 开启含光剑链</div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍杜康村 — 含光剑后续 + 傅剑寒招人</h3>
  <div class="info">
    杜康村对话天剑门小师弟 → 得家传宝剑 → 后续洛阳武器店（任剑南在队发现）→ <strong>含光剑</strong><br>
    <span class="teammate">👤 需要：任剑南（武器店识别）</span>
  </div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍杜康村 — 张帆不送花分支（吸星大法前置）</h3>
  <div class="info">
    <span class="loc">📍 杜康村门口张帆</span><br>
    <strong>操作：</strong>选「不帮张帆」→ 离开杜康村再进 → 再找张帆对话 → <strong>肚痛贴</strong><br>
    <span class="teammate">👤 无特殊要求</span>
  </div>
  <div class="reward"><strong>🎁</strong> 肚痛贴 → 后续带到喀什换<strong>吸星大法</strong>（最优先！）</div>
</div>

<div class="card missable">
  <h3><span class="tag x">易错过</span> 📍杭州 — 小孩见僵尸（<strong>楚绘线绝对前置！</strong>）</h3>
  <div class="info">
    <span class="loc">📍 杭州右上角</span> · <span class="teammate">👤 需要：带萧复</span><br>
    <strong>操作：</strong>找小孩对话 → 触发僵尸事件 → 史刚追捕夜飘香 → 回报小孩 → 获<strong>漂亮石头</strong><br>
    <span class="teammate">👤 萧复</span>
  </div>
  <div class="warning"><strong>⚠️ 必须在杀无名冢傀尸之前完成！</strong>否则楚绘永远无法入队，天外飞仙无法获得</div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍成都 — 猜谜得明光甲</h3>
  <div class="info">
    <span class="loc">📍 成都</span> · 跟少女猜谜<br>
    <strong>答案：</strong>一条鞭法 → 烧饼歌 → 阳明 → 知行合一 → 鄱阳湖 → <strong>明光甲</strong>
  </div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍洛阳 — 乞丐狗皮膏药（三选一·推荐留喀什）</h3>
  <div class="info">
    <span class="loc">📍 洛阳长虹镖局对面巷子</span><br>
    <strong>操作：</strong>施舍乞丐1000两 → 得狗皮膏药<br>
    <strong>⚠️ 三选一分支（背包里的膏药只有一个！）：</strong><br>
    ①交给驿站伙计 → 千锤百炼丹+连连城剑法精要<br>
    ②交给喀什NPC → <strong>吸星大法（推荐！）</strong><br>
    ③自己留着 → 无奖励但不消耗
  </div>
  <div class="warning">强烈建议狗皮膏药留给喀什换吸星大法！给驿站伙计就永远拿不到吸星大法了</div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍成都 — 喂狗开启丐帮血案线</h3>
  <div class="info">
    <span class="loc">📍 成都绝刀门前</span><br>
    <strong>操作：</strong>买包子 → 喂黄狗 → 跟着狗走到破庙前 → 发现人骨 → 开启丐帮血案<br>
    → 前往<strong>杭州丐帮分舵</strong>触发剧情 → 招募<strong>萧遥</strong>
  </div>
</div>

<div class="card missable">
  <h3><span class="tag x">易错过</span> 📍大地图 — 先天功残页传闻（赛王府前！）</h3>
  <div class="info">
    <strong>此阶段开始在大地图反复走动刷传闻：</strong><br><br>
    <strong>① 救状元郎</strong> → 洛阳豆腐西施处对话两人 → 大地图触发 → <strong>先天功残页1+2</strong><br>
    <strong>② 救云游商人</strong> → 乐山大佛附近闲逛 → <strong>先天功残页3</strong><br>
    <strong>③ 先天功残页4</strong> → 集齐3张后大地图触发<br>
    <strong>④ 帮助东瀛人打熊</strong> → 大地图随机 → <strong>九阴总纲</strong>（荆棘核心内功）<br>
    <strong>⑤ 森林偷熊</strong> → <strong>九阴总纲</strong>（备选获取方式）
  </div>
  <div class="warning"><strong>⚠️ 4张先天功残页必须在赛王府前集齐！</strong>进入赛王府后大地图传闻停止刷新</div>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍东渡口 → 杭州码头 → 东海分舵 — <strong>血色姻缘线路4</strong></h3>
  <div class="info">
    <span class="loc">📍 东渡口右侧码头</span><br>
    <strong>操作：</strong>自动触发剧情 → 听到买卖东瀛女子 → 紫绫教训两人<br>
    <span class="teammate">👤 无特殊要求</span><br>
    <br>
    <span class="loc">📍 杭州码头</span><br>
    <strong>操作：</strong>需要暗号才能登船 → 去<strong>杭州青楼</strong>找老鸨 → 套出海鲨帮暗号<br>
    <br>
    <span class="loc">📍 东海分舵</span><br>
    <strong>操作：</strong>杀上分舵 → 躲过广场敌人 → 进大船 → 荆棘跳出来 → 谷月轩单挑敖广 → 敖广认输 → 东瀛女子不愿离开<br>
  </div>
  <div class="reward"><strong>结束后回到东渡口 → 遇到秦红殇 → 血色姻缘正式开启</strong></div>
</div>

<div class="card">
  <h3>✅ 第二阶段完成确认</h3>
  <div class="info">
    ✅ 杭州小孩见僵尸已完成（楚绘前置）<br>
    ✅ 先天功残页开始刷（后续阶段继续刷）<br>
    ✅ 含光剑链第一段完成<br>
    ✅ 肚痛贴已拿（留给喀什换吸星大法）<br>
    ✅ 狗皮膏药已拿（留给喀什）<br>
    ✅ <strong>血色姻缘线路4已完成（东海分舵+敖广+遇秦红殇）</strong><br>
    ✅ 萧遥已招募
  </div>
</div>

<!-- #################### 第三阶段 #################### -->
<div class="phase"><h2>📌 第三阶段 · 黑蝠洞线 + 无名冢线</h2>
<p class="desc">两条主线并行推进。注意先做杭州僵尸前置、先天功传闻继续刷。</p></div>

<div class="priority-box" style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); border-color: var(--accent2);">
  <h3 style="color: var(--accent2);">🔵 本阶段总览</h3>
  <ul>
    <li><strong>黑蝠洞线：</strong>龙井村 → 少林/南少林 → 救不动 → 救孟婆 → 黑蝠洞解锁</li>
    <li><strong>毒龙教线：</strong>毒龙教 → 铁叉部 → 找毒蟾 → 小阿曼入队</li>
    <li><strong>黑蝠洞BOSS：</strong>带小阿曼+沈湘云杀欧阳笑</li>
    <li><strong>无名冢线：</strong>兽王庄纪玟中毒 → 藏海岛采花 → 乐山大佛打傀尸 → 无名冢</li>
    <li><strong>⚠️ 大地图继续刷：</strong>先天功残页、森林猴偷九阳神功（孟婆死后触发）、东瀛浪人偷明玉功</li>
  </ul>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍龙井村 — 黑蝠洞线起点</h3>
  <div class="info">
    <span class="loc">📍 龙井村井边</span> · 接救孟婆任务<br>
    <span class="teammate">👤 无特殊要求</span>
  </div>
</div>

<div class="card">
  <h3><span class="tag u">传闻</span> 📍少林寺 — 夜叉囚禁事件（黑蝠洞前置）</h3>
  <div class="info">
    <span class="loc">📍 大地图</span>：传闻「夜叉护法被少林囚禁」→ 前往少林寺<br>
    <strong>操作：</strong>少林门口左边和尚对话 → 战斗：我方6人+少林门人+铜人 vs 嫖+赌+公孙坚+天龙教众<br>
    <span class="teammate">👤 史燕（偷窃：洗髓再造丹×2、神恩通慧丹×2、霹雳宝甲、千锤百炼丹×3、飘飘丸×3）</span>
  </div>
  <div class="reward"><strong>🎁</strong> 无相劫指 + 5点阅历 + 大量偷窃物品</div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍南少林 → 原始野林 — 救不动</h3>
  <div class="info">
    <span class="loc">📍 南少林</span>：酆都来犯 → 左上找天悟禅师 → 右上找虚明 → 战斗 → 虚明谎称袈裟被偷 → 南少林南边绕触发战斗 → 袈裟拿回 → 南少林人死光 → 右上找天悟禅师<br>
    <span class="loc">📍 原始野林分岔口左边</span> → 救不动 → <strong>不动入队</strong><br>
    <span class="teammate">👤 不动入队</span>（棍法/第一坦克）<br>
    <strong>🎁 附带：</strong>混元功（原始森林救不动）
  </div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍黑蝠洞 — 救孟婆</h3>
  <div class="info">
    <span class="loc">📍 黑蝠洞</span> · <span class="teammate">👤 必须带：不动 + 古实 + 水盼盼</span><br>
    进入黑蝠洞救孟婆 → <strong>水盼盼暂时离队进修</strong>
  </div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍毒龙教 → 铁叉部 → 乐山大佛 — 小阿曼入队</h3>
  <div class="info">
    <span class="loc">📍 毒龙教</span>：打退阿傍 · <span class="teammate">👤 荆棘 → 单挑阿傍 → 抖鳞虎扑式</span><br>
    <span class="loc">📍 铁叉部</span>：打退罗蛇君<br>
    <span class="loc">📍 毒龙教蓝婷</span>：接千年毒蟾任务<br>
    <span class="loc">📍 成都宝福楼店小二</span>：线索 → 紫肤怪人乐山大佛<br>
    <span class="loc">📍 乐山大佛</span>：打毒 → 得<strong>千年毒蟾</strong> → 回毒龙教给蓝婷 → <strong>小阿曼入队</strong><br>
    <span class="teammate">👤 小阿曼入队</span>（鞭法）
  </div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍黑蝠洞 — 杀欧阳笑（沈湘云必须出场！）</h3>
  <div class="info">
    <span class="loc">📍 黑蝠洞</span> · <span class="teammate">👤 必须带：小阿曼（进洞必备） + 沈湘云（必须出战！否则沈澜不入队）</span><br>
    进入黑蝠洞 → 杀欧阳笑 → <strong>寒蝠胆</strong>（沈澜招募前置）→ 黑蝠洞线结束
  </div>
  <div class="warning"><strong>⚠️ 沈湘云必须在欧阳笑大战中出场！</strong>如果沈湘云没出战，沈澜只给钥匙不加入</div>
</div>

<div class="card missable">
  <h3><span class="tag x">易错过</span> 📍大地图 — 孟婆死后 → 森林偷猴 → 九阳神功</h3>
  <div class="info">
    <span class="loc">📍 大地图传闻</span> · <span class="teammate">👤 史燕</span><br>
    孟婆死后（黑蝠洞线完成），大地图出现传闻「森林有猴子，身上带着武功秘籍」<br>
    → 带史燕去森林 → 偷猴子 → <strong>九阳神功</strong>
  </div>
  <div class="warning"><strong>⚠️ 时间窗口：</strong>孟婆死后才触发，赛王府前完成最好</div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍洛阳 — 楚绘线+姜望（继续推进）</h3>
  <div class="info">
    <span class="loc">📍 洛阳古玩店</span>：鉴定漂亮石头 → 选<strong>「不卖」</strong>（卖了楚绘断线！）<br>
    <span class="loc">📍 杭州最右屋</span>：还给小孩的娘 → 跟旁边吴大叔对话 → 触发「看见神仙」<br>
    <span class="teammate">👤 傅剑寒在队 → 选「相信大叔」</span> → 遇神秘人 → 荆棘+傅剑寒打赢 → <strong>天外飞仙精要</strong>
  </div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍兽王庄 → 藏海岛 → 乐山大佛 — 无名冢前置</h3>
  <div class="info">
    <span class="loc">📍 兽王庄</span>：发现纪玟中毒（需藏海花）<br>
    <span class="loc">📍 东渡口 → 藏海岛</span>：出海采藏海花 → 谷月轩+任意三人 vs 花玖瑟<br>
    <span class="loc">📍 兽王庄</span>：交藏海花给纪玟<br>
    <span class="loc">📍 乐山大佛凌云窟</span>：打傀尸 → <strong>无名冢解锁</strong>
  </div>
</div>

<div class="card missable">
  <h3><span class="tag x">易错过</span> 📍无名冢 — 先左转救岳胖子！不要打傀尸！</h3>
  <div class="info">
    <span class="loc">📍 无名冢</span><br>
    <strong>⚠️ 进入无名冢后的操作顺序（严格！）：</strong><br>
    ① <strong>先左转</strong>走岔道 → 救岳胖子 → 出墓穴 → 左边小佛坛解机关 → 再进墓穴找岳胖子<br>
    ② 出无名冢再进 → 右上角找岳胖子<strong>入队</strong> → <strong>四选一武功（推荐天魔解体）</strong><br>
    ③ <strong>带方云华+任剑南</strong>去傀尸房间右边棺材 → <strong>葵花宝典 + 辟邪剑法 + 流星飞坠</strong><br>
    ④ 左边棺材 → <strong>荆轲武决</strong>（史燕暗器）<br>
    <span class="teammate">👤 岳胖子入队（非常重要的队友·偷窃+隐元阁解锁）</span>
  </div>
  <div class="warning"><strong>⚠️ 绝对不要先打傀尸！</strong>打傀尸后葵花宝典等部分物品永久消失。先左转救胖子！</div>
  <div class="reward"><strong>🎁</strong> 天魔解体（推荐）、葵花宝典、辟邪剑法、流星飞坠、荆轲武决</div>
</div>

<div class="card">
  <h3>✅ 第三阶段完成确认</h3>
  <div class="info">
    ✅ 黑蝠洞线完成（欧阳笑已杀、寒蝠胆已得）<br>
    ✅ 不动已入队<br>
    ✅ 小阿曼已入队<br>
    ✅ 无名冢线完成（岳胖子入队、葵花三件套已拿）<br>
    ✅ 九阳神功已偷（或已确认传闻触发）<br>
    ✅ 天外飞仙精要已拿<br>
    ✅ 先天功残页继续刷（还有残页4！）<br>
    <strong>⚠️ 确认先天功4张残页状态——下一阶段赛王府前必须集齐！</strong>
  </div>
</div>

<!-- #################### 第四阶段 #################### -->
<div class="phase"><h2>📌 第四阶段 · 赛王府线</h2>
<p class="desc"><strong>⚠️ 本阶段是游戏最大的「错过点」——先天功残页、软猬甲、左右互搏、坎离水火剑都在此。</strong></p></div>

<div class="priority-box" style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); border-color: var(--tag-miss);">
  <h3 style="color: var(--tag-miss);">🟠 进入赛王府前终极检查</h3>
  <ul>
    <li><strong>✅ 先天功4张残页已全部集齐！</strong>（如果缺→回大地图刷传闻直到集齐）</li>
    <li><strong>✅ 史燕在队</strong>（偷软猬甲+黑玉镯+罗汉拳）</li>
    <li><strong>✅ 水盼盼已练好玉女心经+玉女剑法</strong>（大地图杨雨枫剧情→习得玉女剑法+玉女心经）</li>
    <li><strong>✅ 已确定要带谁学左右互搏</strong>（不动/古实/小阿曼/花痴中至少一个）</li>
    <li><strong>✅ 雪地野店不能换队友！</strong>提前组好队伍再出发</li>
  </ul>
</div>

<div class="card missable">
  <h3><span class="tag s">支线</span> 📍华山 → 铸剑山庄 — 冲灵剑法（赛王府绝对前置！）</h3>
  <div class="info">
    <span class="loc">📍 华山左边山道</span>：找NPC对话 → 凉亭找曹萼华 → 回报NPC → 对战华山门人 → <strong>冲灵残页</strong><br>
    <span class="loc">📍 铸剑山庄</span> · <span class="teammate">👤 需要：傅剑寒+冲灵残页</span>：右侧老管家对话 → 左侧墙壁触发 → <strong>冲灵剑法</strong>
  </div>
  <div class="warning"><strong>⚠️ 必须在去雪地野店之前完成！</strong>先去雪地野店→冲灵剑法再也拿不到</div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍大地图 — 水盼盼玉女剑法</h3>
  <div class="info">
    <span class="loc">📍 大地图随机</span>：遇杨雨枫（神雕侠侣后人）→ 水盼盼习得<strong>玉女剑法+玉女心经</strong><br>
    <strong>如果还没触发，赛王府前多在大地图走动</strong>
  </div>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍东渡口 → 雪地野店 — 雪地练剑（三天）</h3>
  <div class="info">
    <span class="loc">📍 东渡口</span>：找海边小船旁戴帽子渔夫对话 → 得知水盼盼在赛王府<br>
    <strong>（此渔夫需线路4完成后才解锁！这就是为什么线路4必须在赛王府前做）</strong><br>
    <br>
    <span class="loc">📍 雪地野店</span> · <span class="teammate">👤 必须带：萧复 + 水盼盼 + 荆棘（已拿冲灵剑法）</span><br>
    <span class="teammate">👤 推荐带：不动/古实/小阿曼/花痴（学左右互搏·至少一个）</span><br>
    <strong>⚠️ 雪地野店不能换队友！进去前组好队伍！</strong><br>
    <br>
    <strong>第一天：</strong>萧复修炼全真剑法<br>
    <strong>第二天：</strong>大师兄习得<strong>空明拳</strong><br>
    <strong>第三天：</strong><strong>左右互搏</strong>传授（不动/古实/小阿曼/花痴中至少一人）<br>
    <br>
    <strong>冲灵剑法换坎离水火剑：</strong>将冲灵剑法交给岳在渊 → 荆棘 vs 岳在渊坚持4回合 → 三选一拒绝（金蛇剑法/天涯明月刀/铁拳）→ <strong>坎离水火剑精要</strong>（荆棘专属！）
  </div>
  <div class="warning"><strong>⚠️ 雪地野店不能换人！</strong>出发前务必确认：萧复+水盼盼+荆棘（已拿冲灵剑法）+ 不动/古实/小阿曼/花痴至少一个</div>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍赛王府 — 赛王府大战（<strong>全程最关键的BOSS战！</strong>）</h3>
  <div class="info">
    <span class="loc">📍 赛王府</span> · <span class="teammate">👤 <strong>必须带：史燕（偷窃！）</strong></span> · <span class="teammate">👤 推荐带：江瑜（看战马册·丐帮血案）</span><br>
    <br>
    <strong>⚠️ 赛王府战斗前确认：</strong><br>
    ① <strong>先天功4张残页已集齐</strong>（找天机老道 → 选「复原武学」→ 获得<strong>先天功</strong>）<br>
    ② <strong>史燕在出战队伍中</strong><br>
    ③ 江瑜在队（看战马册）<br>
    <br>
    <strong>战斗流程：</strong><br>
    1. 进入赛王府 → 先找天机老道复原先天功<br>
    2. 推进剧情战斗 → <strong>史燕偷取：软猬甲+黑玉镯+罗汉拳</strong><br>
    3. 杀小王爷 → 获得<strong>血刀经+血刀刀法</strong>
  </div>
  <div class="reward"><strong>🎁</strong> 先天功 + 软猬甲 + 黑玉镯 + 罗汉拳 + 血刀经 + 血刀刀法</div>
  <div class="warning">
    <strong>⚠️ 赛王府战斗只打一次！错过不补！</strong><br>
    ① 先天功残页不齐就杀小王爷 = 永久失去先天功<br>
    ② 没带史燕 = 永久失去软猬甲+黑玉镯<br>
    ③ 赛王府后先天功残页再也无法获取
  </div>
</div>

<div class="card missable">
  <h3><span class="tag s">支线</span> 📍怪医居 — 寒蝠胆提交（沈澜招募前置）</h3>
  <div class="info">
    <span class="loc">📍 怪医居</span><br>
    <strong>操作：</strong>赛王府完成后 → 将<strong>寒蝠胆</strong>交给沈澜<br>
    ⚠️ 前提：沈湘云在黑蝠洞欧阳笑大战中出场 → 沈澜加入（否则只给钥匙）<br>
    <strong>沈澜给钥匙 → 藏海岛开宝箱 → <span style="color:var(--accent);font-weight:700;">神龙密咒</span> + 化骨绵掌 → 沈澜入队</strong><br>
    <br>
    <strong>后续：</strong>怪医居左边毒鼎 → <span class="teammate">👤 小阿曼在队</span> → 放入五毒各5只 → 卫紫绫<strong>鼎心无量功</strong>
  </div>
</div>

<div class="card">
  <h3>✅ 第四阶段完成确认</h3>
  <div class="info">
    ✅ 先天功已获得<br>
    ✅ 坎离水火剑已获得（荆棘）<br>
    ✅ 左右互搏已学（不动/古实/小阿曼/花痴）<br>
    ✅ 软猬甲+黑玉镯+罗汉拳已偷<br>
    ✅ 血刀经+血刀刀法已获得<br>
    ✅ 神龙密咒+化骨绵掌已获得<br>
    ✅ 沈澜已入队（或已得钥匙）<br>
    ✅ 鼎心无量功已获得（卫紫绫）<br>
  </div>
</div>

<!-- #################### 第五阶段 #################### -->
<div class="phase"><h2>📌 第五阶段 · 血色姻缘后续（线路5→6→7→8）</h2>
<p class="desc">现在赛王府已完成，回来继续推进血色姻缘。线路5（龙墨）、6（史义）、7（陆少临）可并行推进。</p></div>

<div class="priority-box" style="background: linear-gradient(135deg, #f3e5f5, #e1bee7); border-color: var(--tag-hidden);">
  <h3 style="color: var(--tag-hidden);">🟣 本阶段总览</h3>
  <ul>
    <li><strong>线路5：</strong>龙墨线 —— 杭州青楼找龙墨 → 罗刹分舵 → 成都调停 → 龙墨入队</li>
    <li><strong>线路6：</strong>史义线 —— 景阳冈找史义 → 洛阳 → 史义入队</li>
    <li><strong>线路7：</strong>陆少临线 —— 杜康村 → 丐帮 → 白马寺 → 乐山大佛</li>
    <li><strong>线路8：</strong>秦红殇线 —— 东渡口集合 → 花族塔娅 → 打黑冢罗王 → 秦红殇入队</li>
  </ul>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍杭州青楼 → 罗刹分舵 → 成都 — <strong>血色姻缘线路5·龙墨线</strong></h3>
  <div class="info">
    <strong>⚠️ 前提确认：洛阳客栈小孟支线必须已完成！</strong><br>
    <br>
    <span class="loc">📍 杭州青楼</span>：找龙墨（点苍派少主）→ 触发剧情战斗<br>
    <span class="loc">📍 杭州客栈前</span>：与点苍弟子对话<br>
    <span class="loc">📍 罗刹分舵</span>：连续两场恶战<br>
    <span class="loc">📍 成都门口</span>：各门派要废龙墨武功<br>
    <span class="loc">📍 忘忧谷</span>：招募<strong>花痴</strong><br>
    <span class="loc">📍 成都唐门前</span> · <span class="teammate">👤 带花痴</span>：找剑圣帮忙 → 单挑撑过回合<br>
    <span class="loc">📍 集市</span>：伏击龙墨 → <span class="loc">📍 乐山大佛</span>：招募龙墨<br>
    <span class="teammate">👤 龙墨入队</span>（刀法/浪花斩铁势——游戏最强单体伤害）
  </div>
  <div class="reward"><strong>🎁</strong> 幽冥十三式（成都接剑圣三招）、佛山无影脚、神农济世<br><strong>💡 龙墨入队后马上做：</strong>带龙墨去藏海岛右侧沙滩 → 领悟<strong>浪花斩铁势</strong></div>
  <div class="warning"><strong>⚠️ 洛阳小孟支线没做 → 龙墨线永远无法触发！</strong></div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍景阳冈 → 洛阳 — <strong>血色姻缘线路6·史义线</strong></h3>
  <div class="info">
    <span class="loc">📍 景阳冈左上方</span>：帮史刚打退敌人 → 回山顶找<strong>史义入队</strong>（棍法）<br>
    <strong>🎁 附带：</strong>地煞绝命腿（景阳冈阿森任务→再次对话，臂力80）<br>
    <span class="teammate">👤 史义入队</span>
  </div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍杜康村 → 丐帮 → 白马寺 → 乐山大佛 — <strong>血色姻缘线路7·陆少临线</strong></h3>
  <div class="info">
    <span class="loc">📍 杜康村</span>：陆少临被劫镖剧情<br>
    <span class="loc">📍 杭州丐帮分舵</span>：触发剧情<br>
    <span class="loc">📍 白马寺</span>：货物被劫剧情<br>
    <span class="loc">📍 乐山大佛</span>：完成任务线 → 招募<strong>陆少临</strong>（刀法）
  </div>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍东渡口 → 花族 — <strong>血色姻缘线路8·秦红殇线</strong></h3>
  <div class="info">
    <strong>前提：线路5（龙墨）、6（史义）、7（陆少临）全部完成</strong><br>
    <br>
    <span class="loc">📍 东渡口最里面码头</span>：找秦红殇继续任务<br>
    <span class="loc">📍 忘忧谷</span>：找仙音 → 卫紫绫习得<strong>兰花拂穴手</strong><br>
    <span class="loc">📍 森林</span>：救被点穴的沐郡主<br>
    <span class="loc">📍 东渡口</span>：找汤木 → 需要造船<br>
    <span class="loc">📍 花族部落</span>：长老被囚 → 塔娅翻译 → 说服汤木造船<br>
    <br>
    <strong>花族塔娅入队流程：</strong><br>
    ① 恶人谷救下花族长老<br>
    ② 前往花族部落 → 跟长老对话 → 跟塔娅到右上星象塔<br>
    ③ 收集三张字条：门口右边/长老右边门/村庄栅栏<br>
    ④ 回塔里 → 自动触发 → <strong>塔娅入队</strong><br>
    <br>
    <span class="loc">📍 东渡口</span>：乘船出海 → 和亲船上 → <strong>打黑冢罗王</strong>（沐郡主牺牲）→ 回岸<br>
    <span class="loc">📍 东渡口</span>：<strong>秦红殇入队</strong>
  </div>
  <div class="reward"><strong>🎁</strong> 霹雳刀（和亲船→稚嫩笔迹的信还给秦红殇左边小兵）、塔娅骑士精神（恶人谷四连战后）</div>
</div>

<div class="card">
  <h3>✅ 第五阶段完成确认</h3>
  <div class="info">
    ✅ 龙墨已入队 + 浪花斩铁势已领悟<br>
    ✅ 史义已入队<br>
    ✅ 陆少临已入队<br>
    ✅ 秦红殇已入队 + 塔娅已入队<br>
    ✅ 黑冢罗王已杀<br>
    <strong>💡 塔娅骑士精神：</strong>带塔娅+沈湘云去恶人谷进行四连战（下阶段完成）
  </div>
</div>

<!-- #################### 第六阶段 #################### -->
<div class="phase"><h2>📌 第六阶段 · 恶人谷 + 绿柳山庄</h2>
<p class="desc">龙墨线引发恶人谷开放 → 高昌迷宫救夜叉 → 修罗宫 → 绿柳山庄。注意不杀赵龙、恶人谷任务速清。</p></div>

<div class="priority-box" style="background: linear-gradient(135deg, #ffe0e0, #ffb3b3); border-color: #c0392b;">
  <h3 style="color: #c0392b;">🔴 本阶段核心警告</h3>
  <ul>
    <li><strong>⚠️ 不杀赵龙！</strong>杀了→夜叉不入队</li>
    <li><strong>⚠️ 恶人谷任务尽快清完！</strong>花族拜火大典后色目人入侵→全部清除</li>
    <li><strong>⚠️ 修罗宫开放期间带沈湘云找洛翎枫</strong>→点穴截脉</li>
    <li><strong>⚠️ 绿柳山庄必须带水盼盼！</strong>→倚天断剑</li>
  </ul>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍原始野林 → 恶人谷 — 恶人谷开放</h3>
  <div class="info">
    <span class="loc">📍 原始野林</span>：打番僧 → <strong>恶人谷解锁</strong><br>
    <strong>⚠️ 进入恶人谷后的策略：</strong><br>
    ① <strong>先清完所有恶人谷支线任务！</strong>（薛鬼医、贺陀无戒等）<br>
    ② 然后推进主线 → 高昌迷宫杀心残救夜叉<br>
    ③ 不杀赵龙！<br>
    <br>
    <strong>如果塔娅已入队：</strong>带塔娅+沈湘云在恶人谷进行四连战 → 塔娅习得<strong>骑士精神</strong>
  </div>
  <div class="warning"><strong>⚠️ 花族拜火大典后易触发色目人入侵！</strong>恶人谷全部任务永久清除！必须在拜火大典前清完恶人谷所有内容</div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍高昌迷宫 — 杀心残 → 救夜叉</h3>
  <div class="info">
    <span class="loc">📍 高昌迷宫</span><br>
    杀心残 → 意外救出夜叉 → 出遗迹遭遇游进围堵 → 突围 → 得知阿修罗失踪<br>
    <span class="teammate">👤 注意：不要杀赵龙！</span>
  </div>
</div>

<div class="card missable">
  <h3><span class="tag s">支线</span> 📍修罗宫 — 带沈湘云找洛翎枫</h3>
  <div class="info">
    <span class="loc">📍 修罗宫</span> · <span class="teammate">👤 必须带：沈湘云</span><br>
    修罗宫开放期间 → 厢房找<strong>小孟女友洛翎枫</strong> → 沈湘云习得<strong>点穴截脉</strong>（最强单体控制）<br>
    <span class="teammate">👤 带岳胖子</span> → 额外拿武学
  </div>
  <div class="warning"><strong>⚠️ 完成修罗宫主线后永久关闭！</strong>必须趁开放期间完成</div>
</div>

<div class="card">
  <h3><span class="tag s">支线</span> 📍成都 — 封青霄线（九阳神功获取）</h3>
  <div class="info">
    <span class="loc">📍 成都羊肉汤店</span>：自动触发封青霄教训贺陀无戒剧情<br>
    → 买下簪子 → 衙门还给封青霄 → 封家得知妹妹需九阳<br>
    → 成都破庙前六扇门抓封青霄 → 少林找方丈<br>
    → 回成都找卖菜大婶 → 姜望屋内 → 得知贺陀无戒搞鬼<br>
    → 恶人谷打贺陀无戒 → 回封家 → 拜托找九阳<br>
    <strong>（已有九阳神功的话可直接完成）</strong>
  </div>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍绿柳山庄 — <strong>必须带水盼盼！</strong></h3>
  <div class="info">
    <span class="loc">📍 喀什</span> → 哈什面摊 → <strong>绿柳山庄解锁</strong><br>
    <span class="teammate">👤 <strong>必须带：水盼盼！</strong></span><br>
    进入绿柳山庄 → 自动触发剧情 → 获<strong>倚天断剑</strong><br>
    <br>
    <strong>倚天剑完成链：</strong><br>
    ① 绿柳山庄带水盼盼 → 倚天断剑<br>
    ② 铸剑山庄找任浩然 → 需要<strong>西方异金</strong><br>
    ③ 大地图传闻「西方异金持有者」→ 偷取（番僧/锦衣卫等随机持有）<br>
    ④ 交给任浩然 → <strong>倚天剑</strong>（水盼盼专属，伤害+410，击杀再行动）
  </div>
  <div class="warning"><strong>⚠️ 没带水盼盼 = 永久失去倚天剑！</strong></div>
</div>

<div class="card">
  <h3>✅ 第六阶段完成确认</h3>
  <div class="info">
    ✅ 恶人谷全部任务已清理<br>
    ✅ 高昌迷宫已完成（不杀赵龙）<br>
    ✅ 修罗宫洛翎枫已完成（点穴截脉）<br>
    ✅ 塔娅骑士精神已获得<br>
    ✅ 倚天断剑已获得 → 西方异金已偷 → 倚天剑已打造<br>
    ✅ 封青霄线已完成<br>
  </div>
</div>

<!-- #################### 第七阶段 #################### -->
<div class="phase"><h2>📌 第七阶段 · 花族 + 终章</h2>
<p class="desc">最后的主线推进——花族线 → 山林地堡 → 决战辟邪宫。最终检查清单务必逐项确认！</p></div>

<div class="priority-box">
  <h3>🔑 终章前终极检查清单</h3>
  <ul>
    <li>✅ 楚绘已入队（杭州僵尸前置→全链完成）</li>
    <li>✅ 先天功已获得（4残页集齐+天机老道复原）</li>
    <li>✅ 软猬甲+黑玉镯已偷（赛王府史燕）</li>
    <li>✅ 倚天剑已打造（水盼盼专属）</li>
    <li>✅ 夜叉可入队（未杀赵龙）</li>
    <li>✅ 恶人谷任务已全部清理</li>
    <li>✅ <strong>山林地堡必带岳胖子+内功满级</strong></li>
    <li>✅ 龙墨已入队（小孟支线已完成）</li>
    <li>✅ 方云华已自宫（葵花三件套已装备）</li>
    <li>✅ 古实得太极图（气血+1000内力+500）</li>
    <li>✅ 佛渡拜火三迦叶已学到</li>
    <li>✅ 沈澜已招募</li>
    <li>✅ 六脉神剑已学到（洛阳当铺买不明物→高昌后大地图触发）</li>
    <li>✅ 塔娅骑士精神已解锁</li>
    <li>✅ 玄铁2块已拿（玄铁疑云+山林地堡后）</li>
    <li>✅ 醉仙线已完成（碧海潮生曲+三迦叶）</li>
  </ul>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍花族部落 — 花族线</h3>
  <div class="info">
    <span class="loc">📍 花族部落</span>：对话村长 → 看墙上三张告示 → 塔娅入队（如果之前没入队）<br>
    <span class="loc">📍 雪地野店</span>：找北丑<br>
    <span class="loc">📍 铁叉部附近大地图</span>：遇天王旧部<br>
    <span class="loc">📍 花族</span>：跑剧情 → 塔娅习得<strong>乌衣宝典</strong><br>
    <span class="loc">📍 喀什右下大漠</span>：杀乌衣教首领 → 花族线完成
  </div>
</div>

<div class="card missable">
  <h3><span class="tag m">主线</span> 📍山林地堡 → <strong>必带岳胖子+内功满级！</strong></h3>
  <div class="info">
    <span class="loc">📍 大地图</span>：丐帮指路 → <strong>山林地堡解锁</strong><br>
    <span class="teammate">👤 <strong>必须带：岳胖子（内功必须满级！）</strong></span><br>
    不带岳胖子或不练满内功 = <strong>坏结局</strong><br>
    <br>
    进入山林地堡 → 打赛王爷 → 岳胖子离队<br>
    <br>
    <strong>杀过山林地堡后：</strong><br>
    大地图遇玄铁矿工 → 花<strong>5万</strong>得另一块玄铁 → 老胡锻造<strong>荆棘专属玄铁武器</strong>
  </div>
  <div class="warning"><strong>⚠️ 不带岳胖子 = 坏结局！内功不练满 = 坏结局！</strong>史燕最终战不上场，带双奶+暴力输出</div>
</div>

<div class="card">
  <h3><span class="tag m">主线</span> 📍最终战 — 决战辟邪宫</h3>
  <div class="info">
    <strong>最终战流程：</strong><br>
    赛王府（存档两种结局）→ 回复江天雄 → 少林 → 天龙教（对话夜叉可入队 / 大厅右侧天龙八部剑）→ 铁叉部 → 洛阳 → 风吹雪入队 → 回谷（逍遥御风）→ 卫家堡 → 卫紫绫离队 → <strong>辟邪宫决战</strong>
  </div>
</div>

<div class="card">
  <h3>🏁 通关后彩蛋/后续</h3>
  <div class="info">
    <ul>
      <li><strong>大地图六脉神剑：</strong>洛阳当铺买不明物 → 高昌救夜叉后触发 → <strong>六脉神剑</strong></li>
      <li><strong>敖广招募：</strong>史义救帮主剧情完成 + 招安敖广 → 东渡口船边招募</li>
      <li><strong>古实太极图：</strong>古实开太极10级 → 找古叶 → 洛阳古玩 → 矿场工头 → 郊外小孩 → <strong>太极图</strong></li>
      <li><strong>醉仙线（如果还没做）：</strong>逍遥谷看画（悟80根85）→ 大地图东方未明连环画 → 喀什小孩夜光杯 → 喀什商人马贼葡萄美酒 → 忘忧谷醉仙</li>
      <li><strong>铸剑山庄情义七剑：</strong>任剑南在队调查剑冢断剑，根骨64</li>
    </ul>
  </div>
</div>

</div><!-- /tab-flow -->'''

# Replace the tab-flow content
new_content = content[:start_idx] + new_tab_content + content[end_idx:]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ tab-flow rebuilt successfully!")

# Verify
with open(html_path, "r", encoding="utf-8") as f:
    v = f.read()

checks = [
    ("tab-flow", 'id="tab-flow"'),
    ("tab-side", 'id="tab-side"'),
    ("tab-rumor", 'id="tab-rumor"'),
    ("tab-locations", 'id="tab-locations"'),
    ("tab-recruits", 'id="tab-recruits"'),
    ("tab-builds", 'id="tab-builds"'),
    ("tab-check", 'id="tab-check"'),
    ("tab-items", 'id="tab-items"'),
    ("</script>", '</script>'),
    ("</body>", '</body>'),
    ("</html>", '</html>'),
]
print("\n=== HTML Structure Verification ===")
all_ok = True
for name, marker in checks:
    count = v.count(marker)
    status = "✅" if count == 1 else f"⚠️ ({count})"
    if count != 1 and name not in ('</script>', '</body>', '</html>'):
        all_ok = False
    print(f"  {status} {name}")

opens = v.count('<div')
closes = v.count('</div>')
diff = opens - closes
status = "✅ PERFECT" if diff == 0 else f"⚠️ diff={diff}"
if diff != 0:
    all_ok = False
print(f"\n  {status} <div> tags: {opens} open, {closes} close")

print(f"\n  Total lines: {len(v.splitlines())}")
if all_ok:
    print("\n🎉 All checks passed!")
else:
    print("\n⚠️ Some checks failed — review the output above")
