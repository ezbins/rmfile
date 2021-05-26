#!/usr/bin/python3
# coding=utf-8

import shutil
import os

try:
    paths = open("/data2/backupfile.txt","r")
    for path in paths.read():
        os.chdir(path) # 切換目錄
        os.listdir()#撈目錄底下的檔案們
        #比對要刪除的檔名

except OSError as e:
    print("Error: %s-%s."  %(e.FileNotFoundError,e.OSError))


