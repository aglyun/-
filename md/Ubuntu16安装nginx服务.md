# Ubuntu16安装nginx服务

- 安装服务

```
sudo apt-get install nginx
```

- 测试安装

```
sudo nginx -t
```

- 提示成功

```
nginx: the configuration file /etc/nginx/nginx.conf syntaxis ok
nginx: configuration file /etc/nginx/nginx.conf test issuccessful

```

- 进入nginx的配置目录，并且创建一个新的配置文件

```mu
cd /etc/nginx/conf.d/    # 进入目录
touch my.conf    		 # 创建文件,名字自取
```

- 设置权限

```
chmod 777 my.conf
```

- 打开文件，编辑文件

```
vim my.conf
```

- 配置文件

```
server {
      listen 80;                      >>> 端口
      server_name 127.0.0.1 ;		  >>> 服务名字，也就是域名
      index index.html index.htm;     >>> 文件的首页
      root /home/wbt/Desktop/Projects/H5;    >>> 文件的路径
  }

```

- 重启nginx

```
sudo service nginx restart
```

