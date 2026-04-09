#!/usr/bin/env python3
import subprocess, os, sys

html_file = "/workspace/yerba_buena_fengshui_full.html"
pdf_file  = "/workspace/yerba_buena_fengshui.pdf"
css_file  = "/workspace/font_override.css"

print(f"HTML size: {os.path.getsize(html_file)} bytes")

result = subprocess.run([
    '/app/.venv/bin/weasyprint',
    '--stylesheet', css_file,
    html_file, pdf_file
], capture_output=True, text=True, timeout=180)

print("STDOUT:", result.stdout[:1000] if result.stdout else "(empty)")
print("STDERR:", result.stderr[:2000] if result.stderr else "(empty)")
print("Return code:", result.returncode)

if os.path.exists(pdf_file):
    sz = os.path.getsize(pdf_file)
    print(f"PDF: {sz} bytes ({sz/1024:.0f} KB)")
else:
    print("ERROR: PDF not created")
