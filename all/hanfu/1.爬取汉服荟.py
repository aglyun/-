# _*_coding. utf-8_*_
# 开发时间：2021/3/4 20:37
# 加油！
import os

import requests
from lxml import etree
import json


class HanFuHui(object):
    """ 爬取汉服荟各个作者的详情页和图片
        注意：交流学习使用 造成的后果作者概不负责
    """
    def __init__(self):
        """ 初始化必要的条件 """
        self.url = 'https://www.hanfuhui.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        self.dirs = '汉服荟'
        self.author_name_all = []

    def get_index(self):
        """ 请求首页 """
        r = requests.get(self.url, headers=self.headers).text
        html = etree.HTML(r)
        # index_title = html.xpath('//div[@class="trend_text mt10"]/a/text()')  # 得到标题
        index_url = html.xpath('//div[@class="trend_box"]//a[@class="trend_pic mt10"]/@href')    # 得到详情页url
        author_name_all = html.xpath('//div[@class="userinfo"]/p/a/text()')    # 得到主页所有作者的名字
        new_url = [self.url+i for i in index_url]    # 拼接url
        num = 1
        for i in author_name_all:
            self.author_name_all.append(str(num)+'.'+i)
            num += 1

        return new_url

    def get_detail(self, new_url, all=True):
        """
        :param new_url: 详情页的url
        :param all: 是否开启全部下载，默认False
        :return: author_data, img_url, author_name
        """
        """ 对每个url进行请求，并且找到它的图片rul """
        if all:
            # 如果开启了True，将执行全部下载
            for i in new_url:
                # 对每条url进行请求
                r = requests.get(i, headers=self.headers).text
                # 返回数据
                author_data, img_url, author_name = self.filter_data(r)

                # 因为是反复循环，所以需要在这里执行
                dir_path = self.create_dirs(author_name)  # 创建文件夹
                self.save_image(img_url, dir_path, author_name, author_data)  # 保存图片和作者信息

        else:
            print(self.author_name_all)
            author_number = input('输入序号下载对应的作者数据(如：1)：')
            try:
                r = requests.get(new_url[int(author_number)-1], headers=self.headers).text
                author_data, img_url, author_name = self.filter_data(r)
                return author_data, img_url, author_name
            except Exception as e:
                print('输入的格式不正确')

    def filter_data(self, r):
        """ 过滤数据 """
        html = etree.HTML(r)
        img_url = html.xpath('//div[@class="details_left"]//div[@class="image"]//img/@src')
        title = html.xpath('//div[@class="details_info form_box"]/p/text()')    # 得到详情页标题(待过滤)
        content = html.xpath('//pre[@class="content"]/text()')    # 得到详情页的正文
        author_name = html.xpath('//div[@class="details_user form_box"]//a/text()')[0]   # 作者名称
        author_info = html.xpath('//div[@class="details_user form_box"]//a/@href')[0]    # 作者主页

        # 过滤数据，得到详情页的标题
        for i in range(1):
            # 过滤标题
            t1 = title[i].replace('\r\n', '')
            s1 = t1.replace(' ', '')
            # 过滤正文
            t2 = content[i].replace('\r\n', '')
            s2 = t2.replace(' ', '')
            author_data = {
                '作者名字': author_name,
                '作者主页': self.url + author_info,
                '标题': s1,
                '正文': s2
            }

        # 返回作者个人数据，详情页的图片url, 作者名称
        return author_data, img_url, author_name

    def create_dirs(self, author_name):
        """
        创建保存数据的文件夹
        :param author_name: 作者名称
        :return 返回保存数据的地址
        """
        # author_name = '作者：枭筱0o'
        try:
            os.mkdir(self.dirs)    # 创建主文件夹
        except FileExistsError:
            pass

        try:
            dir_path = os.path.join(self.dirs, '作者：'+ author_name)  # 拼接一个路径
            os.mkdir(dir_path)
            return dir_path
        except FileExistsError:
            return dir_path

    def save_image(self, img_url, dir_path, author_name, zd):
        """
        保存图片、数据
        :param img_url: 详情页的图片url
        :param dir_path: 保存图片的路径
        :param author_name: 作者名称
        :param zd: 拼接好的作者数据
        """
        num = 1
        for i in img_url:
            r = requests.get(i, headers=self.headers).content
            with open('%s/%s_%s.jpg' % (dir_path, num, author_name), 'wb') as f:
                f.write(r)
                print('%s_%s.jpg保存成功...' %(num, author_name))
            num += 1

        # 将作者有关的信息用一个文件存储
        with open('%s/%s.json' % (dir_path, author_name), 'w', encoding='utf=8') as f:
            data = json.dumps(zd, ensure_ascii=False)
            f.write(data)
            print('作者个人数据保存完毕...')

    def control_download(self, t_f):
        """ 控制下载方式 """
        if t_f == '0':
            return True
        return False

    def run(self):
        """ 执行程序 """
        t_f = input('开始全部下载(0)还是单条下载(1)？(输入0或者1):')
        all = self.control_download(str(t_f))
        if all:
            # 多条下载知悉
            new_url = self.get_index()    # 请求首页
            self.get_detail(new_url, all=True)
        else:
            # 单条下载执行
            new_url = self.get_index()    # 请求首页
            author_data, img_url, author_name = self.get_detail(new_url, all=False)
            print(img_url)

            dir_path = self.create_dirs(author_name)   # 创建文件夹
            self.save_image(img_url, dir_path, author_name, author_data)    # 保存图片和作者信息


if __name__ == '__main__':
    h = HanFuHui()
    h.run()


