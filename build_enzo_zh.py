#!/usr/bin/env python3
# Build Enzo BaZi Traditional Chinese report

enzo_zh = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>子平八字命盤全解 — 陳演章</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@300;400;500;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap');
  :root {
    --gold: #c9a84c;
    --deep: #1a1a3a;
    --fire-red: #8b2500;
    --cream: #faf6ee;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:#1a1a2e; font-family:'Noto Sans TC',sans-serif; color:#333; }

  .cover {
    min-height:100vh;
    background: linear-gradient(160deg, #1a0a00 0%, #3a1a00 40%, #5a2a00 100%);
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    text-align:center; padding:60px 40px; position:relative; overflow:hidden;
  }
  .cover::before {
    content:''; position:absolute; top:0; left:0; right:0; bottom:0;
    background: radial-gradient(ellipse at center, rgba(201,168,76,0.2) 0%, transparent 70%);
  }
  .cover-symbol { font-size:72px; margin-bottom:20px; }
  .cover-title { font-size:48px; color:var(--gold); font-weight:700; letter-spacing:6px; margin-bottom:12px; font-family:'Noto Serif TC',serif; }
  .cover-name { font-size:42px; color:#fff; font-weight:500; letter-spacing:8px; margin-bottom:8px; font-family:'Noto Serif TC',serif; }
  .cover-en { font-size:20px; color:rgba(255,255,255,0.6); margin-bottom:40px; letter-spacing:2px; }
  .cover-pillars { display:flex; gap:20px; margin:30px 0; }
  .pillar-box {
    background:rgba(201,168,76,0.15); border:1px solid rgba(201,168,76,0.4);
    border-radius:12px; padding:16px 20px; text-align:center; min-width:80px;
  }
  .pillar-label { font-size:11px; color:rgba(201,168,76,0.7); letter-spacing:2px; margin-bottom:8px; }
  .pillar-char { font-size:34px; color:var(--gold); line-height:1.3; font-family:'Noto Serif TC',serif; }
  .cover-subtitle { font-size:13px; color:rgba(255,255,255,0.45); letter-spacing:4px; margin-top:30px; }
  .cover-date { font-size:13px; color:rgba(255,255,255,0.35); margin-top:10px; }

  .content { background:var(--cream); max-width:900px; margin:0 auto; }
  .section { padding:60px 60px; border-bottom:1px solid rgba(0,0,0,0.08); }
  .section:last-child { border-bottom:none; }

  .section-header { display:flex; align-items:center; gap:16px; margin-bottom:36px; }
  .section-number {
    width:48px; height:48px; border-radius:50%;
    background: linear-gradient(135deg, #7a1a00, #3a0a00);
    color:var(--gold); font-size:18px; font-weight:700;
    display:flex; align-items:center; justify-content:center; flex-shrink:0;
    font-family:'Noto Serif TC',serif;
  }
  .section-title { font-family:'Noto Serif TC',serif; font-size:26px; color:var(--deep); letter-spacing:3px; }

  .chart-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-bottom:36px; }
  .chart-cell {
    background:#fff; border:2px solid #e8dfc8; border-radius:16px;
    padding:20px; text-align:center; box-shadow:0 2px 12px rgba(0,0,0,0.06);
  }
  .chart-cell.day { border-color:var(--gold); background:linear-gradient(135deg,#fff8f0,#fff0e0); }
  .cell-label { font-size:11px; color:#999; letter-spacing:2px; margin-bottom:12px; }
  .cell-stems { font-size:42px; color:#8b2500; line-height:1; margin-bottom:8px; font-family:'Noto Serif TC',serif; }
  .cell-branch { font-size:38px; color:var(--deep); font-family:'Noto Serif TC',serif; }
  .cell-element { font-size:12px; color:#aaa; margin-top:10px; }

  .highlight-box {
    background: linear-gradient(135deg, #fff8f0, #ffeedd);
    border-left:4px solid #8b2500; border-radius:0 12px 12px 0;
    padding:24px 28px; margin:24px 0;
  }
  .highlight-box h3 { color:var(--fire-red); font-family:'Noto Serif TC',serif; font-size:18px; margin-bottom:12px; letter-spacing:2px; }
  .highlight-box p { color:#555; line-height:2.0; font-size:16px; }

  .gold-box {
    background: linear-gradient(135deg, #fdf8ed, #faf0d0);
    border:1px solid rgba(201,168,76,0.3); border-radius:16px;
    padding:28px; margin:24px 0;
  }
  .gold-box h3 { color:#8b6914; font-family:'Noto Serif TC',serif; font-size:18px; margin-bottom:12px; letter-spacing:2px; }
  .gold-box p { color:#555; line-height:2.1; font-size:16px; }

  .special-box {
    background: linear-gradient(135deg, #1a0a00, #3a1a00);
    border-radius:16px; padding:32px; margin:28px 0; color:#fff;
  }
  .special-box h3 { color:var(--gold); font-family:'Noto Serif TC',serif; font-size:20px; margin-bottom:16px; letter-spacing:3px; }
  .special-box p { color:rgba(255,255,255,0.85); line-height:2.0; font-size:16px; }

  p { line-height:2.1; color:#444; margin-bottom:18px; font-size:16px; }

  .element-tag {
    display:inline-block; padding:4px 14px; border-radius:20px;
    font-size:13px; font-weight:700; margin:4px;
  }
  .wood { background:#e8f5e0; color:#2d6a1a; }
  .fire { background:#fdecea; color:#c0392b; }
  .earth { background:#fdf5e0; color:#8b6914; }
  .metal { background:#edf4ff; color:#2c5282; }
  .water { background:#e8f4fd; color:#1a5a8a; }

  .print-btn {
    position:fixed; bottom:30px; right:30px;
    background:linear-gradient(135deg,#7a1a00,#3a0a00); color:var(--gold);
    border:none; padding:14px 28px; border-radius:30px; cursor:pointer;
    font-size:15px; font-weight:700; box-shadow:0 4px 20px rgba(0,0,0,0.3); z-index:999;
  }
  @media print {
    body { background:#fff; }
    .print-btn { display:none; }
    .cover { min-height:100vh; page-break-after:always; }
    .section { page-break-inside:avoid; }
  }
</style>
</head>
<body>

<div class="cover">
  <div class="cover-symbol">🕯️</div>
  <div class="cover-title">子平八字命盤全解</div>
  <div class="cover-name">陳演章</div>
  <div class="cover-en">Enzo Audemars Tran</div>

  <div class="cover-pillars">
    <div class="pillar-box">
      <div class="pillar-label">年柱</div>
      <div class="pillar-char">壬<br>寅</div>
    </div>
    <div class="pillar-box">
      <div class="pillar-label">月柱</div>
      <div class="pillar-char">庚<br>戌</div>
    </div>
    <div class="pillar-box" style="border-color:rgba(201,168,76,0.8);background:rgba(201,168,76,0.25);">
      <div class="pillar-label">日柱 ✦</div>
      <div class="pillar-char">丁<br>酉</div>
    </div>
    <div class="pillar-box">
      <div class="pillar-label">時柱</div>
      <div class="pillar-char">辛<br>丑</div>
    </div>
  </div>

  <div class="cover-subtitle">鄺師傅命理系統 · 子平正宗</div>
  <div class="cover-date">2022年10月11日生 · 美國三藩市</div>
</div>

<div class="content">

  <div class="section">
    <div class="section-header">
      <div class="section-number">一</div>
      <div class="section-title">四柱一覽</div>
    </div>

    <div class="chart-grid">
      <div class="chart-cell">
        <div class="cell-label">年柱</div>
        <div class="cell-stems">壬</div>
        <div class="cell-branch">寅</div>
        <div class="cell-element">水·木<br>壬寅 水虎</div>
      </div>
      <div class="chart-cell">
        <div class="cell-label">月柱</div>
        <div class="cell-stems">庚</div>
        <div class="cell-branch">戌</div>
        <div class="cell-element">金·土<br>庚戌 金狗</div>
      </div>
      <div class="chart-cell day">
        <div class="cell-label">日柱 ✦ 本命</div>
        <div class="cell-stems">丁</div>
        <div class="cell-branch">酉</div>
        <div class="cell-element">火·金<br>丁酉 火雞</div>
      </div>
      <div class="chart-cell">
        <div class="cell-label">時柱</div>
        <div class="cell-stems">辛</div>
        <div class="cell-branch">丑</div>
        <div class="cell-element">金·土<br>辛丑 金牛</div>
      </div>
    </div>

    <div class="highlight-box">
      <h3>日主：丁火 — 燭光之火</h3>
      <p>演章之日主為丁火，乃燭光之火、燈籠之焰。此非烈日之炎、野火之猛，而是寒夜中穩定的燭光——它不爭不奪，卻能照亮黑暗；它不喧不囂，卻令人自然靠近。丁火之人，天生有一種磁性的溫暖，使人如沐春風。他生而為引路之光，為啟迪人心而來。</p>
    </div>
  </div>

  <div class="section">
    <div class="section-header">
      <div class="section-number">二</div>
      <div class="section-title">日坐貴人：命中最罕見的禮物</div>
    </div>

    <div class="special-box">
      <h3>✦ 六十甲子中，只有四日得此殊榮</h3>
      <p>鄺師傅在命盤中發現了一個極為珍貴的格局。六十甲子循環之中，六十個可能的日柱裡，僅有<strong>四個日柱</strong>帶有「日坐貴人」之格：丁亥、丁酉、癸卯、癸巳。<br><br>
      演章生於<strong>丁酉日——正是這四日之一</strong>。<br><br>
      「日坐貴人」意味著：此人一生之中，都將有貴人相助。逢難有人解困，逢機有人引路，逢事有人扶持。貴人不在命盤外——它就坐落在日柱之中，是他本命的一部分，是他與生俱來的氣場。他不是僥倖得到貴人幫助，而是他的本質，自然而然地吸引了生命中的善緣。</p>
    </div>

    <p>更為難得的是，貴人星落在他的<strong>夫妻宮</strong>（日支酉）。鄺師傅明言：演章將來的伴侶，將是他命中最大的貴人之一——婚姻美滿，夫妻相得益彰，另一半不僅是伴侶，更是人生路上的最強後盾。</p>

    <div class="gold-box">
      <h3>✦ 同一個日柱的歷史人物</h3>
      <p>鄺師傅特別提到：歷史上以丁酉日出生的名人，包括<strong>孫中山先生</strong>與<strong>毛澤東</strong>——兩位在近代中國歷史上影響最深遠的人物。一位建立了共和，一位改寫了一個時代。丁酉日柱所承載的能量，是<strong>鼓舞人心的領導力、震撼人心的語言力，以及改變時代的影響力</strong>。命運非宿命，但這份能量，已寫入演章的命盤之中。</p>
    </div>
  </div>

  <div class="section">
    <div class="section-header">
      <div class="section-number">三</div>
      <div class="section-title">燭光祖孫：與外婆的神聖緣分</div>
    </div>

    <p>在鄺師傅對演章命盤的全部觀察中，有一點令人動容，也令外公外婆心頭一暖：</p>

    <div class="highlight-box">
      <h3>丁火外婆，丁火外孫</h3>
      <p>演章的外婆<strong>朱德貞（Mabel）</strong>，同樣是<strong>丁火日主</strong>。家族之中，外公Ken為庚金，媽媽Vanessa為丙火，舅舅Preston為戊土，哥哥Coleton為己土——獨有祖孫二人，同燃一盞丁火之燈。<br><br>
      在命理傳統中，這不是巧合，而是<strong>跨越世代的靈魂共鳴</strong>。外婆與外孫，同一種火，同一種光。外婆理解演章，有一種別人所沒有的深度；而演章，即使年幼，在外婆身邊也會有一種被完全看見、被完全接納的溫暖。這份緣分，是命盤寫就的，也是老天安排的。</p>
    </div>

    <p>丁火之光，耐心而穩定。它不爭，卻照；它不奪，卻暖。這份特質，將外婆與外孫連結在一起：兩人都有一種天然的磁性與溫度，人們會不自覺地被他們吸引，在他們身邊感到安心。</p>
  </div>

  <div class="section">
    <div class="section-header">
      <div class="section-number">四</div>
      <div class="section-title">五行格局分析</div>
    </div>

    <div style="margin:24px 0;">
      <div style="margin-bottom:12px;">
        <span class="element-tag metal">金 ●●● 旺</span>
        <span style="font-size:14px;color:#666;margin-left:8px;">庚戌月之庚、辛丑時之辛、丁酉日之酉</span>
      </div>
      <div style="margin-bottom:12px;">
        <span class="element-tag earth">土 ●●● 旺</span>
        <span style="font-size:14px;color:#666;margin-left:8px;">戌、丑藏己辛癸、辛丑時</span>
      </div>
      <div style="margin-bottom:12px;">
        <span class="element-tag water">水 ●● 有根</span>
        <span style="font-size:14px;color:#666;margin-left:8px;">壬寅年之壬</span>
      </div>
      <div style="margin-bottom:12px;">
        <span class="element-tag fire">火 ● 弱（日主）</span>
        <span style="font-size:14px;color:#666;margin-left:8px;">丁酉日主——即那一盞燭光本身</span>
      </div>
      <div style="margin-bottom:12px;">
        <span class="element-tag wood">木 ○ 最缺</span>
        <span style="font-size:14px;color:#666;margin-left:8px;">壬寅年之寅——全局最需之元素</span>
      </div>
    </div>

    <div class="highlight-box">
      <h3>金環圍燭：丁火鍛庚金</h3>
      <p>丁火燭光，四周皆是金氣（庚、辛、酉）。在命理中，火剋金——丁火正是鍛煉金屬的爐中之焰。演章的本質，是<strong>轉化與淬煉</strong>。他有火，金給了他材料。火與金相遇，是工匠之火——有目的，有控制，從堅硬的材料中創造出美麗的事物。<br><br>
      然而丁火需要木來維持火勢。命局缺木，演章最需要木氣的滋養：多親近大自然、多種植花草、多閱讀文學創作、多接觸藝術——這些木的能量，將成為他燭光最好的柴薪。鄺師傅明言：<strong>木，是他命中最需要的元素。</strong></p>
    </div>
  </div>

  <div class="section">
    <div class="section-header">
      <div class="section-number">五</div>
      <div class="section-title">名字的意義：陳演章</div>
    </div>

    <p>鄺師傅為演章所取的中文名，字字用心，與八字命格相互輝映：</p>

    <div class="gold-box">
      <h3>✦ 演章——「出口成章」</h3>
      <p><strong>演</strong>——演說、表演、呈現。一個能站在舞台上，以語言與姿態感動人心的人。<br><br>
      <strong>章</strong>——文章、篇章、奏章。有組織、有深度、有文學性的表達，帶著一種成熟的權威與美感。<br><br>
      合而觀之，師傅引用了成語<strong>「出口成章」</strong>——開口即是文章，說話如行雲流水，渾然天成，宛如寫就的錦繡文字。鄺師傅在演章的命盤中看見：他將是一個<strong>天生的表達者與演說家</strong>。無論是公眾演講、舞台表演、文學創作，還是領導者的感召力——他的聲音，將是他一生最有力的禮物。</p>
    </div>
  </div>

  <div class="section">
    <div class="section-header">
      <div class="section-number">六</div>
      <div class="section-title">壬寅年：他從何而來</div>
    </div>

    <p>演章生於壬寅年——水虎之年。虎是十二生肖之將帥，天生膽大、獨立、魅力非凡、領袖氣質。壬水之智慧，調和了虎的剛烈，賦予他靈活與深度。</p>

    <p>年柱之寅（虎），同時也是他命局中最主要的<strong>木氣來源</strong>——那根維持丁火燃燒所最需要的薪柴。這意味著，在他生命的起點，命運本身已將他所需之物安放其中。年柱是根，是來處，是家族基因的印記——他帶著這份木，帶著虎的魄力，來到這個世界。</p>

    <div class="highlight-box">
      <h3>虎與雞：自由與精緻之間的張力</h3>
      <p>年支寅（虎）與日支酉（雞）在命盤中形成一種有趣的內在張力：虎代表野性自由、勇往直前；雞代表精緻卓越、一絲不苟。演章一生將在這兩種能量之間尋找平衡——奔放探索的衝動，與精益求精的自我要求。能將兩者融而為一的人，往往成就非凡。</p>
    </div>
  </div>

  <div class="section">
    <div class="section-header">
      <div class="section-number">七</div>
      <div class="section-title">給演章的話</div>
    </div>

    <div class="gold-box">
      <h3>外公外婆寫給你的話</h3>
      <p style="font-style:italic;font-size:17px;line-height:2.3;color:#5a3e1a;">
      演章，我的孩子——<br><br>
      你來到這個世界，帶著一盞燭光。<br><br>
      鄺師傅第一眼看見你的命盤，就說了那個「丁」字。那一刻，外婆的眼眶紅了——因為那也是她自己命裡的「丁」。你和外婆，同一種火，同一種光，跨越了六十多年的時間在這個家族裡重逢。<br><br>
      你會說話。你會用語言照亮人心，就像燭光照亮黑暗一樣自然。這是你天生帶來的禮物——好好珍惜它，好好磨練它。<br><br>
      命裡帶著貴人，不代表你不需要努力。但它確實意味著：你不是孤身一人。這一生，在你最需要的時刻，總會有人出現，為你開一扇門、點一盞燈。<br><br>
      多接觸大自然，多讀書，多唱歌——讓木的能量餵養你心中那盞燭火，讓它燃得長久、燃得明亮。<br><br>
      外公外婆愛你，永遠。🕯️
      </p>
    </div>
  </div>

</div>

<button class="print-btn" onclick="window.print()">🖨️ 列印報告</button>

</body>
</html>"""

with open('/workspace/enzo_bazi_zh.html', 'w', encoding='utf-8') as f:
    f.write(enzo_zh)

print(f"Enzo ZH report: {len(enzo_zh)} chars")
print("Saved.")
