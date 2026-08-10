#!/usr/bin/env python3
"""
重写侠客风云传前传攻略的「人物培养」和「物品获取」两个标签页。
- 人物培养：6个核心内功 + 12个核心招式，每项都有逐步获取指南
- 物品获取：逐步获取指南，每步标注地点/任务/队友/注意冲突
"""

HTML_PATH = r"c:\Users\yanshijie\WorkBuddy\Claw\outputs\侠客风云传前传_终极全攻略.html"
BACKUP_PATH = HTML_PATH.replace(".html", "_backup.html")

# ============================================================
# TAB-BUILDS 新内容
# ============================================================

NEW_BUILDS = r"""<div class="tab-content" id="tab-builds">

<div class="phase"><h2>⚡ 核心武学获取 —— 6大内功 + 12大招式</h2>
<p class="desc">以下为游戏中最强内功与招式，每项都标注完整获取流程。按此攻略走，保证每样都能拿齐。</p></div>

<!-- ===== 核心内功 6 项 ===== -->
<div class="phase"><h2>📖 六大核心内功</h2></div>

<!-- 1. 九阳神功 -->
<div class="card">
  <h3>🔥 九阳神功 — 谷月轩核心内功</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>暴击后霸体 · 保护一格队友 · 击杀后获得buff（攻击+暴击提升）</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程（二选一）</h4>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>方式一：封青霄任务（推荐·稳定）</strong>
    </div>
    <ol>
      <li><strong>前置：</strong>孟婆必须已死亡（主线剧情触发死亡）</li>
      <li><strong>地点：</strong>逍遥谷 → 触发封青霄前来求助的剧情</li>
      <li><strong>条件：</strong>谷月轩在队</li>
      <li><strong>过程：</strong>跟随封青霄前往某地点，完成战斗后获得九阳神功</li>
    </ol>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>方式二：森林传闻偷猴子（可提前获得）</strong>
    </div>
    <ol>
      <li><strong>前置：</strong>孟婆必须已死亡（主线剧情）</li>
      <li><strong>触发：</strong>大地图出现传闻「森林有猴子偷走了武功秘籍」</li>
      <li><strong>地点：</strong>森林 → 进入后遭遇猴子</li>
      <li><strong>队友：</strong>必须带<strong>史燕</strong></li>
      <li><strong>操作：</strong>战斗中史燕<strong>偷取猴子</strong> → 获得九阳神功</li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>森林传闻有时限！孟婆死后到傀尸死亡之前才能触发。如果傀尸已经死了，森林传闻可能不再出现，只能靠封青霄任务获取。</div>
  </div>
  <div class="build-card">
    <h4>🔗 关联武功</h4>
    <ul>
      <li>九阳神功是大师兄核心内功，修炼后搭配<strong>佛渡拜火三迦叶</strong>和<strong>万佛朝宗</strong>效果爆炸</li>
      <li>暴击后霸体配合<strong>螳螂拳</strong>（必中必暴+100%回血）形成无限循环</li>
    </ul>
  </div>
</div>

<!-- 2. 九阴总纲 -->
<div class="card">
  <h3>🌑 九阴总纲 — 荆棘核心内功</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>暴击后霸体 · 攻击附带吸星 · 击杀后恢复内力</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程（二选一）</h4>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>方式一：森林传闻偷熊</strong>
    </div>
    <ol>
      <li><strong>触发时机：</strong>游戏早期即可触发（赛王府之前）</li>
      <li><strong>触发方式：</strong>大地图出现传闻「森林有熊出没，身上好像带着武功秘籍」</li>
      <li><strong>地点：</strong>森林</li>
      <li><strong>队友：</strong>必须带<strong>史燕</strong></li>
      <li><strong>操作：</strong>战斗中史燕<strong>偷取熊</strong> → 获得九阴总纲</li>
    </ol>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>方式二：大地图传闻帮东瀛人</strong>
    </div>
    <ol>
      <li><strong>触发：</strong>大地图出现传闻「东瀛人需要帮助对付熊」</li>
      <li><strong>地点：</strong>大地图 → 遇到东瀛人</li>
      <li><strong>选择：</strong>选「帮助东瀛人」→ 战斗打熊</li>
      <li><strong>奖励：</strong>战斗胜利后获得九阴总纲</li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>两种方式互斥！如果森林偷熊拿到了，东瀛人传闻可能不再触发。建议优先用方式一（偷熊），更早获得。</div>
  </div>
  <div class="build-card">
    <h4>🔗 关联武功</h4>
    <ul>
      <li>荆棘装备九阴总纲 + 血刀经（后期），配合<strong>坎离水火剑</strong>和<strong>浪花斩铁式</strong>，伤害爆炸</li>
      <li>暴击后霸体 + 逍遥雁行式的连斩，荆棘可以一回合清场</li>
    </ul>
  </div>
</div>

<!-- 3. 葵花宝典 -->
<div class="card">
  <h3>🌸 葵花宝典 — 方云华专属·连斩神技</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>闪避后聚气 · <strong>连斩</strong> · 神游（移动后仍可出手） · 梯云纵叠加 = 5格移动</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：招募方云华</strong>
        <ul>
          <li>地点：杭州 → 成都破庙 → 武当</li>
          <li>条件：完成方云华相关剧情，使其入队</li>
        </ul>
      </li>
      <li><strong>步骤2：招募任剑南</strong>
        <ul>
          <li>地点：森林 → 带萧复遇任剑南 → 笑傲江湖曲7级 → 铸剑山庄</li>
        </ul>
      </li>
      <li><strong>步骤3：进入无名冢</strong>
        <ul>
          <li>时间：主线推进到南少林/辟邪宫剧情前后</li>
          <li>地点：无名冢</li>
        </ul>
      </li>
      <li><strong>步骤4：进入傀尸房间</strong>
        <ul>
          <li>队友：必须<strong>同时带方云华 + 任剑南</strong></li>
          <li>操作：进入傀尸所在房间</li>
        </ul>
      </li>
      <li><strong>步骤5：开棺材</strong>
        <ul>
          <li>操作：调查房间内<strong>右侧棺材</strong>（不是左边的！右边才是葵花）</li>
          <li>获得：葵花宝典 + 流星飞坠 + 辟邪剑法</li>
        </ul>
      </li>
      <li><strong>步骤6：方云华自宫</strong>
        <ul>
          <li>操作：让方云华修炼葵花宝典 → 触发自宫剧情</li>
          <li>获得连斩能力，战斗力质的飞跃</li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 冲突提示：</strong>
      <ul>
        <li>如果没带方云华 + 任剑南进无名冢，<strong>永久错过</strong>葵花宝典</li>
        <li>自宫后不可逆，方云华会失去部分男性剧情对话</li>
        <li>左边棺材是<strong>荆轲武决</strong>（史燕暗器），可以先拿左边再拿右边</li>
      </ul>
    </div>
  </div>
</div>

<!-- 4. 血刀经 -->
<div class="card">
  <h3>🔪 血刀经 — 荆棘后期核心内功</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>暴击率大幅提升 · 不受反击 · <strong>连斩</strong> · 击杀后恢复气血</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>时间：</strong>主线推进到赛王府</li>
      <li><strong>地点：</strong>赛王府内</li>
      <li><strong>条件：</strong>主线剧情自动触发赛王府战斗</li>
      <li><strong>操作：</strong>赛王府剧情战斗中<strong>自动获得</strong>血刀经 + 血刀刀法</li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>
      <ul>
        <li>赛王府章节<strong>必须带史燕</strong>！史燕战后自动偷取软猬甲 + 黑玉镯 + 罗汉拳</li>
        <li>血刀经是后期才能获得的，前期靠九阴总纲过渡</li>
        <li>拿到血刀经后荆棘基本起飞：暴击 + 连斩 + 霸体 = 无限行动</li>
      </ul>
    </div>
  </div>
</div>

<!-- 5. 神龙密咒 -->
<div class="card">
  <h3>🐉 神龙密咒 — 卫紫绫核心内功</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>四御属性累计+20% · 暴击后再+20%暴击率 · 暴击后霸体</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：招募沈湘云</strong>
        <ul>
          <li>地点：忘忧谷 → 完成沈湘云相关剧情</li>
        </ul>
      </li>
      <li><strong>步骤2：黑蝠洞打欧阳笑</strong>
        <ul>
          <li>前置：主线推进到黑蝠洞章节</li>
          <li>队友：<strong>沈湘云必须在队出场</strong>（她需要参与战斗）</li>
          <li>奖励：战斗胜利后获得<strong>寒蝠胆</strong></li>
        </ul>
      </li>
      <li><strong>步骤3：找沈澜</strong>
        <ul>
          <li>地点：怪医居 / 沈澜所在地</li>
          <li>条件：将寒蝠胆交给沈澜</li>
          <li>注意：需要沈湘云与沈澜的姐妹关系触发</li>
        </ul>
      </li>
      <li><strong>步骤4：获得钥匙 → 去藏海岛</strong>
        <ul>
          <li>沈澜给钥匙 → 前往藏海岛</li>
        </ul>
      </li>
      <li><strong>步骤5：开宝箱</strong>
        <ul>
          <li>地点：藏海岛宝箱</li>
          <li>获得：<strong>神龙密咒</strong> + 化骨绵掌</li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 冲突提示：</strong>
      <ul>
        <li>如果黑蝠洞战斗沈湘云<strong>没出场</strong>，拿不到寒蝠胆 = 整个链断裂</li>
        <li>寒蝠胆是任务道具，不要误卖掉</li>
        <li>藏海岛需要先完成前置才能进入（龙墨相关剧情）</li>
      </ul>
    </div>
  </div>
</div>

<!-- 6. 先天功 -->
<div class="card">
  <h3>✨ 先天功 — 通用最强心法</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>每回合恢复气血+内力 · 免疫负面状态 · 四御属性大幅提升 · 通用（所有人都可学）</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程（集齐4张残页）</h4>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>残页1 + 残页2：救状元郎传闻</strong>
    </div>
    <ol>
      <li><strong>触发条件：</strong>赛王府之前，大地图出现传闻「状元郎遇险需要救援」</li>
      <li><strong>地点：</strong>大地图 → 遇到被围攻的状元郎</li>
      <li><strong>操作：</strong>选择「出手相救」→ 战斗胜利</li>
      <li><strong>奖励：</strong>先天功残页1 + 先天功残页2</li>
    </ol>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>残页3：救云游商人传闻</strong>
    </div>
    <ol>
      <li><strong>触发条件：</strong>赛王府之前，大地图出现传闻「云游商人被强盗抢劫」</li>
      <li><strong>地点：</strong>大地图 → 遇到被强盗围困的商人</li>
      <li><strong>操作：</strong>选择「出手相救」→ 战斗胜利</li>
      <li><strong>奖励：</strong>先天功残页3</li>
    </ol>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>残页4：隐元阁获取（或大地图传闻）</strong>
    </div>
    <ol>
      <li><strong>方式一：</strong>隐元阁（景阳冈/杭州/成都随机出现）购买 → 残页4</li>
      <li><strong>方式二：</strong>大地图传闻触发 → 获得残页4</li>
    </ol>
    <div class="info" style="background:#fff3cd;padding:10px;border-radius:6px;margin:10px 0;">
      <strong>合成：赛王府天机老道</strong>
    </div>
    <ol>
      <li><strong>前置：</strong>4张残页全部集齐</li>
      <li><strong>地点：</strong>赛王府 → 找天机老道</li>
      <li><strong>操作：</strong>对话选择「复原武学」</li>
      <li><strong>获得：先天功</strong></li>
    </ol>
    <div class="warning"><strong>⚠️ 超级重要：</strong>
      <ul>
        <li><strong>必须在进入赛王府见天机老人之前</strong>集齐4张残页！</li>
        <li>进入赛王府后传闻可能不再刷新，错过 = <strong>永久失去先天功</strong></li>
        <li>残页4最难拿，隐元阁出现随机，请在大地图耐心刷传闻</li>
        <li>如果赛王府前进度太快，残页传闻可能来不及触发，建议适当放慢主线节奏</li>
      </ul>
    </div>
  </div>
</div>

<!-- ===== 核心招式 12 项 ===== -->
<div class="phase"><h2>⚔️ 十二大核心招式</h2></div>

<!-- 1. 佛渡拜火三迦叶 -->
<div class="card">
  <h3>🔥 佛渡拜火三迦叶 — 谷月轩最强招式</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p><strong>直线三格</strong>范围攻击 · 冻伤 · 重伤 · 大师兄核心输出</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：学小无相功</strong>
        <ul>
          <li>条件：找无瑕子学习（主线/剧情获得）</li>
        </ul>
      </li>
      <li><strong>步骤2：触发天山六阳掌 + 天山折梅手</strong>
        <ul>
          <li>条件：小无相功修炼后，无瑕子传授</li>
        </ul>
      </li>
      <li><strong>步骤3���学火焰刀</strong>
        <ul>
          <li>地点：原始森林 → 主线剧情打贺陀佛母 → 战斗胜利获得火焰刀</li>
        </ul>
      </li>
      <li><strong>步骤4：修炼到10级</strong>
        <ul>
          <li>将天山六阳掌修炼到10重</li>
          <li>将火焰刀修炼到10重</li>
        </ul>
      </li>
      <li><strong>步骤5：逍遥谷看画</strong>
        <ul>
          <li>地点：逍遥谷 → 触发看画剧情</li>
          <li>条件：天山六阳掌10重 + 火焰刀10重</li>
        </ul>
      </li>
      <li><strong>步骤6：找醉仙</strong>
        <ul>
          <li>地点：忘忧谷 → 醉仙处</li>
          <li>条件：需要<strong>葡萄美酒 + 夜光杯</strong></li>
          <li>获得：醉仙传授佛渡拜火三迦叶</li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 注意/冲突：</strong>
      <ul>
        <li>天山六阳掌和火焰刀<strong>必须都练到10重</strong>才能触发看画</li>
        <li>葡萄美酒获取链：喀什商人酒被偷 → 大地图马贼 → 恶人谷薛鬼医 → 拿回酒</li>
        <li>夜光杯获取链：大地图东方未明 → 小虾米连环画 → 喀什小孩交换</li>
      </ul>
    </div>
  </div>
</div>

<!-- 2. 坎离水火剑 -->
<div class="card">
  <h3>⚔️ 坎离水火剑 — 荆棘主力输出</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>恐惧 · 震击 · 高伤害 · 荆棘核心输出招式</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：获取冲灵剑法</strong>
        <ul>
          <li>地点：华山 → 华山山顶���发剧情</li>
          <li>获得：冲灵剑法</li>
        </ul>
      </li>
      <li><strong>步骤2：铸剑山庄调查</strong>
        <ul>
          <li>地点���铸剑山庄</li>
          <li>队友：带<strong>傅剑寒</strong></li>
          <li>操作：找老管家对话 → 调查左侧墙壁</li>
          <li>发现相关线索，了解冲灵剑法的秘密</li>
        </ul>
      </li>
      <li><strong>步骤3：去雪地野店交换</strong>
        <ul>
          <li>地点：雪地野店</li>
          <li>条件：持有冲灵剑法</li>
          <li>选项：与店主对话 → 选择<strong>「用冲灵剑法交换」</strong></li>
        </ul>
      </li>
      <li><strong>步骤4：选择换取方式</strong>
        <ul>
          <li>选<strong>「战斗」</strong>→ 打赢后获得坎离水火剑</li>
          <li>（不选战斗只能换金蛇剑法/天涯明月刀/铁掌三选一）</li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 冲突提示：</strong>
      <ul>
        <li>冲灵剑法是唯一物品，换掉就没了（不能再拿回）</li>
        <li>如果冲灵剑法被换掉但战斗<strong>打输了</strong>，坎离水火剑<strong>永久错过</strong></li>
        <li>建议先存档再进雪地野店</li>
      </ul>
    </div>
  </div>
</div>

<!-- 3. 辟邪剑法 -->
<div class="card">
  <h3>⚡ 辟邪剑法 — 方云华自宫后神技</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>直线三格范围 · 必中 · 闪避 · 配合葵花宝典连斩可无限行动</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <p>与<strong>葵花宝典</strong>同时获取（同一棺材），详见上方「葵花宝典」获取流程。</p>
    <ol>
      <li><strong>前提：</strong>方云华 + 任剑南同时在队</li>
      <li><strong>地点：</strong>无名冢傀尸房间右侧棺材</li>
      <li><strong>获得：</strong>葵花宝典 + 流星飞坠 + <strong>辟邪剑法</strong></li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>辟邪剑法和流星飞坠都是方云华自宫后才能发挥最大威力。</div>
  </div>
</div>

<!-- 4. 浪花斩铁式 -->
<div class="card">
  <h3>🌊 浪花斩铁势 — 游戏最强单体伤害</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>单体超高伤害 · 无视防御 · 龙墨专属 · <strong>全游戏最强单体招式</strong></p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：招募龙墨</strong>
        <ul>
          <li>条件：完成洛阳小孟任务（确保龙墨可招募）</li>
          <li>地点：成都 → 龙墨调停任务 → 撑剑圣三招</li>
          <li>奖励：龙墨入队 + 幽冥十三剑 + 佛山无影脚</li>
        </ul>
      </li>
      <li><strong>步骤2：前往藏海岛</strong>
        <ul>
          <li>前置：需要完成藏海岛相关前置剧情</li>
        </ul>
      </li>
      <li><strong>步骤3：找沙滩</strong>
        <ul>
          <li>地点：藏海岛 → <strong>右侧沙滩</strong></li>
          <li>条件：<strong>龙墨必须在队</strong></li>
          <li>操作：在沙滩上触发剧情 → 龙墨领悟浪花斩铁式</li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>
      <ul>
        <li>龙墨不在队的话去沙滩<strong>不会触发</strong>，白跑一趟</li>
        <li>藏海岛还有神龙密咒的宝箱，可以顺便一起拿</li>
      </ul>
    </div>
  </div>
</div>

<!-- 5. 六脉神剑 -->
<div class="card">
  <h3>👆 六脉神剑 — 最强指法</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>直线三格范围 · 反击 · 击退 · 可给大师兄/古实等高内力角色装备</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：洛阳当铺买「不明物」</strong>
        <ul>
          <li>地点：洛阳当铺</li>
          <li>操作：购买名为「不明物」的道具</li>
        </ul>
      </li>
      <li><strong>步骤2：高昌迷宫救夜叉</strong>
        <ul>
          <li>时间：主线推进到高昌迷宫</li>
          <li>地点：高昌迷宫</li>
          <li>操作：救出夜叉（主线/支线）</li>
        </ul>
      </li>
      <li><strong>步骤3：大地图触发</strong>
        <ul>
          <li>条件：救出夜叉后 + 持有「不明物」</li>
          <li>地点：大地图 → 触发特殊事件</li>
          <li>获得：六脉神剑</li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>洛阳当铺的「不明物」尽早买，后期当铺可能关闭或物品刷新。</div>
  </div>
</div>

<!-- 6. 螳螂拳 -->
<div class="card">
  <h3>🥊 螳螂拳 — 必中必暴+100%回血</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p><strong>必中 + 必暴击</strong> · 吸收100%伤害为气血 · 定身 · 大师兄/江瑜可用</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>地点：</strong>高昌迷宫</li>
      <li><strong>位置：</strong>高昌迷宫入口向左走</li>
      <li><strong>触发：</strong>遇到特定战斗（螳螂拳守护者）</li>
      <li><strong>操作：</strong>战斗胜利 → 获得螳螂拳</li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>
      <ul>
        <li>高昌迷宫主线过了就回不去了，<strong>务必在主线期间拿完</strong></li>
        <li>螳螂拳配合九阳神功暴击霸体，大师兄可以无限循环</li>
      </ul>
    </div>
  </div>
</div>

<!-- 7. 不动明王棍 -->
<div class="card">
  <h3>🦯 不动明王棍 — 四格范围捉影神技</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p><strong>四格范围</strong>捉影（把敌人拉到身边）· 不动自带 · 控场神技</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li>不动<strong>自带</strong>不动明王棍，无需额外获取</li>
      <li>重点是把不动练起来，搭配易筋经 + 大闹天宫</li>
    </ol>
    <div class="info"><strong>搭配建议：</strong>不动明王棍捉影 → 大闹天宫群体输出 → 队友收割。不动是队伍的控场核心。</div>
  </div>
</div>

<!-- 8. 骑士精神 -->
<div class="card">
  <h3>🐴 骑士精神 — 周围队友必定左右互搏</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>塔娅被动技能 · <strong>周围两格内所有队友必定左右互搏</strong>（攻击两次！）</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：招募塔娅</strong>
        <ul>
          <li>条件：龙墨成都调停任务中，与塔娅对话</li>
        </ul>
      </li>
      <li><strong>步骤2：前往恶人谷</strong>
        <ul>
          <li>前置：主线推进到恶人谷</li>
        </ul>
      </li>
      <li><strong>步骤3：触发色目人入侵事件</strong>
        <ul>
          <li>条件：<strong>拜火大典之前</strong>进入恶人谷</li>
          <li>队友：<strong>塔娅必须在队</strong></li>
        </ul>
      </li>
      <li><strong>步骤4：恶人谷四连战</strong>
        <ul>
          <li>操作：完成恶人谷色目人相关四场战斗</li>
          <li>获得：塔娅领悟<strong>骑士精神</strong></li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 冲突提示：</strong>
      <ul>
        <li><strong>拜火大典后</strong>色目人会入侵恶人谷，此时触发的是<strong>不同事件</strong>，拿不到骑士精神！</li>
        <li>必须在<strong>拜火大典前</strong>带塔娅去恶人谷完成</li>
        <li>骑士精神是游戏最强辅助技能之一，配合高输出队友效果拔群</li>
      </ul>
    </div>
  </div>
</div>

<!-- 9. 天外飞仙精要 -->
<div class="card">
  <h3>🌠 天外飞仙精要 — 傅剑寒/剑系核心</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>高伤害 · 闪避 · 剑系队友通用</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>步骤1：杭州触发</strong>
        <ul>
          <li>地点：杭州城内右上角</li>
          <li>触发：遇到小孩吴桐 → 对话</li>
        </ul>
      </li>
      <li><strong>步骤2：萧复僵尸事件</strong>
        <ul>
          <li>队友：带<strong>萧复</strong></li>
          <li>地点：杭州 → 触发僵尸相关事件</li>
        </ul>
      </li>
      <li><strong>步骤3：找漂亮石头</strong>
        <ul>
          <li>操作：在事件中找到漂亮石头</li>
          <li>选择：有人想买石头 → <strong>选「不卖」</strong></li>
        </ul>
      </li>
      <li><strong>步骤4：还给小孩娘</strong>
        <ul>
          <li>操作：将漂亮石头还给吴桐母亲</li>
        </ul>
      </li>
      <li><strong>步骤5：找吴大叔</strong>
        <ul>
          <li>触发：与吴桐的叔叔对话</li>
        </ul>
      </li>
      <li><strong>步骤6：傅剑寒出场</strong>
        <ul>
          <li>队友：带<strong>傅剑寒</strong></li>
          <li>选项：选<strong>「相信他」</strong></li>
        </ul>
      </li>
      <li><strong>步骤7：战斗</strong>
        <ul>
          <li>操作：战斗胜利 → 获得天外飞仙精要</li>
        </ul>
      </li>
    </ol>
    <div class="warning"><strong>⚠️ 冲突提示：</strong>
      <ul>
        <li><strong>必须在无名冢杀傀尸之前完成！</strong>无名冢之后杭州事件可能失效</li>
        <li>如果石头卖了，整个链断裂，<strong>永久错过</strong></li>
        <li>傅剑寒不在队无法触发最后一步</li>
      </ul>
    </div>
  </div>
</div>

<!-- 10. 大闹天宫 -->
<div class="card">
  <h3>🐵 大闹天宫 — 不动群攻核心</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>神行 · 天下无狗（群攻） · 不动输出核心招式</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>地点：</strong>恶人谷</li>
      <li><strong>条件：</strong>带<strong>萧复</strong>在队</li>
      <li><strong>触发：</strong>恶人谷内遇到特定剧情/战斗</li>
      <li><strong>操作：</strong>战斗胜利 → 不动领悟大闹天宫</li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>恶人谷在拜火大典后可能被入侵，务必在<strong>拜火大典前</strong>完成所有恶人谷支线。</div>
  </div>
</div>

<!-- 11. 九阴白骨爪 -->
<div class="card">
  <h3>🦴 九阴白骨爪 — 卫紫绫核心招式</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>噬气 · 剧毒 · 连击 · 卫紫绫/毒系核心</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>地点：</strong>山林地堡</li>
      <li><strong>条件：</strong>主线推进到山林地堡（快结局的区域）</li>
      <li><strong>触发：</strong>与山林地堡中的<strong>王爷</strong>战斗</li>
      <li><strong>操作：</strong>战斗胜利 → 获得九阴白骨爪（九阴神爪）</li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>
      <ul>
        <li>山林地堡是后期地图，<strong>带岳胖子</strong>进地堡有额外剧情</li>
        <li>进入前确保队友内功修炼满级</li>
      </ul>
    </div>
  </div>
</div>

<!-- 12. 万佛朝宗 -->
<div class="card">
  <h3>🙏 万佛朝宗 — 大师兄大范围内伤</h3>
  <div class="build-card">
    <h4>效果</h4>
    <p>大范围攻击 · 内伤 · 大师兄群战核心</p>
  </div>
  <div class="build-card">
    <h4>📋 获取流程</h4>
    <ol>
      <li><strong>触发：</strong>大地图传闻出现「隐元阁商人出现」</li>
      <li><strong>地点：</strong>景阳冈 → 隐元阁（随机出现）</li>
      <li><strong>队友：</strong>需要<strong>岳胖子</strong>在队（隐元阁需要岳胖子才能进入）</li>
      <li><strong>操作：</strong>在隐元阁购买万佛朝宗</li>
    </ol>
    <div class="warning"><strong>⚠️ 注意：</strong>隐元阁是随机出现的，出现在不同地点（景阳冈/杭州/成都），需要耐心刷传闻。</div>
  </div>
</div>

<!-- ===== 角色培养汇总 ===== -->
<div class="phase"><h2>👤 角色培养方案汇总</h2></div>

<!-- 谷月轩 -->
<div class="card">
  <h3>👊 谷月轩（大师兄）— 拳掌</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>逍遥鹏飞式</strong>（自带）：回血回蓝+保护+反击霸体</li>
      <li><strong>九阳神功</strong>：暴击霸体+保护+击杀buff → <strong>核心</strong></li>
      <li><strong>小无相功</strong>：反击回蓝+无限反击 → 触发天山六阳掌前置</li>
      <li><strong>先天功</strong>：回血回内+免疫负面+四御提升 → <strong>通用神技</strong></li>
      <li><strong>梯云纵</strong>：+1移动</li>
      <li><strong>逍遥御风</strong>（决战前）：最强心法之一</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>佛渡拜火三迦叶</strong> — 直线三格·冻伤·重伤（核心输出）</li>
      <li><strong>万佛朝宗</strong> — 大范围·内伤（群战核心）</li>
      <li><strong>螳螂拳</strong> — 必中必暴+100%回血+定身</li>
      <li><strong>六脉神剑</strong> — 直线三格·反击·击退</li>
      <li><strong>天山六阳掌</strong> — 聚气</li>
      <li><strong>火焰刀</strong> — 重伤（过渡期主力）</li>
      <li><strong>石破天惊拳</strong> — 内伤+重伤（早期主力）</li>
      <li><strong>空明拳</strong> — 反弹+震击</li>
    </ul>
  </div>
</div>

<!-- 荆棘 -->
<div class="card">
  <h3>🔪 荆棘（二师兄）— 刀法</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>逍遥雁行式</strong>（自带）：暴击+神行+连斩 → 前期核心</li>
      <li><strong>九阴总纲</strong>：暴击后霸体+吸星 → <strong>核心</strong></li>
      <li><strong>血刀经</strong>：暴击提升+不受反击+连斩 → <strong>后期核心</strong></li>
      <li><strong>先天功</strong>：通用神技</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>坎离水火剑</strong> — 恐惧+震击（核心输出）</li>
      <li><strong>走剑行刀</strong> — 两格单体·流血·连斩收割</li>
      <li><strong>阴错阳差</strong> — 一格三目标·缚身（前期群攻）</li>
      <li><strong>狂龙逆斩</strong> — 一格三目标·吸星</li>
      <li><strong>抖鳞虎扑式</strong> — 霸体</li>
      <li><strong>幽冥十三剑</strong> — 必中+吸星</li>
      <li><strong>血刀刀法</strong> — 后期搭配血刀经</li>
    </ul>
  </div>
</div>

<!-- 龙墨 -->
<div class="card">
  <h3>🌊 龙墨 — 刀法（最强单体）</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>千仞决</strong>（自带）</li>
      <li><strong>血刀经</strong>：暴击+连斩</li>
      <li><strong>九阴总纲</strong>：暴击霸体</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>浪花斩铁势</strong> — <strong>全游戏最强单体伤害</strong></li>
      <li><strong>狂风刀法</strong> — 回150%伤害气血+20%攻击</li>
      <li><strong>魔刀七杀</strong> — 无名冢四选一</li>
      <li><strong>残存亦末路</strong> — 左右互搏70%连击</li>
      <li><strong>十殿阎罗刀</strong> — 恐惧+断筋+噬气</li>
      <li><strong>蚩尤刀法</strong> — 成都隐元阁</li>
    </ul>
  </div>
</div>

<!-- 方云华 -->
<div class="card">
  <h3>⚔️ 方云华 — 剑法（自宫连斩）</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>葵花宝典</strong>：闪避聚气+<strong>连斩</strong>+神游 → <strong>核心</strong></li>
      <li><strong>梯云纵</strong>：+1移动（配合神游=5格移动）</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>辟邪剑法</strong> — 直线三格·必中·闪避</li>
      <li><strong>流星飞坠</strong> — 必中+神行</li>
      <li><strong>归藏剑</strong> — 100%吸气血内力</li>
      <li><strong>太极化清</strong> — 净化+乾坤挪移</li>
      <li><strong>天外飞仙精要</strong> — 闪避+高伤害</li>
      <li><strong>饮中八仙剑</strong> — 霸体</li>
    </ul>
  </div>
</div>

<!-- 史燕 -->
<div class="card">
  <h3>🎯 史燕 — 暗器·偷窃专家</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>飞燕功</strong>（自带）：闪避+移动+必中</li>
      <li><strong>明玉功</strong>：额外闪避提升</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>满天花雨</strong> — 超大范围·流血（忘忧谷橘叟→呕血谱）</li>
      <li><strong>烟雾弥漫</strong> — 中等范围·目盲</li>
      <li><strong>荆轲武决</strong> — 缚身+抓影（无名冢左棺材）</li>
      <li><strong>弹指神通</strong> — 楚绘任务</li>
      <li><strong>含沙射影</strong> — 中毒+目盲</li>
    </ul>
  </div>
</div>

<!-- 小阿曼 -->
<div class="card">
  <h3>🐍 小阿曼 — 鞭法</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>毒龙功</strong>（自带）：免疫中毒眩晕+毒息+吸星</li>
      <li><strong>金蛇宝典</strong>：大地图王蓉→荆棘单挑金翅鸟</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>裂风鞭法</strong> — 3格AOE·主力（原始森林救阿傍→大漠找赤蛛虫）</li>
      <li><strong>日月天魔鞭</strong> — 主力（无名冢四选一/偷赛王爷）</li>
      <li><strong>万毒入化</strong> — 找蓝婷练武功</li>
      <li><strong>银蛇千转</strong> — 岳胖子纪纹房间</li>
      <li><strong>百兽之境</strong> — 大地图帮纪纹</li>
      <li><strong>毒龙追魂</strong> — 抓影（自带）</li>
    </ul>
  </div>
</div>

<!-- 卫紫绫 -->
<div class="card">
  <h3>☠️ 卫紫绫 — 毒系</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>神龙密咒</strong>：四御+20%+暴击霸体 → <strong>核心</strong></li>
      <li><strong>鼎心无量功</strong>：怪医居毒鼎</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>九阴白骨爪</strong> — 噬气+剧毒+连击（核心输出）</li>
      <li><strong>化骨绵掌</strong> — 中毒+吸星</li>
      <li><strong>化功大法</strong> — 散功+眩晕</li>
      <li><strong>千蛛万毒手</strong> — 怪医居沈澜</li>
      <li><strong>紫翎霓裳舞</strong> — 破甲+恐惧+内伤</li>
      <li><strong>流风回雪</strong> — 反伤+噬气</li>
      <li>💡 核心套路：休息隐匿→暴击霸体→无限循环</li>
    </ul>
  </div>
</div>

<!-- 不动 -->
<div class="card">
  <h3>🦯 不动 — 棍法·控场</h3>
  <div class="build-card">
    <h4>推荐内功</h4>
    <ul>
      <li><strong>易筋经</strong>（自带）</li>
      <li><strong>左右互搏</strong>（雪地练剑第三天）</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>推荐招式</h4>
    <ul>
      <li><strong>不动明王棍</strong> — <strong>四格捉影</strong>神技</li>
      <li><strong>大闹天宫</strong> — 神行+天下无狗（群攻）</li>
      <li><strong>达摩武诀</strong> — 霸体</li>
      <li><strong>大须弥山棍</strong> — 定身+眩晕</li>
      <li><strong>天王枪法</strong> — 破绽+流血+内伤</li>
      <li><strong>回马枪</strong> — 重伤+神行</li>
    </ul>
  </div>
</div>

<!-- 治疗 -->
<div class="card">
  <h3>💚 治疗 — 沈湘云 / 萧复 / 塔娅</h3>
  <div class="build-card">
    <h4>沈湘云（早期主力奶）</h4>
    <ul>
      <li>药王神篇 | 金针渡劫 | 清莲印法</li>
      <li>点穴截脉（修罗宫小孟后续）</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>萧复（中期过渡）</h4>
    <ul>
      <li>碧海潮生曲 | 百鸟朝凤曲 | 笑傲江湖曲 | 沧海一笑</li>
    </ul>
  </div>
  <div class="build-card">
    <h4>塔娅（后期神奶）</h4>
    <ul>
      <li><strong>武林群侠传</strong> → 徐子易（成都鱼面摊10药草）</li>
      <li><strong>武林通鉴</strong> → 武林群侠传10级见徐子易</li>
      <li><strong>神农济世</strong> → 龙墨成都任务（⚠️代价：再进不了百草门）</li>
      <li><strong>骑士精神</strong> → <strong>周围两格队友必定左右互搏！</strong></li>
      <li><strong>占事略诀</strong> → 战胜黑冢罗王</li>
    </ul>
  </div>
</div>

</div><!-- /tab-builds -->"""

