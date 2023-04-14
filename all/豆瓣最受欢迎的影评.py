import json
import requests
from lxml import etree


class DouBan(object):
    """ 爬取豆瓣最受欢迎的影评 """
    def __init__(self):
        self.url = 'https://movie.douban.com/chart'
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        }
        self.file = open('豆瓣最受欢迎的影评.json', 'w', encoding='utf8')

    def get_url(self):
        """ 请求url """
        data = requests.get(self.url, headers=self.header).content
        """ 过滤数据 """
        html = etree.HTML(data)
        # 获取标题
        title = html.xpath('//td[2]/div/a/text()')
        # 获取评分
        grade = html.xpath('//tr/td[2]/div/div/span[2]/text()')
        title_list = []
        for i in title:
            str1 = i.split()
            try:
                title_list.append(str1[0])
            except Exception as e:
                pass
        # 打包数据
        data = zip(title_list, grade)
        return data

    def save_response(self, data):
        """ 得到已经打包好的数据 """
        # 写入文件
        zd = {}
        print(data)
        for i in data:
            zd[i[0]] = i[1]
            data = json.dumps(zd, ensure_ascii=False)
        self.file.write(data)

    def __del__(self):
        """ 作最后一件事 """
        return self.file.close()


if __name__ == '__main__':
    db = DouBan()
    data = db.get_url()
    db.save_response(data)

