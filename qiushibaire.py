import requests
import re
import os
import _thread

url = 'https://www.qiushibaike.com/imgrank/'
photo_path = os.path.abspath(os.path.dirname(__file__)) + '/photo/'
if not os.path.exists(photo_path):
    os.makedirs(photo_path)
response = requests.get(url)
rps = response.text
html_url = re.findall(r'//\w+.*medium.*\.jpg',rps)

def get_image(html_url):
    global data
    jpg_url = 'http:%s' %html_url
    response = requests.get(jpg_url)
    with open(photo_path + jpg_url.split('/')[-1],'wb') as f:
        f.write(response.content)
        print(jpg_url.split('/')[-1] + '图片下载完成')

for i in html_url:
    _thread.start_new_thread(get_image,(i,))


input('press Enter to exit...\n')
