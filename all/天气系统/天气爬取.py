import requests
from bs4 import BeautifulSoup


def get_search(city):
    """ 搜索页面 """
    a = "http://toy1.weather.com.cn/search?cityname={}".format(city)
    r = requests.get(a)
    r.encoding = 'utf-8'
    # 过滤括号,通过json转成python数据
    data = r.text
    start = data.find(":")
    end = data.find("~")
    ids = data[start+2: end]
    print(ids)
    # 返回id
    return ids

def get_index(ids=101280800):
    a = "http://www.weather.com.cn/weather1d/{}.shtml#input".format(ids)
    r = requests.get(a)
    r.encoding = 'utf-8'
    s = BeautifulSoup(r.text, 'lxml')
    li = s.select('.hover')[0]
    a1 = "http://www.weather.com.cn"
    qitian = a1 + li.select('a')[0].get('href')   # 获取到七天的数据
    # 过滤今天的
    return qitian   # 返回超链接

def get_qitian(city):
    ids = get_search(city)
    url = get_index(ids)  # 得到超链接
    r = requests.get(url)
    r.encoding = 'utf-8'
    # 过滤数据
    s = BeautifulSoup(r.text, 'lxml')
    ul = s.select('.c7d')[0]
    ul = ul.select('li')

    data = []  # 存储天气数据
    for i in ul[0:7]:
        h1 = i.select('h1')[0].get_text()   # 日期
        wea = i.select('.wea')[0].get('title')    # 天气
        tem = i.select('.tem')[0].get_text()  # 温度
        ji = i.select('i')[1].get_text()  # 级别
        data.append([h1, wea, tem, ji])
    return data   # 一定要返回数据




get_search('佛山')








