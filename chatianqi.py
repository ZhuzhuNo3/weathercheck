import requests
def tianqi(city):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s'% city
    req = requests.get(url)
    if req.status_code == 200:
        data = req.text
        dic_city = req.json()
    else:
        print('查询失败')
    return dic_city

dic = tianqi(input())
if dic['status'] == 1000:
    tq = dic['data']['forecast'][0]
    print('%s当前天气为"%s"--"%s",%s'%(
        dic['data']['city'],tq['high'],tq['low'],tq['type']))
else:
    print('无该城市')