# ============================================================
# TAB-ITEMS 新内容 - 逐步获取指南
# ============================================================

NEW_ITEMS = r"""<div class="tab-content" id="tab-items">

<div class="phase"><h2>🎒 关键物品逐步获取指南</h2>
<p class="desc">以下为游戏中最重要的物品获取流程，每一步都标注了地点、需要带的队友、以及需要注意的冲突。</p></div>

<style>
  .step-guide { background: #faf9f6; border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin: 16px 0; }
  .step-guide h3 { color: var(--accent); font-size: 1.1em; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 2px solid var(--border); }
  .step-guide .step { display: flex; gap: 12px; margin: 12px 0; padding: 10px; background: #fff; border-radius: 8px; border-left: 4px solid var(--accent2); }
  .step-guide .step .step-num { min-width: 32px; height: 32px; background: var(--accent2); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.9em; flex-shrink: 0; }
  .step-guide .step .step-body { flex: 1; }
  .step-guide .step .step-body .loc { color: var(--accent); font-weight: bold; }
  .step-guide .step .step-body .teammate { color: var(--tag-recruit); font-weight: bold; }
  .step-guide .step .step-body .action { color: var(--text); }
  .step-guide .reward-box { background: #e8f5e9; border: 1px solid #a5d6a7; border-radius: 8px; padding: 10px 16px; margin-top: 12px; }
  .step-guide .warning-box { background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 10px 16px; margin-top: 12px; }
  .step-guide .warning-box strong { color: #e74c3c; }
  .chain-link { text-align: center; color: var(--muted); margin: 4px 0; font-size: 1.2em; }
</style>

<!-- ===== 1. 先天功 ===== -->
<div class="step-guide">
  <h3>✨ 先天功 —— 通用最强心法（赛王府前必须完成！）</h3>
  <p style="color:var(--muted);margin-bottom:12px;">最终效果：每回合回血回内 · 免疫负面状态 · 四御大幅提升 · 所有人都可学</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">救状元郎传闻</span><br>
      大地图出现传闻「状元郎遇险」，前往救援。<br>
      <span class="teammate">👤 无特殊队友要求</span><br>
      🎁 获得：先天功残页1 + 残页2
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">救云游商人传闻</span><br>
      大地图出现传闻「云游商人被劫」，出手相救。<br>
      <span class="teammate">👤 无特殊队友要求</span><br>
      🎁 获得：先天功残页3
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 隐元阁（景阳冈/杭州/成都随机）</span> · <span class="action">购买残页4</span><br>
      传闻触发隐元阁出现 → 进入购买。<br>
      <span class="teammate">👤 需要岳胖子在队才能进入隐元阁</span><br>
      🎁 获得：先天功残页4
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 赛王府</span> · <span class="action">找天机老道复原</span><br>
      带着4张残页进入赛王府 → 找天机老道 → 选「复原武学」。<br>
      <span class="teammate">👤 无特殊队友要求</span><br>
      🎁 获得：<strong>先天功</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 冲突警告：</strong>
    <ul>
      <li><strong>必须在进入赛王府前集齐全部4张残页！</strong>进入赛王府后大地图传闻停止刷新</li>
      <li>残页1-3通过传闻获得（赛王府前多在大地图走动刷传闻）</li>
      <li>残页4最难拿，隐元阁出现随机，耐心等待传闻</li>
      <li>错过任何一张 = <strong>永久失去先天功</strong></li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：先天功</strong> — 最强通用心法，建议优先给大师兄或荆棘学
  </div>
</div>

<!-- ===== 2. 葵花宝典全套 ===== -->
<div class="step-guide">
  <h3>🌸 葵花宝典 + 辟邪剑法 + 流星飞坠 —— 方云华连斩三件套</h3>
  <p style="color:var(--muted);margin-bottom:12px;">最终效果：连斩 + 直线三格必中 + 闪避 + 神游5格移动</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 杭州</span> · <span class="action">触发方云华剧情</span><br>
      杭州城触发方云华相关事件。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 成都破庙</span> · <span class="action">完成方云华入队任务</span><br>
      成都破庙 → 完成方云华单挑战斗 → 方云华入队。<br>
      <span class="teammate">👤 建议带史燕（破庙内有额外剧情）</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 森林</span> · <span class="action">招募任剑南</span><br>
      带萧复去森林 → 遇任剑南 → 笑傲江湖曲练到7级 → 铸剑山庄招任剑南入队。<br>
      <span class="teammate">👤 需要萧复（触发初遇）、任剑南（最终入队）</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 无名冢</span> · <span class="action">进傀尸房间开右棺材</span><br>
      主线推进到无名冢 → <strong>必须同时带方云华 + 任剑南</strong> → 进入傀尸房间 → 调查右侧棺材。<br>
      <span class="teammate">👤 <strong>必须带：方云华 + 任剑南</strong></span><br>
      🎁 获得：葵花宝典 + 辟邪剑法 + 流星飞坠
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">5</div>
    <div class="step-body">
      <span class="loc">📍 任意地点</span> · <span class="action">方云华修炼葵花宝典自宫</span><br>
      让方云华装备并修炼葵花宝典 → 触发自宫剧情 → 获得连斩能力。<br>
      <span class="teammate">👤 方云华</span>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 冲突警告��</strong>
    <ul>
      <li>没带方云华 + 任剑南进无名冢 = <strong>永久错过</strong>葵花全套</li>
      <li>左侧棺材是荆轲武决（史燕暗器），记得也拿了</li>
      <li>自宫不可逆，方云华会失去部分剧情对话</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：葵花宝典 + 辟邪剑法 + 流星飞坠</strong> — 方云华从废柴变超人的三件套
  </div>
</div>

<!-- ===== 3. 软猬甲+黑玉镯（赛王府） ===== -->
<div class="step-guide">
  <h3>🛡️ 软猬甲 + 黑玉镯 + 罗汉拳 —— 赛王府三件套（一次性！）</h3>
  <p style="color:var(--muted);margin-bottom:12px;">最终效果：高防御反伤护甲 + 稀有饰品 + 罗汉拳秘籍</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 森林</span> · <span class="action">招募史燕</span><br>
      去森林花1万钱招募史燕入队。<br>
      <span class="teammate">👤 史燕（必招，整个游戏最重要的偷窃角色）</span><br>
      ⚠️ 时间窗口：越早招越好，否则错过大量偷窃机会
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 主线推进</span> · <span class="action">进入赛王府章节</span><br>
      按照主线剧情推进到赛王府战斗章节。<br>
      <span class="teammate">👤 正常主线队友即可</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 赛王府内</span> · <span class="action">剧情战斗</span><br>
      赛王府剧情战斗。<strong>史燕必须在出战队伍中！</strong><br>
      <span class="teammate">👤 <strong>史燕必须出战！</strong></span><br>
      战斗中史燕<strong>不需要主动偷取</strong>，战斗胜利后<strong>自动获得</strong>偷窃物品。
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 超级重要：</strong>
    <ul>
      <li>赛王府剧情战斗<strong>只打一次</strong>，错过不再来</li>
      <li><strong>史燕不在出战队伍 = 软猬甲 + 黑玉镯 + 罗汉拳全部永久错过</strong></li>
      <li>战后自动偷取，不需要在战斗中手动偷</li>
      <li>建议进入赛王府前先存档！</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：软猬甲</strong>（高防御反伤）+ <strong>黑玉镯</strong>（稀有饰品）+ <strong>罗汉拳</strong>（秘籍）
  </div>
</div>

<!-- ===== 4. 倚天剑 ===== -->
<div class="step-guide">
  <h3>⚔️ 倚天剑 —— 水盼盼专属·击杀再行动</h3>
  <p style="color:var(--muted);margin-bottom:12px;">最终效果：伤害+410 · 击杀后再行动 · 水盼盼专属</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 武当/主线</span> · <span class="action">获取倚天断剑</span><br>
      武当相关剧情或主线推进中自动获得倚天断剑。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：倚天断剑（此时还不能用）
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">刷西方异金传闻</span><br>
      大地图持续走动 → 传闻出现「西方异金」 → 前往触发点。<br>
      <span class="teammate">👤 需要史燕（偷取西方异金）</span><br>
      西方异金持有者随机：可能是锦衣卫/西域番僧/天龙教众/酆都教众<br>
      ⚠️ 传闻随机触发，需要耐心在大地图上反复走动等待
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 战斗</span> · <span class="action">偷取西方异金</span><br>
      进入战斗 → 史燕偷取持有者身上的西方异金。<br>
      <span class="teammate">👤 <strong>史燕必须在队，战斗中必须手动偷取</strong></span><br>
      🎁 获得：西方异金
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 铸剑山庄</span> · <span class="action">找任浩然重铸</span><br>
      带倚天断剑 + 西方异金 → 铸剑山庄 → 找任浩然 → 重铸倚天剑。<br>
      <span class="teammate">👤 无特殊队友要求</span><br>
      🎁 获得：<strong>倚天剑</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 冲突警告：</strong>
    <ul>
      <li>西方异金<strong>随机触发</strong>，需要在大地图反复刷传闻</li>
      <li>偷取失败或没带史燕 = 拿不到西方异金 = 倚天剑永远做不出来</li>
      <li>建议：看到西方异金传闻立刻存档，然后带史燕去偷</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：倚天剑</strong> — 水盼盼专属，击杀后再行动，后期清场神器
  </div>
</div>

<!-- ===== 5. 醉仙链 ===== -->
<div class="step-guide">
  <h3>🍷 醉仙链 —— 葡萄美酒 + 夜光杯 → 碧海潮生曲 + 佛渡拜火三迦叶</h3>
  <p style="color:var(--muted);margin-bottom:12px;">这是游戏最长的物品链之一，但回报极高：碧海潮生曲 + 大师兄最强招式佛渡拜火三迦叶</p>

  <div class="step">
    <div class="step-num">1A</div>
    <div class="step-body">
      <span class="loc">📍 喀什</span> · <span class="action">接葡萄美酒任务</span><br>
      喀什商人说酒被偷了 → 答应帮忙找回。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">1B</div>
    <div class="step-body">
      <span class="loc">📍 大地图 → 恶人谷</span> · <span class="action">追回葡萄美酒</span><br>
      大地图找马贼 → 追踪到恶人谷 → 找薛鬼医 → 拿回葡萄美酒。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>葡萄美酒</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2A</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">东方未明传闻</span><br>
      大地图遇到东方未明 → 获得小虾米连环画。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>小虾米连环画</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2B</div>
    <div class="step-body">
      <span class="loc">📍 喀什</span> · <span class="action">交换夜光杯</span><br>
      喀什小孩想看的连环画 → 用连环画交换。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>夜光杯</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 忘忧谷</span> · <span class="action">找醉仙</span><br>
      带葡萄美酒 + 夜光杯 → 忘忧谷找醉仙 → 交给醉仙 → 获赠碧海潮生曲。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>碧海潮生曲</strong>（萧复曲谱）
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 逍遥谷</span> · <span class="action">看画 → 醉仙传授佛渡拜火</span><br>
      前提：大师兄天山六阳掌10重 + 火焰刀10重 → 逍遥谷看画 → 再去忘忧谷找醉仙。<br>
      <span class="teammate">👤 谷月轩</span><br>
      🎁 获得：<strong>佛渡拜火三迦叶</strong>（大师兄最强输出）
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 注意：</strong>
    <ul>
      <li>葡萄美酒和夜光杯是两条独立支线，可以并行推进</li>
      <li>佛渡拜火还需要天山六阳掌+火焰刀都10重，这是额外的修炼要求</li>
      <li>整个链路虽然长，但没有严格的时间限制，可以慢慢做</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：碧海潮生曲 + 佛渡拜火三迦叶</strong>
  </div>
</div>

<!-- ===== 6. 冲灵剑法→坎离水火剑 ===== -->
<div class="step-guide">
  <h3>⚔️ 冲灵剑法 → 坎离水火剑 —— 荆棘核心输出</h3>
  <p style="color:var(--muted);margin-bottom:12px;">最终效果：恐惧 + 震击，荆棘主力输出招式</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 华山</span> · <span class="action">获取冲灵剑法</span><br>
      华山顶触发剧情 → 获得冲灵剑法。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 铸剑山庄</span> · <span class="action">调查墙壁线索</span><br>
      找老管家对话 → 带傅剑寒调查左侧墙壁 → 了解冲灵剑法的秘密。<br>
      <span class="teammate">👤 <strong>需要傅剑寒在队</strong></span><br>
      ⚠️ 如果没带傅剑寒，调查不到线索
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 雪地野店</span> · <span class="action">用冲灵剑法交换</span><br>
      与店主对话 → 选「用冲灵剑法交换」→ 再选「战斗」→ 打赢。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>坎离水火剑</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 冲突警告：</strong>
    <ul>
      <li>必须选「战斗」选项才能拿坎离水火剑！选其他选项只能换金蛇剑法/天涯明月刀/铁掌</li>
      <li>如果战斗<strong>打输了</strong>，坎离水火剑<strong>永久错过</strong></li>
      <li>冲灵剑法是唯一物品，换出去就拿不回来了</li>
      <li><strong>强烈建议进雪地野店前存档！</strong></li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：坎离水火剑</strong> — 荆棘核心输出招式
  </div>
</div>

<!-- ===== 7. 九阴总纲+九阳神功（森林偷取） ===== -->
<div class="step-guide">
  <h3>🌳 九阴总纲 + 九阳神功 —— 森林偷取攻略</h3>
  <p style="color:var(--muted);margin-bottom:12px;">大师兄和荆棘的核心内功，都可以通过森林传闻偷取获得</p>

  <h4 style="margin-top:16px;">🐻 九阴总纲（先拿）</h4>
  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">等传闻</span><br>
      游戏早期（赛王府前）大地图出现传闻「森林有熊，身上带着武功秘籍」。<br>
      <span class="teammate">👤 史燕（必带）</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 森林</span> · <span class="action">战斗偷熊</span><br>
      进森林 → 遇到熊 → 战斗 → <strong>史燕偷取熊</strong>。<br>
      <span class="teammate">👤 <strong>史燕必须出战！</strong></span><br>
      🎁 获得：<strong>九阴总纲</strong>
    </div>
  </div>

  <h4 style="margin-top:16px;">🐵 九阳神功（后拿）</h4>
  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 主线</span> · <span class="action">等待孟婆��亡</span><br>
      主线推进到孟婆死亡。<br>
      <span class="teammate">👤 无</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">等传闻</span><br>
      孟婆死后 → 大地图出现传闻「森林有猴子偷走了武功秘籍」。<br>
      <span class="teammate">👤 史燕（必带）</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 森林</span> · <span class="action">战斗偷猴子</span><br>
      进森林 → 遇到猴子 → 战斗 → <strong>史燕偷取猴子</strong>。<br>
      <span class="teammate">👤 <strong>史燕必须出战！</strong></span><br>
      🎁 获得：<strong>九阳神功</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 冲突警告：</strong>
    <ul>
      <li>九阴总纲：也可以在「大地图帮东瀛人打熊」传闻中获取，两种方式互斥</li>
      <li>九阳神功：<strong>必须孟婆死亡后</strong>才触发传闻，孟婆死前怎么刷都不会有</li>
      <li>两颗内功的传闻都有<strong>时间窗口</strong>，傀尸死后传闻可能不再刷新</li>
      <li>森林平时不要乱打野兽，等传闻出现再带史燕进去</li>
      <li>九阳神功也有备用途径：封青霄任务（但需要等后期）</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：九阴总纲 + 九阳神功</strong> — 荆棘和大师兄的核心内功
  </div>
</div>

<!-- ===== 8. 吸星大法 ===== -->
<div class="step-guide">
  <h3>🌀 吸星大法 —— 杜康村→喀什连环任务</h3>
  <p style="color:var(--muted);margin-bottom:12px;">最终效果：吸收敌人内力，强力心法</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 杜康村</span> · <span class="action">与花匠对话</span><br>
      杜康村找到花匠 → 花匠请求帮忙。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      ⚠️ 关键选择：选<strong>「不帮」</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 杜康村</span> · <span class="action">鼓励花匠</span><br>
      不帮之后 → 选<strong>「鼓励他」</strong> → 然后离开杜康村。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 杜康村</span> · <span class="action">再次回来</span><br>
      出杜康村 → 再次进入杜康村 → 找花匠对话 → 获得<strong>肚痛帖</strong>。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>肚痛帖</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 喀什</span> · <span class="action">找士兵</span><br>
      去喀什找到士兵 → 士兵索要肚痛帖。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      ⚠️ 关键选择：选<strong>「拒绝」→ 士兵再要 → 再选「拒绝」</strong>（要拒绝多次！）
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">5</div>
    <div class="step-body">
      <span class="loc">📍 喀什</span> · <span class="action">获得吸星大法</span><br>
      反复拒绝后触发战斗 → 打赢 → 获得吸星大法。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>吸星大法</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 冲突警告：</strong>
    <ul>
      <li>第1步花匠那里<strong>必须选「不帮」</strong>，选帮了就拿不到肚痛帖</li>
      <li>第4步士兵索要时必须<strong>反复拒绝</strong>，如果一次就给了也拿不到</li>
      <li>这是最容易走错的支线之一，一步选错就永久错过</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：吸星大法</strong>
  </div>
</div>

<!-- ===== 9. 含光剑 ===== -->
<div class="step-guide">
  <h3>🗡️ 含光剑 —— 剑中剑（伤害+300）</h3>
  <p style="color:var(--muted);margin-bottom:12px;">一把藏在普通剑里的神器</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 天剑门</span> · <span class="action">与小师弟对话</span><br>
      天剑门找到苦恼的小师弟 → 选择<strong>「鼓励他」</strong>。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 天剑门 → 杜康村</span> · <span class="action">找西门峰</span><br>
      天剑门剧情 → 去杜康村找到西门峰（小师弟的师兄）。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 杜康村</span> · <span class="action">获得传家宝剑</span><br>
      西门峰给一柄传家宝剑（看起来普通）。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：传家宝剑（普通外观）
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 洛阳武器店</span> · <span class="action">发现剑中剑</span><br>
      带传家宝剑去洛阳武器店 → <strong>任剑南必须在队</strong> → 触发发现「剑中剑」。<br>
      <span class="teammate">👤 <strong>任剑南必须在队！</strong></span><br>
      🎁 获得：<strong>含光剑</strong>（伤害+300）
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 注意：</strong>最后一步没有任剑南在队 = 剑中剑不会被发现 = 只能拿到普通剑
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：含光剑</strong> — 伤害+300，前期即可获得的强力武器
  </div>
</div>

<!-- ===== 10. 神龙密咒+化骨绵掌 ===== -->
<div class="step-guide">
  <h3>🐉 神龙密咒 + 化骨绵掌 —— 藏海岛宝箱</h3>
  <p style="color:var(--muted);margin-bottom:12px;">卫紫绫核心内功 + 强力毒掌</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 忘忧谷</span> · <span class="action">招募沈湘云</span><br>
      完成沈湘云招募剧情 → 沈湘云入队。<br>
      <span class="teammate">👤 沈湘云</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 黑蝠洞</span> · <span class="action">打欧阳笑</span><br>
      主线推进到黑蝠洞 → 打欧阳笑。<br>
      <span class="teammate">👤 <strong>沈湘云必须出战！</strong>（她需要参与战斗才有后续剧情）</span><br>
      🎁 获得：<strong>寒蝠胆</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 怪医居/沈澜处</span> · <span class="action">交寒蝠胆给沈澜</span><br>
      找到沈澜 → 交寒蝠胆 → 沈澜给钥匙。<br>
      <span class="teammate">👤 沈湘云（需要沈湘云与沈澜的姐妹剧情触发）</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 藏海岛</span> · <span class="action">开宝箱</span><br>
      用钥匙进入藏海岛 → 找到宝箱 → 打开。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>神龙密咒</strong> + <strong>化骨绵掌</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 冲突警告：</strong>
    <ul>
      <li>黑蝠洞沈湘云没出战 = 拿不到寒蝠胆 = <strong>整个链断裂</strong></li>
      <li>寒蝠胆是任务道具，别卖掉或丢弃</li>
      <li>藏海岛龙墨可以顺便拿浪花斩铁式</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：神龙密咒 + 化骨绵掌</strong>
  </div>
</div>

<!-- ===== 11. 撼天古剑 ===== -->
<div class="step-guide">
  <h3>⚔️ 撼天古剑 —— 攻击+370（需臂力55）</h3>
  <p style="color:var(--muted);margin-bottom:12px;">用羊脂白玉碗在洛阳古玩店交换</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 蜘蛛盗贼团</span> · <span class="action">偷取羊脂白玉碗</span><br>
      遭遇蜘蛛盗贼团 → 战斗中偷取<strong>信长</strong> → 获得羊脂白玉碗。<br>
      <span class="teammate">👤 史燕（偷取）</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 洛阳古玩店</span> · <span class="action">交换撼天古剑</span><br>
      带羊脂白玉碗 → 洛阳古玩店 → 与老板交换。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>撼天古剑</strong>（攻击+370）
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 时间限制：</strong>
    <ul>
      <li><strong>必须在完成洛阳夜飘香任务之前</strong>交换！夜飘香任务完成后古玩店老板会消失</li>
      <li>蜘蛛盗贼团是随机遭遇战</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：撼天古剑</strong> — 攻+370，臂力55可装备
  </div>
</div>

<!-- ===== 12. 太极图（古实） ===== -->
<div class="step-guide">
  <h3>☯️ 太极图 —— 古实专属·气血+1000内力+500</h3>
  <p style="color:var(--muted);margin-bottom:12px;">古实专属神器，巨大属性加成</p>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 武当</span> · <span class="action">古实修炼九阳功到10级</span><br>
      招募古实后 → 修炼古实自带九阳功到10重 → 打赢古叶 → 获得<strong>太极神功</strong>。<br>
      <span class="teammate">👤 古实</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 武当</span> · <span class="action">修炼开太极到10级</span><br>
      修炼四通八达+太极拳到10重 → 再打赢古叶 → 获得<strong>开太极</strong> → 修炼开太极到10重。<br>
      <span class="teammate">👤 古实</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 武当</span> · <span class="action">找古叶触发太极图线索</span><br>
      开太极10重后 → 找古叶对话 → 获得太极图线索。<br>
      <span class="teammate">👤 古实</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 洛阳古玩店</span> · <span class="action">追踪线索</span><br>
      去洛阳古玩店调查。<br>
      <span class="teammate">👤 古实</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">5</div>
    <div class="step-body">
      <span class="loc">📍 矿场 → 郊外</span> · <span class="action">找工头 → 找小孩</span><br>
      矿场找到工头 → 郊外找到小孩 → 获得太极图。<br>
      <span class="teammate">👤 古实</span><br>
      🎁 获得：<strong>太极图</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 注意：</strong>这是一个长链任务，需要古实大量修炼时间。
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：太极图</strong> — 气血+1000、内力+500，古实专属神器
  </div>
</div>

<!-- ===== 13. 天外飞仙精要 ===== -->
<div class="step-guide">
  <h3>🌠 天外飞仙精要 —— 无名冢前必须完成</h3>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 杭州右上角</span> · <span class="action">遇小孩吴桐</span><br>
      触发与吴桐的对话。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 杭州</span> · <span class="action">萧复僵尸事件</span><br>
      带<strong>萧复</strong> → 触发僵尸事件 → 找到漂亮石头。<br>
      <span class="teammate">👤 萧复</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 杭州</span> · <span class="action">石头不卖</span><br>
      有人想买石头 → <strong>选「不卖」</strong> → 还给吴桐的娘。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      ⚠️ 卖了石头 = 整个链断裂
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <span class="loc">📍 杭州</span> · <span class="action">找吴大叔</span><br>
      与吴桐的叔叔「吴大叔」对话。<br>
      <span class="teammate">👤 <strong>傅剑寒必须在队</strong></span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">5</div>
    <div class="step-body">
      <span class="loc">📍 杭州</span> · <span class="action">选择相信傅剑寒</span><br>
      选<strong>「相信傅剑寒」</strong> → 战斗 → 打赢。<br>
      <span class="teammate">👤 傅剑寒</span><br>
      🎁 获得：<strong>天外飞仙精要</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 超级重要：</strong>
    <ul>
      <li><strong>必须在无名冢杀傀尸之前完成！</strong>过了无名冢就失效</li>
      <li>石头卖了 = 永久错过</li>
      <li>傅剑寒不在队 = 无法触发最后一步</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：天外飞仙精要</strong> — 悟性77可学，剑系核心招式
  </div>
</div>

<!-- ===== 14. 六脉神剑 ===== -->
<div class="step-guide">
  <h3>👆 六脉神剑 —— 最强指法</h3>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 洛阳当铺</span> · <span class="action">买「不明物」</span><br>
      洛阳当铺 → 购买名为「不明物」的道具。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      ⚠️ 尽早买，后期当铺可能关闭
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 高昌迷宫</span> · <span class="action">救夜叉</span><br>
      主线推进到高昌迷宫 → 救出被困的夜叉。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">触发特殊事件</span><br>
      救出夜叉后 → 持有不明物 → 大地图触发 → 获得六脉神剑。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>六脉神剑</strong>
    </div>
  </div>

  <div class="reward-box">
    🎁 <strong>最终奖励：六脉神剑</strong> — 直线三格·反击·击退·最强指法
  </div>
</div>

<!-- ===== 15. 骑士精神 ===== -->
<div class="step-guide">
  <h3>🐴 骑士精神 —— 最强辅助（队友必定左右互搏）</h3>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 成都</span> · <span class="action">招募塔娅</span><br>
      龙墨成都调停任务中与塔娅对话 → 塔娅入队。<br>
      <span class="teammate">👤 龙墨（触发调停任务的前提）</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 恶人谷</span> · <span class="action">色目人事件（拜火大典前）</span><br>
      <strong>拜火大典前</strong>带塔娅进恶人谷 → 触发色目人相关四连战。<br>
      <span class="teammate">👤 <strong>塔娅必须在队！</strong></span><br>
      🎁 获得：<strong>骑士精神</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 超级重要：</strong>
    <ul>
      <li><strong>拜火大典后</strong>触发的是色目人<strong>入侵</strong>事件，给的是不同奖励，拿不到骑士精神</li>
      <li>必须在<strong>拜火大典之前</strong>完成</li>
    </ul>
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：骑士精神</strong> — 塔娅周围两格队友<strong>必定左右互搏</strong>（攻击两次）
  </div>
</div>

<!-- ===== 16. 百鸟朝凤 ===== -->
<div class="step-guide">
  <h3>🦜 百鸟朝凤曲 + 罗汉伏魔棍 —— 少林铜人任务</h3>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 少林</span> · <span class="action">史燕触发铜人巡山</span><br>
      带<strong>史燕</strong>进入少林 → 触发「铜人巡山」剧情。<br>
      <span class="teammate">👤 <strong>史燕必须在队</strong></span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 少林</span> · <span class="action">带萧复+水盼盼再入少林</span><br>
      触发铜人巡山后 → 带<strong>萧复 + 水盼盼</strong>再次进入少林 → 触发百鸟朝凤剧情 → 获得百鸟朝凤曲。<br>
      <span class="teammate">👤 <strong>萧复 + 水盼盼必须在队</strong></span><br>
      🎁 获得：<strong>百鸟朝凤曲</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 少林</span> · <span class="action">打十八铜人</span><br>
      百鸟朝凤曲到手后 → 可以挑战十八铜人阵 → 获得罗汉伏魔棍。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>罗汉伏魔棍</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 注意：</strong>步骤顺序不能反！必须先带史燕，再带萧复+水盼盼。反了触发不了。
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：百鸟朝凤曲 + 罗汉伏魔棍</strong>
  </div>
</div>

<!-- ===== 17. 浪花斩铁式 ===== -->
<div class="step-guide">
  <h3>🌊 浪花斩铁势 —— 游戏最强单体伤害</h3>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 洛阳 → 成都</span> · <span class="action">龙墨入队</span><br>
      完成洛阳小孟任务 → 成都龙墨调停 → 撑剑圣三招 → 龙墨入队。<br>
      <span class="teammate">👤 龙墨</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 藏海岛右侧沙滩</span> · <span class="action">领悟浪花斩铁式</span><br>
      带龙墨去藏海岛 → <strong>右侧沙滩</strong> → 触发龙墨剧情 → 领悟。<br>
      <span class="teammate">👤 <strong>龙墨必须在队</strong></span><br>
      🎁 获得：<strong>浪花斩铁势</strong>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠️ 注意：</strong>必须龙墨在队才能触发沙滩剧情，不在队去沙滩白跑。
  </div>
  <div class="reward-box">
    🎁 <strong>最终奖励：浪花斩铁势</strong> — <strong>全游戏最强单体伤害</strong>
  </div>
</div>

<!-- ===== 18. 玉女剑+玉女心经 ===== -->
<div class="step-guide">
  <h3>🌸 玉女剑法 + 玉女心经 —— 水盼盼核心</h3>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 大地图</span> · <span class="action">遇杨雨枫</span><br>
      大地图随机遇到杨雨枫 → 触发剧情。<br>
      <span class="teammate">👤 无特殊要求</span>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <span class="loc">📍 战斗</span> · <span class="action">打九阴幽仆</span><br>
      与九阴幽仆战斗 → 打赢 → 获得玉女剑法 + 玉女心经。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      🎁 获得：<strong>玉女剑法 + 玉女心经</strong>
    </div>
  </div>
  <div class="chain-link">⬇</div>
  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <span class="loc">📍 雪地</span> · <span class="action">修炼到10重 → 全真剑法</span><br>
      玉女心经修炼到10重 → 雪地练剑 → 水盼盼领悟全真剑法。<br>
      <span class="teammate">👤 水盼盼</span>
    </div>
  </div>

  <div class="reward-box">
    🎁 <strong>最终奖励：玉女剑法 + 玉女心经 + 全真剑法</strong> — 水盼盼完整的剑法体系
  </div>
</div>

<!-- ===== 19. 禅宗莲华功 ===== -->
<div class="step-guide">
  <h3>🪷 禅宗莲华功 —— 白马寺答题</h3>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <span class="loc">📍 洛阳白马寺</span> · <span class="action">答题</span><br>
      白马寺主线剧情后 → 与寺内僧人对答。<br>
      <span class="teammate">👤 无特殊要求</span><br>
      ⚠️ 答题答案：<strong>1 → 2 → 3</strong>
    </div>
  </div>

  <div class="reward-box">
    🎁 <strong>最终奖励：禅宗莲华功</strong> — 不错的心法
  </div>
</div>

<!-- ===== 常见误区 & 偷窃速查 ===== -->
<div class="phase"><h2>⚠️ 物品获取关键误区</h2></div>

<div class="priority-box">
  <h3>🔴 永久错过清单（严格时间窗）</h3>
  <ul>
    <li><strong>先天功（4残页）：</strong>必须在<strong>进入赛王府见天机老人前</strong>集齐。进入赛王府后大地图传闻停止</li>
    <li><strong>羊脂白玉碗→撼天古剑：</strong>必须在<strong>洛阳夜飘香任务完成前</strong>给古玩店老板</li>
    <li><strong>天外飞仙精要：</strong>必须在<strong>无名冢杀傀尸前</strong>完成杭州吴桐任务</li>
    <li><strong>小孟任务（迅雷剑法+点穴截脉）：</strong>必须在<strong>龙墨挑战罗刹分舵前</strong>完成</li>
    <li><strong>软猬甲+黑玉镯+罗汉拳：</strong>赛王府战斗<strong>必须带史燕出战</strong>，战后自动获得。不带=永久错过</li>
    <li><strong>葵花宝典三件套：</strong>无名冢必须<strong>同时带方云华+任剑南</strong>进傀尸房间</li>
    <li><strong>西方异金→倚天剑：</strong>传闻随机触发，偷取失败或没带史燕=倚天剑做不出来</li>
    <li><strong>九阳神功（森林）：</strong>必须在<strong>孟婆死后、傀尸死亡前</strong>触发传闻偷猴子</li>
    <li><strong>恶人谷支线：</strong>必须在<strong>拜火大典前</strong>全部清完！拜火大典后色目人入侵，部分支线关闭</li>
    <li><strong>骑士精神：</strong>拜火大典<strong>前</strong>带塔娅进恶人谷完成色目人四连战</li>
  </ul>
</div>

<div class="priority-box" style="background: linear-gradient(135deg, #e8f5e9, #c8e6c9); border-color: var(--tag-recruit);">
  <h3 style="color: var(--tag-recruit);">🟢 史燕/岳胖子偷窃速查</h3>
  <ul>
    <li><strong>史燕偷取（必须偷的）：</strong>赛王府（软猬甲+黑玉镯）、森林熊（九阴总纲）、森林猴（九阳神功）、东瀛浪人（明玉功+三日月无铭）、西方异金持有者（倚天剑前置）、蜘蛛盗贼团信长（羊脂白玉碗）</li>
    <li><strong>岳胖子获取：</strong>华山书架（无双无对）、兽王庄（银蛇千转）、隐元阁购买（万佛朝宗/风神腿/蚩尤刀法等）、玄铁疑云（狂风剑法）</li>
    <li><strong>一场战斗多个目标要偷：</strong>少林三神僧（燃木刀法/罗汉伏魔功/齐眉棍/定海神针·四人全偷）、武当三圣（湛卢剑/龙渊剑/太极剑/推天献印/归藏剑·三人全偷）</li>
    <li><strong>偷窃技巧：</strong>每回合偷一次，优先偷BOSS/精英。史燕速度快，让她先动偷完再输出</li>
  </ul>
</div>

</div><!-- /tab-items -->"""


