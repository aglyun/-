# centos 服务器安装python3

- 下载python3.5 或者其他版本

```
wget  https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
```

- 解压

```
tar -xvf Python-3.7.0.tax.xz
```

- 将包移到到某个地方

```
mv Python-3.7.0 /usr/local/python-3.7（python-3.7是自空白目录，没有的去创建）
cd /usr/local/python-3.7/   进入目录
```

- 编译安装

```
./configure --prefix=/usr/local/sbin/python-3.7
```

- 将他安装到/usr/local/sbin/python-3.7的目录下

```
make && make install

出现：
Installing collected packages: setuptools, pip
Successfully installed pip-10.0.1 setuptools-39.0.1
说明安装成功
```

***

先看一下python的绝对路径

```
which python
返回 /usr/bin/bin   然后把py3软连接到这里即可
```

- 

```
ln -sv /usr/local/sbin/python-3.7/bin/python3 /usr/bin/python3

输入python -V可以查看当前的默认版本
```

