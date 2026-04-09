#!/usr/bin/env python3
"""Generate Excel Plumbing YTD Financial Statement PDF"""
import subprocess, os

# Build HTML in sections
html = ['<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n']
css = '''<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=IBM+Plex+Mono:wght@400&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'IBM Plex Sans',Arial,sans-serif;font-size:11px;color:#1a1a2e;background:#fff}
.hdr{background:linear-gradient(135deg,#1a3a52,#0d2137);color:#fff;padding:26px 44px 20px;display:flex;justify-content:space-between;align-items:flex-end}
.hdr h1{font-size:19px;font-weight:700}
.hdr .sub{font-size:11px;color:#8ab4d4;margin-top:3px}
.hdr-r{text-align:right}
.hdr-r .l{font-size:8px;color:#6a9bbf;text-transform:uppercase;letter-spacing:1px}
.hdr-r .v{font-size:13px;font-weight:600;color:#fff;margin-top:2px}
.sb{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:3px solid #1a3a52}
.sc{padding:16px 22px;border-right:1px solid #e8edf2;background:#f7fafc}
.sc:last-child{border-right:none}
.sc .sl{font-size:8px;text-transform:uppercase;letter-spacing:1px;color:#7a8fa8;margin-bottom:4px}
.sc .sv{font-size:19px;font-weight:700}
.sc .ss{font-size:8px;color:#aab8c4;margin-top:2px}
.content{padding:24px 44px}
.st{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.4px;color:#fff;background:#1a3a52;padding:7px 14px;margin-top:20px;border-radius:2px}
table{width:100%;border-collapse:collapse;font-size:11px}
thead th{background:#e8edf2;color:#3a5270;font-weight:600;font-size:9px;text-transform:uppercase;letter-spacing:0.7px;padding:7px 10px;text-align:right;border-bottom:2px solid #c0cfde}
thead th:first-child{text-align:left}
tbody tr{border-bottom:1px solid #eef2f6}
tbody td{padding:5px 10px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:11px}
tbody td:first-child{text-align:left;font-family:'IBM Plex Sans',sans-serif}
.pct{color:#7a8fa8;font-size:9px}
.pos{color:#0a7c5c}
.neg{color:#c0392b}
.i1 td:first-child{padding-left:24px}
.rs td{background:#eaf2fb!important;border-top:1px solid #c0d4e8;border-bottom:1px solid #c0d4e8;font-weight:600;color:#1a3a52}
.rt td{background:#1a3a52!important;color:#fff!important;font-weight:700;font-size:12px;padding:8px 10px;border-top:2px solid #0d2137;border-bottom:2px solid #0d2137}
.rt td:first-child{color:#fff}
.rg td{background:#0d2137!important;color:#ffd700!important;font-weight:700;font-size:13px;padding:9px 10px;border-top:3px solid #ffd700}
.rg td:first-child{color:#ffd700}
.bl td{height:7px;border:none;background:#fff}
.blk td{border:none;background:#fff}
.ft{padding:12px 44px;border-top:1px solid #e0e8f0;display:flex;justify-content:space-between;font-size:8px;color:#9ab0c0}
</style>\n</head>\n<body>\n'

hdr = '''<div class="hdr">
  <div><h1>EXCEL PLUMBING SUPPLY + SHOWROOM</h1>
  <div class="sub">Branches: 1 &nbsp;|&nbsp; YTD Financial Statement &#8212; January 1 through March 31, 2026</div></div>
  <div class="hdr-r"><div class="l">As of Date</div><div class="v">March 31, 2026</div>
  <div style="margin-top:5px"><div class="l">Printed</div><div class="v" style="font-size:10px">April 2, 2026</div></div></div>
