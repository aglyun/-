# _*_coding. utf-8_*_
# 开发时间：2021/3/11 13:24
# 加油！
import jsonpath
import requests
from urllib import parse
import urllib3


print('----------小红书视频下载--------\n')
headers = {
    # 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MuMu Build/V417IR) Resolution/810*1440 Version/6.82.0.1 Build/6820271 Device/(Netease;MuMu) discover/6.82.0.1 NetType/WiFi',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36',
    'Host': 'edith.xiaohongshu.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe0xG1IbD9/c+qCLOlKGmTtFa+lG43AGfuFUQ6xHxoPkm+NkTZ35/eRYz8Mqj85+g6A2FQxNEmHcber0jn0y0rfe52+MjpWUS4pI27LJrVw9',
    'xy-platform-info': 'platform=android&build=6820271&deviceId=537d5e31-1247-30c3-b245-334d9a0bfbdc',
    'X-B3-TraceId': 'bdbda04900180400',
    # 下面这条比较重要
    'xy-common-params': 'deviceId=537d5e31-1247-30c3-b245-334d9a0bfbdc&identifier_flag=2&tz=Asia%2FShanghai&fid=161544433510d1665886136b1a183886507d9dbd0dbf&app_id=ECFAAF01&device_fingerprint1=202103082019251f18548e4ce396bf7e9611a1dbe5a62b01351977811f412e&uis=light&launch_id=1615451900&project_id=ECFAAF&device_fingerprint=202103082019251f18548e4ce396bf7e9611a1dbe5a62b01351977811f412e&versionName=6.82.0.1&platform=android&sid=session.1615444434883558715956&t=1615454227&build=6820271&x_trace_page_current=search_entry&lang=zh-Hans&channel=BaiduButton'

}
s = 'https://edith.xiaohongshu.com/api/sns/v1/search/recommend_guess?query=&word_request_situation=BACK_WITH_DEL_WORD&pin_word='
sessin = requests.session()
# 先请求搜索引擎,取到请求的
# 需要携带本地缓存进行请求,否在失败
urllib3.disable_warnings()    # 忽略ssl的错误
r = sessin.get(s, headers=headers, verify=False)    # 忽略证书
print(r.text)
d = r.json()
search_id = d.get('data').get('word_request_id')    # 得到搜索的id

# 输入关键词后的链接
name = input('输入视频的名称：')
# name = parse.quote(name+' 视频')

p_url = 'https://edith.xiaohongshu.com/api/sns/v10/search/notes?keyword={}&filters=%5B%5D&sort=&page=1&page_size=20&source=explore_feed&search_id={}&session_id=2895b11ub9t1uk1sonzls&api_extra=&page_pos=0&pin_note_id=&allow_rewrite=1&geo=eyJsYXRpdHVkZSI6MzkuOTA4NTk2LCJsb25naXR1ZGUiOjExNi4zOTczMjR9%0A&word_request_id=&clicked_card=&loaded_ad=&query_extra_info='.format(name+' 视频', search_id)

urllib3.disable_warnings()   # 过滤ssl错误
r = requests.get(p_url, headers=headers, verify=False)
print('搜索结果状态', r)
print(r.json())

author = jsonpath.jsonpath(r.json(), '$.data.items[*].note.user.nickname')    # 作者
title = jsonpath.jsonpath(r.json(), '$.data.items[*].note.title')
video_url = jsonpath.jsonpath(r.json(), '$.data.items[*].note.video_info.url')
print('标题', len(title), title)
print('视频', len(video_url), video_url)
print('作者', len(author), author)

h = {
    'Host': 'sns-video-hw.xhscdn.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.3'
}
for i in range(len(video_url)):
    # 循环请求视频的url
    r = requests.get(video_url[i], headers=h)
    if r.status_code == 200:
        # 保存视频
        try:
            with open('{}-{}.mp4'.format(author[i], title[i]), 'wb') as f:
                f.write(r.content)
                print('{}.mp4 下载完成...'.format(title[i]))
        except OSError as e:
            print(e)
    else:
        print('访问错误')
        continue



