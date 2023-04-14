# Django 配置类模型

- 在django中创建一个app

  ```
  python manage.py startapp 名字
  ```



- 到settings的文件中配置MySQL数据库

  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'demo',         >>> 数据库名
          'HOST': '127.0.0.1',    >>> 数据库地址
          'PORT': 3306,  			>>> 数据库端口
          'USER': 'root',			>>> 数据库用户名
          'PASSWORD': '123456789'	>>> 数据库密码
  
      }
  }
  ```



- 需要安MySQL数据库的驱动，驱动是第三方模块

  ```
  pip install pymysql
  ```



- 在项目下的同名文件夹中的 __ init __ 文件写下下面的代码

  ```
  from pymysql import install_as_MySQLdb
  
  install_as_MySQLdb()
  ```



- 在app中的模型文件中创建模型类 models.py

  ```
  class HBook(models.Model):    >>>  类名
      title = models.CharField(max_length=10, verbose_name='书名')
      reading = models.IntegerField(verbose_name='阅读量')
  
      class Meta:       >>> 这个内部类名是固定的写法
          db_table = 'books'    >>> 定于数据表的名字
          verbose_name = '书本'  >>> 站点显示的名字
          verbose_name_plural = verbose_name    >>> 后台显示的名字
  ```



- 进入 python manage.py shell 环境中写模型类对象的方法

  ```
  python manage.py shell
  
  # 进入后, 导入模型类
  from app名.模型名 import 模型类名
  # 如：
  from demo.models import Book
  
  # 使用类对象写数据
  b = Book(title='西游记', readign=100)
  # 保存
  b.save()
  ```

  