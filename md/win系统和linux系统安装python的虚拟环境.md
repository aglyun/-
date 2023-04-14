# win系统和linux系统安装python的虚拟环境

### - 第一种，win中安装

```
1、安装virtualenv和virtualenvwrapper-win：

	pip install virtualenv -i https://pypi.douban.com/simple
	pip install virtualenvwrapper-win -i https://pypi.douban.com/simple
	
2、创建虚拟环境：
	mkvirtualenv  虚拟环境名称
	比如：mkvirtualenv xunihuanj
	
3、查看所有已经安装的虚拟环境：
	workon
	
4、进入
	workon 环境名
	
5、退出
	deactivate

```



### - 第二种，在linux中安装

```
1） ubuntu 

1、安装虚拟环境
	sudo pip3 install virtualenv 或pip
	sudo pip3 install virtualenvwrapper
	
2、打开~/.bashrc文件，并添加如下：
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh

------------------------------------------------------------------------------

centos7下是这样

vim ~/.bashrc

export WORKON_HOME=/root/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/python/bin/virtualenvwrapper.sh
、、、、、
近来发现用CentOS上使用vim竟然用不了，所以从新安装相关的环境；

首先使用命令查看相关的是不是安装了vim：如下：

[root@localhost conf]# rpm -qa|grep vim

出现如下的命令

vim-minimal-7.4.160-1.el7.x86_64

[root@localhost conf]# yum -y install vim*

安装虚拟环境
export WORKON_HOME=/root/.virtualenvs 
source /usr/local/python/bin/virtualenvwrapper.sh

# 3、运行
source ~/.bashrc

原因： 1.     本地根本没有virtualenvwrapper.sh这个文件

          
 2。   ~/.bashrc文件中virtualenvwrapper.sh文件的path配置不对。

在安装virtualenvwrapper时，并没有生成virtualenvwrapper.sh这个文件，使用命令 find / -name virtualenvwrapper.sh 无法找到这个文件，此时可能是你用pip3安装的virtualenvwrapper。


解决办法：1,卸载已有，重新安装     
2,配置~/.bashrc文件

pip3 uninstall virtualenvwrapper

pip3 install virtualenvwrapper


然后使用 find / -name virtualenvwrapper.sh 查看这个文件的位置，我的是在  /usr/bin/virtualenvwrapper.sh

/usr/local/python/bin/virtualenvwrapper.sh

创建虚拟环境的命令
mkvirtualenv -p python3 django_py3

复习命令
# 虚拟环境
mkvirtualenv  # 创建虚拟环境
rmvirtualenv  # 删除虚拟环境
workon  # 进入虚拟环境、查看所有虚拟环境
deactivate  # 退出虚拟环境

# pip
pip install  # 安装依赖包
pip uninstall  # 卸载依赖包
pip list  # 查看已安装的依赖包
pip freeze  # 冻结当前环境的依赖包

从requirements.txt文件安装
pip install -r requirements.txt
删除某个安装包
pip uninstall Werkzeug
检查安装包依赖是否完整
pip check flask
安装特定版本的安装包
pip install flask==0.8
pip安装的加速技巧
1.使用豆瓣或者阿里云的源进行加速软件的安装

pip install -i https://pypi.douban.com/simple/  flask




2.设置配置文件，不用每次都输入网址

# ~/.pip/pip.conf

cat pip.conf

[global]

index-url = https://pypi.douban.com/simple


pip 本地部署，离线源
#下载到本地

pip install –download=“pwd” -r requirements.txt


pip download -d pwd -r requirements.txt

#本地安装

pip install --no-index -f file://'pwd' -r requirements.txt


....................233333

# 使用这种方式，就不怕断网了，只需要下载一次。

# pip 还能自动帮助我们处理各种依赖关系
--------------------- 


创建工程的命令为：

pip install django==1.11.20

pip install django 安装是最新的版本

django-admin startproject 工程名称

#数据库子用户
create database myuxi_db2 default charset=utf8;

create user myuxi2 identified by 'myuxi2'; 
grant all on myuxi_db2.* to 'myuxi2'@'%'; 
flush privileges;

导出Python环境安装包
[root@bogon ~]# pip freeze > packages.txt
这将会创建一个 packages.txt文件，其中包含了当前环境中所有包及各自的版本的简单列表（即pip list 所列出的包列表）
安装导入Python环境包
[root@bogon ~]# pip install -r packages.txt
```

