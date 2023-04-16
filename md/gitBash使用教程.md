[TOC]

***

#### windows中使用git
在Windows中使用GitHub需要进行以下步骤：

1. 首先，需要在计算机上安装Git。可以从Git官方网站（https://git-scm.com/downloads）下载适合于Windows的Git安装程序，并按照提示进行安装。

2. 安装完成后，打开Git Bash命令行工具，输入以下命令来配置Git：

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

这将设置您的用户名和电子邮件地址，这些信息将显示在您提交的每个Git提交中。

3. 接下来，需要创建一个GitHub帐户并登录。可以通过访问GitHub网站（https://github.com/）并单击“注册”按钮来创建帐户。如果已经拥有帐户，请单击“登录”按钮并输入您的凭据。

4. 创建一个新的代码库（repository）。在GitHub网站上，单击右上角的“+”图标，然后选择“New repository”。输入代码库名称和描述，并选择是否要将其设置为公共或私有。

5. 现在，在本地计算机上创建一个新文件夹来存储代码库。打开Git Bash命令行工具并导航到新文件夹。使用以下命令将本地文件夹与远程代码库关联：

```
git init
git remote add origin https://github.com/username/repositoryname.git
```

将“username”替换为您的GitHub用户名，将“repositoryname”替换为您的代码库名称。

6. 现在，可以将文件添加到本地代码库中。使用以下命令将文件添加到暂存区：

```
git add filename
```

将“filename”替换为要添加的文件名。

7. 使用以下命令将文件提交到本地代码库：

```
git commit -m "commit message"
```

将“commit message”替换为您的提交消息。

8. 最后，使用以下命令将本地更改推送到远程代码库：

```
git push origin master
```

这将把您的更改推送到名为“master”的分支中。

#### 克隆其他分支 在地址后面加上 -b 分支名
要克隆其他分支的代码，请使用git clone命令并指定分支名称。以下是详细步骤：

1. 打开终端或命令行界面。
2. 使用cd命令导航到要存储代码的目录。
3. 输入以下命令：

```
git clone -b
```

4. 将替换为要克隆的存储库的URL。
5. 将替换为要克隆的分支的名称。

例如，如果要克隆名为“my_project”的存储库中的“dev”分支，则应输入以下命令：

```
git clone https://github.com/my_username/my_project.git -b dev
```
***
#### git 怎么push整个文件夹包括代码上传到github?
```
1. 使用命令 git add. 将所有文件添加到 Git 仓库中。这会把所有更改过的文件和新文件都加入到 Git 的暂存区
2. 使用命令 git commit -m "提示" 提交更改的文件
3. 推送命令 git push 地址 分支名  如: git push origin master

- 也可以使用 git add 文件夹名/ 添加所有文件至暂存区 
```
#### git进入了vim模式后怎么保存退出？
```angular2html
在使用 Git 命令时，如果进入了 Vim 编辑器模式，可以按照以下步骤保存并退出：

1. 首先，按下 Esc 键，确保处于命令模式（Command Mode）。
2. 然后输入 :wq 或者 :x，其中 :w 表示保存文件，:q 表示退出 Vim，而 :wq 则表示保存并退出。
3. 按下回车键，就可以保存并退出 Vim 编辑器模式了。

如果只是想退出 Vim 而不保存任何更改，可以按下 Esc 键，然后输入 :q!，最后按下回车键即可。
```
#### git怎么删掉github上面多余的文件夹?
```angular2html
1. git pull origin master   # 拉取项目，类似刷新
2. git rm -r --cached 文件名
3. git commit -m '删除了xxx'
4. git push origin master  # 提交删除的操作
```
#### 远程库各种操作
```angular2html
1. git remote     # 查看有多少个远程库
2. git remote -v  # 查看远程库并且显示地址
3. git remote add 地址名 git地址  # 创建一个远程库地址 
   如： git remote add origin https://github.com/xxx/xxxx.git 
4. git remote remove 远程库名  # 删除远程库地址

```
#### 分支的各种操作
```angular2html
1. git branch        # 查看全部分支
2. git branch 分支名   # 创建分支
   如：git branch new   
3. git checkout 分支名   # 切换分支
4. git branch -d 分支名   # 删除分支
```
#### 状态
```angular2html
git status  查看是否添加文件和当前的操作状态
git diff --name-only --cached  查看add了多少文件
git reset  撤销被add的文件

# 如果你确信本地分支是正确的，可以使用 --allow-unrelated-histories 参数强制合并两个独立的历史记录。示例
git pull origin main --allow-unrelated-histories

```