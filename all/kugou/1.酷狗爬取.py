# _*_coding. utf-8_*_
# 开发时间：2021/3/7 16:15
# 加油！
import json
import time

import requests
import re
import jsonpath


class KuGou(object):
    """ 酷狗音乐爬取，以手机端为例子 """
    def __init__(self, single=False):
        """ 初始化必要的条件 """
        print('---------- 酷狗音乐爬取 --------- [已开启 %s 模式下载]\n'% ('单条' if single else '多条'))
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
        self.single = single    # 是否开启单条下载，默认不开启

    def get_url(self):
        """ 请求搜索的url """
        r = requests.get(self.url, headers=self.headers).text
        return r

    def get_mp3_hash(self, mp3_hash):
        """ 请求MP3 hash的url """
        if self.single:
            # 开启单条下载
            print('找到以下歌曲(%s首)：' % len(self.select_filename), self.select_filename)
            self.num = int(input('输入序号下载对应的歌曲：'))
            mp3_hash = mp3_hash[self.num-1]
            mp3_url = 'http://m.kugou.com/api/v1/song/get_song_info?cmd=playInfo&hash=%s&from=mkugou&apiver=2&mid=ea508c5dea03f9e42ae0b43db34fc25e&userid=0&platid=4&dfid=3399X52DX9G83YHx0n1DNZWs' % mp3_hash
            r = requests.get(mp3_url, headers=self.m_headers).text
            d = json.loads(r)
            mp3_single_url = d.get('url')
            return mp3_single_url    # 返回单条地址

        # 下面是开启多条下载时才执行
        mp3_path_lb = []  # 用于储存音乐的真实地址
        print('找到以下歌曲(%s首)：'% len(self.select_filename), self.select_filename)
        # y_n = str(input('确认继续?(y/n)'))
        # if y_n != 'y':
        #     return 0
        for i in mp3_hash:
            mp3_url = 'http://m.kugou.com/api/v1/song/get_song_info?cmd=playInfo&hash=%s&from=mkugou&apiver=2&mid=ea508c5dea03f9e42ae0b43db34fc25e&userid=0&platid=4&dfid=3399X52DX9G83YHx0n1DNZWs' % i
            r = requests.get(mp3_url, headers=self.m_headers).text
            d = json.loads(r)
            mp3_path_lb.append(d.get('url'))
        print('[%s]歌曲所有音乐地址' % self.music_name, mp3_path_lb)
        return mp3_path_lb

    def get_mp3_url(self, mp3_path_url):
        """ 请求mp3真实地址 """
        if self.single:
            r = requests.get(mp3_path_url, headers=self.m_headers).content
            self.download(r, self.num-1)  # 调用下载器
            return 0    # 结束该方法

        num = 0
        for i in mp3_path_url:
            r = requests.get(i, headers=self.m_headers).content
            self.download(r, num)    # 调用下载器
            num += 1

    def download(self, byte_data, num):
        """ 下载 """
        try:
            # path = 'F:\\Desktop\\KuGouMusic\\'
            with open('%s.mp3' % self.filename[num], 'wb') as f:
                f.write(byte_data)
                print('[%s]下载成功...' % self.filename[num])
        except OSError as e:
            print(e)

    def filter_data(self, data):
        """ 过滤数据 """
        fin = re.findall(r'\{.*\}', data)[0]
        d = json.loads(fin)

        filename = jsonpath.jsonpath(d, '$.data.info[*].filename')
        mp3_hash = jsonpath.jsonpath(d, '$.data.info[*].hash')
        self.filename = filename
        self.select_filename = []
        num = 0    # 拼装成有序号的名字
        for i in filename:
            self.select_filename.append(str(num+1)+'.'+ i)
            num += 1
        return mp3_hash

    def __del__(self):
        print('结束:', time.strftime('%X'))

    def run(self):
        print('开始', time.strftime('%X'))
        data = self.get_url()
        mp3_hash = self.filter_data(data)
        mp3_path_lb = self.get_mp3_hash(mp3_hash)
        if mp3_path_lb != 0:
            self.get_mp3_url(mp3_path_lb)
        print('程序已终止')


if __name__ == '__main__':
    k = KuGou(single=False)
    k.run()
