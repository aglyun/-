# python datetime 时间模块

```
# 导包
import datetime
# 创建，获取到当时时间
t = datetime.datetime().now()   >>> 使用变量t接收
print(t)   >>> 2020-05-07 15:03:37.684097
```

- 默认打印的时间的秒数带有小数点，影响美观，而且可以自定义格式打印

  

- 自定义格式需要引用.strftime('x-x-x ')的自定义格式

  ```
  datatime.datetime().now().strftime('%Y-%m-%d %H:%M:%S)
  >>> 2020-05-07 15:10:10
  ```

  

- 也可以使用时间的变量去使用格式化方法

  ```
  t.strftime('%Y-%m-%d %H:%M:%S)
  >>> 2020-05-07 15:10:10
  ```

  