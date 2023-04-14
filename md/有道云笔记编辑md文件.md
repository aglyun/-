# MarkDown编辑器说明

#### 目录  [toc]
```
[toc]
```



#### 代码高亮  ``````
```
代码高亮
​```
def demo():
    print('hello world')
    
    
class Demo:
    def __init__(self):
        self.a = 1
    
    def run(self):
        print(self.a)
​```
```
***
#### 水平线 ***
***

#### 代办事项 - [ ]和- [x]

```
- [x] 完成1
    - [x] 完成2
    - [x] 完成3
- [ ] 未完成1
- [ ] 未完成2
```

- [x] 完成1
    - [x] 完成2
    - [x] 完成3
- [ ] 未完成1
- [ ] 未完成2

****

#### 流程图 graph TD

```
​```
graph TD
    a[方括号是四方形] --> b(括号是圆角型)
    a[方括号是四方形] --> c{大括号是正方形}  
    c{大括号是正方形} --> |说明| d[xxx]
​```
```

****
#### 序列图 sequenceDiagram
```
​```
sequenceDiagram
    loop 标题
        a->>b: 这是啥图？
    end
​```
```



***
#### 甘特图 gantt
```
​```
gantt

dateFormat 数据格式
title 图表标题

section 左边标题1
右边数据: xxx, 10d

section 左边标题2
右边数据: xxx, 8d

section 左边标题3
右边数据: xxx, 6d

section 左边标题4
右边数据: xxx, 4d
​```
```

***
#### 表格 ||| 和 |-|-|

```
|xxx|xxx|xxx|
|-|-|--|
|xxx|xxx|

```

| xxx  | xxx  | xxx  |
| ---- | ---- | ---- |
| xxx  | xxx  |      |



****
#### 列表 -
- 1
- 2
- 3
    - 3.1
    - 3.2
    - 3.3

****
#### 有序列表 1. 2. 3.
1. 列表1
2. 列表2
    1. 列表2.1
    2. 列表2.2

****
#### 引用 >

```
> xxxx 
```

> xxxxxxxxxx <br>
> xxxxxxxxxx



****
#### 图片和链接

```
![图片链接](http://xxx)
[文件链接](http://xxx)
```



![图片](http://fore.cool/img/20190517/wz.jpg)
[文字链接1](Http://xxxx)

[文字链接2](Http://www.baidu.com)

****

#### 字体

```
<font face='黑体/华文彩云/xxx'>字体</font>
<font color='red'>红色字体</font>
<font size=20px>字体大小</font>

*斜体*
**粗体**

++下划线++
==高亮==
~~中线~~
```

*斜体*

**粗体**f

<font face='黑体' size=10px>黑体</font>

<font face='stcaiyun'>华文彩云</font>

<font color='red'>红色</font>

++下划线++

==abc==

~~中线~~











