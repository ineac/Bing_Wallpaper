# Bing_Wallpaper
python 获取当日必应壁纸并自动设置为桌面壁纸

## 思路
url：http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1

将url中的 json 文件下载下来，获取其中当前壁纸的后部分url（前部分url为：www.bing.com），在images下的url中。

将 前部分url 和 后部分url 拼接起来，组成完整的url

使用 urllib 将图片下载下来（下载下来的图片文件名为当前日期.jpg）


