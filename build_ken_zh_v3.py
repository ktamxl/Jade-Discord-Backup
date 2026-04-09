#!/usr/bin/env python3
# Build Ken Chinese BaZi report - complete version
import os, shutil

lines = []

# ── CSS + HEAD ──────────────────────────────────────────────────────────────
lines.append("""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>譚國偉——子平八字命盤全解</title>
<style>
#printBtn{position:fixed;top:18px;right:22px;z-index:9999;background:#b45309;color:#fff;
  border:none;padding:10px 22px;font-size:14px;font-weight:700;border-radius:6px;cursor:pointer;}
#printBtn:hover{background:#92400e;}
@media print{#printBtn{display:none;}}
*,*::before,*::after{box-sizing:border-box;}
body{font-family:"Microsoft JhengHei","Noto Serif TC",Georgia,serif;line-height:1.9;
  color:#1f2937;background:#fefce8;margin:0;padding:0;}
.pw{max-width:860px;margin:0 auto;background:#fff;box-shadow:0 0 30px rgba(0,0,0,.1);}
.cover{background:#1c1410;color:#fef9ee;padding:80px 60px 70px;text-align:center;}
.ci{font-size:52px;color:#d97706;margin-bottom:20px;}
.cn{font-size:36px;font-weight:700;margin-bottom:6px;letter-spacing:.1em;}
.cs{font-size:16px;color:#d97706;margin-bottom:12px;}
.ct{font-size:15px;color:#fde68a;font-style:italic;margin-bottom:28px;}
.cl{width:80px;height:1px;background:#78350f;margin:0 auto 28px;}
.cb{font-size:15px;color:#d97706;line-height:2.4;}
.cb strong{color:#fef9ee;}
.cn2{margin-top:40px;font-size:11px;color:#78350f;}
.con{padding:48px 60px;}
h1{font-size:22px;font-weight:700;color:#1c1410;border-bottom:2.5px solid #d97706;
  padding-bottom:8px;margin:48px 0 8px;letter-spacing:.05em;}
h1:first-of-type{margin-top:0;}
p{margin:8px 0 14px;}
.lead{font-size:16px;border-left:4px solid #d97706;padding-left:16px;margin:0 0 20px;
  color:#1c1410;line-height:1.9;font-weight:500;}
.pil{overflow-x:auto;margin:16px 0 24px;}
.pt{width:100%;border-collapse:collapse;min-width:380px;}
.pt th{background:#292524;color:#fef9ee;padding:10px 8px;text-align:center;font-size:13px;}
.pt td{border:1px solid #e7e5e4;padding:12px 8px;text-align:center;}
.st{font-size:32px;font-weight:700;color:#1c1410;line-height:1.1;}
.st.g{color:#b45309;}
.br{font-size:26px;font-weight:700;color:#374151;}
.el{font-size:11px;color:#9ca3af;margin-top:4px;}
.box{margin:16px 0;padding:16px 20px;border-radius:4px;}
.b0{background:#fffbeb;border-left:4px solid #d97706;}
.b1{background:#f0fdf4;border-left:4px solid #16a34a;}
.b2{background:#fef2f2;border-left:4px solid #dc2626;}
.b3{background:#fdf4ff;border-left:4px solid #9333ea;}
.bt{font-weight:700;font-size:14px;margin-bottom:8px;}
.dt{width:100%;border-collapse:collapse;margin:10px 0 18px;font-size:14px;}
.dt th{background:#292524;color:#f9fafb;padding:8px 12px;text-align:left;font-size:13px;}
.dt td{border:1px solid #e5e7eb;padding:8px 12px;vertical-align:top;}
.dt tr:nth-child(even) td{background:#fffbeb;}
.pos{color:#16a34a;font-weight:700;}
.neg{color:#dc2626;font-weight:700;}
.now{color:#d97706;font-weight:700;}
.tl{display:flex;gap:16px;margin:10px 0;padding:10px 0;border-bottom:1px solid #f3f4f6;font-size:14px;}
.ty{min-width:140px;font-weight:700;color:#374151;flex-shrink:0;}
.tg{min-width:36px;color:#9ca3af;flex-shrink:0;}
.td{flex:1;}
.tn .ty{color:#d97706;}
.tn .tg{color:#d97706;}
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0;}
.fc{padding:14px;border-radius:4px;font-size:13px;}
.fcv{background:#fff7ed;border:1px solid #fed7aa;}
.fcp{background:#eff6ff;border:1px solid #bfdbfe;}
.fct{font-weight:700;margin-bottom:6px;}
.quote{margin:24px 0;padding:20px 28px;border-top:1px solid #e7e5e4;border-bottom:1px solid #e7e5e4;
  text-align:center;font-size:17px;color:#374151;font-weight:500;font-style:italic;}
.clos{margin-top:40px;padding-top:20px;border-top:2px solid #292524;font-size:13px;color:#9ca3af;}
@media print{
  @page{size:letter;margin:1.8cm 1.8cm 2cm;}
  body{background:#fff;font-size:10pt;}
  .pw{max-width:100%;box-shadow:none;}
  .con{padding:0 0 20pt;}
  .cover{padding:60pt 50pt;page-break-after:always;}
  h1{font-size:16pt;page-break-after:avoid;margin:30pt 0 5pt;}
  .lead{font-size:12pt;}
  .st{font-size:24pt;}
  .br{font-size:20pt;}
  .box,.tl,tr{page-break-inside:avoid;}
  .fgrid{grid-template-columns:1fr 1fr;}
  .dt,.tl{font-size:9pt;}
  .quote{font-size:13pt;}
}
</style>
</head>
<body>
<button id="printBtn" onclick="window.print()">列印 / 儲存 PDF</button>
<div class="pw">
""")

