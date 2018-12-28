import requests
import re
import os
import _thread

def get_image(threadName):
    url = 'https://www.qiushibaike.com/imgrank/'

    photo_path = os.path.abspath(os.path.dirname(__file__)) + '/photo/'
    response = requests.get(url)
    rps = response.text
    html_url = re.findall(r'//\w+.*medium.*\.jpg',rps)
    for index,jpg in enumerate(html_url[:10]):
        url_jpg = 'https:' + jpg
        response = requests .get(url_jpg)
        with open(photo_path + 'image'+ str(index+1) + '.jpg','wb') as file:
            print('%s: 正在下载图片...' % threadName)
            for data in response.iter_content(128):
                file.write(data)
try:
    _thread.start_new_thread(get_image, ('Thread-1',))
    _thread.start_new_thread(get_image, ('Thread-2',))
except:
    print("Error: unable to start thread")

input('press Enter to exit...\n')
