#!/usr/bin/python3
# coding=UTF-8

import os
import re
import datetime
import time
import fnmatch


def get_datetime():
    return datetime.date.today()


def get_removeday():
    with open("/home/administrator/day.txt", "r", encoding="UTF-8") as days:
        day = int(days.read().strip())
        return day


try:
    with open("/home/administrator/backupfile.txt", "r",
              encoding="UTF-8") as file_path:
        # 取得當下時間，timestamp
        right_date = get_datetime()
        for path in file_path:
            patten = re.compile("^/")
            if patten.match(path):
                # 切換目錄
                os.chdir(path.strip())
                # 撈目錄底下的檔案們
                file_list = os.listdir()
                # 每個檔案取得mtime，與當下時間比較
                for file in file_list:
                    if fnmatch.fnmatch(file, "*.bz2"):
                        file_date = datetime.date.fromisoformat(
                            time.strftime(
                                '%Y-%m-%d',
                                time.localtime(os.path.getmtime(file))))
                        if (right_date - file_date).days >= get_removeday():
                            os.remove(file)
                            print("rm down")

except OSError as e:
    print("Error: %s-%s." % (e.FileNotFoundError, e.OSError))

if __name__ == "__main__":
    get_datetime()
    get_removeday()