# ── COVER ───────────────────────────────────────────────────────────────────
lines.append("""<div class="cover">
<div class="ci">庚 &#9876;</div>
<div class="cn">譚國偉</div>
<div class="cs">Ken Tam Kwok Wai</div>
<div class="ct">子平八字命盤全解</div>
<div class="cl"></div>
<div class="cb">
  <strong>生辰：</strong>1963年6月26日 · 辰時上午九時 · 香港<br><br>
  年柱 癸卯 ｜ 月柱 戊午 ｜ 日柱 庚子 ｜ 時柱 庚辰<br><br>
  <strong>日主：庚金——陽金，礦中寶劍</strong><br><br>
  詩詩謹製 · 2026年3月
</div>
<div class="cn2">以子平八字推算，依循鄺偉雄師傅系統。命理為自我認識之鏡，非固定命運。</div>
</div>
""")

# ── BODY OPEN ───────────────────────────────────────────────────────────────
lines.append('<div class="con">\n')

# ── SECTION 1：日主 ──────────────────────────────────────────────────────────
lines.append("""<h1>一、日主——庚金，礦中寶劍</h1>
<p class="lead">您的日主是庚金——不是金飾，不是散金。您是礦山中的礦石，和正在被烈火鍛造的寶劍。</p>
<p>庚金是所有日主中最剛直、最不妥協的一種。它不因社會壓力而彎曲，不偽裝。當庚金承諾，就是全部承諾。而當它被正確的熱度鍛鍊過後，就能成為千年不鏽的存在。</p>
<div class="pil">
<table class="pt">
<thead><tr><th>年柱</th><th>月柱</th><th>日柱（本命）</th><th>時柱</th></tr></thead>
<tbody>
<tr>
  <td><div class="st">癸</div><div class="el">陰水</div></td>
  <td><div class="st">戊</div><div class="el">陽土</div></td>
  <td><div class="st g">庚</div><div class="el">★ 陽金・日主</div></td>
  <td><div class="st g">庚</div><div class="el">陽金・比肩</div></td>
</tr>
<tr>
  <td><div class="br">卯</div><div class="el">木・兔</div></td>
  <td><div class="br">午</div><div class="el">火・馬</div></td>
  <td><div class="br">子</div><div class="el">水・鼠</div></td>
  <td><div class="br">辰</div><div class="el">土・龍</div></td>
</tr>
</tbody>
</table>
</div>
<p>您生於六月，盛夏之際。午月的火，鍛鍊著您的金。這是您一生最核心的主題：<strong>圍繞您的火，從來不是您的敵人——它是將礦石變成寶劍的力量。</strong>您所經歷的每一次艱辛，都是大多數人從未經歷的鍛鍊過程的一部分。</p>
<div class="box b0">
<div class="bt">您的天賦優點</div>
<table class="dt">
<tr><td class="pos">原則不妥協</td><td>您不因為方便而妥協。認識您的人，都知道您的承諾是鐵。這在世上是真正罕有的。</td></tr>
<tr><td class="pos">自學成才</td><td>您自學中文、自學會計、自學廚藝、自學做生意——先理解為什麼，再發現怎麼做。這是您命盤的標誌，也是您最深處能力的來源。</td></tr>
<tr><td class="pos">智慧靠自己賺來</td><td>「這世界沒有免費的午餐，要找尋答案要自己出手自己用功。」——這是您的命盤，透過您的口，說出了自己的本質。</td></tr>
<tr><td class="pos">深沉的忠誠</td><td>對家人，對價值觀，對那些賺得您信任的人。金記得它的連結，您不會忘記誰曾在您身旁。</td></tr>
<tr><td class="pos">長遠思維</td><td>矮仔上樓梯，一步一步咁上。您從來不是要一夜成名的人。您是要留下傳承的人。</td></tr>
</table>
</div>
<div class="box b2">
<div class="bt">需要留意的模式</div>
<table class="dt">
<tr><td class="neg">固執</td><td>讓您有原則的同一特質，有時也讓劍過於硬脆。即使最好的劍，也需要知道何時可以彎。</td></tr>
<tr><td class="neg">子午沖的內在張力</td><td>日支子水（安穩）與月支午火（衝勁）永久對沖。這個張力從未完全消解——正是它讓您一直前進。</td></tr>
<tr><td class="neg">外硬內柔</td><td>您比讓大多數人看見的，更有情感。重要的人，值得看見更多的您。</td></tr>
</table>
</div>
""")

