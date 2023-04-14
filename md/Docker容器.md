# Docker容器

***

- 意思是以交互(i)，终端(t)，后台(d)的模式运行一个容器，别名是ubuntu-test ,镜像是ubuntu

```dockerfile
docker run -itd --name ubuntu-test ubuntu /bin/bash
```

- docker 查看命令帮助

#### 开始

- 拉取合适的镜像

```dockerfile
docker pull python:3.8    # 下载了一个python3.8
docker pull mysql:5.6     # mysql数据库5.6
docker pull ubuntu:lates  # 乌班图系统lates默认标签
```

- 创建容器

```dockerfile
docker run -可选参数 镜像名 /bin/bash 
# 这时候会进入终端交互，输入exit可以退出
```

#### 查看

- 查看镜像

```dockerfile
docker images
查看容器ip
docker inspect 容器id
```

- 查看全部容器

```dockerfile
docker ps -a
```

#### 启动，停止，删除容器

- 启动

```dockerfiler
docker start 容器id
```

- 重启

```dockerfile
docker restart 容器id
```

- 停止

```dockerfile
docker stop 容器id
```

- 删除

```dockerfile
docker container rm 容器id
或者
docker rm 容器id
```

- 刪除镜像

```docker
docker rmi 镜像id
```



- 在远程启动容器，比如使用shell

```dockerfile
docker exec -it 容器id /bin/bash
```

- 进入容器的终端使用exec，这样退出也不会停止容器

```dockerfile
docker exec -it 容器id /bin/bash
```

#### 开启容器服务：mysql

- 拉取镜像

```
docker pull mysql:latest   // 也可以其他镜像，不一定非要latest
```

- 开启容器服务

```
docker run -itd --name 标签名(随便写) -p 本机端口:容器端口 -e MYSQL_ROOT_PASSWORD=数据库密码 镜像的标签
```

- 例子

```
1. 比如我拉取了一个mysql:latest的数据库镜像，我要设置3306端口，那么如下：
docker run -itd --name mysql_1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:latest
```

- 然后开启第二个mysql服务，用3307端口

```
docker run -itd --name mysql_2 -p 3307:3307 -e MYSQL_ROOT_PASSWORD=123456 mysql:latest
```

- 参数说明：

```
-i 表示以“交互模式”运行容器
-t 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即 分配一个伪终端。
--name 为创建的容器命名
-v 表示目录映射关系(前者是宿主机目录，后者是映射到宿主机上的目录，即 宿主机目录:容器中目录)，可以使 用多个-v 做多个目录或文件映射。注意:最好做目录映射，在宿主机上做修改，然后 共享到容器上。
-d 在run后面加上-d参数,则会创建一个守护式容器在后台运行(这样创建容器后不 会自动登录容器，如果只加-i -t 两个参数，创建后就会自动进去容器)。
-p 表示端口映射，前者是宿主机端口，后者是容器内的映射端口。可以使用多个-p 做多个端口映射
-e 为容器设置环境变量
-p 设置端口，如 当前主机端口:容器端口
--network=host 表示将主机的网络环境映射到容器中，容器的网络与主机相同
```



#### 开启容器服务 python

- 一样的步骤，先拉取镜像

```
docker pull python:latest
```

- 开启容器

```
docker run -itd --name py3 python:latest
```



#### 导出导入容器,

- 导出

```
docker export 容器id > 文件名.tar
```

- 导入

```
cat 文件名.tar | docker import -xxx:标签
如：
cat demo.tar | docker import -my/demo:1.0
```



- 加载镜像

```
docker load -i 镜像.tar
或者
docker load < 镜像.tar
```

