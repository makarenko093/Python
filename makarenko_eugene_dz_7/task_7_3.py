import os
import shutil

copy_path = os.path.join('my_project', 'templates')
path = os.path.abspath(os.path.join('my_project'))
for paths, dirs, files in os.walk(path):
    if paths.split('\\')[-1] == 'templates':
        shutil.copytree(paths, copy_path, dirs_exist_ok=True)

