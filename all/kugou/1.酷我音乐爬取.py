# _*_coding. utf-8_*_
# 开发时间：2021/3/8 8:12
# 加油！
import time
import requests
import jsonpath
import urllib.parse
import json


class KuWo(object):
    """ 爬取酷狗 如果运行不了请更改self.headers 中的Cookie信息，因为Cookie信息会过期 """
    def __init__(self, single=True):
        print('---------- 酷我音乐爬取 --------- [已开启 %s 模式下载]\n' % ('单条' if single else '多条'))
        self.name = str(input('输入歌曲名称：'))
        self.search_url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1&reqId=2f0fb4b0-7fc7-11eb-8c20-ab9258d5c042'.format(self.name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'http://www.kuwo.cn/search/list?key={}'.format(urllib.parse.quote(self.name)),
            'csrf': 'NOBRQVH1DXQ',
            'Cookie': '_ga=GA1.2.866934884.1615161845; _gid=GA1.2.534992817.1615161845; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1615161845; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1615162780; kw_token=NOBRQVH1DXQ'
        }
        self.single = single

    def get_url(self):
        """ 请求搜索的url """
        r = requests.get(self.search_url, headers=self.headers).text
        data = json.loads(r)
        music_count = data.get('data').get('total')
        print('找到%s首歌，计%s页，每页有30首' % (music_count,round(int(music_count)/30)))

        page = int(input('输入跳转的页数'))
        url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&httpsStatus=1&reqId=2f0fb4b0-7fc7-11eb-8c20-ab9258d5c042'.format(self.name, page)
        r = requests.get(url, headers=self.headers).text
        data = json.loads(r)
        # 得到的数据是 {'code': 200, 'curTime': 1615167727786, 'data': {'total': '1599', 'list': [*]...
        self.filter_data(data)     # 调用过滤器

    def filter_data(self, r):
        """
        过滤数据, 过滤歌名，歌手，歌曲rid标识
        :param r: 请求返回的响应数据
        :return:
        """
        music_name = jsonpath.jsonpath(r, '$.data.list[*].name')        # 歌名
        music_singer = jsonpath.jsonpath(r, '$.data.list[*].artist')    # 歌手
        music_rid = jsonpath.jsonpath(r, '$.data.list[*].rid')          # 歌曲的rid标识

        music_name_singer = zip(music_name, music_singer)

        # 全局歌曲名称，方便调用
        m = [i for i in zip(music_singer, music_name)]
        self.global_music_name = [i[0]+'-'+i[1] for i in m]

        num = 1
        self.new_n_singer = []
        for i, k in music_name_singer:
            s = str(num) +'.'+k+'-'+i
            self.new_n_singer.append(s)
            num += 1
        print('找到以下歌曲(%s首)：' %len(self.new_n_singer), self.new_n_singer)
        if self.single:
            # 判断是否开启了单条下载
            self.number = int(input('输入序号下载对应的歌曲：'))-1
        music_data = zip(self.new_n_singer, music_rid)   # 打包数据，格式变成('牛奶@咖啡-明天，你好', '', 1065516)

        # 拼接mp3地址，是页面地址，并非mp3的下载地址
        mp3_path_url_lb = []

        for i in music_data:
            mp3_url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1615166289374&httpsStatus=1&reqId=24d196f0-7fac-11eb-976d-a91cc979a82b'.format(i[1])
            mp3_path_url_lb.append(mp3_url)
        print('地址拼接完毕：', mp3_path_url_lb)

        self.get_mp3_rid(mp3_path_url_lb)    # 调用请求音乐rid页面的方法

    def get_mp3_rid(self, mp3_path_url_lb):
        """
        通过rid来进行音乐地址的请求
        :param mp3_path_url_lb: 接受一个mp3的真实地址列表
        :return:
        """
        if self.single:
            # 如果是单条下载，则执行些代码
            r = requests.get(mp3_path_url_lb[self.number], headers=self.headers).text
            data = json.loads(r)
            mp3_path = data.get('url')
            print('单条数据取到的MP3真实地址', mp3_path)
            self.get_mp3_path(mp3_path)
        else:
            # 全部请求地址，列表用于添加到下载地址，用于下载
            download_url_lb = []
            for k in mp3_path_url_lb:
                r = requests.get(k, headers=self.headers).text
                data = json.loads(r)
                # 提取mp3地址并且添加到列表中
                download_url_lb.append(jsonpath.jsonpath(data, '$.url')[0])
            # 调用请求mp3真实地址的方法
            self.get_mp3_path(download_url_lb)

    def get_mp3_path(self, download_url_lb):
        """
        请求音乐的真实地址
        :param download_url: 用于接受一个mp3的下载地址列表
        :param flag: 判断标志
        :return:
        """
        if self.single:
            # 判断是否开启了单条下载
            r = requests.get(download_url_lb).content
            # # 调用下载器
            self.download(r, self.global_music_name[self.number])
        else:
            num = 0
            for i in download_url_lb:
                r = requests.get(i, headers=self.headers).content
                self.download(r, self.global_music_name[num-1])    # 调用下载器，用num作为下标取值
                num += 1

    def download(self, byte_data, music_name):
        """ 下载 """
        try:
            with open('{}.mp3'.format(music_name), 'wb') as f:
                f.write(byte_data)
                print('[{}]下载完成...'.format(music_name))
        except OSError as e:
            print(e)

    def __del__(self):
        print('结束', time.strftime('%X'))

    def run(self):
        print('开始', time.strftime('%X'))
        self.get_url()


if __name__ == '__main__':
    kw = KuWo(single=False)
    kw.run()