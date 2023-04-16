# Flask数据库迁移

- 安装迁移库

```python
pip install flask-migrate
```

- 初始化迁移库

```python
from flask_migrate import Migrate
migrate = Migrate(app, db)
```

- 终端中执行命令

  > flask db init   初始化迁移
  >
  > flask db migrate    生成迁移文件
  >
  > flask db upgrade    更新数据库
  >
  > flask db downgrade    撤销本次操作，回到上一次 

- 如果执行命令出错是因为没有指定flask app
- 命令： set FLASK_APP=程序文件.py



