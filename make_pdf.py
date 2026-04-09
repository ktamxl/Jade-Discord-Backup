#!/usr/bin/env python3
import subprocess, os

# Write HTML file
html = open('/workspace/build_fin_stmt.py').read()
# Extract just the HTML part (remove the python code if any)
# Actually, build_fin_stmt.py has the HTML as a Python string variable
# Let's write the HTML directly

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'IBM Plex Sans', Arial, sans-serif; font-size: 11px; color: #1a1a2e; background: #fff; }
.header { background: linear-gradient(135deg,#1a3a52 0%,#0d2137 100%); color: #fff; padding: 28px 48px 22px; display: flex; justify-content: space-between; align-items: flex-end; }
.header h1 { font-size: 20px; font-weight: 700; }
.header .subtitle { font-size: 12px; color: #8ab4d4; margin-top: 4px; }
.header-right { text-align: right; }
.header-right .lbl { font-size: 9px; color: #6a9bbf; text-transform: uppercase; letter-spacing: 1px; }
.header-right .val { font-size: 14px; font-weight: 600; color: #fff; margin-top: 2px; }
.summary-bar { display: grid; grid-template-columns: repeat(4,1fr); border-bottom: 3px solid #1a3a52; }
.s-cell { padding: 18px 24px; border-right: 1px solid #e8edf2; background: #f7fafc; }
.s-cell:last-child { border-right: none; }
.s-cell .s-label { font-size: 9px; text-transform: uppercase; letter-spacing: 1.2px; color: #7a8fa8; margin-bottom: 5px; }
.s-cell .s-value { font-size: 20px; font-weight: 700; }
.s-cell .s-sub { font-size: 9px; color: #aab8c4; margin-top: 2px; }
.content { padding: 28px 48px; }
.sec-title { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: #fff; background: #1a3a52; padding: 8px 16px; margin-top: 22px; border-radius: 2px; }
table { width: 100%; border-collapse: collapse; font-size: 11px; }
thead th { background: #e8edf2; color: #3a5270; font-weight: 600; font-size: 9.5px; text-transform: uppercase; letter-spacing: 0.8px; padding: 8px 12px; text-align: right; border-bottom: 2px solid #c0cfde; }
thead th:first-child { text-align: left; }
tbody tr { border-bottom: 1px solid #eef2f6; }
tbody td { padding: 6px 12px; text-align: right; font-family: 'IBM Plex Mono',monospace; font-size: 11px; }
tbody td:first-child { text-align: left; font-family: 'IBM Plex Sans',sans-serif; font-size: 11px; }
td.pct { color: #7a8fa8; font-size: 9.5px; font-family: 'IBM Plex Mono',monospace; }
td.pos { color: #0a7c5c; }
td.neg { color: #c0392b; }
.i1 td:first-child { padding-left: 26px; }
.row-sub td { background: #eaf2fb !important; border-top: 1px solid #c0d4e8; border-bottom: 1px solid #c0d4e8; font-weight: 600; }
.row-tot td { background: #1a3a52 !important; color: #fff !important; font-weight: 700; font-size: 12px; padding: 9px 12px; border-top: 2px solid #0d2137; border-bottom: 2px solid #0d2137; }
.row-tot td:first-child { color: #fff !important; }
.row-gtot td { background: #0d2137 !important; color: #ffd700 !important; font-weight: 700; font-size: 13px; padding: 10px 12px; border-top: 3px solid #ffd700; }
.row-gtot td:first-child { color: #ffd700 !important; }
.blank td { height: 8px; border: none; background: #fff; }
.spacer-row td { border: none; height: 6px; background: #fff; }
.footer { padding: 14px 48px; border-top: 1px solid #e0e8f0; display: flex; justify-content: space-between; font-size: 9px; color: #9ab0c0; }
.footer .co { font-weight: 600; color: #6a8aab; }
</style>
</head>
<body>
<div class="header">
  <div><h1>EXCEL PLUMBING SUPPLY + SHOWROOM</h1><div class="subtitle">Branches: 1 &nbsp;|&nbsp; YTD Financial Statement &#8212; January 1 through March 31, 2026</div></div>
  <div class="header-right"><div class="lbl">As of Date</div><div class="val">March 31, 2026</div><div style="margin-top:6px"><div class="lbl">Printed</div><div class="val" style="font-size:11px">April 2, 2026</div></div></div>
</div>
<div class="summary-bar">
  <div class="s-cell"><div class="s-label">Net Sales (YTD)</div><div class="s-value" style="color:#1a3a52">$11,518,991</div><div class="s-sub">+13.6% vs Prior Year</div></div>
  <div class="s-cell"><div class="s-label">Gross Profit (YTD)</div><div class="s-value" style="color:#0a7c5c">$3,345,628</div><div class="s-sub">29.0% Gross Margin</div></div>
  <div class="s-cell"><div class="s-label">Operating Income (YTD)</div><div class="s-value" style="color:#c0392b">($88,760)</div><div class="s-sub">&#8722;0.8% of Sales</div></div>
  <div class="s-cell"><div class="s-label">Net Income (YTD)</div><div class="s-value" style="color:#0a7c5c">$67,097</div><div class="s-sub">+0.6% of Sales</div></div>
</div>
<div class="content">
<div class="sec-title">Net Sales</div>
<table>
<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>
<tbody>
<tr><td>Sales &#8211; Counter</td><td>1,258,972.83</td><td class="pct">10.9%</td><td>846,046.45</td><td class="pct">8.3%</td><td class="pos">412,926.38</td><td class="pct">+48.8%</td></tr>
<tr><td>Sales &#8211; Showroom</td><td>9,306,949.52</td><td class="pct">80.8%</td><td>7,101,395.83</td><td class="pct">70.0%</td><td class="pos">2,205,553.69</td><td class="pct">+31.1%</td></tr>
<tr><td>Sales &#8211; Direct</td><td>131,674.65</td><td class="pct">1.1%</td><td>607,385.30</td><td class="pct">6.0%</td><td class="neg">(475,710.65)</td><td class="pct">&#8722;78.3%</td></tr>
<tr><td>Sales &#8211; Inside</td><td>1,116,266.22</td><td class="pct">9.7%</td><td>1,840,425.37</td><td class="pct">18.2%</td><td class="neg">(724,159.15)</td><td class="pct">&#8722;39.3%</td></tr>
<tr><td>Sales &#8211; Returns</td><td class="neg">(390,023.66)</td><td class="pct">(3.4%)</td><td class="neg">(326,451.10)</td><td class="pct">(3.2%)</td><td class="neg">(63,572.56)</td><td class="pct">&#8722;19.5%</td></tr>
<tr class="i1"><td>Freight &amp; Delivery Rebate</td><td>59,826.55</td><td class="pct">0.5%</td><td>47,803.23</td><td class="pct">0.5%</td><td class="pos">12,023.32</td><td class="pct">+25.2%</td></tr>
<tr class="i1"><td>Tax Rebate / Promotion</td><td class="neg">(30.00)</td><td class="pct">(0.0%)</td><td class="neg">(721.90)</td><td class="pct">(0.0%)</td><td class="pos">691.90</td><td class="pct">+95.8%</td></tr>
<tr class="i1"><td>Delivery Charge</td><td>23,706.54</td><td class="pct">0.2%</td><td>16,551.31</td><td class="pct">0.2%</td><td class="pos">7,155.23</td><td class="pct">+43.2%</td></tr>
<tr class="i1"><td>Restocking Charge</td><td>11,648.02</td><td class="pct">0.1%</td><td>7,412.90</td><td class="pct">0.1%</td><td class="pos">4,235.12</td><td class="pct">+57.1%</td></tr>
<tr class="row-tot"><td>NET SALES</td><td>11,518,990.67</td><td class="pct">100.0%</td><td>10,139,847.39</td><td class="pct">100.0%</td><td>1,379,143.28</td><td class="pct">+13.6%</td></tr>
</tbody>
</table>
<div class="sec-title">Cost of Goods Sold</div>
<table>
<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>
<tbody>
<tr><td>Cost of Goods Sold &#8211; Counter</td><td>909,154.20</td><td class="pct">7.9%</td><td>685,209.22</td><td class="pct">8.3%</td><td class="neg">(223,944.98)</td><td class="pct">&#8722;32.7%</td></tr>
<tr><td>Cost of Goods Sold &#8211; Showroom</td><td>6,699,426.47</td><td class="pct">58.2%</td><td>4,828,116.76</td><td class="pct">58.6%</td><td class="neg">(1,871,309.71)</td><td class="pct">&#8722;38.8%</td></tr>
<tr><td>Cost of Goods Sold &#8211; Direct</td><td>96,444.64</td><td class="pct">0.8%</td><td>34,738.88</td><td class="pct">0.4%</td><td class="neg">(61,705.76)</td><td class="pct">&#8722;177.6%</td></tr>
<tr><td>Cost of Goods Sold &#8211; Inside</td><td>1,015,858.42</td><td class="pct">8.8%</td><td>617,163.55</td><td class="pct">7.5%</td><td class="neg">(398,694.87)</td><td class="pct">&#8722;64.6%</td></tr>
<tr><td>Cost of Goods Sold &#8211; Returns</td><td class="neg">(242,240.86)</td><td class="pct">(2.1%)</td><td class="neg">(182,103.95)</td><td class="pct">(2.2%)</td><td class="neg">(60,136.91)</td><td class="pct">&#8722;33.0%</td></tr>
<tr><td>Freight In and Out</td><td>266.58</td><td class="pct">0.0%</td><td>314.14</td><td class="pct">0.0%</td><td class="neg">(47.56)</td><td class="pct">&#8722;15.1%</td></tr>
<tr class="row-sub"><td>Total Cost of Product Sold</td><td>8,478,909.45</td><td class="pct">73.6%</td><td>7,551,066.09</td><td class="pct">74.5%</td><td>927,843.36</td><td class="pct">+12.3%</td></tr>
<tr class="spacer-row"><td colspan="7"></td></tr>
<tr><td>Purchases</td><td>8,271,272.58</td><td class="pct">71.8%</td><td>7,434,161.85</td><td class="pct">73.3%</td><td class="neg">(837,110.73)</td><td class="pct">&#8722;11.3%</td></tr>
<tr class="i1"><td>Clear Purchases to Inventory</td><td class="neg">(8,271,272.58)</td><td class="pct">(71.8%)</td><td class="neg">(7,434,161.85)</td><td class="pct">(73.3%)</td><td class="neg">(837,110.73)</td><td class="pct">&#8722;11.3%</td></tr>
<tr><td>Comm-Cost / COGS Difference</td><td class="neg">(15,106.34)</td><td class="pct">(0.1%)</td><td class="neg">(4,457.61)</td><td class="pct">(0.1%)</td><td class="neg">(10,648.73)</td><td class="pct">&#8722;238.9%</td></tr>
<tr><td>Clear Comm-Cost Difference to P&amp;L</td><td>15,106.34</td><td class="pct">0.1%</td><td>4,457.61</td><td class="pct">0.1%</td><td class="pos">10,648.73</td><td class="pct">+238.9%</td></tr>
<tr><td>Purchase Discounts Taken</td><td class="neg">(130,743.52)</td><td class="pct">(1.1%)</td><td class="neg">(89,734.33)</td><td class="pct">(1.1%)</td><td class="neg">(41,009.19)</td><td class="pct">&#8722;45.7%</td></tr>
<tr><td>Vendor Rebates / Promotion</td><td class="neg">(175,946.07)</td><td class="pct">(1.5%)</td><td class="neg">(144,665.82)</td><td class="pct">(1.8%)</td><td class="neg">(31,280.25)</td><td class="pct">&#8722;21.6%</td></tr>
<tr><td>Freight In &#8211; Vendor</td><td>57,906.94</td><td class="pct">0.5%</td><td>40,070.13</td><td class="pct">0.5%</td><td class="neg">(17,836.81)</td><td class="pct">&#8722;44.5%</td></tr>
<tr><td>Inventory Adjustments</td><td class="neg">(67,954.34)</td><td class="pct">(0.6%)</td><td class="neg">(65,324.77)</td><td class="pct">(0.8%)</td><td class="neg">(2,629.57)</td><td class="pct">&#8722;4.0%</td></tr>
<tr><td>Vendor Defect Allowance</td><td class="neg">(12,676.07)</td><td class="pct">(0.1%)</td><td class="neg">(8,702.23)</td><td class="pct">(0.1%)</td><td class="neg">(3,973.84)</td><td class="pct">&#8722;45.7%</td></tr>
<tr><td>Restocking Charge &#8211; Vendor</td><td>3,717.79</td><td class="pct">0.0%</td><td>2,236.26</td><td class="pct">0.0%</td><td class="pos">1,481.53</td><td class="pct">+66.2%</td></tr>
<tr><td>Sales Discounts Given</td><td class="neg">(20,338.33)</td><td class="pct">(0.2%)</td><td class="neg">(14,219.00)</td><td class="pct">(0.2%)</td><td class="neg">(6,119.33)</td><td class="pct">&#8722;43.0%</td></tr>
<tr class="row-sub"><td>Total Other Cost of Goods Sold</td><td class="neg">(305,546.87)</td><td class="pct">(2.7%)</td><td class="neg">(252,022.14)</td><td class="pct">(3.1%)</td><td class="neg">(53,524.73)</td><td class="pct">&#8722;21.2%</td></tr>
<tr class="blank"><td colspan="7"></td></tr>
<tr class="row-tot"><td>TOTAL COST OF GOODS SOLD</td><td>8,173,362.58</td><td class="pct">71.0%</td><td>7,418,813.96</td><td class="pct">73.2%</td><td>754,548.62</td><td class="pct">+10.2%</td></tr>
<tr class="blank"><td colspan="7"></td></tr>
<tr class="row-gtot"><td>GROSS PROFIT</td><td>3,345,628.09</td><td class="pct">29.0%</td><td>2,721,033.43</td><td class="pct">26.8%</td><td class="pos">624,594.66</td><td class="pct">+23.0%</td></tr>
</tbody>
</table>
<div class="sec-title">Operating Expenses</div>
<table>
<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025</th><th class="pct">%</th><th>$ Change</th><th class="pct">% Chg</th></tr></thead>
<tbody>
<tr><td>Accounts Payable Over / Short</td><td class="neg">(0.09)</td><td class="pct">(0.0%)</td><td class="neg">(2.55)</td><td class="pct">(0.0%)</td><td class="pos">2.46</td><td class="pct">+96.5%</td></tr>
<tr><td>Advertising &amp; Promotion</td><td>32,000.21</td><td class="pct">0.3%</td><td>19,769.03</td><td class="pct">0.2%</td><td class="neg">(12,231.18)</td><td class="pct">&#8722;61.9%</td></tr>
<tr><td>Bank Charges</td><td>25.00</td><td class="pct">0.0%</td><td>25.00</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>
<tr><td>Business Tax &#8211; San Francisco</td><td>19,610.50</td><td class="pct">0.2%</td><td>8,452.00</td><td class="pct">0.1%</td><td class="neg">(11,158.50)</td><td class="pct">&#8722;132.0%</td></tr>
<tr><td>Computer &#8211; Website Maintenance</td><td>99.99</td><td class="pct">0.0%</td><td>99.99</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>
<tr><td>Computer &#8211; Software Support</td><td>32,902.07</td><td class="pct">0.3%</td><td>23,480.96</td><td class="pct">0.3%</td><td class="neg">(9,421.11)</td><td class="pct">&#8722;40.1%</td></tr>
<tr><td>Contributions</td><td>1,035.00</td><td class="pct">0.0%</td><td>535.00</td><td class="pct">0.0%</td><td class="neg">(500.00)</td><td class="pct">&#8722;93.5%</td></tr>
<tr><td>Credit Card Processing</td><td>225,090.36</td><td class="pct">2.0%</td><td>149,528.09</td><td class="pct">1.8%</td><td class="neg">(75,562.27)</td><td class="pct">&#8722;50.5%</td></tr>
<tr><td>Dues &amp; Subscriptions</td><td>27,559.36</td><td class="pct">0.2%</td><td>18,999.93</td><td class="pct">0.2%</td><td class="neg">(8,559.43)</td><td class="pct">&#8722;45.1%</td></tr>
<tr><td>Employee Benefits</td><td>15,063.94</td><td class="pct">0.1%</td><td>11,489.29</td><td class="pct">0.1%</td><td class="neg">(3,574.65)</td><td class="pct">&#8722;31.1%</td></tr>
<tr><td>Freight &amp; Delivery</td><td>8,286.34</td><td class="pct">0.1%</td><td>6,804.94</td><td class="pct">0.1%</td><td class="neg">(1,481.40)</td><td class="pct">&#8722;21.8%</td></tr>
<tr><td>Insurance &#8211; Medical &amp; Dental</td><td>197,806.92</td><td class="pct">1.7%</td><td>148,691.69</td><td class="pct">1.8%</td><td class="neg">(49,115.23)</td><td class="pct">&#8722;33.0%</td></tr>
<tr><td>Insurance &#8211; Property &amp; Casualty</td><td>26,918.40</td><td class="pct">0.2%</td><td>22,653.08</td><td class="pct">0.3%</td><td class="neg">(4,265.32)</td><td class="pct">&#8722;18.8%</td></tr>
<tr><td>Insurance &#8211; Vehicles</td><td>9,190.91</td><td class="pct">0.1%</td><td>2,657.35</td><td class="pct">0.0%</td><td class="neg">(6,533.56)</td><td class="pct">&#8722;245.9%</td></tr>
<tr><td>Insurance &#8211; Workers&#8217; Compensation</td><td>21,785.45</td><td class="pct">0.2%</td><td>19,395.32</td><td class="pct">0.2%</td><td class="neg">(2,390.13)</td><td class="pct">&#8722;12.3%</td></tr>
<tr><td>Legal &amp; Professional Expense</td><td>1,237.50</td><td class="pct">0.0%</td><td>1,237.50</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>
<tr><td>Licenses &amp; Fees</td><td>1,405.00</td><td class="pct">0.0%</td><td>1,405.00</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>
<tr><td>Office Supplies &amp; Expense</td><td>5,618.43</td><td class="pct">0.0%</td><td>4,966.62</td><td class="pct">0.1%</td><td class="neg">(651.81)</td><td class="pct">&#8722;13.1%</td></tr>
<tr><td>Payroll Taxes &#8211; Federal</td><td>779,101.11</td><td class="pct">6.8%</td><td>249,411.18</td><td class="pct">3.0%</td><td class="neg">(529,689.93)</td><td class="pct">&#8722;212.4%</td></tr>
<tr><td>Payroll Taxes &#8211; State</td><td>62,964.85</td><td class="pct">0.5%</td><td>56,733.62</td><td class="pct">0.7%</td><td class="neg">(6,231.23)</td><td class="pct">&#8722;11.0%</td></tr>
<tr><td>Petty Cash / Misc Expenses</td><td>13,350.35</td><td class="pct">0.1%</td><td>11,326.04</td><td class="pct">0.1%</td><td class="neg">(2,024.31)</td><td class="pct">&#8722;17.9%</td></tr>
<tr><td>Rent Expense</td><td>659,209.36</td><td class="pct">5.7%</td><td>479,604.68</td><td class="pct">5.8%</td><td class="neg">(179,604.68)</td><td class="pct">&#8722;37.4%</td></tr>
<tr><td>Repairs &amp; Maintenance</td><td>4,254.00</td><td class="pct">0.0%</td><td>3,856.00</td><td class="pct">0.0%</td><td class="neg">(398.00)</td><td class="pct">&#8722;10.3%</td></tr>
<tr><td>Salaries &amp; Wages</td><td>1,167,899.69</td><td class="pct">10.1%</td><td>763,623.75</td><td class="pct">9.3%</td><td class="neg">(404,275.94)</td><td class="pct">&#8722;52.9%</td></tr>
<tr><td>Showroom Expense</td><td>49,938.69</td><td class="pct">0.4%</td><td>42,019.09</td><td class="pct">0.5%</td><td class="neg">(7,919.60)</td><td class="pct">&#8722;18.8%</td></tr>
<tr><td>Unsecured Property Tax &#8211; SF</td><td>475.25</td><td class="pct">0.0%</td><td>475.25</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>
<tr><td>Utilities &#8211; Electric</td><td>27,290.10</td><td class="pct">0.2%</td><td>21,016.35</td><td class="pct">0.3%</td><td class="neg">(6,273.75)</td><td class="pct">&#8722;29.9%</td></tr>
<tr><td>Utilities &#8211; Garbage</td><td>12,408.67</td><td class="pct">0.1%</td><td>9,220.60</td><td class="pct">0.1%</td><td class="neg">(3,188.07)</td><td class="pct">&#8722;34.6%</td></tr>
<tr><td>Utilities &#8211; Internet</td><td>3,312.60</td><td class="pct">0.0%</td><td>2,250.00</td><td class="pct">0.0%</td><td class="neg">(1,062.60)</td><td class="pct">&#8722;47.2%</td></tr>
<tr><td>Utilities &#8211; Security</td><td>1,050.00</td><td class="pct">0.0%</td><td>1,050.00</td><td class="pct">0.0%</td><td>&#8212;</td><td class="pct">&#8212;</td></tr>
<tr><td>Utilities &#8211; Telephone</td><td>11,332.64</td><td class="pct">0.1%</td><td>10,698.35</td><td class="pct">0.1%</td><td class="neg">(634.29)</td><td class="pct">&#8722;5.9%</td></tr>
<tr><td>Utilities &#8211; Water &amp; Sewer</td><td>4,224.71</td><td class="pct">0.0%</td><td>3,190.70</td><td class="pct">0.0%</td><td class="neg">(1,034.01)</td><td class="pct">&#8722;32.4%</td></tr>
<tr><td>Vehicle &#8211; Expense</td><td>11,940.58</td><td class="pct">0.1%</td><td>8,840.99</td><td class="pct">0.1%</td><td class="neg">(3,099.59)</td><td class="pct">&#8722;35.1%</td></tr>
<tr class="row-tot"><td>TOTAL OPERATING EXPENSES</td><td>3,434,387.89</td><td class="pct">29.8%</td><td>2,103,504.84</td><td class="pct">25.5%</td><td class="neg">(1,330,883.05)</td><td class="pct">&#8722;63.3%</td></tr>
<tr class="blank"><td colspan="7"></td></tr>
<tr class="row-gtot"><td>OPERATING INCOME (LOSS)</td><td class="neg">(88,759.80)</td><td class="pct">(0.8%)</td><td>617,528.59</td><td class="pct">6.1%</td><td class="neg">(706,288.39)</td><td class="pct">&#8722;114.4%</td></tr>
</tbody>
</table>
<div class="sec-title">Other Income &amp; Expense</div>
<table>
<thead><tr><th>Account</th><th>YTD 2026</th><th class="pct">%</th><th>YTD 2025