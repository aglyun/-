# _*_coding. utf-8_*_
# 开发时间：2021/3/9 17:20
# 加油！
import os

import requests
import jsonpath
from lxml import etree


class Wzry(object):
    """ 爬取王者荣耀皮肤 """
    def __init__(self):
        print('----------王者荣耀皮肤下载器----------\n')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        self.dirs = '王者荣耀皮肤'

    def get_api(self):
        """ 请求api """
        api_url = 'https://pvp.qq.com/web201605/js/herolist.json'
        r = requests.get(api_url, headers=self.headers).json()
        return r

    def filter_data(self, r):
        """ 过滤数据 """
        id = jsonpath.jsonpath(r, '$..ename')                   # 英雄id
        self.hero_name = jsonpath.jsonpath(r, '$..cname')            # 英雄名称
        num = 1    # 计数
        num_name = []    # 序号和英雄名字
        num_id = {}      # 序号和英雄id
        for i in self.hero_name:
            num_name.append(str(num)+'.'+i)
            num_id[num] = id[num-1]            # 序号绑定id
            num += 1

        return num_name, num_id

    def get_hero_info(self, hero_id, skin_num):
        """ 英雄主页 """
        # hero_id 是一个字典
        id = hero_id.get(skin_num)
        info_url = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(id)
        r = requests.get(info_url, headers=self.headers)
        r.encoding='gbk'    # 转换编码

        # 过滤数据，取出皮肤名字
        html = etree.HTML(r.text)
        skin_name = html.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')

        skin_name = [i.split('|') for i in skin_name]
        skin_name = [i.split('&') for i in skin_name[0]]
        skin_lb = []    # 存储过滤好的皮肤名称
        for i in skin_name:
            skin_lb.append(i[0])

        return skin_lb

    def get_img_path(self, skin_lb, id_dict, num_id, dir_name):
        """
        请求皮肤地址
        :param skin_lb: 皮肤列表
        :param id_dict: 英雄id的字典数
        :param num_id:  输入的序号
        """
        hero_id = id_dict.get(num_id)
        print('找到以下皮肤：', skin_lb)
        for i in range(len(skin_lb)):
            img_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(hero_id, hero_id, i+1)
            r = requests.get(img_url, headers=self.headers).content
            self.download(r, dir_name, i ,skin_lb)

    def download(self, byte_data, dir_path, num_id, skin_lb):
        """
        :param byte_data: 接收一个二进制数据
        :dir_path: 接收一个下载地址
        :num_id: 输入的序号
        :skin_lb: 皮肤列表
        """
        with open(dir_path + '/{}.jpg'.format(skin_lb[num_id]), 'wb') as f:
            f.write(byte_data)
            print('{}.jpg下载完成...'.format(skin_lb[num_id]))

    def create_dirs(self, key):
        """
        创建文件夹 存储图片
        :param key: 英雄的序号
        :return:
        """
        try:
            os.mkdir(self.dirs)  # 创建主文件夹
        except FileExistsError:
            pass
        try:
            # 拼接英雄路径
            dir_path = os.path.join(self.dirs, self.hero_name[key-1])
            os.mkdir(dir_path)
            return dir_path
        except FileExistsError:
            return dir_path

    def run(self):
        r = self.get_api()
        name, id_zd = self.filter_data(r)
        print(name)
        skin_num = int(input('输入序号下载对应的皮肤：'))
        dir_name = self.create_dirs(skin_num)
        skin_lb = self.get_hero_info(id_zd,skin_num)
        self.get_img_path(skin_lb, id_zd, skin_num, dir_name)


if __name__ == '__main__':
    w = Wzry()
    w.run()

