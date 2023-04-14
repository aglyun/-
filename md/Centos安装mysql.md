# Centos安装mysql

卸载

```
1、yum remove mysql mysql-server mysql-libs compat-mysql51

2、rm -rf /var/lib/mysql

3、rm /etc/my.cnf
```

查看是否存在残留

```
rpm -qa | grep mysql  
rpm -qa | grep 软件名
```



命令安装

```
yum -y install mysql
yum -y install mysql-server  mysql-devel
```

登录mysql，修改密码

```
use mysql;   // 选中mysql数据库
alter user root@localhost identified by '你的密码';
```

开发外网连接

```
update user set host='%' where user='root'; 
```

重启服务器

```
service mysqld restart
```

开启

```
service mysqld start
```

关闭

```
service mysqld stop
```



乌班图

```
启动mysql：
方式一：sudo /etc/init.d/mysql start 
方式二：sudo service mysql start

停止mysql：
方式一：sudo /etc/init.d/mysql stop 
方式二：sudo service mysql stop

重启mysql：
方式一：sudo/etc/init.d/mysql restart
方式二：sudo service mysql restart
```

