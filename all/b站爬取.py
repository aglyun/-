# _*_coding. utf-8_*_
# 开发时间：2021/3/10 18:38
# 加油！
import os
import re
import requests
from lxml import etree


class Bili(object):
    """ b站爬取  合并视频序号ffmpeg，或者注释58行代码 self.ffmpeg(v_title)，注释后视频和音频是两个文件 """
    def __init__(self):
        print('----------BiliBili视频下载器----------\n')
        name = input('输入视频名称')
        self.search_url = 'https://search.bilibili.com/all?keyword={}'.format(name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'https://www.bilibili.com/video/BV1pt411G7k1?from=search'
        }
        self.dirs = '视频'
        try:
            os.mkdir(self.dirs)
        except Exception as e:
            print(e)

    def get_url(self):
        """ 请求搜索的首页 """
        r = requests.get(self.search_url, headers=self.headers)
        return r.text

    def get_video_url(self, video_info):
        #  请求视频主页
        # 循环请求
        for i in range(len(video_info)):
            r = requests.get(video_info[i], headers=self.headers)
            # 调用过滤器，过滤出音频和视频、视频标题
            self.filter_video_info(r.text)

    def filter_video_info(self, r):
        # 过滤视频主页
        title = etree.HTML(r).xpath('//div[@id="viewbox_report"]/h1/@title')    # 找到视频的标题
        video = etree.HTML(r).xpath('//script[contains(text(), "window.__playinfo__")]/text()')    # 在scrpt中找到了视频的链接
        # 使用re找出视频链接
        mp4 = re.findall(r'baseUrl":"(.*?)"', video[0])[0]    # 用括号括起来是分组数据
        mp3 = re.findall(r'"audio":\[\{"id":\d+,"baseUrl":"(.*?)"', video[0])[0]    # 得到mp3地址

        # 请求资源地址开始
        self.get_mp3_mp4(mp4, mp3, title[0])

    def get_mp3_mp4(self, mp4, mp3, v_title):
        """ 开始请求视频的地址和音频的地址 """
        r1 = requests.get(mp4, headers=self.headers).content
        self.download(r1, v_title, '.mp4')
        r2 = requests.get(mp3, headers=self.headers).content
        self.download(r2, v_title, '.mp3')

        # 下载完毕后，合并文件
        self.ffmpeg(v_title)

    def filter_data(self, r):
        html = etree.HTML(r)    # 对响应进行解析
        video_name = html.xpath('//li[@class="video-item matrix"]/a/@href')    # 得到视频名称
        # 视频主页
        video_info = ['https:'+i for i in video_name]
        print(video_info)

        return video_info

    def download(self, byte_data, v_title, f_type):
        """
        :param byte_data: 二进制数据
        :param v_title:   视频名称
        :param f_type:    文件的格式
        """
        print(v_title+f_type)
        with open('视频/{}{}'.format(v_title, f_type), 'wb') as f:
            f.write(byte_data)

    def ffmpeg(self, v_title):
        """ 合并视频 """
        os.system('ffmpeg -i 视频/{}.mp3 -i 视频/{}.mp4 -c copy 视频/{}_ok.mp4 -loglevel quiet'.format(v_title, v_title, v_title))
        # 删除源文件
        os.remove('视频/{}.mp4'.format(v_title))
        os.remove('视频/{}.mp3'.format(v_title))
        print('{}.mp4保存成功...'.format(v_title))

    def run(self):
        r = self.get_url()
        video_info = self.filter_data(r)
        self.get_video_url(video_info)


if __name__ == '__main__':
    b = Bili()
    b.run()