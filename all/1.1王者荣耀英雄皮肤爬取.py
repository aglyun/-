# coding:utf-8
import re, os
import requests
import random


class WxryIamge:
    def __init__(self):
        # 英雄主页url
        self.index_url = "https://pvp.qq.com/web201605/herolist.shtml"
        # 拼接url
        self.join_url = "https://pvp.qq.com/web201605/"

        # 构造请求求头
        self.headers = [
             "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
             "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
             "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
        ]
        # 随机请求头
        self.new_headers = {'User-Agent': random.choice(self.headers)}
        # 询问输入英雄名字
        self.hero_input_name = str(input('输入英雄的名字:(如：小乔、李白)'))

    def get_index(self):
        """ 请求英雄列表主页 """
        r = requests.get(self.index_url, headers=self.new_headers)
        data = r.content.decode('gbk')
        # 过滤英雄名字
        hero_skin_names = re.compile(r'alt=".*"')
        # hero_skin_name2 用来拼接成字典的key
        hero_skin_names2 = hero_skin_names.findall(data)


        # 过滤英雄皮肤主页
        com = re.compile(r'herodetail/.*\.shtml')
        hero_url = com.findall(data)
        # 进行迭代过滤
        # self.hero_skin_url 用来拼接成字典的value
        self.hero_skin_url = []    # 英雄皮肤链接
        for i in hero_url[0:93]:
            name_url = self.join_url+i
            self.hero_skin_url.append(name_url)

        zd = {}    # 空字典，用于存储英雄的名字(key)和皮肤链接(value)
        i = 0
        while i < len(hero_skin_names2[0:93]):
            a = hero_skin_names2[i]
            b = self.hero_skin_url[i]
            # 组合英雄名字和皮肤链接
            zd[a] = b
            i += 1
        # 拼接名字
        s = 'alt="%s"' % self.hero_input_name
        # 判断输入的英雄名字是否存在列表中
        if s in zd.keys():
            print('ok')
            self.get_hero_skin_name(zd.get(s))
            self.save_img(zd.get(s))    # 保存图片函数

        else:
            print('没有找到该英雄的皮肤')

    def get_hero_skin_name(self, url):
        """ 请求英雄皮肤的名字"""
        # 进行皮肤名字过滤
        r = requests.get(url, headers=self.new_headers)    # 随机请求头这里容易出问题
        data = r.content.decode('gbk')

        # 对皮肤名字进行过滤
        com = re.compile(r'imgname.*&')
        hero_skin_name = com.findall(data)
        try:
            # 二次过滤
            name1 = [i.split('imgname="') for i in hero_skin_name]
            name2 = [i.split('|') for i in name1[0]]
            name3 = [i.split('&') for i in name2[1]]
            name_len = len(name3)
            # 对皮肤数量进行计算
            self.skin_num = name_len
            # 对皮肤名字进行拼接
            self.skin_name = []
            for i in range(name_len):
                # print('%s.%s_%s.jpg 保存中...' % (i+1,name3[i][0] ,self.hero_input_name))
                self.skin_name.append( '%s.%s_%s.jpg' % (i+1,name3[i][0] ,self.hero_input_name))
        except Exception as e:
            print(e)
            print('获取皮肤名称出错啦')


    def save_img(self, url):
        """ 保存英雄皮肤图片 """
        r = requests.get(url, headers=self.new_headers)
        data = r.content.decode('gbk')
        # 进行图片过滤

        img_list = []    # 图片url列表
        folder_name = self.hero_input_name  # 文件夹名字

        for i in range(self.skin_num):
            img = re.compile(r'//game\.gtimg\.cn/images/yxzj/img201606/skin/hero-info/.*-bigskin-')
            img_url = img.findall(data)
            # 拼接图片url
            img_url = "https:%s%s.jpg" % (img_url[0], i+1)
            img_list.append(img_url)

        # 将图片进行下载
        # 创建分类目录
        try:
            path = os.path.abspath('.')
            os.mkdir(path+"/王者荣耀皮肤/%s" % folder_name)
        except Exception:
            pass
        flag = 0 # 标记
        for i in img_list:
            r = requests.get(i, headers=self.new_headers)
            img_data = r.content
            with open('王者荣耀皮肤/%s/%s' % (folder_name, self.skin_name[flag]), 'wb') as f:
                    f.write(img_data)

            print("正在下载...", self.skin_name[flag])
            flag += 1


if __name__ == '__main__':
    w = WxryIamge()
    w.get_index()



