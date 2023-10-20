import subprocess

from project.path_get import path_get
from project.whiteCheck import check
import webbrowser
import time


if __name__ == '__main__':
    print('PyCharm')
    file_path = path_get()
    print(file_path)
    while 1:
        if check():
            webbrowser.open("https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default")
            time.sleep(1)
            webbrowser.open("https://ys.mihoyo.com/main/")
            try:
                subprocess.Popen([file_path], shell=True)
            except Exception as e:
                print(f"无法启动应用程序: {e}")
            break
