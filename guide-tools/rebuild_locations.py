#!/usr/bin/env python3
"""Rebuild tab-locations with ALL game locations."""
import re

html_path = r"c:\Users\yanshijie\WorkBuddy\Claw\outputs\侠客风云传前传_终极全攻略.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find tab-locations boundaries
start = content.find('<div class="tab-content" id="tab-locations">')
end = content.find('</div><!-- /tab-locations -->')
if start == -1 or end == -1:
    print("ERROR: Cannot find tab-locations boundaries")
    exit(1)
end += len('</div><!-- /tab-locations -->')

T = '    <tr class="hl">'
R = '    <tr>'
TE = '  </table>'
TS = '  <table>'
T2 = '    <tr><th style="width:14%">位置/NPC</th><th>内容/任务/奖励</th><th style="width:13%">需求</th></tr>'
T3 = '    <tr><th style="width:14%">内容</th><th>需求</th></tr>'

new_content = """<div class="tab-content" id="tab-locations">

<div class="phase"><h2>🏠 逍遥谷</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">位置/NPC</th><th>内容/任务/奖励</th><th style="width:13%">需求</th></tr>
    <tr><td>右下小屋一楼</td><td>肉包子×3（餐桌）</td><td>—</td></tr>
    <tr><td>右下小屋二楼</td><td>逍遥散、九转还魂丹 / 床铺→荆棘秘籍二选一（回龙逆斩/不动一剑痕）</td><td>—</td></tr>
    <tr class="hl"><td>喂猫（灶台旁）</td><td>给咸鱼（老胡旁屋子取4条）→选项3「破烂的书」→<strong>仙音乐集</strong>（必拿！） 其余→智慧果</td><td>咸鱼</td></tr>
    <tr class="hl"><td>一楼古琴</td><td>萧复+水盼盼触发少林寺百鸟朝凤后→摸琴→切磋无论输赢得<strong>绕梁琴</strong></td><td>萧复、水盼盼</td></tr>
    <tr><td>左侧下方小屋</td><td>剧情后地上捡<strong>武林宝典</strong>（岳胖子掉落） + 桌上蜘蛛</td><td>—</td></tr>
    <tr class="hl"><td>右侧上方小屋</td><td>大师兄根骨85+悟性80看画→<strong>佛渡拜火三迦叶</strong>前置（需火焰刀+天山六阳掌10重+醉仙任务）</td><td>后期</td></tr>
    <tr><td>左侧上方小屋</td><td>书架上取<strong>萧皓霜家书</strong>（萧复入队前置）</td><td>—</td></tr>
    <tr><td>师父切磋（1）</td><td>大小内功8重→第一次请益→小无相功/日月神功（随机）</td><td>—</td></tr>
    <tr><td>师父切磋（2）</td><td>第一次所选内功满10重→第二次请益→天山六阳掌/天山折梅手/刀山剑岳（随机）</td><td>—</td></tr>
    <tr class="hl"><td>决战前师父切磋</td><td>谷月轩+荆棘vs无瑕子→胜利得<strong>逍遥御风</strong></td><td>终章前</td></tr>
    <tr><td>老胡</td><td>荆棘切磋→藤甲+八方藏刀式 / 每入队新队友→<strong>觥筹交错组</strong>（杭州酒楼开轰趴）</td><td>—</td></tr>
    <tr><td>老胡（不动）</td><td>不动入队后带不动见老胡→<strong>机关武偶</strong>（不动专属饰品）</td><td>不动</td></tr>
  </table>
</div>

<div class="phase"><h2>🎵 弦箫洞 & 弦箫幽谷</h2></div>
<div class="priority-box"><ul>
  <li>主线第一站，追傀尸进洞→解谜→进入幽谷</li>
  <li>谷月轩悟性80→调查中间棋盘→<strong>十王走马式</strong></li>
  <li>萧复悟性60→调查树下琴→<strong>声无哀乐</strong></li>
  <li>田里采白菜×9→种智慧果→传闻金翅鸟来采收（乌鸦则枯萎）</li>
  <li>主线结束后再来当初翻过的栅栏→开通秘密通道→大地图解锁弦箫幽谷</li>
</ul></div>
<div class="card">
  <table>
    <tr><th>步骤</th><th>内容</th></tr>
    <tr class="hl"><td>解谜</td><td>调查古琴选「高山流水」→依次选 宫、征、羽、商、角 →暗门开启</td></tr>
    <tr><td>河道</td><td>水退后捡：草鱼×5、虹鲤×1、神鱼×1（别捡完，留空间后续再来）</td></tr>
    <tr class="hl"><td>种田</td><td>采收白菜×9 → 种智慧果 → 传闻栏出现金翅鸟即可回来收爆米花</td></tr>
    <tr><td>密道</td><td>主线结束后重来→荆棘当初翻过的栅栏处触发→大树移动→大地图新增弦箫幽谷入口</td></tr>
  </table>
</div>

<div class="phase"><h2>🏯 洛阳</h2></div>
<div class="card">
  <table>
    <tr><th style="width:12%">NPC/位置</th><th>内容</th><th style="width:12%">需求</th></tr>
    <tr class="hl"><td>关伟碰瓷</td><td>（限时！1洛必须做）对话关伟→周围3人→老太太家→紫衣人→关伟→老太太→碰瓷人→赌场老板（给3000=智慧果3 / 打架=咸鱼）→碰瓷人→老太太家找碰瓷人→<strong>石破天惊拳精要</strong></td><td>—</td></tr>
    <tr><td>叶半仙（衙门地牢）</td><td>对话选斩首→游戏中期再进洛阳去矿场找→<strong>蟹雕像</strong></td><td>—</td></tr>
    <tr class="hl"><td>郊外猎人</td><td>打金翅鸟→<strong>金雁功</strong>（推荐给史燕学）</td><td>—</td></tr>
    <tr class="hl"><td>菜篮大盗</td><td>与买菜两人+衙门口两老者→江府对面树下找人→选「更适合逮捕此贼」→守卫帮忙打→千年人参+2000钱→此贼升官到衙门</td><td>—</td></tr>
    <tr><td>胸口碎大石</td><td>看表演→铁匠铺拿精钢→外面熔炉打锤→交任务（可故意失败多次找老板补精钢练打铁）→后期沈湘云在队有额外剧情</td><td>⚠️第一次别带沈湘云</td></tr>
    <tr><td>小白豆浆</td><td>买一份→白马寺右边给小孩卢小小</td><td>—</td></tr>
    <tr><td>野鸡斗鸡</td><td>给蜈蚣（洛阳城内+郊外各1条）→<strong>桂圆红枣鸡汤</strong></td><td>—</td></tr>
    <tr><td>古董店</td><td>右上柜子拿裂开的镯子→老板要<strong>羊脂白玉碗</strong>（大地图幸长身上偷/蜘蛛盗贼团偷）→<strong>撼天古剑</strong></td><td>⚠️楚绘招募前完成</td></tr>
    <tr class="hl"><td>赌场</td><td>开一楼两个宝箱→选<strong>溪山行旅图</strong>（字画摊三图之一）</td><td>—</td></tr>
    <tr><td>城门口守卫</td><td>对话发现打瞌睡→一直拒绝收钱→战斗→十全大补丹 / 选收600→阅历</td><td>—</td></tr>
    <tr><td>白马寺</td><td>给小孩卢小小小白豆浆 / 进寺找住持答题→123→<strong>禅宗莲花功</strong>+江瑜入队</td><td>—</td></tr>
    <tr><td>卖鱼妹子（许媛）</td><td>给7条草鱼（弦箫洞5+郊外小岛2）→<strong>鱼雕像</strong></td><td>—</td></tr>
    <tr class="hl"><td>字画摊</td><td>三幅赝品：溪山行旅图(赌场)/庐山高(大地图盗贼偷)/早春图(焦大偷)→每交一1000钱→全交额外<strong>九花玉露丸×3</strong></td><td>—</td></tr>
    <tr class="hl"><td>面摊</td><td>交<strong>虹鲤三鲜面</strong>（杜康村面摊拿虹鲤换）→三选一：<strong>梯云纵</strong>（推荐）/ 环柄刀 / 丹药</td><td>—</td></tr>
    <tr class="hl"><td>天剑门</td><td>鼓励小师弟→故意战败→西门峰「义正辞严」→杜康村桥边找到小师弟→<strong>家传宝剑</strong>→洛阳武器店（任剑南在队→选不卖→离队→铸剑山庄→<strong>含光剑</strong>）</td><td>任剑南</td></tr>
    <tr><td>破庙</td><td>门口乞丐给1000→<strong>狗皮膏药</strong>（每回合回血150）→给驿站伙计换千锤百炼丹 / 给西域换怪鲶鱼<br>佛像后面：<strong>连城剑法精要</strong></td><td>—</td></tr>
    <tr><td>酒馆</td><td>初遇卫紫绫、楚绘 / 初遇傅剑寒、无颠→无颠倒地后桌下捡<strong>大金刚拳精要</strong></td><td>—</td></tr>
    <tr class="hl"><td>江府</td><td>江天雄身后摸<strong>拜月七绝</strong>（江瑜在队） | 江瑜切磋：第一次→地煞无极功 / 第二次→<strong>苍天有极</strong></td><td>江瑜</td></tr>
    <tr><td>白马寺凉亭</td><td>姜望剧情→鱼面摊答题<strong>21443</strong>→谷月轩+卫紫绫悟性+1</td><td>—</td></tr>
    <tr class="hl"><td>咸鱼粥</td><td>沈湘云在队→古玩店隔壁老婆婆→集市鱼贩→郊外渔翁（选不买！）→河洛客栈厨房点鱼→帮忙战斗（<strong>故意战败</strong>！战败得迅雷剑法）→得虹鲤→交任务沈湘云+100气血+3悟性</td><td>沈湘云</td></tr>
    <tr><td>擂台后续</td><td>沈湘云在队→完成咸鱼粥后与碎大石对话→劝回家→再进洛阳老婆婆房前→<strong>朱玉金簪</strong></td><td>沈湘云</td></tr>
    <tr class="hl"><td>小孟的决心</td><td>酒馆厨房接→河洛客栈→罗煞分舵恶战→修罗宫左边找骆女侠→河洛客栈老杜→<strong>神鱼</strong>（+300气血）→大地图后续「小孟的决心」</td><td>沈湘云 / ⚠️龙墨杀罗煞前完成！</td></tr>
    <tr><td>矿场</td><td>救过叶半仙后→对话</td><td>—</td></tr>
    <tr class="hl"><td>玄铁疑云</td><td>任剑南在队→鱼摊许媛→郊外大妈→矿场工头→渔翁前小岛调查尸体→天剑门内（岳胖子→狂风剑法）→西门玄→矿场左侧矿工→心残→工头→<strong>玄铁</strong>。给任浩然→无极刀剑 / 老胡打造</td><td>任剑南 / 岳胖子</td></tr>
    <tr class="hl"><td>李徽之家</td><td>带岳胖子去小白豆浆对话→李徽之家→调查两柜子之间→岳胖子偷窃被抓→一系列战斗→<strong>一阳指 + 多罗叶指</strong></td><td>岳胖子</td></tr>
    <tr class="hl"><td>当铺</td><td>岳胖子在队→花10万买不明物→高昌救夜叉后大地图→<strong>六脉神剑</strong></td><td>岳胖子</td></tr>
    <tr><td>衙门</td><td>史燕在队→交一袋赃物选给史燕→<strong>盗墓笔记</strong>（史燕专属）</td><td>史燕</td></tr>
    <tr><td>郊外种花大叔</td><td>给映山红（藏海岛偷花玖瑟）→<strong>火红金丹</strong>→再对话→茯苓首乌丸</td><td>—</td></tr>
    <tr><td>碰瓷的家</td><td>逃出洛阳城任务时进入→千锤百炼丹</td><td>—</td></tr>
    <tr class="hl"><td>豆腐西施（先天功前置）</td><td>对话两人→大地图救状元郎（传闻）→对话三人→蜘蛛盗贼团传闻→大地图救云游商人→残页1+2→找状元郎→隐元阁残页3→大地图遇斗篷客战斗→残页4→赛王府天机老道复原→<strong>先天功</strong></td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🍶 杜康村</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">NPC/位置</th><th>内容/任务/奖励</th><th style="width:13%">需求</th></tr>
    <tr><td>左下矿工（阿平）</td><td>沈湘云对话→荆棘气血+50→<strong>蓝晶矿</strong>（燕宇招募链第一环）</td><td>沈湘云</td></tr>
    <tr class="hl"><td>种花小哥（张帆）</td><td>选「种得真好」→帮送花→酒馆杜鹃→得兰花 / <strong>选拒绝→再进村→得肚痛贴</strong>（喀什换吸星大法）</td><td>—</td></tr>
    <tr class="hl"><td>面摊</td><td>给虹鲤→<strong>虹鲤三鲜面</strong>→拿回洛阳面摊交→选<strong>梯云纵</strong></td><td>—</td></tr>
    <tr><td>右边大妈（招弟）</td><td>要虹鲤→找何爷→找赵老翁拿钓竿→回报何爷得虹鲤→给招弟→1000钱</td><td>—</td></tr>
    <tr><td>酒馆小二</td><td>买即墨老酒（恶人谷找喝任务用）</td><td>—</td></tr>
    <tr><td>桥边小师弟</td><td>天剑门任务后→给<strong>家传宝剑</strong></td><td>—</td></tr>
    <tr class="hl"><td>傅剑寒招募</td><td>李大娘→食客→李大娘→洛阳捕快→集市摊贩→李大娘→城门卫兵→赵寡妇→酒馆傅剑寒→夜闯钱府（史燕→夜明珠）→门口打焦大等→杜康村招募</td><td>史燕</td></tr>
    <tr><td>收集品</td><td>入口珍贵药草 / 神龛蜘蛛 / 桥上蟾蜍 / 张帆旁蜈蚣 / 招弟旁蟾蜍 / 米摊珍贵药草 / 何爷附近稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🏛️ 少林寺</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">位置/NPC</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr><td>门前扫地僧</td><td>答<strong>26阶</strong>→全队经验+阅历</td><td>—</td></tr>
    <tr><td>左侧蹲马步僧（长兄如父）</td><td>拿书信→龙井村右上找王思思→回报→<strong>大须弥山棍</strong></td><td>—</td></tr>
    <tr><td>上方看花僧（佛渡有缘人）</td><td>喀什右下进大漠找徒弟→战斗→回报→<strong>金刚不坏体</strong></td><td>—</td></tr>
    <tr><td>右侧练武僧</td><td>大师兄大金刚拳精通后触发战斗→蛙雕像+洗髓再造丹</td><td>大师兄</td></tr>
    <tr class="hl"><td>右侧小径和尚（FFF团）</td><td>先带<strong>史燕</strong>（萧复+水盼盼<strong>不能</strong>在队）→与两铜人对话触发「驱逐情侣」→再带萧复+水盼盼→<strong>百鸟朝凤曲</strong>→十八铜人战斗→<strong>罗汉伏魔棍</strong>（⚠️顺序不能反！）</td><td>史燕→萧复+水盼盼</td></tr>
    <tr class="hl"><td>少林防卫战</td><td>传闻「夜叉被抓」→守门僧对话→开打→<strong>无相劫指</strong></td><td>—</td></tr>
    <tr><td>无色方丈</td><td>救回不动后可挑战罗汉阵（不动离队去南少林后）</td><td>—</td></tr>
    <tr><td>左侧三神僧</td><td>切磋→史燕可偷：燃木刀法/罗汉伏魔功（仅一次）</td><td>史燕</td></tr>
    <tr class="hl"><td>不动招募</td><td>南少林剧情完毕后→在少林寺招收不动</td><td>完成南少林线</td></tr>
  </table>
</div>

<div class="phase"><h2>⛰️ 武当</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">位置/NPC</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr><td>掌门卓人清</td><td>对话→三黄宝蜡丹×3 + 梯云踪 / 方云华在队→请益两次→紫霞神功+太极化清</td><td>—/方云华</td></tr>
    <tr><td>左下看门弟子</td><td>送信景阳冈→打劈挂掌门→回武当大战→劈卦神拳精要+<strong>紫薇软剑</strong> / 高昌遗迹再遇此人</td><td>—</td></tr>
    <tr><td>右上看守弟子</td><td>给五宝花蜜酒×3（小阿曼在队→毒龙教大厅拿）→<strong>倚天屠龙功精要</strong></td><td>小阿曼</td></tr>
    <tr><td>右侧下方弟子</td><td>森林打猴王→<strong>龙泣剑精要</strong>（需根骨67）</td><td>—</td></tr>
    <tr class="hl"><td>古叶（古实师父）</td><td>古实九阳功10级→打古叶→<strong>太极神功</strong> / 四通八达+太极拳10级→再打→<strong>开太极</strong></td><td>古实</td></tr>
    <tr class="hl"><td>古叶（太极图）</td><td>古实开太极10级→古叶对话→洛阳古玩店老板→矿场工头→洛阳郊外小孩→<strong>太极图</strong>（古实专属·气血+1000内力+500）</td><td>古实</td></tr>
    <tr><td>古实招募</td><td>杭州方云华任务完成后→武当找古实→切磋→入队</td><td>—</td></tr>
    <tr><td>收集品</td><td>大殿右侧石阶下：蜘蛛 / 右侧石阶上走：稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🏔️ 华山</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">位置</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr><td>正厅左边坐垫</td><td>摸<strong>玉佩</strong>→去青城派还给右侧弟子→<strong>灵飞经</strong></td><td>—</td></tr>
    <tr><td>正厅右侧书架</td><td>摸秘籍→<strong>无双无对</strong></td><td>岳胖子</td></tr>
    <tr><td>左侧凉亭</td><td>拿<strong>呕血谱</strong>→忘忧谷橘叟换满天花雨</td><td>—</td></tr>
    <tr class="hl"><td>左侧山顶</td><td>（限时！三派掌门后第一次来）曹萼华剧情→帮华山弟子→战斗→<strong>冲灵剑法残本</strong></td><td>—</td></tr>
    <tr><td>掌门曹岱</td><td>对话选奖励→<strong>连山诀</strong>（气血）或 正气诀（内力），推荐连山诀</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🗡️ 铸剑山庄</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">位置/NPC</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr><td>庄主任浩然</td><td>给蓝晶矿→<strong>清风剑</strong> + 琼华剑 / 燕宇在队→太乙晶石</td><td>—</td></tr>
    <tr><td>任剑南招募</td><td>森林萧复+任剑南→笑傲江湖7重→再找→贺陀战→铸剑山庄招募</td><td>萧复</td></tr>
    <tr><td>左侧剑冢</td><td>任剑南在队→调查断剑→<strong>情义七剑</strong>（需根骨64）</td><td>任剑南</td></tr>
    <tr class="hl"><td>右侧老管家</td><td>华山冲灵残页后→老管家→带傅剑寒去右侧墙壁调查→<strong>冲灵剑法</strong></td><td>傅剑寒</td></tr>
    <tr class="hl"><td>重铸倚天剑</td><td>绿柳山庄得倚天断剑+<strong>西方异金</strong>（大地图传闻偷取）→任浩然铸造→<strong>倚天剑</strong>（水盼盼专属）</td><td>水盼盼</td></tr>
  </table>
</div>

<div class="phase"><h2>🏛️ 青城派</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>大树下燕宇→荆棘切磋→打赢入队（燕宇在队全队阅历翻倍！）</td><td>前置：沈湘云→杜康村蓝晶矿→铸剑山庄</td></tr>
    <tr><td>右侧青城门人→归还玉佩（华山坐垫下捡）→<strong>灵飞经</strong></td><td>—</td></tr>
    <tr><td>⚠️ 紫阳子→对话触发大地图事件，当前打不过先别对话</td><td>—</td></tr>
    <tr class="hl"><td>诚王支线（血色姻缘后期）：青城山找诚王→荆棘打心魔→洛阳古玩店→回青城→洛阳破庙</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🎵 忘忧谷</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">NPC</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr><td>沈湘云招募</td><td>进谷自动剧情→邀沈湘云入队（唯一治疗！）</td><td>—</td></tr>
    <tr class="hl"><td>橘叟</td><td>给呕血谱（华山凉亭）→对弈→<strong>满天花雨</strong></td><td>—</td></tr>
    <tr><td>书生</td><td>给快雨时晴帖（大地图强盗偷）→战斗→<strong>快雨时晴刀</strong></td><td>—</td></tr>
    <tr><td>仙音</td><td>将仙音乐集给萧复→<strong>清心普善咒</strong>（萧复的加移动技能）</td><td>萧复</td></tr>
    <tr class="hl"><td>醉仙（字谜）</td><td>猜四句诗对应人物：一棋(橘叟)二书(书生)三琴(仙音)四画(丹青)→<strong>醉拳+酒仙葫芦</strong></td><td>—</td></tr>
    <tr class="hl"><td>醉仙（进阶）</td><td>给葡萄美酒+夜光杯→切磋→萧复<strong>碧海潮生曲</strong>/ 大师兄火焰刀+天山六阳掌10重→<strong>佛渡拜火三迦叶</strong></td><td>萧复 / 大师兄</td></tr>
    <tr><td>花痴招募</td><td>龙墨线推进到成都→忘忧谷找花痴→入队</td><td>龙墨线进度</td></tr>
    <tr><td>仙音（血色姻缘）</td><td>森林救沐萍任务→忘忧谷找仙音学<strong>点穴手</strong>→练到5级→回森林</td><td>血色姻缘线</td></tr>
  </table>
</div>

<div class="phase"><h2>💀 怪医居</h2></div>
<div class="card">
  <table>
    <tr><th>时机</th><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>首次（主线）</td><td>带卫紫绫见沈澜→卫紫绫领悟<strong>千蛛万毒手+星宿心法</strong></td><td>—</td></tr>
    <tr><td>收集品</td><td>左侧砂锅→蜈蚣 / 瓶罐→珍贵药草+蝎子 / 上台阶炉灶→蟾蜍+蜘蛛</td><td>—</td></tr>
    <tr class="hl"><td>黑蝠洞后</td><td>把寒蝠胆给沈澜→得蛇形钥匙→藏海岛宝箱→<strong>化骨绵掌+神龙秘咒</strong></td><td>完成黑蝠洞</td></tr>
    <tr><td>毒虫熬汤</td><td>小阿曼在队→点左上毒锅→交5种毒虫各5只→卫紫绫领悟<strong>鼎心无量功</strong></td><td>小阿曼</td></tr>
    <tr class="hl"><td>沈澜招募</td><td>每次招募需沈湘云在队→来怪医居对话</td><td>沈湘云</td></tr>
  </table>
</div>

<div class="phase"><h2>🌲 森林</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">内容</th><th style="width:13%">需求</th></tr>
    <tr class="hl"><td>史燕入队→1万钱招募（偷窃核心！）</td><td>—</td></tr>
    <tr class="hl"><td>任剑南→带萧复→获<strong>笑傲江湖曲</strong>→萧复练到7重→再来对话→贺陀战斗→铸剑山庄招募</td><td>萧复</td></tr>
    <tr class="hl"><td>传闻「熊拖走九阴幽仆」→打熊→史燕/岳胖子偷→<strong>九阴总纲</strong></td><td>史燕/岳胖子</td></tr>
    <tr class="hl"><td>传闻「猴子拿破书」→（孟婆死后触发）打猴子→偷→<strong>九阳神功</strong></td><td>史燕/岳胖子</td></tr>
    <tr><td>打熊→熊掌（成都肉摊换大王蛇胆）/ 玉蜂浆（兽王庄换兽王功）</td><td>—</td></tr>
    <tr><td>打猴子→猴儿酒</td><td>—</td></tr>
    <tr class="hl"><td>救沐萍（血色姻缘后期）→忘忧谷学点穴手5级→森林救人</td><td>血色姻缘线</td></tr>
  </table>
</div>

<div class="phase"><h2>🏠 八卦门</h2></div>
<div class="card">
  <table>
    <tr><th>步骤</th><th>内容</th></tr>
    <tr><td>1</td><td>进八卦门→自动触发商家兄弟吵架</td></tr>
    <tr><td>2</td><td>成都百草门→发现商仲智大量买药</td></tr>
    <tr><td>3</td><td>回八卦门大殿→阻止下药→检查无毒→门口出现发光花→点花</td></tr>
    <tr><td>4</td><td>东渡口→入口卖鱼处→妇人食物中毒→卫紫绫发现真相</td></tr>
    <tr class="hl"><td>5</td><td>回八卦门→战斗打赢商仲智→<strong>八卦游身掌</strong>→商仲仁入队</td></tr>
    <tr class="hl"><td>额外</td><td>左边书柜→<strong>鹰爪功</strong>（商仲仁/岳胖子）</td></tr>
    <tr><td>额外</td><td>调查左边桌上字→古实vs商仲仁→BUFF（古实+商仲仁在队）</td></tr>
    <tr class="hl"><td>额外</td><td>商仲仁在队→打赢商鹤鸣→<strong>八卦乱环式</strong></td></tr>
  </table>
</div>

<div class="phase"><h2>⛩️ 景阳冈</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">NPC/任务</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr><td>大娘与阿森</td><td>跑腿→得<strong>龙井虾仁</strong>→再对话→<strong>地煞绝命腿</strong></td><td>—</td></tr>
    <tr><td>老头与阿丹</td><td>劝老爷子→东渡口传话→<strong>蛇雕像</strong></td><td>—</td></tr>
    <tr><td>老虎</td><td>战斗→<strong>九阴飞絮</strong></td><td>—</td></tr>
    <tr class="hl"><td>劈挂掌门（黄天化）</td><td>武当送信任务→打劈挂掌门→后续回武当大战</td><td>武当弟子信</td></tr>
    <tr class="hl"><td>史义招募（血色姻缘）</td><td>景阳冈左上方→帮史义打退敌人→入队→一起去洛阳香烛店</td><td>血色姻缘线</td></tr>
    <tr><td>收集品</td><td>蜘蛛 / 毒蛇 / 稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🌾 龙井村</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr><td>右上王思思→少林寺左侧僧人的妹妹→回报少林得<strong>大须弥山棍</strong></td><td>—</td></tr>
    <tr class="hl"><td>井边三人→触发<strong>龙井异事</strong>→打孟婆→需三派传人（古实+水盼盼+少林传人）驱散寒毒</td><td>古实、水盼盼、不动</td></tr>
    <tr class="hl"><td>龙井异事完成后→大地图黑蝠洞解锁，水盼盼暂时离队</td><td>—</td></tr>
    <tr><td>收集品：左边毒蛇/珍贵药草×3 / 右边蜈蚣 / 上方蜈蚣</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🛕 南少林</h2></div>
<div class="card">
  <table>
    <tr><th>步骤</th><th>内容</th><th>需求</th></tr>
    <tr><td>1</td><td>进入→剧情得知酆都人来犯→左上找天悟禅师→右上找虚明→选休息→战斗（黑白无常偷：<strong>血饮</strong>/紫金双刃）→得<strong>如影随形腿精要</strong></td><td>—</td></tr>
    <tr><td>2</td><td>出南少林→大地图南少林西南方绕→遇袈裟窃贼→战斗夺回红叶袈裟</td><td>—</td></tr>
    <tr class="hl"><td>3</td><td>回南少林→发现被屠→左院找到天悟禅师→要你去救不动</td><td>—</td></tr>
    <tr><td>收集品</td><td>大殿左侧麻袋：稀有矿石×4 / 左院手推车旁：珍贵药草×4 / 左院大塔：蜘蛛 / 右院小塔：蜘蛛</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🌳 原始野林</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>南少林后→第一个岔口上方→救不动→战斗→<strong>混元功</strong>→不动入队</td><td>南少林线</td></tr>
    <tr class="hl"><td>小阿曼在队→遇受伤阿傍→大漠找赤蛛虫→<strong>裂风鞭法</strong></td><td>小阿曼</td></tr>
    <tr class="hl"><td>野林密会（主线）→接到江天雄传信后→探查→打番僧→自动解锁恶人谷</td><td>龙墨线后期</td></tr>
    <tr><td>收集品：毒蛇×4 / 珍贵药草</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>⚓ 东渡口</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">任务</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr class="hl"><td>卖猴子骗局</td><td>入口一群人→听说猴子卖钱→东渡口附近闲逛→争夺猴子事件→1万买下→回东渡口揭发→杭州客栈二楼打幕后→<strong>七彩云霞</strong></td><td>—</td></tr>
    <tr class="hl"><td>血色姻缘·起始</td><td>杭州码头海沙帮→切口（杭州妓院老鸨）→东海分舵→救完回东渡口→秦红殇登场→接<strong>血色姻缘</strong></td><td>—</td></tr>
    <tr class="hl"><td>渔夫解锁赛王府</td><td>水盼盼龙井村离队后→与海边小船旁老头对话→说海面结冰出不了海→需完成东海分舵敖广→再来→解锁赛王府</td><td>⚠️需先完成东海分舵</td></tr>
    <tr><td>卖海鲜</td><td>八卦门二商事件关键NPC→询问食客中毒线索</td><td>八卦门线</td></tr>
    <tr class="hl"><td>血色姻缘·护送</td><td>后期秦红殇归队→渡口问村民→组塔娅→汤木对话→出海护送沐萍→船上找3间谍/7鸡/1信→战黑冢罗王</td><td>塔娅</td></tr>
    <tr><td>敖广招募</td><td>完成护送后→东海分舵招安敖广→入队</td><td>—</td></tr>
    <tr><td>秦红殇招募</td><td>血色姻缘全完成后→东渡口最里面码头招募</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🏙️ 成都</h2></div>
<div class="card">
  <table>
    <tr><th style="width:12%">位置/NPC</th><th>内容</th><th style="width:12%">需求</th></tr>
    <tr class="hl"><td>绝刀门前黄狗</td><td>喂包子→跟狗走→破庙前人骨→杭州丐帮分舵→<strong>萧遥招募</strong></td><td>包子</td></tr>
    <tr><td>樵夫</td><td>乐山大佛拿珍珠→<strong>兽王戒</strong></td><td>—</td></tr>
    <tr><td>肉摊老板</td><td>给熊掌（森林打熊）→<strong>大王蛇胆</strong>（内力+50）</td><td>—</td></tr>
    <tr><td>水果少女</td><td>谜题：一条鞭法/烧饼歌/一条鞭法/知行合一/鄱阳胡→<strong>明光甲</strong></td><td>—</td></tr>
    <tr class="hl"><td>羊肉汤店徐子易</td><td>面摊桌下找书→10药草给老板→<strong>武林群侠传</strong> / 塔娅学会后再对话→<strong>武林通鉴</strong>（推荐带傅剑寒）</td><td>塔娅</td></tr>
    <tr><td>百草门前小女孩</td><td>西湖醋鱼+东坡肉（杭州客栈买）→<strong>虎鹤双形腿精要</strong></td><td>—</td></tr>
    <tr><td>芙蓉楼年芙蓉</td><td>→<strong>庖丁解牛精要</strong> / 龙墨完成后+夏侯非→安慰→经验</td><td>—</td></tr>
    <tr class="hl"><td>破庙</td><td>方云华任务→带史燕/岳胖子→救方云华→方单挑浪→<strong>意乱情迷感悟</strong></td><td>史燕/岳胖子</td></tr>
    <tr><td>宝福楼</td><td>水盼盼招募（荆棘单挑） / 小二情报 / 毒龙教线→小二告知毒蟾下落</td><td>—</td></tr>
    <tr><td>百草门</td><td>八卦门线→商仲智买药 / 龙墨线后→打守门得<strong>神农济世</strong>（⚠️永久无法进百草门）</td><td>—</td></tr>
    <tr class="hl"><td>封青霄系列</td><td>羊肉汤店→赎钗子（100钱）→衙门→封家→破庙打六扇门→少林方丈→卖菜大娘→茶馆姜望→恶人谷打贺陀→封家→找九阳→喀什带花痴找天山弟子→得楞伽经→回成都→<strong>九阳神功</strong></td><td>后期</td></tr>
    <tr><td>龙墨调停</td><td>龙墨挑三大派→成都门口群聚→忘忧谷花痴→唐门找剑圣→单挑撑回合→集市伏击→乐山大佛招募</td><td>花痴</td></tr>
    <tr><td>收集品</td><td>入口珍贵药草 / 羊肉汤店旁毒蛇 / 宝福楼旁蜘蛛</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🌉 杭州</h2></div>
<div class="card">
  <table>
    <tr><th style="width:12%">位置/NPC</th><th>内容</th><th style="width:12%">需求</th></tr>
    <tr class="hl"><td>谢家惨案</td><td>绿衣红衣女子→所有人对话→妓院桥紫衣人→包子铺前刘叔→收尸人→进屋→刚进城找方云华开打</td><td>—</td></tr>
    <tr class="hl"><td>桥头乞丐</td><td>5000钱买秘籍→客栈老板→大师兄悟性70+→<strong>井中八法精要</strong>；不足70可选卖（1万）或不卖（打架）</td><td>—</td></tr>
    <tr><td>客栈</td><td>买西湖醋鱼/东坡肉/龙井虾仁</td><td>—</td></tr>
    <tr><td>包子铺</td><td>买肉包子（成都喂狗用）</td><td>—</td></tr>
    <tr class="hl"><td>楚绘招募系列</td><td>给洛阳古玩羊脂白玉碗→姜望白马寺→<strong>带萧复破庙下小孩吴桐（杀傀尸前！）</strong>→漂亮石头不卖→杭州右上还给小孩娘（傅剑寒在队→选相信→天外飞仙精要）→桥上史捕头（史燕在队）→扫马棚→青楼前唐伯虎+姜望→桥上捕快→成都芙蓉坊→市集楚绘→洛阳客栈→杂货铺血迹→衙门史捕头→市集姜望→客栈楚绘→杂货铺伏击夜飘香→<strong>风花雪月</strong></td><td>萧复、傅剑寒、史燕</td></tr>
    <tr class="hl"><td>人口贩卖</td><td>码头海沙帮→妓院老鸨取切口→回码头→东海分舵</td><td>—</td></tr>
    <tr><td>龙墨系列</td><td>杭州妓院→遇龙墨→战斗→客栈前点苍弟子→罗煞分舵</td><td>血色姻缘线</td></tr>
    <tr class="hl"><td>丐帮血案</td><td>成都喂狗后→杭州丐帮分舵→赛王府（带江瑜看战马册）→成都唐冠南（史燕）→武当→杭州破庙</td><td>江瑜/史燕</td></tr>
    <tr><td>萧遥招募</td><td>成都喂狗→杭州丐帮分舵→剧情→招募</td><td>—</td></tr>
    <tr><td>血色姻缘·越狱</td><td>杭州客栈二楼史义→青城找诚王→洛阳古玩店→青城→洛阳破庙</td><td>后期</td></tr>
    <tr><td>收集品</td><td>珍贵药草 / 毒蛇 / 稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🗿 乐山大佛</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr><td>找5块漂亮石头给和尚→<strong>观音明心鼎</strong>（带史燕好找，入口草地4+走道1）</td><td>史燕推荐</td></tr>
    <tr class="hl"><td>虚真→大地图救少林门人（浪狂毒追杀）→<strong>达摩武诀</strong>（不动专属，需根骨80）</td><td>不动</td></tr>
    <tr><td>成都买米给菜园旁小沙弥→<strong>药王神篇</strong></td><td>—</td></tr>
    <tr><td>菜园和尚→弄坏师父的花→问菜园左边屋前的方丈→经验</td><td>—</td></tr>
    <tr class="hl"><td>亭子对话→凌云窟打傀尸（兽王庄纪纹中毒链前置）</td><td>—</td></tr>
    <tr class="hl"><td>平地右边捡珍珠→自动触发打浪→得珍珠→成都樵夫→兽王戒</td><td>—</td></tr>
    <tr class="hl"><td>毒龙教线→成都小二→乐山大佛打毒→得<strong>千年毒蟾</strong></td><td>毒龙教线</td></tr>
    <tr class="hl"><td>传闻「盗贼团出没」→乐山大佛附近绕→触发<strong>救云游商人</strong>（先天功残页）</td><td>—</td></tr>
    <tr><td>收集品：入口草地→草/毒蛇 / 上山→珍贵药草</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🐊 兽王庄</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>带咸鱼→鳄鱼池战斗→<strong>鳄皮护甲</strong>（气血+800减伤8%）</td><td>咸鱼</td></tr>
    <tr class="hl"><td>包子/咸鱼→打熊→千年人参 / 给玉蜂浆（森林打熊掉落）→<strong>兽王功</strong></td><td>—</td></tr>
    <tr><td>三人对话→进屋右侧→纪纹→接藏海岛任务</td><td>—</td></tr>
    <tr class="hl"><td>屋里左边桌上盒子→<strong>银蛇千转</strong></td><td>岳胖子</td></tr>
    <tr class="hl"><td>沈湘云检查纪纹（中毒）→东渡口出海藏海岛采花→救纪纹→乐山大佛凌云窟→<strong>开启无名冢</strong></td><td>沈湘云</td></tr>
  </table>
</div>

<div class="phase"><h2>🐍 毒龙教</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>进毒龙教→荆棘劝架单挑阿傍→<strong>抖鳞虎扑式</strong>（荆棘限定霸体）+ 香包（免毒）→门口左边拿花</td><td>—</td></tr>
    <tr class="hl"><td>铁叉部→打罗蛇君→回毒龙教→千年毒蟾被偷→成都宝福楼小二→乐山大佛→战斗→<strong>千年毒蟾</strong>+<strong>小阿曼入队</strong></td><td>—</td></tr>
    <tr><td>蓝婷左侧→<strong>五宝花蜜酒</strong>（武当需×3）</td><td>小阿曼</td></tr>
    <tr><td>原始野林遇阿傍→大漠找赤蛛虫→<strong>裂风鞭法</strong></td><td>小阿曼</td></tr>
    <tr class="hl"><td>与黄娟/蓝婷切磋→可偷：催魂蚀心精要/毒龙刀法精要/苗蛊毒功残本（可循环）</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>⚔️ 铁叉部</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>毒龙教线→铁叉部→发现被屠→打罗蛇君</td><td>—</td></tr>
    <tr class="hl"><td>终章前→铁叉部→打黑白无常（偷<strong>血饮</strong>）+ 阎王（偷<strong>阎罗</strong>）→<strong>十殿阎罗刀精要+投名状</strong></td><td>敖广可带</td></tr>
    <tr><td>大厅宝箱→<strong>牛头叉</strong></td><td>—</td></tr>
    <tr><td>收集品：毒蛇 / 珍贵药草 / 稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🐫 喀什</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">NPC</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr><td>扒墙大叔（阿多）</td><td>给狗皮膏药→<strong>怪鲶鱼</strong>（+100气血）</td><td>—</td></tr>
    <tr><td>上方老人（巴尔塔）</td><td>给龙井虾仁→<strong>惊鸿靴</strong></td><td>—</td></tr>
    <tr class="hl"><td>上方小孩</td><td>给小虾米连环画（大地图遇东方未明传闻）→<strong>夜光杯</strong>（醉仙进阶任务）</td><td>—</td></tr>
    <tr class="hl"><td>上方士兵</td><td>给肚痛贴→一直选拒绝→<strong>吸星大法</strong></td><td>—</td></tr>
    <tr><td>集市商人</td><td>高昌迷宫左侧拾遗骸→<strong>接骨木魔杖</strong></td><td>—</td></tr>
    <tr class="hl"><td>商人（美酒遭掠）</td><td>找回酒→大地图喀什附近闲逛遇马贼→恶人谷薛鬼医→<strong>葡萄美酒</strong>（醉仙进阶）</td><td>—</td></tr>
    <tr><td>推手推车的人</td><td>左上小孩→不要遗弃猫→说服→<strong>龟雕像</strong>（塔娅任务后）</td><td>—</td></tr>
    <tr class="hl"><td>天山弟子（尚精忠）</td><td>封青霄线→带花痴→猴子对话→<strong>楞伽经</strong></td><td>花痴</td></tr>
    <tr class="hl"><td>右下大漠</td><td>塔娅乌衣宝典后→刺杀乌衣教主（一回合秒不掉就读档）→<strong>骑士精神</strong>前置</td><td>塔娅</td></tr>
    <tr class="hl"><td>拜火大典</td><td>花族+恶人谷线完成后→喀什触发大典→色目人入侵传闻</td><td>—</td></tr>
    <tr class="hl"><td>小吃摊</td><td>修罗宫后→打听绿柳山庄情报→夜叉出现→绿柳山庄解锁</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🏜️ 高昌迷宫</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">位置</th><th>内容</th></tr>
    <tr class="hl"><td>入口左走</td><td>战斗→<strong>螳螂拳</strong></td></tr>
    <tr><td>十字路口</td><td>左侧墓地→遗骸（喀什商人→接骨木魔杖）</td></tr>
    <tr><td>继续左走</td><td><strong>聂隐剑</strong></td></tr>
    <tr><td>右走十字路口继续右</td><td><strong>十面埋伏曲</strong> / 武当弟子战斗（武当送信任务后续）</td></tr>
    <tr class="hl"><td>十字路口向下</td><td>打心残→救夜叉→出迷宫遇游进围堵→修罗宫解锁</td></tr>
    <tr><td>收集品</td><td>珍贵药草 / 稀有矿石 / 毒蛇 / 蜘蛛</td></tr>
  </table>
</div>

<div class="phase"><h2>🏝️ 藏海岛</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>兽王庄纪纹中毒→东渡口出海→岛上找花→打花玖瑟→采解药→救纪纹（可偷：<strong>映山红</strong>→洛阳种花大叔换火红金丹）</td><td>沈湘云</td></tr>
    <tr class="hl"><td>黑蝠洞后→沈澜给蛇形钥匙→岛上宝箱→<strong>化骨绵掌+神龙秘咒</strong></td><td>蛇形钥匙</td></tr>
    <tr class="hl"><td>龙墨在队→右侧沙滩→领悟<strong>浪花斩铁式</strong>（游戏最强单体伤害）</td><td>龙墨</td></tr>
    <tr><td>收集品：珍贵药草×3 / 蜘蛛 / 毒蛇</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>⚔️ 罗煞分舵</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>小孟任务：酒馆→河洛客栈→罗煞分舵恶战→罗煞+丰都鬼众→<strong>神鱼</strong></td><td>⚠️龙墨杀罗煞前完成！</td></tr>
    <tr class="hl"><td>龙墨线：杭州点苍弟子告知→罗煞分舵连续两场恶战→判官可偷<strong>倚天屠龙功/慈悲刀法精要/葡萄美酒</strong></td><td>龙墨线</td></tr>
    <tr><td>收集品：蜘蛛 / 稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🏴‍☠️ 东海分舵</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>人口贩卖线→藏发光船舱→战斗→敖广登场→回东渡口遇秦红殇</td><td>—</td></tr>
    <tr class="hl"><td>后期招安→东海分舵打敖广→敖广可招募</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>❄️ 雪地野店</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>身上有冲灵剑法→冰面上选「试一试」→荆棘vs岳在渊撑4回合→得<strong>坎离水火剑</strong> / 拒绝→金蛇剑法/天涯明月刀/铁掌三选一</td><td>冲灵剑法</td></tr>
    <tr><td>门口→稀有矿石×2 / 左侧楼梯上→珍贵药草×2</td><td>—</td></tr>
    <tr class="hl"><td>塔娅入队后→冰面左边亭子找北丑→恶搞→线索→大地图铁叉部附近找南宫龙飞</td><td>塔娅</td></tr>
    <tr class="hl"><td>赛王府前置→东渡口渔夫让来看两老头切磋→看完→回去解锁赛王府</td><td>水盼盼离队</td></tr>
  </table>
</div>

<div class="phase"><h2>🏯 赛王府</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>三天切磋（不能换人！建议带萧复、不动、古实、小阿曼、花痴）<br>D1：水盼盼玉女心法+剑法10重+萧复→全真剑法<br>D2：大师兄→空明拳<br>D3：不动+古实+小阿曼+花痴→<strong>左右互搏</strong></td><td>多队友</td></tr>
    <tr class="hl"><td>赛王府战斗→史燕在队→偷得<strong>软猬甲+黑玉镯+铁罗汉（罗汉拳）</strong> / 4残页→天机老道复原→<strong>先天功</strong></td><td>史燕</td></tr>
    <tr class="hl"><td>赛王爷掉落→<strong>血刀经+血刀刀法</strong></td><td>—</td></tr>
    <tr class="hl"><td>丐帮血案→江瑜看战马册→右边养马兵→成都唐冠南（史燕）→武当→杭州破庙</td><td>江瑜/史燕</td></tr>
    <tr class="hl"><td>山林地堡→赛王爷地道（喝酒卫兵左边柱子）→需岳胖子在队（完美结局必备）</td><td>岳胖子</td></tr>
  </table>
</div>

<div class="phase"><h2>👻 无名冢</h2></div>
<div class="card">
  <table>
    <tr><th>步骤</th><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>前置</td><td>兽王庄纪纹中毒→藏海岛采药→乐山大佛凌云窟打傀尸→无名冢解锁</td><td>沈湘云、萧复</td></tr>
    <tr class="hl"><td>救岳胖子</td><td>进墓穴<strong>先左转！绝对不要打傀尸！</strong>→左手岔道救胖子→出墓开机关→<strong>岳胖子入队</strong>→四选一武功（推荐天魔解体）</td><td>⚠️先左转</td></tr>
    <tr class="hl"><td>葵花宝典</td><td>方云华+任剑南同时在队→右边傀尸房间→<strong>葵花宝典+流星飞坠+辟邪剑法</strong>（方云华自宫后秒天秒地）</td><td>方云华+任剑南</td></tr>
    <tr><td>荆轲武诀</td><td>左上方→史燕专属武功</td><td>史燕</td></tr>
    <tr><td>收集品</td><td>蜘蛛×3 / 珍贵药草 / 稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🦇 黑蝠洞</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>龙井异事（三派传人）完成→大地图黑蝠洞解锁</td><td>古实、水盼盼、不动</td></tr>
    <tr class="hl"><td>进洞→需带小阿曼（必备！）→5个假欧阳笑→真欧阳笑（气盾）→打赢得<strong>寒蝠胆</strong></td><td>小阿曼</td></tr>
    <tr class="hl"><td>寒蝠胆→怪医居找沈澜→得蛇形钥匙→藏海岛开宝箱→<strong>化骨绵掌+神龙秘咒</strong></td><td>—</td></tr>
    <tr><td>欧阳笑可偷：玄冥神功残本 / 大王蛇胆 / 十全大补丹 / 九转还魂丹</td><td>—</td></tr>
    <tr class="hl"><td>⚠️ 建议完成赛王府+沈澜对话后再来，前期难度极高</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>👹 恶人谷</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">NPC</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr class="hl"><td>带鳄鱼的人</td><td>史义/敖广在队→打井水给鳄鱼→<strong>金刚甲+鳄鱼的眼泪</strong></td><td>史义/敖广</td></tr>
    <tr><td>喝（酒鬼）</td><td>傅剑寒→给即墨老酒（杜康村买）→<strong>离火玄冰镖</strong></td><td>傅剑寒</td></tr>
    <tr class="hl"><td>阿萨幸（舞棒恶人）</td><td>心残死后→带萧复→选一直帮助→萧复单挑→<strong>大闹天宫精要</strong></td><td>萧复</td></tr>
    <tr><td>叶三娘</td><td>找失踪妹妹→问村内人→村外赌群→尸体在左下草丛→<strong>盘月剑</strong></td><td>—</td></tr>
    <tr><td>李武靖</td><td>水盼盼在队→喀什商人→东渡口静云庵弟子→回恶人谷→<strong>血饮</strong></td><td>水盼盼</td></tr>
    <tr class="hl"><td>贺陀+无戒</td><td>封青霄线→恶人谷打贺陀+无戒→六扇门帮忙→为封青霄洗冤</td><td>封青霄线</td></tr>
    <tr class="hl"><td>全区域</td><td>⚠️ <strong>花族拜火大典前必须清完！</strong>否则传闻「色目人入侵恶人谷」将永久清除所有恶人谷任务</td><td>—</td></tr>
    <tr class="hl"><td>色目人入侵</td><td>塔娅在队→检查尸体→花族拿药→喀什找传教士（10智慧果）→恶人谷决战→<strong>骑士精神</strong></td><td>塔娅</td></tr>
  </table>
</div>

<div class="phase"><h2>🌸 花族部落</h2></div>
<div class="card">
  <table>
    <tr><th>步骤</th><th>内容</th><th>需求</th></tr>
    <tr><td>1</td><td>恶人谷线后→对话村长→塔娅出场→星象塔解谜（墙上三张告示）→<strong>万物皆数</strong></td><td>—</td></tr>
    <tr><td>2</td><td>抵御乌衣族→雪地野店找北丑→大地图铁叉部附近遇南宫龙飞→回花族→塔娅学<strong>乌衣宝典</strong>（练到5级）</td><td>塔娅</td></tr>
    <tr class="hl"><td>3</td><td>喀什右下大漠杀乌衣教主→完成</td><td>塔娅</td></tr>
    <tr class="hl"><td>4</td><td>色目人入侵（拜火大典后传闻）→塔娅在队→恶人谷检查尸体→花族拿药→喀什传教士10智慧果→回恶人谷决战</td><td>塔娅</td></tr>
    <tr class="hl"><td>5</td><td>谷月轩单挑仙希尔→<strong>天山心法+西洋怀表</strong>（色目人入侵支线奖励）</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🌸 修罗宫</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>高昌救夜叉后→青城山报信→修罗宫解锁→男子勿入→战斗后得知阿修罗失踪</td><td>高昌迷宫</td></tr>
    <tr class="hl"><td>小孟后续→修罗宫左侧找骆翎枫→沈湘云可学会<strong>点穴截脉</strong></td><td>沈湘云</td></tr>
    <tr><td>与任清璇对话→得修罗宫情报</td><td>—</td></tr>
    <tr><td>调查屋内秘笈→<strong>落英神剑掌</strong>（岳胖子）</td><td>岳胖子</td></tr>
    <tr class="hl"><td>修罗宫后续→喀什打听→夜叉→绿柳山庄解锁</td><td>—</td></tr>
    <tr><td>收集品：毒蛇 / 蜘蛛 / 珍贵药草 / 稀有矿石</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🏡 绿柳山庄</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>喀什夜叉→绿柳山庄解锁→需<strong>水盼盼在队</strong>才能穿过迷阵</td><td>水盼盼</td></tr>
    <tr><td>→避开巡逻守卫→房间内救阿修罗→战斗（九阴+小怪）</td><td>—</td></tr>
    <tr class="hl"><td>九阴残血→杨雨枫出现→用九阴真经换人→赛王爷出现重伤九阴→抢走真经→山庄坍塌</td><td>—</td></tr>
    <tr class="hl"><td>回修罗宫→与任清璇对话→获<strong>修罗心法</strong> + <strong>九阴神爪+倚天断剑</strong></td><td>—</td></tr>
    <tr class="hl"><td>倚天断剑→铸剑山庄+西方异金→<strong>倚天剑</strong>（水盼盼专属）</td><td>水盼盼</td></tr>
  </table>
</div>

<div class="phase"><h2>🐉 天龙教</h2></div>
<div class="card">
  <table>
    <tr><th style="width:14%">内容</th><th style="width:13%">需求</th></tr>
    <tr class="hl"><td>终章→对话夜叉可入队</td><td>完成前置</td></tr>
    <tr class="hl"><td>右上房间→<strong>天龙八部剑</strong>（夜叉在队）</td><td>夜叉</td></tr>
    <tr><td>对战罗蛇君→偷<strong>吸星大法</strong></td><td>—</td></tr>
    <tr><td>对战龙王→群战</td><td>—</td></tr>
    <tr class="hl"><td>挑战自在天→<strong>玉连环影</strong>（姬无双+任清璇）</td><td>姬无双、任清璇</td></tr>
    <tr><td>牢房酆都鬼众→<strong>雪月交光</strong>（姬无双+敖广）</td><td>姬无双、敖广</td></tr>
  </table>
</div>

<div class="phase"><h2>🕳️ 山林地堡</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>前置：五个据点（无名冢/黑蝠洞/赛王府/恶人谷/绿柳山庄）全部打通→大地图遇丐帮弟子→赛王府开启地道</td><td>—</td></tr>
    <tr class="hl"><td>赛王府→喝酒卫兵左边柱子→开启暗门→进入山林地堡</td><td>—</td></tr>
    <tr class="hl"><td>⚠️ <strong>必须带岳胖子！</strong>否则无法触发完美结局。不动在队有额外对话。</td><td>岳胖子（完美结局必备）</td></tr>
    <tr><td>打赛王爷→偷<strong>天魔鞭精要</strong></td><td>—</td></tr>
    <tr class="hl"><td>最终战→对战摄心赛王爷+卫紫绫→<strong>九阴总纲+九阴飞絮篇</strong></td><td>—</td></tr>
    <tr class="hl"><td>⚠️ 战斗后<strong>岳胖子离队</strong>（完美结局触发条件需岳胖子内功满级）</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🏰 卫家堡（决战）</h2></div>
<div class="card">
  <table>
    <tr><th>内容</th><th>需求</th></tr>
    <tr class="hl"><td>洛阳→禀报江天雄→少林寺→铁叉部→天龙教→逍遥谷（师父切磋→逍遥御风）</td><td>—</td></tr>
    <tr class="hl"><td>卫家堡→卫紫绫离队→全体队友可选8人→打游进+锦衣卫→<strong>五色甲+殇瑶</strong></td><td>—</td></tr>
    <tr class="hl"><td>右上角房间→最终BOSS辟邪老人→通关</td><td>—</td></tr>
  </table>
</div>

<div class="phase"><h2>🌍 大地图随机事件</h2></div>
<div class="card">
  <table>
    <tr><th style="width:18%">事件</th><th>内容</th><th style="width:13%">需求</th></tr>
    <tr class="hl"><td>营救状元郎</td><td>战斗→洛阳交→得三个豆腐（加血上限）</td><td>—</td></tr>
    <tr class="hl"><td>救云游商人</td><td>传闻「盗贼团出没」→景阳冈/乐山大佛附近→战斗→先天功残页1+2</td><td>—</td></tr>
    <tr class="hl"><td>蜘蛛盗贼团</td><td>→战斗→先天功残页（后续残页3隐元阁买，残页4大地图斗篷客）</td><td>—</td></tr>
    <tr class="hl"><td>西方异金</td><td>传闻→大地图遇锦衣卫/番僧→偷取→铸剑山庄重铸倚天剑</td><td>水盼盼</td></tr>
    <tr class="hl"><td>东方未明</td><td>→<strong>小虾米连环画</strong>→喀什小孩换夜光杯</td><td>—</td></tr>
    <tr class="hl"><td>上官雁传功</td><td>傅剑寒在队→大地图遇上官雁→<strong>意寒神功</strong></td><td>傅剑寒</td></tr>
    <tr class="hl"><td>杨云事件</td><td>傅剑寒在队→救人→打万劳九+武林人士→<strong>兽王功</strong> / 打何未峰→<strong>天山幻影剑精要</strong></td><td>傅剑寒</td></tr>
    <tr class="hl"><td>浪人与熊</td><td>→战斗→再遇→无奖励</td><td>—</td></tr>
    <tr><td>王蓉与雕</td><td>→<strong>金蛇宝典</strong></td><td>—</td></tr>
    <tr><td>帮助凌香儿</td><td>→战斗→无特殊奖励</td><td>—</td></tr>
    <tr><td>帮助杨雨枫</td><td>→<strong>玉女剑法+玉女心经</strong></td><td>—</td></tr>
    <tr><td>帮助古墓派</td><td>→<strong>玉女剑法+玉女心经</strong></td><td>—</td></tr>
    <tr class="hl"><td>帮助何秋娟</td><td>→<strong>天山幻影剑精要</strong></td><td>—</td></tr>
    <tr><td>两兄弟要粥</td><td>→<strong>腊八粥</strong></td><td>—</td></tr>
    <tr><td>投资巩总</td><td>给1万→再遇→老人参</td><td>—</td></tr>
    <tr class="hl"><td>老乞丐传功</td><td>叫花鸡+萧遥在队→<strong>亢龙有悔</strong></td><td>萧遥</td></tr>
    <tr><td>焦大焦二</td><td>→偷<strong>半山妖+早春图</strong>（字画摊）</td><td>—</td></tr>
    <tr class="hl"><td>江洋大盗</td><td>→一袋赃物→偷<strong>庐山高/兰亭序/东方宝典/橘中密</strong></td><td>—</td></tr>
    <tr class="hl"><td>东瀛浪人</td><td>→偷<strong>明玉功+三日月·无铭</strong></td><td>—</td></tr>
    <tr class="hl"><td>四十二章经事件</td><td>→<strong>虎啸功+银狐飞絮</strong> / 乐山大佛虚真→<strong>达摩武诀</strong></td><td>—</td></tr>
    <tr><td>丐帮陷害事件</td><td>→<strong>天下无狗</strong></td><td>—</td></tr>
    <tr class="hl"><td>浪人vs剑圣</td><td>观战→<strong>村正</strong></td><td>—</td></tr>
    <tr class="hl"><td>江天雄传话</td><td>→原始野林恶战→<strong>火焰刀秘籍</strong></td><td>—</td></tr>
    <tr><td>三方会谈抢森林</td><td>帮任意一方（纪纹给武功）</td><td>—</td></tr>
    <tr><td>野生的徐子淇</td><td>→正气诀×6</td><td>—</td></tr>
    <tr class="hl"><td>丐帮报信</td><td>五个据点全通后→大地图遇丐帮→激活赛王府山林地堡</td><td>—</td></tr>
    <tr class="hl"><td>玄铁事件</td><td>终章→大地图遇→老胡打造玄铁武器</td><td>—</td></tr>
  </table>
</div>

</div><!-- /tab-locations -->
"""

# Replace the old content
before = content[:start]
after = content[end:]
content = before + new_content + after

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

# Verify
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

opens = content.count('<div')
closes = content.count('</div>')
print(f'<div> tags: {opens}, </div> tags: {closes}, diff: {opens - closes}')

# Check all tab-content ids
import re
tabs = re.findall(r'tab-content[^>]*id="([^"]*)"', content)
print(f'Tab contents found: {len(tabs)} -> {tabs}')

# Check html/body end tags
for tag in ['</script>', '</body>', '</html>']:
    count = content.count(tag)
    print(f'{tag}: {count}')

print('\nDone! tab-locations completely rebuilt.')
