#!/usr/bin/env python3
import subprocess
import os
import sys

html_file = "/workspace/fengshui_final_report.html"
css_file = "/workspace/font_override.css"
pdf_file = "/workspace/fengshui_final_report.pdf"
font_file = "/workspace/NotoSansCJKtc-Regular.otf"

# Check font exists
if os.path.exists(font_file):
    size = os.path.getsize(font_file)
    print(f"Font file found: {size} bytes")
else:
    print("ERROR: Font file not found!")
    sys.exit(1)

# Check HTML exists
if os.path.exists(html_file):
    size = os.path.getsize(html_file)
    print(f"HTML file found: {size} bytes")
else:
    print("ERROR: HTML file not found!")
    sys.exit(1)

# Run WeasyPrint
print("Running WeasyPrint...")
result = subprocess.run([
    '/app/.venv/bin/weasyprint',
    '--stylesheet', css_file,
    html_file,
    pdf_file
], capture_output=True, text=True, timeout=120)

print("STDOUT:", result.stdout[:2000] if result.stdout else "(empty)")
print("STDERR:", result.stderr[:2000] if result.stderr else "(empty)")
print("Return code:", result.returncode)

# Check PDF
if os.path.exists(pdf_file):
    pdf_size = os.path.getsize(pdf_file)
    print(f"PDF created: {pdf_size} bytes ({pdf_size/1024:.1f} KB)")
    if pdf_size > 100*1024:
        print("SUCCESS: PDF is larger than 100KB!")
    else:
        print("WARNING: PDF is smaller than 100KB, may be empty/blank")
else:
    print("ERROR: PDF was not created")
