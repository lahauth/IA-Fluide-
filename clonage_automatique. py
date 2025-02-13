"""
Module de Clonage Automatique - Protection contre la suppression et altération du framework
"""

import shutil
import os

def detect_modification(repo_path):
    if not os.path.exists(repo_path):
        clone_repository(repo_path)

def clone_repository(repo_path):
    clone_path = repo_path + "_clone"
    shutil.copytree(repo_path, clone_path)
    print(f"Clonage effectué : {clone_path}")