#!/usr/bin/env python3
"""打包本地版：eraser/橡皮擦合成-本地版.zip
解压得到「橡皮擦合成」文件夹：index.html + vendor/ag-psd.js + 说明.txt，双击 index.html 即可使用。
发布前运行一次：python3 build_offline.py
"""
import pathlib, re, zipfile
root = pathlib.Path(__file__).parent
eraser = root / "eraser"
html = (eraser / "index.html").read_text(encoding="utf-8")
# the local copy must not offer the download link again (the version stamp stays)
html, n = re.subn(r'<a href="橡皮擦合成-本地版\.zip"[^>]*>本地版</a>', '', html)
assert n == 1, "download link not found"
ver = re.search(r'<a id="ver"[^>]*>(v\d{6})</a>', html)
assert ver, "version stamp not found"
out = eraser / "橡皮擦合成-本地版.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("橡皮擦合成/index.html", html)
    z.write(eraser / "vendor" / "ag-psd.js", "橡皮擦合成/vendor/ag-psd.js")
    z.write(root / "本地版说明.txt", "橡皮擦合成/说明.txt")
    z.write(root / "LICENSE.md", "橡皮擦合成/LICENSE.md")
print(f"wrote {out.name} ({ver.group(1)}): {out.stat().st_size/1e6:.2f} MB")
