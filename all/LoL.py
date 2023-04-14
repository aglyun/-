# _*_coding. utf-8_*_
# 开发时间：2021/3/9 14:47
# 加油！
import os
import requests
import jsonpath


class LoL(object):
    """ lol英雄资料爬取 """
    def __init__(self):
        print('---------- LoL英雄皮肤爬取 --------- \n')
        self.index_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'    # 首页

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        self.dirs = 'LoL皮肤'

    def get_url(self):
        """ 请求首页的url """
        r = requests.get(self.index_url, headers=self.headers).json()
        return r

    def filter_data(self, r):
        """ 过滤数据 """
        name = jsonpath.jsonpath(r, '$.hero[*].title')      # 英雄名称
        heroId = jsonpath.jsonpath(r, '$.hero[*].heroId')   # 英雄id
        num = 1    # 计数序号
        name_lb = []    # 展示序号
        hero_id = {}    # 序号和英雄id绑定
        self.hero_name = {}    # 序号和英雄名称绑定
        # 拼接列表，成为一个可选序号下载的方式
        for i in range(len(name)):
            name_lb.append(str(num)+'.'+name[i])
            hero_id[num] = heroId[i]
            self.hero_name[num] = name[i]

            num += 1
        print('共{}位英雄：'.format(len(name_lb)), name_lb)
        return hero_id

    def get_hero_id(self, hero_id, key):
        """
         通过英雄的id来获取相关的皮肤、资料
        :param hero_id: 英雄的绑定id
        :param key: 输入的序号
        """
        # 通过英雄id获取英雄资料
        hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(hero_id.get(key))
        r = requests.get(hero_url, headers=self.headers).json()
        return r

    def filter_skin(self, r):
        """ 过滤出皮肤、语音、信息 """
        banAudio = jsonpath.jsonpath(r, '$.hero.banAudio')   # 语音
        # 皮肤
        heroTitle = r.get('hero').get('title')  # 英雄名字
        mainImg = jsonpath.jsonpath(r, '$.skins[*].mainImg')        # 皮肤链接
        mainImg = [i for i in mainImg if i != '']                   # 过滤掉空列表
        skin_name = jsonpath.jsonpath(r, '$.skins[*].name')         # 皮肤名字
        skin_name = [skin_name[i] for i in range(len(mainImg))]     # 过滤掉不是皮肤名字的数据

        # 打包皮肤数据
        img_data = zip(skin_name, mainImg)
        return img_data

    def get_img(self, img_data, dir_path):
        """ 开始请求图片地址 """
        for i in img_data:
            r = requests.get(i[1], headers=self.headers).content
            # 调用下载器
            self.download(r, dir_path, i[0])

    def download(self, byte_data, dir_path, img_name):
        """
        :param byte_data: 接收一个二进制数据
        :dir_path: 接收一个下载地址
        :img_name: 接收一个图片的名称
        """
        with open(dir_path+'/{}.jpg'.format(img_name), 'wb') as f:
            f.write(byte_data)
            print('{}.jpg下载完成...'.format(img_name))

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
            dir_path = os.path.join(self.dirs,  self.hero_name.get(key))
            os.mkdir(dir_path)
            return dir_path
        except FileExistsError:
            return dir_path

    def run(self):
        r = self.get_url()
        
        hero_id = self.filter_data(r)
        key = int(input('输入序号爬取对应的英雄数据：'))
        r = self.get_hero_id(hero_id, key)
        img_data = self.filter_skin(r)    # 过滤皮肤数据
        dir_path = self.create_dirs(key)  # 创建保存数据的文件夹
        self.get_img(img_data, dir_path)


if __name__ == '__main__':
    l = LoL()
    l.run()