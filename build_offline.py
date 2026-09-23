#!/usr/bin/env python3
"""打包本地版：eraser/无损改图-本地版.zip
解压得到「无损改图」文件夹：index.html + vendor/ag-psd.js + 说明.txt，双击 index.html 即可使用。
发布前运行一次：python3 build_offline.py
"""
import pathlib, re, zipfile
root = pathlib.Path(__file__).parent
eraser = root / "eraser"
html = (eraser / "index.html").read_text(encoding="utf-8")
# the local copy must not offer the download link again (the version stamp stays)
html, n = re.subn(r'<a href="无损改图-本地版\.zip"[^>]*>本地版</a>', '', html)
assert n == 1, "download link not found"
ver = re.search(r'<a id="ver"[^>]*>(v\d{6}[a-z]?)</a>', html)
assert ver, "version stamp not found"
out = eraser / "无损改图-本地版.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("无损改图/index.html", html)
    z.write(eraser / "vendor" / "ag-psd.js", "无损改图/vendor/ag-psd.js")
    z.write(root / "本地版说明.txt", "无损改图/说明.txt")
    z.write(root / "LICENSE.md", "无损改图/LICENSE.md")
print(f"wrote {out.name} ({ver.group(1)}): {out.stat().st_size/1e6:.2f} MB")
