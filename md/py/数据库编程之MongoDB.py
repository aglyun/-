# _*_coding.utf-8 _*_
# 开发时间：2021/1/7  下午11:23
# 加油！

# mysql 操作mongodb数据库
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# 创建数据库和创建集合都是使用字典赋值的方式
# 1. 创建数据库
py_db = client['py_db']

# 2. 创建集合
tb_demo = py_db['demo']

# 3. 插入数据: insert_one({字典数据})
# 返回一个InsertOneResult对象，可以调用inserted_id来获取它的id
x = tb_demo.insert_one({'title': '我是Python数据', 'name': 'agl'})
print(x.inserted_id) # > 得到id

# 4. 插入多条数据：insert_many([{数据1}, {数据2}, {数据3...}])
data_list = [{'name': 'de1'}, {'name': 'de2'}]
# x = tb_demo.insert_many(data_list)
# print(x.inserted_ids[0] , x.inserted_ids[1]) # 得到id列表，可以使用下标取值

# 5. 插入数据，可以重写集合数据的id
data_list = []
for i in range(1,10):
    id = {}
    id['_id'] = i
    data_list.append(id)
print(data_list)
# x = tb_demo.insert_many(data_list)
# print(x.inserted_ids)   # > 返回id 1，2，3，4，5，6，7，8，9

# 查询数据
# 单条数据： find_one()
data = tb_demo.find_one()
print('单数据：', data)
print('单数据取key：', data.get('name'))
# 所有数据: find()，需要把数据全部遍历出来
data_all = tb_demo.find()
for i in data_all:
    # print(i)
    pass

# 条件查询： 控制查询结果
# find({条件}), 语法和mongodb的差不多
# 0代表假，1为真，两者不能同时出现
for i in tb_demo.find({}, {'title': 0, }):
    print(i)
# {} 空大括号表示返回全部数据
# {'title': 0, 'name': 0} 表示不返回title和name的数据，如果填了其他数值表示返回

# 高级查询： find({'$gt': 'xxx'}) 语法和mongodb的差不多
# $gt大于 $gte大于等于 $lt小于 $lte小于等于 $ne不等于
for i in tb_demo.find({'_id': {'$gte': 5}}):
    print('_id大于5的数据', i)

# 正则查找数据: {'$regex': '表达式'}
for i in tb_demo.find({'name': {'$regex': '^a'}}):
    print('开头包含a的数据', i)
# 正则匹配邮箱数据
for i in tb_demo.find({'email': {'$regex': '^\w@\w{6}\.\w{5}'}}):
    print('邮箱：', i)

# 获取全部数据库，返回一个列表
db_name = client.list_database_names()
print('目前所有数据库：', db_name)


db = input(">")
if db in db_name:
    print('%s数据库已经存在' % db)

