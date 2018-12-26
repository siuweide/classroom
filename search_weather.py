import requests

while True:
    city = input('请输入你要查询的城市；输入q退出查询\n')
    if city != 'q':
        try:
            url = ('http://wthrcdn.etouch.cn/weather_mini?city=%s' %city)
            response = requests.get(url)
            result = response.json()
            print(result)
            print(city+result['data']['ganmao'])
            print('今日%s空气质量：%s' % (city,result['data']['aqi']))
            print('今日%s温度%s' %(city,result['data']['forecast'][0]))
        except:
            print('你输入的城市名有误，请重新输入！')
    elif city == 'q':
        print('退出查询')
        break
