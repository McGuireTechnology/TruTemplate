#!/usr/bin/env python3
import subprocess
import shutil
import os

# Get list of staged .md files at the root
result = subprocess.run([
    'git', 'diff', '--cached', '--name-only', '--diff-filter=ACM'
], capture_output=True, text=True)
staged_files = [f for f in result.stdout.strip().split('\n') if f.endswith('.md') and '/' not in f]

for filename in staged_files:
    src = os.path.join(os.getcwd(), filename)
    dst = os.path.join(os.getcwd(), 'docs', filename)
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print(f'Copied {filename} to docs/{filename}')
        # Add the copied file to the stage
        subprocess.run(['git', 'add', f'docs/{filename}'])
