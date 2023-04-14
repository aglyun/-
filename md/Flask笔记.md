# 安装pipenv虚拟环境
***
- 安装pipenv
```python
    pip install pipenv
```
- 创建虚拟环境
```python
    去某个文件夹，使用命令:
    pipenv install  即可
```
- 进入虚拟环境
```python
    先来到某个文件夹，使用命令:
    pipenv shell  即可
```
- 退出虚拟环境
```python
    exit
```
***
# 开始Flask之旅
### 第一个
```python
   # 导包
   from flask import Flask   # Flask类
   # 创建对象
   app = Flask(__name__)
   
   # 这个app里面有很多方法，调用.route()就可以实现一个陈程序
   @app.route('/')
   def index():
        return "我是一个网站"
```
### 启动服务
- run
```text
   使用run启动服务
   在代码后面写上即可：
   app.run()
```
- flask run
```python
   使用flask内置服务启动
   在命令行中输入：flask run 即可
```
- flask run --prot=8000 更换端口
- flask run这个命令默认是执行app.py,如果更改其他文件，则：
```python
    windows:
    输入命令: set FLASK_APP=文件名
    Linex:
    输入命令: export FLASK_APP=文件名
```
- flask run --host=0.0.0.0
```python
   执行该行命令，同一局域网的可以访问该网站
```
- 改变生产环境,默认环境是：production(生产环境如果出错没有调试信息，开发环境有)
```python
    首先安装：pip install python-dotenv
    然后新建文件： .flaskenv
    在文件中写： FLASK_ENV=development  这个是开发环境
    
```
#### 项目配置
- flask shell 进入交互环境
- 所有的配置都是通过app.config的属性统一操作，操作方式为字典的形式
- app.config['ADMIN_NAME'] = 'Demo'
- 配置的名称必须是大写，小写无效
- app.config.update()  可以一次性设置多个
```python
    app.config.update(
        TESTING=True,
        SECRET_KEY=‘_abcde123‘    
)
```
- 配置还可以创建一个后缀名为.json的文件存储，具体操作后续补上
- 获取url，使用url_for()，需要导包
```python
    直接调用，或者在另一个路中使用：
    url_for('index')  打印即可看到index的路由
    如果是动态路由，则：
    url_for('index',name='abc')  打印看到路由
    注意：需要在with app.test_request_context():下调用
```
### Flask命令
- 自定义flask路由(注册属于自己的flask命令)
- 在终端可以看到打印:flask 自定义命令
```python
    @app.cli.command()
    def cmd():
        click.echo('你好，我是自定义的flask命令')
    或者：
    @app.cli.command('命令名称')
    
```
#### 模块和静态文件
- 模块文件放在templates文件夹，静态文件放在static文件夹
- url一些处理规则
```python
    <类型:变量名> 如：
    @app.route(hello/<int:age>)
    @app.route(hello/<string:name>)
    @app.route(hello/<any(值1,值2,值3...):name>)
    def demo(name):
       return name
    还有很多，比如：
    string  字符串
    int     整型
    float   浮点型
    path    路径，路由
    any     匹配指定值中的一个的元素
    uuid    uuid字符串
```
### 响应这一块
- 预处理（请求钩子）每次执行请求都会先进行这个请求
```python
    把函数注册为before_request就会预先处理这些函数
    @app.before_request
    def demo():
        pass  
```
- 返回自定义状态码
```python
    在路由函数中返回的时候，加上状态码即可，比如：
    return 'ok', 200
```
- 重定向
```python
    return '',301,{'xxx': 'https://baidu.com'}
    或者使用redirect函数
    return redirect('https://baidu.com')
    重定向到自己写的路由
    return redirect(url_for('函数名'))
```
- 自定义错误响应
```python
    abort()函数
    @app.route('/404')
    def not_found():
        abort(404)
```
- 响应数据格式：
```python
    使用make_respnse(数据)，返回一个响应
    响应.mimetype = '类型'
    类型如下：
    text/plain(文本)   text/html   image/png  application/json
```
- jsonify转换json数据的格式
```python
    return jsonify(name='Tom',age=20)  
    return jsonify({'name':'Tom', 'age':20})
```
- Cookie
```python
    1. 先创建响应: 响应=make_response(数据)
    2. 响应.set_cookie('name', name)
    3. 返回响应： return 响应
```
- 获取cookie
```python
    c = request.cookies.get('cookie键')
    print(c)
```
- 设置session
```python
    1. 必须设置一个全局的秘钥，使用app.secret_key = 随机字符串
    2. 在函数中打开session的开关
    session['key'] = True   即可
```
- 获取session
```python
    /////
```
- 简单例子
```python
app.secret_key = 'faffjdf!@#$%%^&*<>'    # session秘钥
@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')   # 获取name，如果获取不到就从cookie中获取
    if name is None:
        name = request.cookies.get('name', '匿名')  # get(键,获取不到返回的值)
        response = "<h1>我是%s</h1>" %name
        if 'login_in' in session:    # 判断设置的session键是否在session中
            response += '[已认证]'
        else:
            response += '[未认证]'
        return response

# 设置cookie
@app.route('/set/<name>')
def set_c(name):
    response = make_response('我是一个set_c的响应数据')
    response.set_cookie('name', name)
    return response
# 获取cookie
@app.route('/get/')
def get_C():
    name = request.cookies.get('name')
    return '你的cookie是%s' %name

# session
@app.route('/login')
def login():
    session['login_in'] = True  # 当访问这个函数时，会设置一个session
    return redirect(url_for('hello'))   # 重定向到hello页面
# 删除session
@app.route('/logout')
def logout():
    if 'login_in' in session:
        session.pop('login_in')   # 删除session
    return redirect(url_for('hello'))
```
- abort(状态码),可以返回一些错误页面，比较好用

