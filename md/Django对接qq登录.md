# Django对接qq登录

- 需要有开发者的APP ID和APP KEY(申请步骤流程QQ互联有)



- QQ登录请求地址：GET方式

```
https://graph.qq.com/oauth2.0/authorize
```



- 四个必要的请求参数，类型，客户端id， 回调地址(重定向)，state状态值

```
response_type    固定值：code

client_id		 你的应用id
redirect_uri     回调地址，登录成功后跳转到的页面
state			 状态值（不知道有什么用，但是必填）
```



- 可以把参数写在配置文件，使用的时候直接调用使用

```
文件名：settings.py

# QQ登录参数
QQ_CLIENT_ID = '101***382'                                          # QQ互联id
QQ_CLIENT_KEY = '09a0d190***************048a8e7b0'                  # QQ互联key
QQ_REDIRECT_URI = 'http://demo.myuxi.wang/oauth_callback.html'      # 回调网址
QQ_STATE = '/index.html'                                            # 首页

# 这些常量的名字自定义，想写什么就写什么，大写不好辨认也可以小写
```



### 有了参数后，创建djangoApp

- 创建app后，创建模型类。保存qq登录后返回的openid

```
class OAuthQQUser(BaseModel):
    """ qq登录用户数据 """
    
    user = models.ForeignKey('user.Users', on_delete=models.CASCADE, verbose_name='用户')
    openid = models.CharField(max_length=64, verbose_name='openid', db_index=True) # 外键
	reate_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'tb_oauth_qq'
        verbose_name = 'qq登录用户数据'
        verbose_name_plural = verbose_name
```



- 执行数据库迁移

```
python manage.py makemigrations
python manage.py migrate
```



- 新建一个文件，用来写qq登录的url(可以写在视图，但是代码太多不好维护)

```
文件名： qq.py


class OAuthQQTool(object):

    """ qq认证辅助工具类 """
    def __init__(self, client_id=None, redirect_uri=None, state=None, client_key=None):
        """
        这几个参数都是qq登录必要的参数
        
        :param client_id: 应用id
        :param redirect_uri: 回调网址
        :param state: 状态值
        :param client_key: 应用key(秘钥)
        """
        # 因为有四个必要的参数，全要写，但是有一个是固定参数的，可以直接写在下面的函数，不用赋值
        # key也是qq互联的一个参数，只是写在了settings文件中
        
        self.client_id = client_id if client_id else settings.QQ_CLIENT_ID    # 三元表达式
        self.redirect_uri = redirect_uri if redirect_uri else settings.QQ_REDIRECT_URI
        self.state = state or settings.QQ_STATE    # or 或者
        self.client_key = client_key or settings.QQ_CLIENT_KEY
        
        # 上面几个参数都是直接从配置文件中调用，可以写在这里，看个人需求

    def get_login_url(self):
        """ 获取qq登录url """
        url = "https://graph.qq.com/oauth2.0/authorize?"
        
        # 配置参数
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'state': self.state,
        }

        # 拼接url
        url += urlencode(params)    # urlencode是python内置的爬虫模块，可以将字典转成网址参数
        print('拼接完成：', url)
        
        return url    # 返回url
```



- 在视图类中创建视图，调用qq登录工具

```
# get /oauth/qq/authorization/
from mall.tool.QQ.qq import OAuthQQTool


class QQAuthView(APIView):
    """ 获取qq登录的url"""
    def get(self, request):
        """ 获取next参数 """
        next = request.query_params.get('next')    # next是前端的要求，和qq登录无关
        print(next)

        # 调用qq登录工具，传入状态值
        oauth_qq = OAuthQQTool(state=next)

        # 调用qq登录工具的请求rul函数
        login_url = oauth_qq.get_login_url()

        # 返回前端需要的json数据
        return Response({'login_url': login_url})
```

