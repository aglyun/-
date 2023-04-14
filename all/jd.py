# _*_coding. utf-8_*_
# 开发时间：2021/3/8 14:04
# 加油！
import json

import requests
import jsonpath
import re


name = input('输入名称')
url = 'https://search-x.jd.com/Search?callback=jQuery9020875&area=20&enc=utf-8&keyword={}&adType=7&page=1&ad_ids=291%3A24&xtest=new_search&_=1615183282248'.format(name)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
}

r = requests.get(url, headers=headers)
r1 = requests.get('https://item.jd.com/68190292618.html', headers=headers)
print(r1.text)
fin = re.findall(r'\{.*\}', r.text)[0]
search_data = json.loads(fin)
print(search_data.get('291'))
# 通过jsonpath来过滤数据
sku_id = jsonpath.jsonpath(search_data, '$.291[*].sku_id')
ad_title = jsonpath.jsonpath(search_data, '$.291[*].ad_title')
img = jsonpath.jsonpath(search_data, '$.291[*].image_url')
link_url = jsonpath.jsonpath(search_data, '$.291[*].link_url')
shop_name = jsonpath.jsonpath(search_data, '$.291[*].shop_link.shop_name')
sku_price = jsonpath.jsonpath(search_data, '$.291[*].sku_price')
print('商品id：', sku_id)
print('商品标题', ad_title)
print('商品缩略图', img)
print('商品链接', link_url)
print('店铺名称', shop_name)
print('商品价格', sku_price)


s = 'https://img14.360buyimg.com/n2/'+'jfs/t1/119495/21/218/261491/5e99b0b8Efcfb2cec/73e241fe5f366df2.jpg'

print(s)

