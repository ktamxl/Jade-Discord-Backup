
import os, shutil

head = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>譚太太命盤全解</title>
<style>
#printBtn {
  position: fixed; top: 18px; right: 22px; z-index: 9999;
  background: #9333ea; color: #fff; border: none;
  padding: 10px 22px; font-size: 14px; font-weight: 700;
  border-radius: 6px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.18);
  font-family: Georgia, serif;
}
#printBtn:hover { background: #7e22ce; }
@media print { #printBtn { display: none; } }
*, *::before, *::after { box-sizing: border-box; }
body { font-family: "Noto Serif TC", "Source Han Serif TC", "Microsoft JhengHei", Georgia, serif; line-height: 1.9; color: #1f2937; background: #fdf4ff; margin: 0; padding: 0; }
.page-wrap { max-width: 860px; margin: 0 auto; background: #fff; box-shadow: 0 0 30px rgba(0,0,0,0.1); }
.cover { background: #1e0535; color: #fdf4ff; padding: 80px 60px 70px; text-align: center; }
.cover-icon { font-size: 52px; color: #c084fc; margin-bottom: 20px; }
.cover-name { font-size: 36px; font-weight: 700; margin-bottom: 6px; letter-spacing: 0.1em; }
.cover-sub { font-size: 16px; color: #a78bfa; margin-bottom: 12px; }
.cover-title { font-size: 15px; color: #e9d5ff; font-style: italic; margin-bottom: 28px; }
.cover-line { width: 80px; height: 1px; background: #4c1d95; margin: 0 auto 28px; }
.cover-bazi { font-size: 15px; color: #a78bfa; line-height: 2.4; }
.cover-bazi strong { color: #e9d5ff; }
.cover-note { margin-top: 40px; font-size: 11px; color: #6d28d9; }
.content { padding: 48px 60px; }
h1 { font-size: 22px; font-weight: 700; color: #1e0535; border-bottom: 2.5px solid #9333ea; padding-bottom: 8px; margin: 48px 0 10px; letter-spacing: 0.05em; }
h1:first-of-type { margin-top: 0; }
h2 { font-size: 17px; font-weight: 700; color: #2d1b69; margin: 28px 0 8px; }
p { margin: 8px 0 14px; }
.lead { font-size: 16px; border-left: 4px solid #9333ea; padding-left: 16px; margin: 0 0 20px; color: #1e0535; line-height: 1.9; font-weight: 500; }
.pw { overflow-x: auto; margin: 16px 0 24px; }
.pt { width: 100%; border-collapse: collapse; min-width: 380px; }
.pt th { background: #2d1b69; color: #fdf4ff; padding: 10px 8px; text-align: center; font-size: 13px; }
.pt td { border: 1px solid #e9d5ff; padding: 12px 8px; text-align: center; }
.stem { font-size: 32px; font-weight: 700; color: #1e0535; line-height: 1.1; }
.stem.fire { color: #dc2626; }
.branch { font-size: 26px; font-weight: 700; color: #374151; }
.el { font-size: 11px; color: #9ca3af; margin-top: 4px; }
.box { margin: 16px 0; padding: 16px 20px; border-radius: 4px; }
.bp { background: #fdf4ff; border-left: 4px solid #9333ea; }
.bg { background: #f0fdf4; border-left: 4px solid #16a34a; }
.bn { background: #eff6ff; border-left: 4px solid #2563eb; }
.bw { background: #fef2f2; border-left: 4px solid #dc2626; }
.bh { background: #fff7ed; border-left: 4px solid #f97316; }
.bt { font-weight: 700; font-size: 14px; margin-bottom: 8px; }
.dt { width: 100%; border-collapse: collapse; margin: 10px 0 18px; font-size: 14px; }
.dt th { background: #2d1b69; color: #f9fafb; padding: 8px 12px; text-align: left; font-size: 13px; }
.dt td { border: 1px solid #e5e7eb; padding: 8px 12px; vertical-align: top; }
.dt tr:nth-child(even) td { background: #fdf9ff; }
.pos { color: #16a34a; font-weight: 700; }
.neg { color: #dc2626; font-weight: 700; }
.now { color: #9333ea; font-weight: 700; }
.tl { display: flex; gap: 16px; margin: 10px 0; padding: 10px 0; border-bottom: 1px solid #f3f4f6; font-size: 14px; }
.tl-yr { min-width: 130px; font-weight: 700; color: #374151; flex-shrink: 0; }
.tl-gz { min-width: 36px; color: #9ca3af; flex-shrink: 0; }
.tl-desc { flex: 1; }
.tn .tl-yr { color: #9333ea; }
.tn .tl-gz { color: #9333ea; }
.quote { margin: 24px 0; padding: 20px 28px; border-top: 1px solid #e9d5ff; border-bottom: 1px solid #e9d5ff; text-align: center; font-size: 17px; color: #2d1b69; font-weight: 500; letter-spacing: 0.05em; }
.closing { margin-top: 40px; padding-top: 20px; border-top: 2px solid #2d1b69; font-size: 13px; color: #9ca3af; }
@media print {
  @page { size: letter; margin: 1.8cm 1.8cm 2cm; }
  body { background: #fff; font-size: 10pt; }
  .page-wrap { max-width: 100%; box-shadow: none; }
  .content { padding: 0 0 20pt; }
  .cover { padding: 60pt 50pt; page-break-after: always; }
  .cover-icon { font-size: 40pt; }
  .cover-name { font-size: 30pt; }
  h1 { font-size: 16pt; page-break-after: avoid; margin: 30pt 0 5pt; }
  h2 { font-size: 13pt; page-break-after: avoid; }
  .lead { font-size: 12pt; }
  .stem { font-size: 24pt; } .branch { font-size: 20pt; }
  .box, .tl, tr { page-break-inside: avoid; }
  .dt, .tl { font-size: 9pt; }
  .quote { font-size: 13pt; }
}
</style>
</head>
<body>
<button id="printBtn" onclick="window.print()">🖨️ 列印 / 儲存PDF</button>
<div class="page-wrap">
<div class="cover">
  <div class="cover-icon">丁 🕯</div>
  <div class="cover-name">譚太太</div>
  <div class="cover-sub">Mabel Tam</div>
  <div class="cover-title">子平八字命盤全解<br>Four Pillars of Destiny — Complete Life Reading</div>
  <div class="cover-line"></div>
  <div class="cover-bazi">
    <strong>生辰：</strong>1961年12月20日 &middot; 子時（晚上11:00 &ndash; 凌晨1:00）<br><br>
    年柱 辛丑 ｜ 月柱 庚子 ｜ 日柱 丁亥 ｜ 時柱 庚子<br><br>
    <strong>日主：丁火 &mdash; 陰火，燭光</strong><br><br>
    夫君譚國偉謹獻
  </div>
  <div class="cover-note">此命盤以子平八字為基礎，以鄺偉雄師傅系統推算。命理為認識自我之鏡，非固定命運——您的選擇，塑造您的人生。</div>
</div>
<div class="content">
'''

body = ""

body += """<h1>一、日主：丁火——陰火，燭光</h1>
<p class="lead">您的日主是丁火——不是烈日，不是篝火，而是燭光。</p>
<p>燭光是世上最安靜、卻最有力量的存在之一。它不喧嘩，不搶眼，但黑暗的房間裡，所有人的目光都會落在它身上。它不需要做什麼，單是存在，就帶來了溫暖。它照亮面孔，安定空間，讓人感到被看見、被照料。</p>
<p>這就是您。您的力量不在於音量，而在於深度、溫度，以及一種幾乎難以形容的能力——讓身邊的人感到被看見、被珍視。</p>
<div class="pw"><table class="pt"><thead><tr><th>年柱</th><th>月柱</th><th>日柱（本命）</th><th>時柱</th></tr></thead><tbody>
<tr><td><div class="stem">辛</div><div class="el">陰金</div></td><td><div class="stem">庚</div><div class="el">陽金</div></td><td><div class="stem fire">丁</div><div class="el">★ 陰火・日主</div></td><td><div class="stem">庚</div><div class="el">陽金</div></td></tr>
<tr><td><div class="branch">丑</div><div class="el">土・牛</div></td><td><div class="branch">子</div><div class="el">水・鼠</div></td><td><div class="branch">亥</div><div class="el">水・豬</div></td><td><div class="branch">子</div><div class="el">水・鼠</div></td></tr>
</tbody></table></div>
<p>您生於十二月子時——一年最冷的月份、一天最黑的時刻。在隆冬的深夜燃起的一支燭光。在如此深重的寒冷與黑暗中守住這份光，需要非凡的內在力量。而您守住了——靜靜地，穩穩地，守了一輩子。</p>
<div class="box bp"><div class="bt">您的天賦優點</div><table class="dt">
<tr><td class="pos">深沉的溫暖</td><td>您在哪裡，哪裡就有家的感覺。人們在您身邊不由自主地放鬆，說不清原因，但就是如此。</td></tr>
<tr><td class="pos">極高的情商</td><td>您默默地、精準地看穿人心。那些未被說出口的情緒、那些表面之下的張力——您往往第一個察覺。</td></tr>
<tr><td class="pos">以行動表達的愛</td><td>您不用言語說「我愛你」。您用行動說——記住每一個細節，在別人開口之前就已安排妥當。您是家人的心臟。</td></tr>
<tr><td class="pos">外柔內剛</td><td>外人以為您柔順，熟悉您的人知道——某些事情上，您絕不退讓。燭光在風中搖曳，但它不熄滅。</td></tr>
<tr><td class="pos">韌性</td><td>您的命盤充滿壓力，您卻依然在這裡，依然溫暖，依然付出。這不是運氣，這是非凡的意志力。</td></tr>
</table></div>
<div class="box bw"><div class="bt">需要留意的模式</div><table class="dt">
<tr><td class="neg">承擔太多</td><td>您把別人的擔憂當作自己的責任。試圖照亮整個世界的燭光，會燃燒得更快。有些事，您可以放手。</td></tr>
<tr><td class="neg">把壓力藏在心裡</td><td>出了問題，您傾向於默默消化，不輕易說出口。這保護了別人，卻讓自己付出代價。</td></tr>
<tr><td class="neg">把自己放在最後</td><td>您把所有人照顧好，才輪到自己。在人生這個階段，您自己的休息與滋養，比過去任何時候都更重要。</td></tr>
<tr><td class="neg">需要溫暖</td><td>寒冷的環境——無論是氣候還是人情——比別人更能消耗您。請主動為自己創造溫暖。</td></tr>
</table></div>"""

body += """<h1>二、命盤全局——燭光在隆冬中守候</h1>
<p class="lead">您的命盤是一支燭光，四面被金和水包圍——在最寒冷的季節，最黑暗的時刻。然而火焰不滅。這份堅守，是您一生最核心的故事。</p>
<p>天干三顆金（辛、庚、庚）壓制著您的丁火；地支子水兩現（月支、時支），再加上亥水日支，寒水浸圍。然而，就在您的日支亥中，藏著一根甲木——正印，靜靜地、始終如一地，為您的燭光提供燃料。您的守護，一直都在。</p>
<div class="box bp"><div class="bt">五行力量分析</div><table class="dt">
<tr><th>五行</th><th>角色</th><th>旺弱</th><th>含義</th></tr>
<tr><td><strong>火</strong></td><td>日主（您）</td><td class="neg">極弱</td><td>您一人獨撐這份光，四周都是挑戰。您始終比別人更需要努力，才能維持同樣的溫暖。</td></tr>
<tr><td><strong>金</strong></td><td>財星</td><td class="neg">極旺</td><td>您對財務有天然的敏銳，能力遠超外人所見。但財多身弱，需要伴侶的支撐才能充分發揮。</td></tr>
<tr><td><strong>水</strong></td><td>官星（夫星）</td><td class="neg">極旺</td><td>夫星旺盛，強大、主導，有時令人窒息，但也帶來結構與保護。</td></tr>
<tr><td><strong>土</strong></td><td>食傷（表達）</td><td>中等</td><td>您的創造力、您的聲音、您照顧與滋養他人的能力——真實存在，只是不常顯露。</td></tr>
<tr><td><strong>木</strong></td><td>印星（智慧與保護）</td><td class="neg">極弱・藏</td><td>您命中最珍貴的元素，也是最稀缺的。藏在日支亥中，始終在那裡，始終守護著您。</td></tr>
</table></div>
<div class="box bh"><div class="bt">最美麗的發現：丁壬合化木</div>
<p>您的日支（亥）中藏有壬水——您的夫星。您的日主丁火與這顆壬水，在命理上形成一個最動人的組合：<strong>丁壬合化木</strong>。</p>
<p>木是您的印星——滋養、保護您丁火日主的力量。<strong>您與丈夫之間的深層連結，在命盤的最底處，化成了智慧與保護，源源不斷地滋養著您。</strong>婚姻本身，就是您最重要的內在力量之源。這樣的命理組合極為難得。這是屬於您的。</p>
</div>"""

body += """<h1>三、性格——外柔內剛，深情藏底</h1>
<p>丁火日主是八字所有日主中，情感最細膩、最有深度的一種。她們能感知文字無法捕捉的東西，在進入一個房間之前，就已感受到了氣氛。</p>
<table class="dt"><thead><tr><th>特質</th><th>在生活中的表現</th></tr></thead><tbody>
<tr><td class="pos">靜默的觀察者</td><td>您什麼都看見了。您一生都在精準地讀懂人——他們的動機、真實的感受、言語背後的含義。只是，您不一定說出來。</td></tr>
<tr><td class="pos">以行動為愛的語言</td><td>您不說「我愛你」，您用照顧說。記住每一個細節，在需求被說出之前就已預先安排妥當。</td></tr>
<tr><td class="pos">外柔內剛</td><td>不熟悉您的人以為您柔順好說話。熟悉您的人明白——某些事情上，您不會動搖。燭光在風中搖，但不熄。</td></tr>
<tr><td class="pos">深沉的忠誠</td><td>一旦您給出了信任，就是全部。您是那種任何時刻打電話，對方都知道您會在的人。</td></tr>
<tr><td class="neg">憂慮</td><td>水壓火，命盤天然帶有一份背景性的操心與焦慮。您為愛的人所擔負的牽掛，是一條幾乎不曾中斷的線。學習放下，是一輩子的功課——也是值得去做的功課。</td></tr>
<tr><td class="neg">不擅索取</td><td>您付出慷慨，卻難以接受。您同樣值得被照顧。</td></tr>
</tbody></table>
<div class="quote">「燭光從不邀功。它只是照亮房間——而每一個曾被它溫暖過的人，一輩子都不會忘記。」</div>"""

body += """<h1>四、財運——財大身弱，兼顧共管</h1>
<p>金是您的財星，而您的命盤裡金極旺——天干三顆金星。您對財務的本能敏銳是真實的，您的能力遠比外人所看到的要強。</p>
<table class="dt"><thead><tr><th>財運特質</th><th>解讀</th></tr></thead><tbody>
<tr><td><strong>天然能力</strong></td><td>您對金錢的本能敏銳——什麼值錢、什麼是浪費、資源流向哪裡——這些您都看得清楚。您不浪費，您也看得出別人的浪費。</td></tr>
<tr><td><strong>挑戰</strong></td><td>財多身弱：命盤中的財富能量大於日主本身能承載的。婚姻是您財運最重要的支柱——兩人共同管理、共同決策，效果最佳。</td></tr>
<tr><td><strong>最好的方式</strong></td><td>伴侶合作、共同決定。您的財務直覺，加上適合的伴侶力量，才是財富真正穩固的組合。</td></tr>
<tr><td><strong>現在（2025–2035）</strong></td><td>財務穩定。重點應放在享受所建立的一切，而非製造新的壓力。您已賺得了這份安穩。</td></tr>
</tbody></table>"""

body += """<h1>五、感情婚姻——丁壬合，燭光在粉中燃燒</h1>
<p>女命的夫星，是管剋日主的那個五行。丁火被水所剋，水就是夫星。而您的命盤水氣極旺——夫星是您命中最主導的力量之一。</p>
<div class="box bh"><div class="bt">譚國偉與譚太太——一對難得的命理組合</div>
<p><strong>Ken（譚國偉）的日主是庚金（陽金）。您的日主是丁火（陰火）。</strong></p>
<p>丁壬合化木：您的日主（丁）與日支亥中的壬水（夫星）相合，在命理上形成一個最為美麗的組合，合而化為木——您的印星，也就是滋養保護您的力量。<strong>在最深的層次上，這段婚姻，化成了您的智慧與保護。</strong></p>
<p>從Ken的角度看：丁火（您）是他的正印——智慧星。您是滋養他、溫暖他、給他深度的那個力量。<em>他鍛造金屬，您提供讓金屬蛻變的熱度。</em>彼此成就，彼此完整。</p>
<p>補充：Ken的日柱是庚子，與您的月柱和時柱（庚子）完全相同。你們共享相同的核心能量——這造就了一種無需言說的深層默契。</p>
</div>
<table class="dt"><thead><tr><th>感情特質</th><th>解讀</th></tr></thead><tbody>
<tr><td><strong>夫星特質</strong></td><td>強大、有能力、有主見。他帶著自己的引力場。他帶來壓力，也帶來保護——而隨著歲月，保護的比重越來越重。</td></tr>
<tr><td><strong>你們的相處</strong></td><td>燭光與金屬：他是托住您的結構，您是讓他蛻變的溫度。沒有燭光，金屬是冷的，沒有方向；沒有金屬，燭光沒有燈座，容易熄滅。</td></tr>
<tr><td><strong>婚姻給予您的</strong></td><td>在您的命盤裡，婚姻透過丁壬合，真正啟動了您的印星。正確的伴侶不只是帶來愛，更帶來了您命中最需要的那個元素。</td></tr>
<tr><td><strong>配偶宮（亥）</strong></td><td>亥水深沉、靈性、充滿情感深度。婚姻對您而言，是靈魂層面的連結，不只是生活安排。</td></tr>
</tbody></table>"""

body += """<h1>六、子女——子女是您最大的福氣</h1>
<p>您的食傷星是土——丁火自然生出的元素。子女，從命理上說，是您火焰的延伸與表達。</p>
<table class="dt"><thead><tr><th>子女特質</th><th>解讀</th></tr></thead><tbody>
<tr><td><strong>Vanessa（譚穎珊・丙火）</strong></td><td>Vanessa的日主是丙火（陽火）——與您相同的五行，只是更強、更外顯。她是您燭光放大成太陽的樣子。她的熱情與溫暖，根源在您，她汲取您的力量，有時未必說出口。</td></tr>
<tr><td><strong>Preston（譚詠昌・戊土）</strong></td><td>Preston的日主是戊土（陽土）——火所生出的元素。他從您的火焰中誕生。他的深沉、他的原則、他的標準——那支從不熄滅的燭光，塑造了他。</td></tr>
<tr><td><strong>您對他們的意義</strong></td><td>您是兩個孩子性格的根源。Vanessa的溫暖，Preston的原則，都來自同一個地方：您，在每一個寒冬裡，守住那份光。</td></tr>
<tr><td><strong>福氣</strong></td><td>子女是您命中最深的喜悅。隨著他們成長，這份關係只會越來越美。</td></tr>
</tbody></table>"""

body += """<h1>七、事業——溫潤待人，家人福氣</h1>
<div class="box bp"><div class="bt">您的天然角色</div>
<p>丁火日主的人，在能直接感受到自己溫暖與關懷的地方最能發揮。不是舞台，不是聚光燈，而是那個讓一切運作起來的房間——您在那裡，氣氛就不一樣。在任何家庭或團隊中，您是凝聚文化、定調氣氛、第一個察覺問題的那個人。這不是小事，這是無可替代的。</p>
</div>
<table class="dt"><thead><tr><th>事業特質</th><th>解讀</th></tr></thead><tbody>
<tr><td><strong>天然優勢</strong></td><td>情商、溫暖、財務直覺、讓關係和系統在幕後順暢運作的能力</td></tr>
<tr><td><strong>最適合的方式</strong></td><td>合作而非單打獨鬥。您的命盤為協作而設計。與合適的人一起，您能完成一個人力所不及的事。</td></tr>
<tr><td><strong>您真正的貢獻</strong></td><td>您讓身邊的事情，「感覺好」。這是一種稀有而無可替代的禮物。</td></tr>
<tr><td class="now"><strong>現在（2025–2035）</strong></td><td class="now">穩定的時期。選擇性地付出精力。您已不需要事事承擔——學會更有智慧地選擇，讓燭光燃得更長。</td></tr>
</tbody></table>"""

body += """<h1>八、健康福氣——保護心臟，守住溫暖</h1>
<p>丁火主<strong>心臟、眼睛、神經系統</strong>。金水在命盤中大量壓制丁火，這些部位最容易吸收您的壓力與歲月的負擔。</p>
<table class="dt"><thead><tr><th>健康範疇</th><th>建議</th></tr></thead><tbody>
<tr><td><strong>心臟與血液循環</strong></td><td>保暖。避免長時間受寒受濕。定期體檢。您的體質對溫度的敏感度比常人更高，這是命盤的現實。</td></tr>
<tr><td><strong>神經系統・焦慮</strong></td><td>水壓火，帶來背景性的焦慮與操心。這不是您的想像——這在命盤中有根有據。真正能令神經系統安靜下來的方式，是投資，不是奢侈。</td></tr>
<tr><td><strong>溫暖是良藥</strong></td><td>您生於深冬子時。溫熱的食物、溫暖的環境、溫暖的人陪伴——這些對您而言，不是偏好，而是體質的需要。</td></tr>
<tr><td><strong>休息</strong></td><td>您已付出了幾十年。您被允許——您被<em>要求</em>——在這個人生階段多休息。從不休息的燭光，會燃盡。</td></tr>
</tbody></table>
<div class="box bg"><div class="bt">您的福氣</div>
<p>您帶著一個極具挑戰的命盤，以優雅、尊嚴與溫暖，走過了六十多個年頭。在您的日支亥中，始終靜靜藏著甲木——那根滋養燭光的木。它一直都在。您所積累的智慧、您所建立的家庭、那些愛您的人——這些都是您的木。它們讓燭光繼續燃燒。而在走過這麼多個冬天之後，它依然燃燒著。</p>
</div>"""

body += """<h1>九、田宅——家是您的根基與滋養</h1>
<table class="dt"><thead><tr><th>田宅特質</th><th>解讀</th></tr></thead><tbody>
<tr><td><strong>家作為避風港</strong></td><td>對您而言，家不只是居住的地方，而是您充電、復原的所在。居家環境的溫度與品質，對您的健康和心情影響深遠——這不是挑剔，而是體質的需要。</td></tr>
<tr><td><strong>家應有的感覺</strong></td><td>溫暖、安靜、舒適。不是以地位驅動，而是以靈魂驅動。一踏進門就能感到放鬆的地方。</td></tr>
<tr><td><strong>置業能力</strong></td><td>命盤中金（財星）極旺，置業的財力是真實存在的。共同決策、仔細審視，效果最好。</td></tr>
<tr><td><strong>現在的理想</strong></td><td>減少管理，增加享受。能簡化的盡量簡化。燭光，在安靜溫暖的房間裡，燃燒得最美。</td></tr>
</tbody></table>"""

body += """<h1>十、一生大運——燭光的旅程</h1>
<p>子平八字以十年大運追蹤人生的節奏。每個十年，帶著不同的能量。以下是您這一生非凡旅程的輪廓：</p>
<div class="tl"><div class="tl-yr">0–4歲<br>（1961–65）</div><div class="tl-gz"></div><div class="tl-desc"><strong>燭光初燃。</strong>生於深冬子時——命理上最寒冷的起點。無論早年歲月帶來什麼，它們在一切開始之前，已教會了您：如何守住自己的溫暖。</div></div>
<div class="tl"><div class="tl-yr">4–14歲<br>（1965–75）</div><div class="tl-gz">己亥</div><div class="tl-desc"><strong>童年・少女時代。</strong>己土食神大運——表達、聰敏、細膩的感知力。一個什麼都看在眼裡的孩子。您在懂得語言之前，就已經開始讀懂氣氛了。</div></div>
<div class="tl"><div class="tl-yr">14–24歲<br>（1975–85）</div><div class="tl-gz">戊戌</div><div class="tl-desc"><strong>尋找自己。</strong>戊土帶來安靜的穩定感；戌中藏丁火，細微地溫暖著命盤。這十年，您在形成自己的價值觀、標準，以及對自己是誰的認知。</div></div>
<div class="tl"><div class="tl-yr">24–34歲<br>（1985–95）</div><div class="tl-gz">丁酉</div><div class="tl-desc"><strong>燭光找到了它的燈座。</strong>丁火比肩大運——同類幫扶，日主有力。<strong>您認識了Ken，結婚，生育了Vanessa和Preston。</strong>您的燭光找到了燈座。這十年是一切的根基。</div></div>
<div class="tl"><div class="tl-yr">34–44歲<br>（1995–2005）</div><div class="tl-gz">丙申</div><div class="tl-desc"><strong>家庭的全盛期。</strong>丙火劫財大運——強力幫扶日主。子女在成長，一切同時向您伸手。而您，把一切都撐住了。</div></div>
<div class="tl"><div class="tl-yr">44–54歲<br>（2005–15）</div><div class="tl-gz">乙未</div><div class="tl-desc"><strong>智慧降臨。</strong>乙木正印大運——您命中最需要的元素，第一次成為大運主角！壓力開始減輕。思路變得清晰，心情變得輕盈。<strong>您感受到了這個變化。</strong></div></div>
<div class="tl"><div class="tl-yr">54–64歲<br>（2015–25）</div><div class="tl-gz">甲午</div><div class="tl-desc"><strong>您一生最好的十年。</strong>甲木正印（最強印星！）加午火劫財——木與火同時扶持您的丁火。<strong>是您一生最平衡、最舒適、最平和的十年。</strong>您多年來給予的溫暖，終於回到了您身上。</div></div>
<div class="tl tn"><div class="tl-yr">64–74歲<br>（2025–35）★ 現在</div><div class="tl-gz">癸巳</div><div class="tl-desc"><strong>當下：火焰繼續燃燒。</strong>癸水財星在運，但巳火（劫財）在支中扶持日主，為燭光補充能量。<strong>這個十年，是享受您所建立的一切的時候。</strong>不是製造新的壓力——而是接受您多年來如此慷慨付出的那份溫暖，讓它回到您身上。</div></div>
<div class="tl"><div class="tl-yr">74–84歲<br>（2035–45）</div><div class="tl-gz">壬辰</div><div class="tl-desc"><strong>圓滿。</strong>壬水是夫星的能量。這個十年帶著一種完整的質感——被愛您的人環繞，您也環繞著他們。</div></div>
<div class="tl"><div class="tl-yr">84歲以上<br>（2045+）</div><div class="tl-gz">辛卯</div><div class="tl-desc"><strong>悠長的燭光。</strong>命盤走完一個完整的週期，卯木印星出現，再為丁火添薪。一份安靜、持久的光，燃入高齡。</div></div>"""

body += """<h1>十一、2026–2027 流年重點</h1>
<div class="box bg"><div class="bt">2026年 丙午年——溫暖與活力</div>
<p>丙火劫財到來，午火在支中加持——同類之火，直接幫扶您的丁火日主。<strong>這是近年來您感覺最有活力、最輕盈的一年。</strong>多出門，多見見您愛的人，有機會就去旅行。這一年，宇宙給了您一份好禮——請雙手接受。</p>
</div>
<div class="box bn"><div class="bt">2027年 丁未年——舒適與喜悅</div>
<p>丁火比肩（與您日主完全相同的元素）到來，如同看見最好狀態的自己。未土中藏乙木——印星暗中護持。<strong>2027年是真實的舒適、家人的溫暖、安靜的幸福。</strong>請好好品味每一個時刻。</p>
</div>
<div class="quote">「走過六十個冬天的燭光，知道一件太陽只能猜測的事：在黑暗中，忠實地給予溫暖，是世上最持久的光。」</div>
<div class="closing">
<p><strong>關於此命盤：</strong>本報告以子平八字推算，依循鄺偉雄師傅所用之系統——與推算您丈夫Ken命盤的師傅相同。命理是認識自我的鏡子，而非固定的命運。您的選擇，塑造您的人生；命理，揭示旅途的地形。</p>
<p><strong>製作：</strong>詩詩（Sisi）謹製，代Ken呈上 &middot; 2026年3月 &middot; <em>願這份燭光，照亮您所有美好的歲月。——您的丈夫，懷著感恩與愛。</em></p>
</div>
</div></div></body></html>"""

# Write complete file
with open('/workspace/mabel_bazi_zh.html', 'w', encoding='utf-8') as f:
    f.write(head + body)

import os, shutil
os.makedirs('/workspace/mabel_zh_dist', exist_ok=True)
shutil.copy('/workspace/mabel_bazi_zh.html', '/workspace/mabel_zh_dist/index.html')

final = open('/workspace/mabel_bazi_zh.html', encoding='utf-8').read()
print(f"Total: {len(final)} chars")
print(f"H1 count: {final.count('<h1>')}")
print(f"Has </html>: {'</html>' in final}")
