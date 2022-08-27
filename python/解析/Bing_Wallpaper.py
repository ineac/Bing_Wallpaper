
import json
import jsonpath
import urllib.request
import time
import ctypes
import os

    
def get_content():
    urllib.request.urlretrieve(url,'D:/IDM download/images/'+ name +'.json')

def down_load():

    jsonname = 'D:/IDM download/images/'+ name +'.json'

    obj = json.load(open(jsonname,'r',encoding='utf-8'))
    # print(obj)
    src = jsonpath.jsonpath(obj,'$.images[*].url')
    

    url = 'https://cn.bing.com/'+ src[0]
    print(url)

    filename = 'D:/IDM download/images/'+ name + '.jpg'
    print(filename)
    urllib.request.urlretrieve(url=url,filename=str(filename))

    if os.path.exists(jsonname):
        os.remove(jsonname)
    else:
        print("文件不存在")

    return filename

if __name__ == '__main__':
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    name = time.strftime("%Y%m%d",time.localtime())

    # 1.下载 json 文件
    get_content()

    # 2.下载 图片
    filename = down_load()
    # 3. 设置为桌面壁纸
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filename , 0)
