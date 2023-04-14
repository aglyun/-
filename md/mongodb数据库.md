# MongoDB数据库操作
***
> Ubuntu安装：sudo apt install mongodb-server

- 进入MongoDB服务器
```mongojs
mongo
```
#### 操作 ------
- 创建数据库: use
```mongojs
> use 数据库名称
```

- 查看数据库: db/ show dbs
```mongojs
> db
- 查看所有数据库
> show dbs
- 注意，创建的数据库需要插入数据才能显示
```
- 删除数据库: dropDatabase()
```mongojs
- 切换到要删除的数据库：> use 数据库名称
- 注意：use可以创建数据库，也可以切换到数据库
- 执行dropDatabase()时，集合的数据被清空
> db.dropDatabase() 
```
- 创建集合(相当于数据表): createCollection()
```mongojs
> db.createCollection('集合名', {附带参数,可有可无})
> db.集合名称.insert({插入数据})

- 创建集合也可以添加参数限制它的大小和数量
- 集合名称：demo 
- capped表示固定集合，超出大小会覆盖最早的数据
- autoIndexId: 表示自动创建索引
- size: 限定大小
- max: 限定数据的数量
- autoIndexId这个参数一般来说不需要
> db.createCollection('demo', {capped: true, autoIndexId:true, size: 1000000, max: 10000})
```
- 删除集合: drop()
```mongojs
> db.集合名.drop()
```
- 查看集合: show tables
```mongojs
> show tables
> show collections
```

- 插入文档(插入数据表): insert()
```mongojs
- 插入的数据必须是键值对
- 语法： db.集合名.insert({key: 'value'})
> db.demo.insert({title: '标题',
                  by: 'baidu',
                  url: 'https://www.baidu.com',
                  lb: ['data1','data2', 'data3'],
                  likes: 100
})
- 也可以把要插入的数据定义为变量后再插入
- 插入的数据会变成另一个键值对，拥有独立的id

> data = ({title: 'this is var value'})
> db.demo.insert(data)

```
- 查看文档数据: find()
```mongojs
> db.集合名.find()
- 统计
> db.集合名.count()
- 漂亮输出
> db.集合名.find().pretty()
```
- 更新文档(表数据): update()
```mongojs
- update()接受四个参数
- update(value1, valuel2, value3, value4)
- value1: 查询条件
- value2: 设置新数据
- value3: 是否插入不存在的新值true/false（默认false）
- value2: 是否更新全部true/false（默认false）

- 原本数据直接替换成指定的数据:
> db.demo.update({'title': 'python'},{'title': 'python3'}) 

- 替换单条数据，而不是全部
> db.demo.update({'title': 'python'},{$set: {'title': 'python3'}}) 

- 如果title条件=python的结果有多个，将第四个参数设置为真可以进行全部替换
> db.demo.update({'title': 'python'},{'title': 'python3'}, true, true)

- save()通过ID更新指定的文档(必须是id)
> db.demo.save({'_id': ObjectId("5xxxx"), 'key1': 'valuel1'})
```
- 删除集合数据(表数据)
```mongojs
- 语法： db.集合名.remove({条件}) 默认删除条件相符合的
> db.demo.remove({'title': 'root'})

- 要单一删除，添加 justOne参数，设置为true或者1
> db.demo.remove({'title': 'root'}, {'justOne': true})
```
#### 查询
- find(条件)
```mongojs
> db.demo.find({'title': 'root'})  - 条件查找

> db.demo.find() - 无条件查找

- 漂亮打印数据
> db.demo.find().pretty() 
```
- MongoDB的条件操作符
```mongojs
- 操作符需要加上$符号
- :(等于), lt(小于), lte(小于等于), gt(大于), gte(大于等于), ne(不等于)

> db.demo.find({'num': 100})  - num等于100
> 类似sql语句的: select * from demo where num=100;

> db.demo.find({'num': {$lt: 100}})   - num小于100
> db.demo.find({'num': {$lte: 100}})  - num小于等于100
> db.demo.find({'num': {$gt: 100}})   - num大于100
> db.demo.find({'num': {$gte: 100}})  - num大于等于100
> db.demo.find({'num': {$ne: 100}})   - num不等于100
- 也可以多写几个操作符
> db.demo.find({'num': {$lt: 7, $gt: 5}})  - num小于7又大于5的

- 同时，任何语句中都可能使用到，比如：
> db.demo.remove({'num': {$gt: 100}})  - 删除num大于100的数据
```
- and(和) 条件
```mongojs
- and其实就是多个条件
> db.demo.find({'title': 'admin', 'name': 'Tom'})
```
- or(或者) 条件: $or
```mongojs
> db.demo.find({$or: [{'title': 'admin'},{'name': 'Lisa'}]})
- $or 作为条件放在key的位置(mongodb数据库所有的数据都是键值对，符号也是，不能脱离大括号)
```
- and 和 or的联合使用
```mongojs
db.demo.find({'title': 'admin', $or: [{'title': 'root'}, {'name': 'Tom'}]})

- 解析： 第一段 {'title': 'admin', 它查找的数据必须包含admin
- 解析： 第二段 $:[{'title': 'root'}, {'name': 'Tom'}]}, 它查找的数据必须是root或者Tom，必定有一个数据
```
- 类型： $type
```mongojs
> db.demo.find({'data': {$type: 'string'}})
- 找出key为data的string类型的值
```
- 控制显示的数据数量： limit(数量)
```mongojs
> db.demo.find().limit(10)  - 显示 10条数据
```
- 跳过指定数量：skip(数量)
```mongojs
> db.demo.find().skip(10)   - 跳过10条数据，其余的全部显示

- 如果 skip 和 limit 组合使用，会先执行 skip 再执行 limit
> db.demo.find().limit(5).skip(1)

- 会先跳过1条数据再显示五条数据，即使反过来也是一样
> db.demo.find().skip(1).limit(5)
```
- 排序: sort({字段:1/-1})
```mongojs
- 1是正序 -1是反序
- 以num为字段进行正序排序，反之是-1
> db.demo.find().sort({'num': 1})
```
- 索引: createIndex({字段：1/-1})
```mongojs
> db.demo.createIndex({'index': 1})
- 查看： db.demo.getIndexes()
- 大小： db.demo.totalIndexSize()
- 删除所有： db.demo.dropIndexes()
- 删除指定： db.demo.dropIndexes('索引名称')
```
- 聚合： aggregate()
```mongojs

```


 