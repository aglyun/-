# coding:utf-8
import json
import requests
from jsonpath import jsonpath


class DouBan(object):
    def __init__(self):
        self.start = int(input('输入页数(共3页):')) -1
        print(self.start*18)
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=windows&for_mobile=1&callback=jsonp%s&start=%s&count=18&loc_id=108288&_=1589294942698" % (self.start+1,self.start*18)
        self.file = open('name.json', 'a')

    def get_url(self, url):
        """ 请求url """
        headers = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3724.8Safari / 537.36",
            "Referer": "https://m.douban.com/tv/american",
        }
        r = requests.get(url, headers=headers).text[8:-2]
        data = json.loads(r)    # 将字符串转为字典

        json_name = jsonpath(data, '$..title')      # 数据提取电影名字
        json_score = jsonpath(data, '$..value')     # 数据提取电影评分

        # 将数据提取转为字典
        try:
            s = zip(json_name, json_score)
        except TypeError:
            s = zip(['没有数据'],['没有数据'])


        for i in s:
            # 创建一个新字典
            zd = {}
            zd['名称'] = i[0]
            zd['评分'] = i[1]
            yield zd

    def save(self, file, data):
        """ 保存数据 """
        file.write(data + ',\n')

    def __del__(self):
        # 类被终结后做的最后一口气，关闭文件
        return self.file.close()

    def transfer_data(self, data):
        """ 数据转换 """
        for i in data:
            new_data = json.dumps(i, ensure_ascii=False)
            self.save(self.file, new_data)
            print('写入 %s 成功'%i)


    def run(self):
        data = self.get_url(self.url)
        self.transfer_data(data)



if __name__ == '__main__':
    db = DouBan()
    db.run()

