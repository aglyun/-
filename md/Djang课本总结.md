# Djang中的文件上传和下载

#### 上传功能

- 使用FILES.get(前端名字，None)获取上传的对象
- 使用chunks()方法进行分流上传， multiple_chunk()检查上传的文件大小是否超过2.5m，返回布尔型数据，可以使用这个方法对小于2.5m的文件直接写入而不使用分流写入
- 原理：获取上传对象，然后写入字节数据到本地

```
f = FILE.get('前端名字', None)

# 新建文件
file = open(f.name, 'wb')    # f.name 是获取上传文件的名字

# 使用分流模式将数据写入到文件
for i in f.chunks():
	file.write(i)    # 分流写入
	
# 可以进行判断文件的大小
if f.mulitple_chunks():
	结果真，返回True
	结果假，返回False
```

- 其他扩展
- 1.文件大小计算 ：文件对象.size/1024/1024
- 2.文件类型 ：文件对象.content_type

<hr>

#### 下载功能

- StreamingHttpResponse ：使用范围广，支持大规模数据或文件输出，速度慢
- FileResponse：速度快，支持数据或文件输出

- 原理：获取到文件对象，然后选择其中一种格式进行读取数据，返回数据

```
Views.py

""" 第一种方法 """
def dow1():
    # 获取到文件对象，大小是1GB
	file_name = os.path.join(BASE_DIR, 'static/file/泰坦尼克号.mp4')
	
    try:
        # 使用第一种格式进行下载
        r = StreamingHttpResponse(open(file_name, 'rb'))   # 读取数据，是rb格式读取
        r['content_type'] = 'application/octet-stream'     # 文件类型
        r['Content-Disposition'] = 'attachment;filename=text.mp4'
        return r    # 返回数据
    except Exception:
        raise HttpResponse('下载错误')	
        
        
""" 第二种方法 """
def dow2(request):
    """ 使用FileResponse下载"""
    # 1.获取文件路径
    file_name = os.path.join(BASE_DIR, 'static/file/泰坦尼克号.mp4')
    
    # 2. 打开文件
    f = open(file_name, 'rb')
    
    # 3. 调用FileResponse函数进行读取数据
    r = FileResponse(f, as_attachment=True)
    
    # 4.返回数据
    return r

```



<hr>



- 扩展知识
- html中使用{%变量  '别名'%}这种格式的叫做上下文
- 如：< a href="{% url 'dow2' %}">下载2</a>    url是变量， dow2是路由的别名

```
urlpatterns = [
    path('down/', views.index, name='index1'),  # 别名 
 
    path('down/1/', views.dow1, name='dow1'),    # 别名

    path('down/2/', views.dow2, name='dow2')     # 别名
]
```

- 应用场景：

```
<a href="{% url 'dow1' %}">下载1</a>
<a href="{% url 'dow2' %}">下载2</a>
```

