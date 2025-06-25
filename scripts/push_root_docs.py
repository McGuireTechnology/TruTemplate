#!/usr/bin/env python3
import shutil
import os


# Get all .md files at the root
root_dir = os.getcwd()
all_files = os.listdir(root_dir)
root_md_files = [f for f in all_files if f.endswith(".md") and os.path.isfile(f)]

for filename in root_md_files:
    src = os.path.join(root_dir, filename)
    dst = os.path.join(root_dir, "docs", filename)
    if os.path.exists(dst):
        src_mtime = os.path.getmtime(src)
        dst_mtime = os.path.getmtime(dst)
        # Only copy if the root file is newer than the docs file
        if src_mtime > dst_mtime:
            shutil.copyfile(src, dst)
            print(f"Copied {filename} to docs/{filename}")
    else:
        shutil.copyfile(src, dst)
        print(f"Copied {filename} to docs/{filename}")
