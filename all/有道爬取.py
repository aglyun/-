# _*_coding. utf-8_*_
# 开发时间：2021/3/2 13:43
# 加油！
from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get('http://dict.youdao.com/')
input = chrome.find_element_by_id('translateContent')
input.send_keys('你好')
chrome.find_element_by_tag_name('button').click()

# 关闭弹窗
chrome.refresh()


# 译文
p = chrome.find_elements_by_class_name('trans-container')
print(p[0].text)
