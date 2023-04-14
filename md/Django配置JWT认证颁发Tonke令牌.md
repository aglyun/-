# Django配置JWT认证颁发Tonke令牌

- 安装jwt模块

```
djangorestframework-jwt
```



- 创建新文件，返回jwt数据 (返回什么数据，看前端需要什么数据)

```
自定义文件名:py3jwt

def response_jwt_payload_handler(token, user=None, request=None):
    """ 自定义返回jwt的数据 """
    data = {
        'id': user.id,				# id
        'username': user.username,  # 用户名
        'mobile': user.mobile,		# 用户手机
        'token': token				# 令牌
    }
    return data

```



- 在配置文件中进行jwt的配置

```
# DRF子框架的配置

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',    # token
        # 下面两个不是jwt的
        'rest_framework.authentication.SessionAuthentication',    # 基本认证
        'rest_framework.authentication.BasicAuthentication',      # session认证
    ),
}


# jwt配置
JWT_AUTH = {
    # token 的有效期，days=1，表示有效期为1天
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 指定返回的数据
    # 'JWT_RESPONSE_PAYLOAD_HANDLER': '返回jwt的文件名.函数名',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.py3jwt.response_jwt_payload_handler',
    
}
```



- 在序列化器中的创建用户方法后写生成token的代码

```

```

```
--序列化器
class Create...(serializers.ModelSerializer):
......
......
	def create(self, validated_data):
		......
		......
		# jwt, 颁发token认证
        from rest_framework_jwt.settings import api_settings    # 导包
        
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)    # user是ORM语句的对象(创建用户的对象)
        token = jwt_encode_handler(payload)
        
        user.token = token    # 赋值
		
	
		
```



### 另外，如果使用了jwt加密，需要使用它指定的方法登录

- 使用 “obtain_jwt_token” 路由进行登录

```

re_path(r'^路径/$', obtain_jwt_token)

```

- obtain_jwt_token 里面封装了视图类，登录方法已经实现好了