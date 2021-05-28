#!/usr/bin/python3
# coding=UTF-8

import shutil
import os
import datetime
import time


def get_datetime():
    return datetime.date.today()


try:
    with open("C:\\Users\\Dennis\\backupfile.txt", "r",
              encoding="UTF-8") as file_path:
        # 取得當下時間，timestamp
        right_date = get_datetime()
        for path in file_path:
            # 切換目錄
            os.chdir(path)
            # 撈目錄底下的檔案們
            file_list = os.listdir()
            # 每個檔案取得mtime，與當下時間比較
            for file in file_list:
                file_date = datetime.date.fromisoformat(
                    time.strftime('%Y-%m-%d',
                                  time.localtime(os.path.getmtime(file))))                
                if (right_date - file_date).days == 0:
                    print("The same date")

                # 3天以外刪除

except OSError as e:
    print("Error: %s-%s." % (e.FileNotFoundError, e.OSError))

if __name__ == "__main__":
    get_datetime()