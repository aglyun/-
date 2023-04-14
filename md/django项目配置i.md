# django项目配置

### 一

- 创建settings文件夹
- 将原本的settings.py文件复制到settings的文件夹，重名为dev.py
- 修改manage.py文件中的配置，将‘xxx.settings'改成'xxx.settings.dev'
- 删除原本的settings.py

- 修改wsgl.py 文件，将’xxx.settings' 改成'xxx.settings.dev'



### 二

- 杀死后台运行霸占端口的django服务

```
sudo netstat -tulpn    >>> 查看进程，找到127.0.0.1:8000
kill -9 进程号
```



