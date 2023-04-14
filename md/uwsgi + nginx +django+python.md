# uwsgi + nginx +django项目配置

#### 以宝塔部署为例

- django+python

```python
将项目上传到服务器，然后安装依赖包（步骤忽略）
```

- uwsgi配置： uwsgi.ini

```python
[uwsgi]
# 内网ip
socket = 172.28.198.229:8002    

# 项目目录，和manage.py同目录
chdir = /home/Projects/HBBlog/hb

# 项目中wsgi.py文件的
wsgi-file = HBBlog/wsgi.py
# 进程
processes = 1
# 线程
threads = 2
# uwsgi服器的角色
master = True
# 存放程的文件
pidfile = uwsgi.pid
# 日志文件，因uwsgi可以离端在后台行，日志看不。我以前的runserver是依端的
daemonize=uwsgi.log
# 指定依的境
virtualenv = /home/Projects/HBBlog/hb/ceshi_venv
```

- nginx配置： demo.conf

```nginx
# 这是一个流
upstream openmall {
  server 172.28.198.229:8002 ;  # 内网ip必须和uwsgi的一致
}

# 反向代理服务
server {    # 这个nginx的服务是反向代理，后端的，可以使用ip+端口来访问
	 server_name = api.hbyuyan.cn;	# 绑定域名，可以使用域名来访问
     location / {
        include uwsgi_params;
        uwsgi_pass openmall;    # 指定一个流
    }
}
```

- 前端的nginx

```nginx
server
{
    listen 80;    # 这个服务是前端项目
    server_name 120.25.228.10 test.hbyuyan.cn;  # 绑定了一个域名，可以使用域名来访问
    index  index.html index.htm;
    root /home/Projects/HBBlog/www;
}
```

- 前端的nginx和后端的nginx可以写在同一个文件中

