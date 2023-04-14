# _*_coding. utf-8_*_
# 开发时间：2021/3/5 15:01
# 加油！
import time

import requests
import json
import threading


class HanFuHuiAPI(object):
    """ 汉服荟api的爬取 """
    def __init__(self):
        """  初始化必要的数据时 """
        self.top_f = open('汉服荟总数据.json', 'w', encoding='utf-8')
        self.url_lb = []
        self.num = input('输入爬取的数量：(共603页，每一页20条数据)')
        for i in range(1, int(self.num)+1):
            url = "https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=0&objecttype=album&page=%s&count=20" % i
            self.url_lb.append(url)

        self.headers = {
                'origin': 'https://www.hanfuhui.com',
                'referer': 'https://www.hanfuhui.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        self.s = '_700x.jpg'    # 拼接图片

    def get_api(self, url, s=None):
        """
        开始请求api接口
        :param url: 传入url
        """
        for i in url:
            r = requests.get(i, headers=self.headers).text
            zd = json.loads(r)    # json数据格式转换
            # 调用过滤方法
            self.filter_data(zd)

    def filter_data(self, zd):
        """ 过滤数据 """
        data = zd.get('Data')
        for i in range(len(data)):
            author_data = data[i]
            # 作者名称
            name = author_data.get('User').get('NickName')
            # 性别
            gender = author_data.get('User').get('Gender')
            # 签名
            describe = author_data.get('User').get('Describe')
            # 正文
            content = author_data.get('Content')
            # 详情页
            id = author_data.get('ID')
            # 作者主页
            info = author_data.get('User').get('UserName')
            # 作者头像
            head_img = author_data.get('User').get('HeadUrl')
            # 得到图片链接
            img = author_data.get('ImageSrcs')
            img_url = [i + self.s for i in img]
            self.package_data(name, gender, describe, content, id, info, head_img, img_url)

    def package_data(self, name, gender, describe, content, id, info, head_img, img_url):
        """ 封装数据 """
        data = {
            '姓名': name,
            '性别': gender,
            '签名': describe,
            '正文': content,
            '详情页': 'https://www.hanfuhui.com/Details/%s' % id,
            '作者主页': 'https://www.hanfuhui.com/u/%s' % info,
            '作者头像': head_img + self.s,
            '作品图片': img_url
                }

        # 保存到总文件
        self.top_f.write(json.dumps(data, ensure_ascii=False)+'\n')
        return data

    def thread_number(self):
        """ 控制多线程，默认开启2个，最高5个 """
        lb_len = len(self.url_lb)
        try:
            t = input('请输入线程数量：(最高5条，输入其他数默认使用两条)')
            th = lb_len / int(t)  # 线程控制 2
        except Exception:
            print('线程错误，将使用默认两条线程...')
            t = 2
            th = lb_len / int(t)  # 线程控制 2
        print('你使用的是：%s条线程执行程序...' % t)
        print('正在分配任务...')
        self.t1 = self.url_lb[:int(th)]             # 线程1
        self.t2 = self.url_lb[:int(th * 2)]         # 线程2
        self.t2 = self.t2[int(th):]  # 截取
        print('t1', self.t1)
        print('t2', self.t2)

        self.t3 = self.url_lb[:int(th * 3)]          # 线程3
        self.t3 = self.t3[int(th * 2):]  # 截取
        print('t3', self.t3)

        self.t4 = self.url_lb[:int(th * 4)]          # 线程4
        self.t4 = self.t4[int(th * 3):]  # 截取
        print('t4', self.t4)

        self.t0 = self.url_lb[:int(th * 5)]          # 线程5
        self.t0 = self.t0[int(th * 4):]
        print('t0', self.t0)
        print('任务分配完毕，开始执行...')
        return t, self.t1, self.t2, self.t3, self.t4, self.t0

    def run(self):
        t, *ts = self.thread_number()
        print('---------')
        url_lb = [i for i in ts if i !=[]]
        print(url_lb)

        # 创建目标
        print('开始', time.strftime('%X'))
        for i in range(int(t)):
            threading.Thread(target=self.get_api, args=[url_lb[i]]).start()

    def __del__(self):
        print('结束', time.strftime('%X'))
        self.top_f.close()


if __name__ == '__main__':
    h = HanFuHuiAPI()
    h.run()