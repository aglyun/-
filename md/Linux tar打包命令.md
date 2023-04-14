# Linux tar打包命令

- 打包

```
tar -cvf 文件名.tar.gz  目录名
# 打包相对目录资源
tar -cvf 文件名.tar.gz *
```



- 解包

```
tar -xvf 文件名.tar.gz
# 解包单个文件
tar -xvf 文件名.tar.gz 目录/文件1
```



- 查看压缩包结构

```
tar -tf 文件名.tar.gz
```



- 参数说明

```
c  压缩
x  解压
v  显示过程
f  文件名
t  查看
```

#### 常用方法如上

