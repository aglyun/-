# django设置cookie

#### 普通设置cookie，默认明文状态，需要自行加密

- 方法：set_cookie()
- max_age () 有效期单位为秒

```
- views.py

def index(request):
	r = HttpResponse("Cookie设置成功！")   # 这个是响应页面
	r.set_cookie('uuid', '123456', max_age=120)    # 设置cookie和有效期
	return r
```

- 查看cookie
- 使用COOKIES.get()

```
- views.py

def index(request):
	r = request.COOKIES.get('uuid')
	return HttpResponse(r)
```

- 自定义加密，使用hashlib模块

```
import hashlib
values = '123abc'
data = hashlib.blake2b(values.encode()).hexdigest()    # 进行哈希加密
data将是一串加密后的字符串，不可逆
```




<hr>

#### 内置的加密cookie

- 方法：set_signed_coookie()
- max_age() 有效期单位为秒
- salt 是密钥，解密的时候需要填上

```
- views.py

def index(request):
	r = HttpResponse("Cookie设置成功！")  
	r.set_signed_cookie('uuid', '123', salt='xxx', max_age=120)   
	return r
```

- 解密cookie

```
- views.py

def index(request):
    r = request.get_signed_cookie('uuid', salt='xxx')   # 获取uuid，然后输入xxx密钥
    return HttpResponse(r)
```