### request请求这一块
- 监听http，使用methods=['GET','POST']
```python
    @app.route('/', methods=['GET','POST'])
```
- request的多种属性
```python
    c = request.cookies.get('key')   # 获取cookie
    h = request.host                 # 获取主机
    a = request.args.get('name')     # 获取url疑问号的参数abc/?name=Tom
    l = request.blueprint            # 获取蓝图版本
    header = request.headers         # 获取头部
    method = request.method          # 获取请求方法
    user = request.user_agent        # 获取客户端版本信息
    re = request.referrer            # 获取跳转的链接
```
#### ORM语句
- 查询: 对象.query.过滤方法()或者查询方法
```python
    对象 = 模型类()
    user = User()
    a = user.query.get(id)
    a.字段名称   # 查看
    # 过滤
    user.query.filter_by(id=10).first()
    user.query.filter_by(title='标题').first()

    and 用法:
    from sqlalchemy import and_
    filter(and_(条件1，条件2))   # 或者
    filter(条件1，条件2)
    filter(and_(user.title=='标题',user.name=='小明'))
    filter(user.title=='标题',user.name=='小明')

    or 用法：
    和and一模一样

```
- 修改
```python
    对象.字段 = '新值'
    例如：
    user = User()
    a = user.query.get(1)
    a.title = '我是新标题'
    # 提交到数据库
    db.session.commit()
```
- 删除
```python
    db.session.delete(对象)
    db.session.commit()
    例如：
    user = User()
    a = user.query.get(1)
    db.session.delete(a)
    db.session.commit()
```
- 插入数据
```python
    user = User(name='小明',age=20,sex='男')
    db.session.add(user)
    db.session.commit()
```
#### shell上下文
```python
# 注册shell上下文
@app.shell_context_processor
def 函数名():
    return dict(db=db,ck=CkDB)
    db 是数据库，ck是CkDB模型类
```
#### 数据库 一对多
- 创建两张表
```python
    # 一对多关系
class Author(db.Model):
    # 作者
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    mobile = db.Column(db.String(11), unique=True)
    # 属性关系 : relationship('下属的大写模型类名')
    # books是关系名，方便查找下级，写什么都可以，abc的都可以
    books = db.relationship('Book')

class Book(db.Model):
    # 文章
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True)
    content = db.Column(db.Text)
    # 外键 ForeignKey(‘模型类小写.id’)
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))
    
# 别忘了创建表
db.create_all()
```
- 在shell中测试操作
- 添加数据
```python
    u = Author(name='罗贯中')
    b = Book(title='三国', conent='无内容')
    b2 = Book(title='十万个为什么', conent='无内容')
    db.session.add(u)
    db.session.add(b)
    db.session.add(b2)
    db.session.commit()  # 提交数据
```
- 修改书本成为作者的下级
```python
    b.author_id = 1   # 1 便是作者的id
    b2.author_id = 1   # 1 便是作者的id
    db.session.commit()
```
- 或者作者添加书本为下级
```python
    u.books.append(b)   # b是Book的模型类
    u.books.append(b2)   # b是Book的模型类
    db.session.commit()
```
- 查看有关系的数据
```python
    u.books   # 查看所有下级,数据是一个列表
    b.author_id   # 查看上级的id，一个int类型数据
```
- 删除(解除)有关系的数据
```python
    u.books.remove(下级模型类对象)
    u.books.remove(b)
```
- 双向关系，使用属性back_populates="对方的变量名"
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # 设置双向关系 # back_populates=对方定义的那个变量，比如user
    books = db.relationship('Book', back_populates='user')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    # 设置双向关系
    # 第一必须要有外键
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='books')
```
- 添加数据，绑定关系
```python
    u = User(naem='罗贯中')
    b1 = Book(title='三国')
    b2 = Book(title='三国演义')
    # 先添加提交数据，commit()
    # 操作关联
    b1.user = u
    b2.user = u
    # 然后提交数据即可
    # 如果想解除关联
    b1.user = None  # 即可 
    # 查看关联的数据
    u.books  # 得到已经绑定的数据
```
- 多对一关系
- 和一对多一样，只不过是把:变量 = db.relationship('City')放到了下级那进行关联
- 外键也放在下级那

- 一对一关系
- 和双向关联一样，只不过 db.relationship('上级类'),这里不需要属性back_populates='xxx
- 只能绑定一个，绑定多个会出错，例子：中国的首都是北京

#### 多对多
- 格式也是双向关系
- 设置一个外表，存储A外键和B外键
- A表和B表
```python
# 关联表
# 变量 = db.Table(表名,db.Column('A表名称',类型,外键id),db.Column('B表名称',类型,外键id))
ass_tab = db.Table('st_association',
         db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
         db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id')))
# A表
class Student(db.Model):
    # 学生类
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    # 设置关联关系,外键需要单独写在关联表中，secondary='外键表名'
    t = db.relationship('Teacher',secondary='st_association',back_populates='s')
# B表
class Teacher(db.Model):
    # 老师类
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    # 双向关联
    s = db.relationship('Student',secondary='st_association',back_populates='t')

````