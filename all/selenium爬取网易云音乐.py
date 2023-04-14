# _*_coding. utf-8_*_
# 开发时间：2021/1/13 15:13
# 加油！
import re

from selenium import webdriver

chrome = webdriver.Chrome()
url = "https://music.163.com/discover/toplist?id=3778678"
# 创建谷歌驱动
# chrome = webdriver.Chrome()
# 开启请求
chrome.get(url)
iframe = chrome.find_element_by_name('contentFrame')
# 切换到iframe中
chrome.switch_to.frame(iframe)


def music_url():
    """ 找到歌单的url """
    # 切换到表格
    chrome.find_element_by_tag_name('tbody')
    # 找到tr节点
    tr = chrome.find_elements_by_tag_name('tr')
    # 找到name属性为txt的节点
    chrome.find_element_by_class_name('txt')
    # 找到b节点的，注意用的是elements，多条
    b = chrome.find_elements_by_tag_name('a')
    url = [] # 歌曲url
    for i in b:
        # 将a标签全部遍历出来，取href属性
        s = i.get_attribute('href')
        try:
            # 使用正则进行过滤
            if re.match(r'^https://music.163.com/song\?id=\d+$', s):
                # 将过滤好的数据进行添加到列表
                if s not in url:
                    url.append(s)
            else:
                pass
        except TypeError:
            pass
    return url


def music_title():
    """ 找到歌单列表标题 """
    # 切换body节点
    chrome.find_element_by_tag_name('body')
    # 切换到表格
    chrome.find_element_by_tag_name('tbody')

    # 找到tr节点
    chrome.find_elements_by_tag_name('tr')
    # 找到name属性为txt的节点
    chrome.find_element_by_class_name('txt')
    # 找到b节点的，注意用的是elements，多条
    b = chrome.find_elements_by_tag_name('b')
    title = []
    for i in b:
        # 标题
        name = i.get_attribute('title')
        # 添加到列表
        title.append(name)
    return title


def music_single():
    """ 找到单曲的歌词和下载链接  """
    # url = music_url()[0]
    url = 'https://music.163.com/song?id=1807537867'
    # 开启请求
    chrome.get(url)
    iframe = chrome.find_element_by_name('contentFrame')
    # 切换到iframe中
    chrome.switch_to.frame(iframe)
    # 找到歌词的div id=lyric-content id=flag_more
    gc1 = chrome.find_element_by_id('lyric-content')
    # 点击展开歌词
    chrome.find_element_by_id('flag_ctrl').click()
    gc2 = chrome.find_element_by_id('flag_more')
    print(gc1.text)
    print(gc2.text)
    import  requests
    # 直接请求歌曲的链接
    m_url = 'https://m801.music.126.net/20210113225705/9b47086678c65f934487cfd2a1af4042/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/5473405566/4acb/0b43/3d43/45325e38968d3aa96a4d873636609224.m4a'
    r = requests.get(m_url)
    with open('网易音乐.m4a', 'wb') as f:
        f.write(r.content)
    print('下载成功')




    pass

if __name__ == '__main__':
    title = music_title()
    url = music_url()
    print(title)
    print(url)
    # 歌词
    music_single()



""" # 下面的代码是找到一键播放按钮
# 切换到第a标签
# a_list = chrome.find_elements_by_tag_name('a')
# 得到很多标签不知道怎么办，使用for循环出来
# for i in a_list:
#     if i.get_attribute('title') == '播放':
#         print('ok')
#         i.click()
#         break
#     continue
"""