def main():
    print("Reading HTML file...")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Backup
    print(f"Creating backup: {BACKUP_PATH}")
    with open(BACKUP_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    # Replace tab-builds
    builds_start_marker = '<div class="tab-content" id="tab-builds">'
    builds_end_marker = '</div><!-- /tab-builds -->'

    b_start = content.find(builds_start_marker)
    b_end = content.find(builds_end_marker, b_start)

    if b_start == -1 or b_end == -1:
        print(f"ERROR: Cannot find tab-builds markers! start={b_start}, end={b_end}")
        return

    b_end += len(builds_end_marker)
    print(f"tab-builds: lines {content[:b_start].count(chr(10))+1} to {content[:b_end].count(chr(10))+1}")

    content = content[:b_start] + NEW_BUILDS + content[b_end:]

    # Replace tab-items
    items_start_marker = '<div class="tab-content" id="tab-items">'
    items_end_marker = '</div><!-- /tab-items -->'

    i_start = content.find(items_start_marker)
    i_end = content.find(items_end_marker, i_start)

    if i_start == -1 or i_end == -1:
        print(f"ERROR: Cannot find tab-items markers! start={i_start}, end={i_end}")
        return

    i_end += len(items_end_marker)
    print(f"tab-items: lines {content[:i_start].count(chr(10))+1} to {content[:i_end].count(chr(10))+1}")

    content = content[:i_start] + NEW_ITEMS + content[i_end:]

    # Write
    print(f"Writing updated file...")
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"DONE! Updated: {HTML_PATH}")
    print(f"Backup saved: {BACKUP_PATH}")


if __name__ == "__main__":
    main()
