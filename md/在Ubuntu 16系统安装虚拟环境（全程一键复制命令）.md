# 在Ubuntu 16系统安装虚拟环境（全程一键复制命令）

- 国内源（例如下载某个模块，这个仅做示例，不要复制)

```
pip3 install 模块名 -i https://pypi.douban.com/simple/ 
pip install --upgrade pip    更新pip
```



- 安装/下载环境

```
sudo pip3 install virtualenv 或pip
sudo pip3 install virtualenvwrapper
```



- 创建文件夹

```
mkdir ~/.virtualenvs
```



- vim ~/.bashrc 打开文件，添加以下内容

```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh
```



- 运行

```
source ~/.bashrc
```



<hr>

以上是安装虚拟环境的步骤，下面是创建虚拟环境步骤：

- 创建环境

```
mkvirtualenv 环境名称
```

- 删除环境

```
rmvirtualenv  环境名称
```

- 进入环境

```
workon 环境名称
```

- 查看环境

```
workon
```

- 退出环境

```
deactivate
```



<hr>

- 其他pip命令(python)

```
pip install  # 安装依赖包
pip uninstall  # 卸载依赖包
pip list  # 查看已安装的依赖包
pip freeze  # 冻结当前环境的依赖包
```

- python 安装项目/创建项目命令

```
安装框架：
pip3 install django==2.2.2    # 指定版本
pip3 install django 		  # 不指定默认安装是最新版


创建项目：
django-admin startproject 项目名称
创建项目app：(在项目的根目录下)
python3 manage.py staryapp 应用名称
```

