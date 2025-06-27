import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def define_env(env):
    from scripts.push_root_docs import copy_root_markdown_to_docs
    from scripts.update_license_year import update_license_year_main
    copy_root_markdown_to_docs()
    update_license_year_main()
