# django-redis数据库用法
***
#### 以列表的方式添加数据
- django中的redis配置
```python
CACHES = {
    "history": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
```
- 链接数据库
```python
from django_redis import get_redis_connection
redis_ok = get_redis_connection('django配置的redis数据库名') # 比如上面的'history'
```
- 添加列表的数据
```python
# 先创建管道，使用队列来添加数据
p = redis_ok.pipeline()

# 添加数据，这个key是一个redis存储的对象，里面包含多个值
p.lpush(key, values)

# 设置最大数量
p.ltrim(key, 开始索引, 结束索引)
# 如： p.ltrim(key, 0, 5) 表示最多五条，以列表的形式存放

# 提交
p.execute()
```
- 获取数据
```python
# 使用lrange会返回一个列表数据
lb = p.lrange(key, 开始索引， 结束索引)
```
- 删除数据
```python
p.lrem(key, 开始索引，结束索引)
```
***
#### 以普通方式来添加数据
- 添加数据
```python
# 语法： redis对象.setex('key', 有效期秒, 'value')
redis.setex('name', 60, 'Tom')
```
- 获取数据
```python
# 语法： redis对象.get('key')
name = redis_ok.get('name')
```
***
#### redis数据库日常操作
- 进入数据库
```text
redis-cli
```
- 切换数据库
```text
select 序号
> select 1
```
- 显示所有数据
```text
keys *
```
- 添加数据
```text
set key value
> set demo 1
```
- 获取数据
```text
get 值
> get demo
```
- 删除数据
```text
del 值
del demo
```