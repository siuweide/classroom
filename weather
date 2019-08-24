import requests
import json

def weather():
    while True:
        city_name = input("请输入你要查询的城市，按回车退出。")
        try:
            if city_name:
                req = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city_name)
                json_data = json.loads(req.text)
                # print(json_data)
                city = json_data["data"]["city"]
                date = json_data["data"]["forecast"][0]["date"]
                high = json_data["data"]["forecast"][0]["high"]
                low = json_data["data"]["forecast"][0]["low"]
                type = json_data["data"]["forecast"][0]["type"]
                print("%s，%s的天气是%s，最%s，最%s" %(date,city,type,high,low))
            else:
                break
        except:
            print("你输入的城市名称有误，请重新输入！")
    print('已成功退出！')
weather()
