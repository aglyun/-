# Ubuntu防火墙设置

- 查看

```
sudo ufw status  
```

- 添加开放端口

```
sudo ufw allow 22   // 开启22端口 
sudo ufw allow 8001/tcp
```

- 重启

```
sudo ufw reload  
```

- 开启防火墙

```
 sudo ufw enable
```

- 关闭防火墙

```
sudo ufw disable 
```



## centos中

- 开启防火墙服务

```
service iptables start
```

- 关闭防火墙服务

```
service iptables stop
```

- 其他

```
默认是firewall作为防火墙,安装第三方防火墙 iptables
yum install iptables-services -y
编辑防火墙看链接：https://www.jianshu.com/p/d0fac4648870
```

其他防火墙问题链接：https://www.jianshu.com/p/d0fac4648870

