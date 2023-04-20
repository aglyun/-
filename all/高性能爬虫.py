import requests
from threading import Thread
from random import randint


url = "http://itmooc.tech/263.html"


def f(s):
    number = randint(100000, 999999)    # 随机验证码
    # 构造请求数据
    data = {
        'secret_key': number,
        'Submit': '阅读全文',
    }
    # 请求100ci
    for i in range(100):
        requests.post(url, data=data)
        print('{}号线程：随机验证码：{}'.format(s, number))


# 创建20个线程
for i in range(1, 5):
    t = Thread(target=f, args=[i])
    t.start()   # 启动
