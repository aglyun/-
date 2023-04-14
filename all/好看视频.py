# _*_coding. utf-8_*_
# 开发时间：2021/3/11 11:39
# 加油！
import re

import requests
import jsonpath

print('---------好看视频下载--------\n')
name = input('输入视频的名称')
search_url = 'https://sv.baidu.com/haokan/ui-search/pc/search/video?pn=1&rn=10&query={}'.format(name)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
}

r = requests.get(search_url, headers=headers).json()
title = jsonpath.jsonpath(r, '$.data.list[*].title')    # 得到标题
info_url = jsonpath.jsonpath(r, '$.data.list[*].url')    # 得到标题
vid = jsonpath.jsonpath(r, '$.data.list[*].vid')    # 得到vid
print(title)
print(info_url)
print(vid)

video_url = 'https://haokan.baidu.com/videoui/api/commentget?rn=10&url_key=6371665770727286477&pn=1&child_rn=2'


for i in range(len(vid)):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        # 'referer': 'https://haokan.baidu.com/v?vid={}'.format(vid[i])
    }
    # 通过vid来获取视频地址，循环请求
    url = 'https://haokan.baidu.com/v?vid={}'.format(vid[i])
    r = requests.get(url, headers=headers)
    fin = re.findall(r'"url":"(.*?)"', r.text)[0].replace('\\', '')    # 过滤数据
    print('fin', fin)

    # 请求视频地址
    r = requests.get(fin, headers=headers)
    print(r)
    with open('视频/{}.mp4'.format(title[i]), 'wb') as f:
        f.write(r.content)
        print('{}.mp4保存成功...'.format(title[i]))

