# _*_coding. utf-8_*_
# 开发时间：2021/3/7 21:25
# 加油！
import json
import time

import requests
import re
import jsonpath
import threading


class KuGou(object):
    """ 酷狗音乐爬取，以手机端为例子 """
    def __init__(self):
        """ 初始化必要的条件 """
        print('---------- 酷狗音乐爬取 --------- ')
        self.music_name = input('请输入音乐名称(默认展示100首歌，可以自行更改数量，官方最大数量200首每页)：')
        # 开始的url，可以更改pagesize参数
        self.url = 'http://mobilecdn.kugou.com/api/v3/search/song?format=jsonp&keyword=%s&page=0&pagesize=100&showtype=1&callback=kgJSONP613683248' % self.music_name

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            # 'Referer': 'http://m.kugou.com/search/index',
        }
        self.m_headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Referer': 'http://m.kugou.com/search/index',
        }

    def get_url(self):
        """ 请求搜索的url """
        r = requests.get(self.url, headers=self.headers).text
        return r

    def get_mp3_hash(self, mp3_hash):
        """ 请求MP3 hash的url """
        mp3_path_lb = []  # 用于储存音乐的真实地址
        mp3_name = []     # 用于存储音乐的名字
        print('找到以下歌曲(%s首)：'% len(self.select_filename), self.select_filename)
        for i in mp3_hash:
            mp3_name.append(i[0])    # 将名称添加到列表
            mp3_url = 'http://m.kugou.com/api/v1/song/get_song_info?cmd=playInfo&hash=%s&from=mkugou&apiver=2&mid=ea508c5dea03f9e42ae0b43db34fc25e&userid=0&platid=4&dfid=3399X52DX9G83YHx0n1DNZWs' % i[1]
            r = requests.get(mp3_url, headers=self.m_headers).text
            d = json.loads(r)
            mp3_path_lb.append(d.get('url'))
        print('[%s]歌曲所有音乐地址' % self.music_name, mp3_path_lb)
        print('名称', mp3_name)
        # 打包数据，丢给get_mp3_url方法进行请求
        mp3_name_path_lb = zip(mp3_name, mp3_path_lb)
        self.get_mp3_url(mp3_name_path_lb)    # 调用请求mp3地址的方法,此时它得到的数据包是(歌名,mp3地址)

    def get_mp3_url(self, mp3_name_path_lb):
        """ 请求mp3真实地址 """
        # for遍历打包的数据，i[0]歌名，i[1]是地址
        for i in mp3_name_path_lb:    # 上一个方法传来了链接，没有名字
            r = requests.get(i[1], headers=self.m_headers).content
            self.download(r, i[0])    # 调用下载器

    def download(self, byte_data, filename):
        """ 下载 """
        try:
            # path = 'F:\\Desktop\\KuGouMusic\\'
            with open('%s.mp3' % filename, 'wb') as f:
                f.write(byte_data)
                print('[%s]下载成功...' % filename)
        except OSError as e:
            print(e)

    def filter_data(self, data):
        """ 过滤数据 """
        fin = re.findall(r'\{.*\}', data)[0]
        d = json.loads(fin)

        filename = jsonpath.jsonpath(d, '$.data.info[*].filename')
        mp3_hash = jsonpath.jsonpath(d, '$.data.info[*].hash')
        self.select_filename = []
        self.mp3_file_hash = mp3_hash
        num = 0    # 拼装成有序号的名字
        for i in filename:
            self.select_filename.append(str(num+1)+'.'+ i)
            num += 1
        name_hash = zip(filename, mp3_hash)
        name_hash_lb = []
        for i in name_hash:
            name_hash_lb.append(i)
        return name_hash_lb

    def thread_number(self, hash_lb):
        """ 控制多线程，默认开启2个，最高5个 """
        lb_len = len(hash_lb)
        try:
            t = input('请输入线程数量：(最高5条，输入其他数默认使用两条)')
            th = lb_len / int(t)  # 线程控制 2
        except Exception:
            print('线程错误，将使用默认两条线程...')
            t = 2
            th = lb_len / int(t)  # 线程控制 2
        print('你使用的是：%s条线程执行程序...' % t)
        print('正在分配任务...')
        self.t1 = hash_lb[:int(th)]             # 线程1
        self.t2 = hash_lb[:int(th * 2)]         # 线程2
        self.t2 = self.t2[int(th):]  # 截取
        print('t1', self.t1)
        print('t2', self.t2)

        self.t3 = hash_lb[:int(th * 3)]          # 线程3
        self.t3 = self.t3[int(th * 2):]  # 截取
        print('t3', self.t3)

        self.t4 = hash_lb[:int(th * 4)]          # 线程4
        self.t4 = self.t4[int(th * 3):]  # 截取
        print('t4', self.t4)

        self.t0 = hash_lb[:int(th * 5)]          # 线程5
        self.t0 = self.t0[int(th * 4):]
        print('t0', self.t0)
        print('任务分配完毕，开始执行...')
        return t, self.t1, self.t2, self.t3, self.t4, self.t0

    def __del__(self):
        print('结束:', time.strftime('%X'))

    def run(self):
        data = self.get_url()
        mp3_hash = self.filter_data(data)
        print(mp3_hash)

        t, *ts = self.thread_number(mp3_hash)
        print('---------')
        url_lb = [i for i in ts if i != []]
        print(url_lb)

        # 创建目标
        print('开始', time.strftime('%X'))
        for i in range(int(t)):
            threading.Thread(target=self.get_mp3_hash, args=[url_lb[i]]).start()


if __name__ == '__main__':
    k = KuGou()
    k.run()
