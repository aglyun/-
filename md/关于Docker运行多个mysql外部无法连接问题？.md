# 关于Docker运行多个mysql外部无法连接问题？

- 当docker开启多个mysql容器服务的时候，每个容器的映射端口不一样，比如：
- 3306:3306  3307:3307 3309:3309等，但是这些有个误区就是，跑进mysql里面修改root的权限，和新增账号开启远程连接，其实根本不必！
- 主要解决方法是：

```
1. 进入容器
2. 更新apt-get update
3. 下载vim，用vim修改mysql的配置即可
```

- mysql的配置在 cd /etc/mysql， 用vim打开 my.cnf ,在配置中添加:

```
port=你设置的端口
比如：
port=3306
prot=3307
port=3309
```

- 保存好，退出，重启mysql容器

```
docker restart 容器id
```

- 这样就能连接上mysql