</div>
<div class="sb">
  <div class="sc"><div class="sl">Net Sales (YTD)</div><div class="sv" style="color:#1a3a52">$11,518,991</div><div class="ss">+13.6% vs Prior Year</div></div>
  <div class="sc"><div class="sl">Gross Profit (YTD)</div><div class="sv" style="color:#0a7c5c">$3,345,628</div><div class="ss">29.0% Gross Margin</div></div>
  <div class="sc"><div class="sl">Operating Income (YTD)</div><div class="sv" style="color:#c0392b">($88,760)</div><div class="ss">&#8722;0.8% of Sales</div></div>
  <div class="sc"><div class="sl">Net Income (YTD)</div><div class="sv" style="color:#0a7c5c">$67,097</div><div class="ss">+0.6% of Sales</div></div>
</div>
<div class="content">
'''

def sec(title, rows):
    s = ['<div class="st">' + title + '</div>\n<table>\n']
    s.append('<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>\n<tbody>\n')
    for r in rows:
        cls = r[0]
        cells = r[1:]
        s.append('<tr' + (' class="' + cls + '"' if cls else '') + '>')
        for i, c in enumerate(cells):
            tag = 'td'
            s.append('<' + tag + ((' class="' + r[0] + '"') if i == 0 and r[0] else '') + '>' + str(c) + '</' + tag + '>')
        s.append('</tr>\n')
    s.append('</tbody>\n</table>\n')
    return ''.join(s)

def c(v, pct=False, pos=False, neg=False, em=False):
    cls = []
    if pct: cls.append('pct')
    if pos: cls.append('pos')
    if neg: cls.append('neg')
    cname = ' '.join(cls) if cls else ''
    return '<td' + (' class="' + cname + '"' if cname else '') + '>' + str(v) + '</td>'

rows_net = [
  ('', 'Sales &#8211; Counter', '1,258,972.83', True, False, '846,046.45', True, False, '412,926.38', False, True, '+48.8%', True, False),
  ('', 'Sales &#8211; Showroom', '9,306,949.52', True, False, '7,101,395.83', True, False, '2,205,553.69', False, True, '+31.1%', True, False),
  ('', 'Sales &#8211; Direct', '131,674.65', True, False, '607,385.30', True, False, '(475,710.65)', False, False, '&#8722;78.3%', True, False),
  ('', 'Sales &#8211; Inside', '1,116,266.22', True, False, '1,840,425.37', True, False, '(724,159.15)', False, False, '&#8722;39.3%', True, False),
  ('', 'Sales &#8211; Returns', '(390,023.66)', False, True, '(326,451.10)', False, True, '(63,572.56)', False, False, '&#8722;19.5%', True, False),
]

# Actually just use raw HTML strings for reliability
html_parts = []

# Write to file
with open('/workspace/fin_stmt.html', 'w') as f:
    f.write('<!DOCTYPE html>\n<html lang="en\">\n<head>\n<meta charset="UTF-8">\n')
    f.write(css)
    f.write('</head>\n<body>\n')
    f.write(hdr)
    
    # Net Sales
    f.write('<div class="st">Net Sales</div><table>\n<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>\n<tbody>\n')
    rows = [
      ('Sales &#8211; Counter','1,258,972.83','10.9%','846,046.45','8.3%','412,926.38','+48.8%','','','','','pos',''),
      ('Sales &#8211; Showroom','9,306,949.52','80.8%','7,101,395.83','70.0%','2,205,553.69','+31.1%','','','','','pos',''),
      ('Sales &#8211; Direct','131,674.65','1.1%','607,385.30','6.0%','(475,710.65)','&#8722;78.3%','','','','','neg',''),
      ('Sales &#8211; Inside','1,116,266.22','9.7%','1,840,425.37','18.2%','(724,159.15)','&#8722;39.3%','','','','','neg',''),
      ('Sales &#8211; Returns','(390,023.66)','(3.4%)','(326,451.10)','(3.2%)','(63,572.56)','&#8722;19.5%','','','','','neg',''),
      ('Freight &amp; Delivery Rebate','59,826.55','0.5%','47,803.23','0.5%','12,023.32','+25.2%','','','','','pos',''),
      ('Tax Rebate / Promotion','(30.00)','(0.0%)','(721.90)','(0.0%)','691.90','+95.8%','','','','','pos',''),
      ('Delivery Charge','23,706.54','0.2%','16,551.31','0.2%','7,155.23','+43.2%','','','','','pos',''),
      ('Restocking Charge','11,648.02','0.1%','7,412.90','0.1%','4,235.12','+57.1%','','','','','pos',''),
    ]
    for r in rows:
        name,ytd26,pct26,ytd25,pct25,chg,pctchg = r[0],r[1],r[2],r[3],r[4],r[5],r[6]
        ct = r[7]  # type: pos, neg, or ''
        c1 = 'pos' if ct=='pos' else ('neg' if ct=='neg' else '')
        c2 = 'pct'; c3 = ''; c4 = 'pos' if '+' in str(ytd25) and ytd25 != '—' else ('neg' if '(' in str(ytd25) else '')
        c5 = 'pct'
        c6 = 'pos' if '+' in chg else 'neg'
        c7 = 'pct'
        def td(v,cls=''): return '<td' + (' class="'+cls+'"' if cls else '') + '>' + str(v) + '</td>'
        f.write('<tr>' + td(name) + td(ytd26,c1) + td(pct26,c2) + td(ytd25,c3) + td(pct25,c5) + td(chg,c6) + td(pctchg,c7) + '</tr>\n')
    f.write('<tr class="rt"><td>NET SALES</td><td>11,518,990.67</td><td class="pct">100.0%</td><td>10,139,847.39</td><td class="pct">100.0%</td><td>1,379,143.28</td><td class="pct">+13.6%</td></tr>\n')
    f.write('</tbody>\n</table>\n')
    
    # COGS
    f.write('<div class="st">Cost of Goods Sold</div><table>\n<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>\n<tbody>\n')
    cogs_rows = [
      ('Cost of Goods Sold &#8211; Counter','909,154.20','7.9%','685,209.22','8.3%','(223,944.98)','&#8722;32.7%','neg'),
      ('Cost of Goods Sold &#8211; Showroom','6,699,426.47','58.2%','4,828,116.76','58.6%','(1,871,309.71)','&#8722;38.8%','neg'),
      ('Cost of Goods Sold &#8211; Direct','96,444.64','0.8%','34,738.88','0.4%','(61,705.76)','&#8722;177.6%','neg'),
      ('Cost of Goods Sold &#8211; Inside','1,015,858.42','8.8%','617,163.55','7.5%','(398,694.87)','&#8722;64.6%','neg'),
      ('Cost of Goods Sold &#8211; Returns','(242,240.86)','(2.1%)','(182,103.95)','(2.2%)','(60,136.91)','&#8722;33.0%','neg'),
      ('Freight In and Out','266.58','0.0%','314.14','0.0%','(47.56)','&#8722;15.1%','neg'),
    ]
    for r in cogs_rows:
        def td(v,cls=''): return '<td' + (' class="'+cls+'"' if cls else '') + '>' + str(v) + '</td>'
        ct = r[7]
        c1 = 'neg' if ct=='neg' else ('pos' if ct=='pos' else '')
        c6 = 'neg' if '&#8722;' in r[5] else 'pos'
        f.write('<tr>' + td(r[0]) + td(r[1],c1) + td(r[2],'pct') + td(r[3]) + td(r[4],'pct') + td(r[5],c6) + td(r[6],'pct') + '</tr>\n')
    def td(v,cls=''): return '<td' + (' class="'+cls+'"' if cls else '') + '>' + str(v) + '</td>'
    f.write('<tr class="rs"><td>Total Cost of Product Sold</td><td>8,478,909.45</td><td class="pct">73.6%</td><td>7,551,066.09</td><td class="pct">74.5%</td><td>927,843.36</td><td class="pct">+12.3%</td></tr>\n')
    f.write('<tr class="blk"><td colspan="7"></td></tr>\n')
    cogs2 = [
      ('Purchases','8,271,272.58','71.8%','7,434,161.85','73.3%','(837,110.73)','&#8722;11.3%'),
      ('Clear Purchases to Inventory','(8,271,272.58)','(71.8%)','(7,434,161.85)','(73.3%)','(837,110.73)','&#8722;11.3%'),
      ('Comm-Cost / COGS Difference','(15,106.34)','(0.1%)','(4,457.61)','(0.1%)','(10,648.73)','&#8722;238.9%'),
      ('Clear Comm-Cost Difference to P&amp;L','15,106.34','0.1%','4,457.61','0.1%','10,648.73','+238.9%'),
      ('Purchase Discounts Taken','(130,743.52)','(1.1%)','(89,734.33)','(1.1%)','(41,009.19)','&#8722;45.7%'),
      ('Vendor Rebates / Promotion','(175,946.07)','(1.5%)','(144,665.82)','(1.8%)','(31,280.25)','&#8722;21.6%'),
      ('Freight In &#8211; Vendor','57,906.94','0.5%','40,070.13','0.5%','(17,836.81)','&#8722;44.5%'),
      ('Inventory Adjustments','(67,954.34)','(0.6%)','(65,324.77)','(0.8%)','(2,629.57)','&#8722;4.0%'),
      ('Vendor Defect Allowance','(12,676.07)','(0.1%)','(8,702.23)','(0.1%)','(3,973.84)','&#8722;45.7%'),
      ('Restocking Charge &#8211; Vendor','3,717.79','0.0%','2,236.26','0.0%','1,481.53','+66.2%'),
      ('Sales Discounts Given','(20,338.33)','(0.2%)','(14,219.00)','(0.2%)','(6,119.33)','&#8722;43.0%'),
    ]
    for r in cogs2:
        c1 = 'neg' if '(' in r[1] else ''
        c6 = 'neg' if '&#8722;' in r[5] else 'pos'
        f.write('<tr>' + td(r[0]) + td(r[1],c1) + td(r[2],'pct') + td(r[3]) + td(r[4],'pct') + td(r[5],c6) + td(r[6],'pct') + '</tr>\n')
    f.write('<tr class="rs"><td>Total Other Cost of Goods Sold</td><td class="neg">(305,546.87)</td><td class="pct">(2.7%)</td><td class="neg">(252,022.14)</td><td class="pct">(3.1%)</td><td class="neg">(53,524.73)</td><td class="pct">&#8722;21.2%</td></tr>\n')
    f.write('<tr class="blk"><td colspan="7"></td></tr>\n')
    f.write('<tr class="rt"><td>TOTAL COST OF GOODS SOLD</td><td>8,173,362.58</td><td class="pct">71.0%</td><td>7,418,813.96</td><td class="pct">73.2%</td><td>754,548.62</td><td class="pct">+10.2%</td></tr>\n')
    f.write('<tr class="blk"><td colspan="7"></td></tr>\n')
    f.write('<tr class="rg"><td>GROSS PROFIT</td><td>3,345,628.09</td><td class="pct">29.0%</td><td>2,721,033.43</td><td class="pct">26.8%</td><td class="pos">624,594.66</td><td class="pct">+23.0%</td></tr>\n')
    f.write('</tbody>\n</table>\n')
    
    # Operating Expenses
    f.write('<div class="st">Operating Expenses</div><table>\n<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>\n<tbody>\n')
    op_rows = [
      ('Accounts Payable Over / Short','(0.09)','0.0%','(2.55)','0.0%','2.46','+96.5%','pos'),
      ('Advertising &amp; Promotion','32,000.21','0.3%','19,769.03','0.2%','(12,231.18)','&#8722;61.9%','neg'),
      ('Bank Charges','25.00','0.0%','25.00','0.0%','&#8212;','&#8212;',''),
      ('Business Tax &#8211; San Francisco','19,610.50','0.2%','8,452.00','0.1%','(11,158.50)','&#8722;132.0%','neg'),
      ('Computer &#8211; Website Maintenance','99.99','0.0%','99.99','0.0%','&#8212;','&#8212;',''),
      ('Computer &#8211; Software Support','32,902.07','0.3%','23,480.96','0.3%','(9,421.11)','&#8722;40.1%','neg'),
      ('Contributions','1,035.00','0.0%','535.00','0.0%','(500.00)','&#8722;93.5%','neg'),
      ('Credit Card Processing','225,090.36','2.0%','149,528.09','1.8%','(75,562.27)','&#8722;50.5%','neg'),
      ('Dues &amp; Subscriptions','27,559.36','0.2%','18,999.93','0.2%','(8,559.43)','&#8722;45.1%','neg'),
      ('Employee Benefits','15,063.94','0.1%','11,489.29','0.1%','(3,574.65)','&#8722;31.1%','neg'),
      ('Freight &amp; Delivery','8,286.34','0.1%','6,804.94','0.1%','(1,481.40)','&#8722;21.8%','neg'),
      ('Insurance &#8211; Medical &amp; Dental','197,806.92','1.7%','148,691.69','1.8%','(49,115.23)','&#8722;33.0%','neg'),
      ('Insurance &#8211; Property &amp; Casualty','26,918.40','0.2%','22,653.08','0.3%','(4,265.32)','&#8722;18.8%','neg'),
      ('Insurance &#8211; Vehicles','9,190.91','0.1%','2,657.35','0.0%','(6,533.56)','&#8722;245.9%','neg'),
      ('Insurance &#8211; Workers&#8217; Compensation','21,785.45','0.2%','19,395.32','0.2%','(2,390.13)','&#8722;12.3%','neg'),
      ('Legal &amp; Professional Expense','1,237.50','0.0%','1,237.50','0.0%','&#8212;','&#8212;',''),
      ('Licenses &amp; Fees','1,405.00','0.0%','1,405.00','0.0%','&#8212;','&#8212;',''),
      ('Office Supplies &amp; Expense','5,618.43','0.0%','4,966.62','0.1%','(651.81)','&#8722;13.1%','neg'),
      ('Payroll Taxes &#8211; Federal','779,101.11','6.8%','249,411.18','3.0%','(529,689.93)','&#8722;212.4%','neg'),
      ('Payroll Taxes &#8211; State','62,964.85','0.5%','56,733.62','0.7%','(6,231.23)','&#8722;11.0%','neg'),
      ('Petty Cash / Misc Expenses','13,350.35','0.1%','11,326.04','0.1%','(2,024.31)','&#8722;17.9%','neg'),
      ('Rent Expense','659,209.36','5.7%','479,604.68','5.8%','(179,604.68)','&#8722;37.4%','neg'),
      ('Repairs &amp; Maintenance','4,254.00','0.0%','3,856.00','0.0%','(398.00)','&#8722;10.3%','neg'),
      ('Salaries &amp; Wages','1,167,899.69','10.1%','763,623.75','9.3%','(404,275.94)','&#8722;52.9%','neg'),
      ('Showroom Expense','49,938.69','0.4%','42,019.09','0.5%','(7,919.60)','&#8722;18.8%','neg'),
      ('Unsecured Property Tax &#8211; SF','475.25','0.0%','475.25','0.0%','&#8212;','&#8212;',''),
      ('Utilities &#8211; Electric','27,290.10','0.2%','21,016.35','0.3%','(6,273.75)','&#8722;29.9%','neg'),
      ('Utilities &#8211; Garbage','12,408.67','0.1%','9,220.60','0.1%','(3,188.07)','&#8722;34.6%','neg'),
      ('Utilities &#8211; Internet','3,312.60','0.0%','2,250.00','0.0%','(1,062.60)','&#8722;47.2%','neg'),
      ('Utilities &#8211; Security','1,050.00','0.0%','1,050.00','0.0%','&#8212;','&#8212;',''),
      ('Utilities &#8211; Telephone','11,332.64','0.1%','10,698.35','0.1%','(634.29)','&#8722;5.9%','neg'),
      ('Utilities &#8211; Water &amp; Sewer','4,224.71','0.0%','3,190.70','0.0%','(1,034.01)','&#8722;32.4%','neg'),
      ('Vehicle &#8211; Expense','11,940.58','0.1%','8,840.99','0.1%','(3,099.59)','&#8722;35.1%','neg'),
    ]
    for r in op_rows:
        def td(v,cls=''): return '<td' + (' class="'+cls+'"' if cls else '') + '>' + str(v) + '</td>'
        ct = r[7]
        c1 = 'neg' if ct == 'neg' else ('pos' if ct == 'pos' else '')
        c6 = 'neg' if '&#8722;' in r[5] else ('pos' if '+' in r[5] else '')
        c1 = c1 + (' pct' if c1 else 'pct')
        f.write('<tr>' + td(r[0]) + td(r[1],c1) + td(r[2],'pct') + td(r[3]) + td(r[4],'pct') + td(r[5],c6) + td(r[6],'pct') + '</tr>\n')
    def td(v,cls=''): return '<td' + (' class="'+cls+'"' if cls else '') + '>' + str(v) + '</td>'
    f.write('<tr class="rt"><td>TOTAL OPERATING EXPENSES</td><td>3,434,387.89</td><td class="pct">29.8%</td><td>2,103,504.84</td><td class="pct">25.5%</td><td class="neg">(1,330,883.05)</td><td class="pct">&#8722;63.3%</td></tr>\n')
    f.write('<tr class="blk"><td colspan="7"></td></tr>\n')
    f.write('<tr class="rg"><td>OPERATING INCOME (LOSS)</td><td class="neg">(88,759.80)</td><td class="pct">(0.8%)</td><td>617,528.59</td><td class="pct">6.1%</td><td class="neg">(706,288.39)</td><td class="pct">&#8722;114.4%</td></tr>\n')
    f.write('</tbody>\n</table>\n')
    
    # Other Income/Expense
    f.write('<div class="st">Other Income &amp; Expense</div><table>\n<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>\n<tbody>\n')
    def td(v,cls=''): return '<td' + (' class="'+cls+'"' if cls else '') + '>' + str(v) + '</td>'
    other = [
      ('Interest Income','33,126.19','0.3%','32,852.82','0.4%','273.37','+0.8%','pos'),
      ('Realized Capital Gains/Loss &#8211; Fidelity','&#8212;','0.0%','&#8212;','0.0%','&#8212;','&#8212;',''),
      ('Interest/Dividend Income &#8211; Fidelity','123,588.15','1.1%','95,937.71','1.2%','27,650.44','+28.8%','pos'),
    ]
    for r in other:
        ct = r[7]
        c1 = 'pos' if ct=='pos' else ('neg' if ct=='neg' else '')
        c6 = 'pos' if '+' in r[5] else ('neg' if '&#8722;' in r[5] else '')
        f.write('<tr>' + td(r[0]) + td(r[1],c1) + td(r[2],'pct') + td(r[3]) + td(r[4],'pct') + td(r[5],c6) + td(r[6],'pct') + '</tr>\n')
    f.write('<tr class="rs"><td>Total OTHER INCOME</td><td>156,714.34</td><td class="pct">1.4%</td><td>128,790.53</td><td class="pct">1.6%</td><td class="pos">27,923.81</td><td class="pct">+21.7%</td></tr>\n')
    f.write('<tr class="blk"><td colspan="7"></td></tr>\n')
    f.write('<tr><td>Gain/Loss on Currency Exchange</td><td>&#8212;</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>\n')
    f.write('<tr class="rs"><td>Total OTHER EXPENSE</td><td>&#8212;</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>\n')
    f.write('<tr class="blk"><td colspan="7"></td></tr>\n')
    f.write('<tr class="rg"><td>INCOME BEFORE INCOME TAX</td><td>67,954.54</td><td class="pct">0.6%</td><td>746,319.12</td><td class="pct">7.4%</td><td class="neg">(678,364.58)</td><td class="pct">&#8722;90.9%</td></tr>\n')
    f.write('<tr class="blk"><td colspan="7"></td></tr>\n')
    f.write('<tr><td>Federal Income Tax</td><td>857.55</td><td class="pct">0.0%</td><td>857.55</td><td class="pct">0.0%</td><td