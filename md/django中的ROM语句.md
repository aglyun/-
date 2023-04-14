# django中的ROM语句

[toc]

#### 新增数据

- 关键字：objects

- 进入django的shell环境：

```
python manage.py shell
```

- 导包：

```
from 应用名.models import 模型类1，模型类2
```

```
例如:有一个Demo的模型类，里面有name和age字段

---方法1---
- 不需要使用d.save(), 他会自动保存
d = Demo.objects.create(name='xxx', age='20')    # name和age是模型类的字段

- 如果有外键,则
d = Demo.objects.create(name='xxx', age='20', 外键_id=1)

---方法2---
d = dict(name='xxx', age='20')
Deom.objects.create(**d)   # 解包
```

- get_or_create：自动判断插入的数据是否已存在，数据存在会不执行新增数据

```
Demo.objects.get_or_create(name='xxx', age='20')
>>> 返回(<Demo: xxx>, False)    # 代码已经存在了这条数据，无法新增该条数据
>>> 返回(<Demo: xxx>, True)    # 如果是True，说明可以新增数据
```



#### 删除数据

```
Demo.objects.all().delete()    # 删除全部数据
Demo.objects.get(id=1).delete()   # 删除id为1的一条数据
Demo.objects.filter(id__gt=10).delete()   # 删除id大于10以上的多条数据

-- 如果数据有外键，外键也会被删除
```



#### 修改数据

- 赋值修改

```
d = Demo.objects.get(id=1)    # 获取到id为1的这条数据
d.name = 'xxx'    # 将他的name的值改为'xxx'
d.save()    # 保存
```

- update

```
 Demo.objects.filter(id=1).update(name='fore')
 >>> 返回1 说明有一条数据修改成功，注意查询方法用的是filter不是get
```







#### 查询数据

##### 查询所有数据  all()

```
d = Demo.objects.all() 
- sql： select * from 数据表;
```

##### 查询指定数量 all()

```
d = Demo.objects.all()[:3]
- sql： select * from 数据表 limit 3;
```

##### 查询某个字段  values()

```
d = Demo.objects.values("name")   >>> 获取到所有name字段的数据
- sql： select name from 数据表;
```

##### 精准查询  get()

```
d = Demo.objects.get(id=1) 
- sql： select * from 数据表 where id=1;
```

##### 模糊查询  filter()

```
d = Demo.objects.filter(id__gt=10)    # 查询id大于10以上的数据
- sql: select * from 数据表 where id>10;
```

##### 模糊中的多个条件查找 filter()

```
Demo.objects.filter(id=1, name='王美仁') 
- sql： select * from 数据表 where id=1 and name='王美仁';
```

##### 模糊查询or(或者) filter()

- 需要导包：from django.db.models import Q

```
# 就是 Q(字段1)|Q(字段2)|Q(字段3)...     = 字段1 or 字段2 or 字段3...
Demo.objects.filter(Q(字段1)|Q(字段2)) 
- sql： select * from 数据表 where id=1 or id=2 or id=3;
-------------------------------------------------------------
# 另外还有"不等于"的查找的关键词
如： exclude: objects.exclude(id=1)  # 排除id为1的数据，其他全部展现
# 第二个是给 Q加上~即可
Demo.objects.filter(~Q(id=1))  # 排除id为1的数据
- sql： select * from 数据表 where not (id=1);  # 不要括号也行
```

##### 查询统计数据 count()

```
Demo.objects.filter(id=1).count()
Demo.objects.filter(id__gt=5).count()    # 统计id大于5以上的数据的数量
- sql： select count(id>5) from 数据表;
```

##### 去重 distinct()

```
Demo.objects.values('字段').filter(条件)
Demo.objects.values('name').filter(id__gt=1).distinct()   # 大于1以上的被查出
- sql： select distinct name from 数据表 where id>1;
```

##### 排序 order_by()

- 降序

```
Demo.objects.order_by('-id')    # 以id字段为降序排序，升序便是把‘-’去掉即可
- sql： select * from 数据表 order by id;    # 升序
- sql： select * from 数据表 order by id desc;    # 降序
```

- 聚合查询

```
# 导包
fromo django.db.models import Sum, Count    # 是大写不是小写
```

- annotate

```
Demo.objects.values('name').annotate(Sum('id'))
结果：
>>> <QuerySet [{'name': '王美仁', 'id__sum': Decimal('1')}]>‘
- sql： select name,sum(id) as 'id_sum' from 数据表 group by name;  # as id_sum可有可无
```

- aggregate

```
Demo.objects.aggregate(Count('id'))
>>> {'id__count': 数量}    # 代表以id为查询的数据有多少条
- sql： select count(id) from 数据表;
```

##### ROM中的匹配符

```
__gt    # 大于				filter(id__gt=1)
__lt	# 小于				filter(id__lt=1)
__gte	# 大于等于			   filter(id__gte=1)
__lte	# 小于等于			   filter(id__lte=1)
__in	# 判断是否在列表内		 filter(id__in=[1,2,3])
__isnull  # 判断字段是否为空     filter(name__isnull=True/False)  
```

- 模糊匹配

| 匹配符        | 用法                          | 说明                                                         |
| ------------- | ----------------------------- | ------------------------------------------------------------ |
| __icontains   | filter(name__icontains='陈')  | 模糊匹配，忽悠大小写                                         |
| __contains    | filter(name__contains='陈')   | 如sql中的like 'xxx%'  %代表模糊 如:陈%                       |
| __startswith  | filter(name__startswith='s')  | 以s开头的                                                    |
| __istartswith | filter(name__istartswith='s') | 以s开头的，并且忽略大小写                                    |
| __endswith    | filter(name__endswith='s')    | 以s结尾的                                                    |
| __iendswith   | filter(name__iendswith='s')   | 以s结尾的，并且忽略大小写（规律：xxx+swith）如：start，istart，end，iend |
| __year        | filter(date__year='2020')     | 以2020年开始的                                               |
| __month       | filter(date__month='07')      | 以7月份开始的                                                |
| __day         | filter(date__month='30')      | 以30号开始的                                                 |

- 精准匹配

| 匹配符   | 用法                         | 说明                      |
| -------- | ---------------------------- | ------------------------- |
| __exact  | filter(name__exact='王美仁') | 如同sql中的 like '王美仁' |
| __iexact | filter(name__iexact='wmr)    | 忽略大小写                |

##### 关联查询

- 反向查询  模型类名小写+set
- 通过父级查询下级
- 一对多查询

```
如果 模型类 A 关联了B
b = B.objects.get(id=1)    >>> 得到'美女组'
b.a_set.all()    >>> 得到与B关联的所有数据（'美女组'下的所有数据）
```

- 正向查询 
- 通过下级查询父级
- 一对一查询

```
a = A.objeects.get(id=1)    >>> 得到'王美仁'
a.外键    >>>  得到父级，也就是'美女组'
```



- 如果外键设置了别名，查询的时候需要用别名，而不是用模型类小写+set

```
如果模型类A的外键写了别名：
name = models.ForeignKey(B,related_name='abc')    # 参数related_name='xxx'

查询时用别名'abc'：
b = B.objects.filter(id=1).first() # 和'b = B.objects.get(id=1)'是一样的
b.abc.all()    >>> 得到关联的所有数据 fdsf
```



