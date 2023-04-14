# _*_coding:utf-8 _*_
# DateTime: 2020/8/26 21:51
import re
import requests
from lxml import etree
from fontTools.ttLib import TTFont

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.56 Safari/537.36',
    'Referer': 'https://www.qidian.com/rank',
    'Cookie': 'e1=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C43%22%2C%22l1%22%3A5%7D; _yep_uuid=599e4b1e-8153-715e-98f1-a94de9d37a29; _csrfToken=8V6A8Se0OkHSk0in95p3tgdQRu7L3UTaof7ghQZF; newstatisticUUID=1591497591_988057117; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C45%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%2C%22l1%22%3A3%7D; lrbc=1018027842%7C564853922%7C1%2C1021828355%7C544458088%7C0%2C1012408364%7C417126027%7C0; rcr=1018027842%2C1021828355%2C1012408364',
}
url_ = 'https://www.qidian.com/rank/yuepiao?style=1'

r = requests.get(url_, headers=headers).content
with open('字体.html', 'wb') as f:
    f.write(r)
html = etree.HTML(r)
title_data = html.xpath("//div[@class='book-mid-info']/h4/a/text()")
yuepiao_data = html.xpath("//div[@class='book-right-info']//p/span/style/text()")[0]
print(title_data)
# 找到.woff后缀的文件
re_data = re.findall(r"[a-zA-Z]{8}\.woff", yuepiao_data)[0]
# 进行拼接
font_url = 'https://qidian.gtimg.com/qd_anti_spider/{}'.format(re_data)
# 请求字体文件地址
r = requests.get(font_url, headers=headers)
# 保存文件.woff
with open('字体.woff', 'wb') as f:
    f.write(r.content)
# 通过第三方库进行xml的格式转换
font_obj = TTFont('字体.woff')
font_obj.saveXML('字体.xml')    # 保存为xml格式

cmap_data = font_obj.getBestCmap()    # getBestCmap去除映射对应的数据
# 打开html文件

with open('字体.html', 'r', encoding='utf-8') as f:
    r_data = f.read()
lb = []
for i in re.findall(r'&#100[0-9]{3}.*?<', r_data):
    lb.append(i)
data_list = []
# 清洗数据
for i in lb:
    new_i = i.replace('<', '')
    new_i = new_i.replace('&#', '')
    data_list.append(new_i)
# 得到最终数据
new_lb = [i.split(';') for i in data_list]


# 英汉字典
en_zh = {
    'three': 3,'five':5,'zero':0,'four':4,'seven':7,'one':1,'period':'周','six':6,'two':2,'eight':8,'nine':9
}
piao_list = []    # 列表，用于存储清洗后的票数
for i in new_lb:   # new_lb 是过滤后的数据，如100275，100278等
    counts = ''   # 记录翻译后的数字，每次循环都会清空数据
    try:    # 之所以异常捕捉，是因为列表中有空格数据，如 [['100275','100278', ' ' ]]
        for k in i:   # 再次循环取出100275这些嵌套的数据
            # 取出英文数字
            en = cmap_data[int(k)]   # cmap_data是一个字典，通过getBestCmap()得到,里面有映射数据
            # 取出对应的译文，用num保存，默认是int类型
            num = en_zh[en]
            counts += str(num)    # 将一个组的数字译文拼接，转为str类型
    except Exception:
        pass
    piao_list.append(counts)    # 将拼接好的数字添加到列表

# title_data是标题数据， piao_list是票数，将他们进行打包
title_font_data = zip(title_data, piao_list)    # 总数据
for i in title_font_data:
    print(i)    # 输出打包后的数据
