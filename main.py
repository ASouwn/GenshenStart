from whiteCheck import check
from PIL import Image
import webbrowser
import time

if __name__ == '__main__':
    print('PyCharm')
    while 1:
        if check() == 'true':
            # img = Image.open('原神启动.png')
            # img.show()

            webbrowser.open("https://www.yuanshen.com/#/")
            # wait a while, and then go to another page
            time.sleep(1)
            webbrowser.open("https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default")
            break
