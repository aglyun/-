# _*_coding. utf-8_*_
# 开发时间：2021/1/9 12:55
# 加油！

import shelve
""" python3.6.9以下shelve模块保存的文件会生成三个，3.6.9以上生成单个文件 """

# 构造数据
zd = {'name': 'agl', 'age': 18, 'from': 'china', 'is_author': True, 'mobile': '17777123456','pwd': 'qwe123', 'email': 'xx@qq.com'}
# 写入数据
w_file = shelve.open('demo')
w_file['agl'] = zd
# 读取数据
r_file = shelve.open('demo')
data = r_file.get('agl')
print(data['pwd'])


