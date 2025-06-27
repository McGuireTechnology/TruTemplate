#!/usr/bin/env python3
import shutil
import os
import re


def copy_root_markdown_to_docs(*args, **kwargs):
    root_dir = os.getcwd()
    docs_dir = os.path.join(root_dir, "docs")
    all_files = os.listdir(root_dir)
    root_md_files = [f for f in all_files if f.endswith(".md") and os.path.isfile(f)]
    notice = (
        "<!--\n    NOTE: This file is auto-copied from the repository root.\n"
        "    Please edit the original in the root directory, not in docs/.\n--->\n\n"
    )
    for filename in root_md_files:
        src = os.path.join(root_dir, filename)
        dst = os.path.join(docs_dir, filename)
        with open(src, "r", encoding="utf-8") as f:
            content = f.read()
        # Prepend notice if not already present
        new_content = content
        if not content.lstrip().startswith("<!--"):
            new_content = notice + content
        else:
            # If a previous notice exists, replace it
            new_content = re.sub(r"^<!--.*?-->", notice.strip(), content, count=1, flags=re.DOTALL) + "\n" + "\n".join(content.splitlines()[1:])
        # Only write if content has changed
        write_file = True
        if os.path.exists(dst):
            with open(dst, "r", encoding="utf-8") as f:
                existing_content = f.read()
            if existing_content == new_content:
                write_file = False
        if write_file:
            with open(dst, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Copied {filename} to docs/{filename} with edit notice")


# For manual script execution
if __name__ == "__main__":
    copy_root_markdown_to_docs()