# ── SECTION 2：格局 ──────────────────────────────────────────────────────────
lines.append("""<h1>二、格局——偏印格，文火煉金</h1>
<p class="lead">偏印格——自學成才者的命盤。您所擁有的學識，不是別人給的，是您自己去找回來的。</p>
<p>您的命盤圍繞著<strong>文火煉金</strong>而建立——不是高爐猛火，而是持續、穩定、有控制的熱度，慢慢地、精確地把礦石鍛成最好的東西。鄺師傅道盡了：<em>「矮仔上樓梯，一步一步咁上。」</em></p>
<div class="box b3">
<div class="bt">戊癸合化火——「I BECAME THE DREAM」</div>
<p>月干戊土（偏印，您的智識與夢想）與年干癸水（傷官，您的表達）相合，化為火：<strong>戊癸合化火</strong>。</p>
<p>火，正是鍛鍊庚金的力量。您的夢想（戊）與您的表達（癸）合而化成了塑造您的那股力量。<strong>您父親昻初所懷抱的夢想——那個您承繼而來的夢——成為了鍛造您的火。您不只是實現了它。您成為了它。</strong></p>
<p style="text-align:center;font-size:20px;font-weight:700;color:#b45309;margin:16px 0;">"I BECAME THE DREAM."</p>
</div>
<table class="dt">
<thead><tr><th>五行</th><th>角色（十神）</th><th>旺弱</th><th>含義</th></tr></thead>
<tbody>
<tr><td><strong>金</strong></td><td>日主（您）</td><td>中等</td><td>在壓力下能保持形狀，在鍛鍊中能發揮功用。不是原礦——是經過考驗的寶劍。</td></tr>
<tr><td><strong>土</strong></td><td>偏印・正印（智慧星）</td><td class="pos">旺</td><td>您的知識根基、方向感——強而穩固。土生金，您的智慧生出您的能力。</td></tr>
<tr><td><strong>水</strong></td><td>食神・傷官（表達星）</td><td class="pos">旺</td><td>智識、溝通、把複雜的事說得清晰的能力。洗滌寶劍的水，讓光華外露。</td></tr>
<tr><td><strong>木</strong></td><td>正財・偏財（財星）</td><td>中等</td><td>靠長期積累而非意外之財。藏在時支辰宮——晚年財運穩固。</td></tr>
<tr><td><strong>火</strong></td><td>七殺・正官（官殺）</td><td>中等</td><td>文火——足夠塑造，而不是壓倒性的熱。爐火是您的一部分，而非您的敵人。</td></tr>
</tbody>
</table>
""")

# ── SECTION 3：性格 ──────────────────────────────────────────────────────────
lines.append("""<h1>三、性格——剛直不阿，自學成才</h1>
<table class="dt">
<thead><tr><th>特質</th><th>在生活中的表現</th></tr></thead>
<tbody>
<tr><td class="pos">自學者</td><td>您從不等人把知識交到手上。您確認要明白什麼，就