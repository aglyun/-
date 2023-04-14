# html5笔记，防忘记

- [TOC]

- 图片对齐方式

```
align = 'botton'   下 
align = 'top'      上
align = 'middle'   中
```

- 表单 form

```
radio 单选项
男<input type="radio" value="男" name='radio' checked="checked" />
女<input type="radio" name='radio' value="女"/>

设置checked="checked" 为选中这个组件
将所有radio组件的name属性设置为相同即可实现单选

checkbox: 多选框
hidden: 隐藏域
reset: 重置按钮
file: 文件上传

select 下拉列表
<select name="下拉列表">
    <option value="小明">小明</option>
    <option value="小红">小红</option>
    <option value="小东">小东</option>
    <option value="小南">小南</option>
    <option value="小西">小西</option>
</select>
-- select 和option是一对的，如同列表ul和li是一对的
```

- 锚(mao)点 #

```
1. <a name='a'></a>  我是锚点
2. <a href='#a'>点我跳到锚点</a>

-- 注意，一个页面中锚点的名称(name)不能重复
```

- 邮件连接 mailto

```
<a href="mailto:邮箱地址">反馈</a>
```

- 下载链接

```
<a href='1.logo'>点我下载</a>
```

#### 文章

- 整体，独立区块 article

```
<article>
	<h1>xxx</h1>
	<p>xxxx</p>
</article>
```

- 章节，节点 section 

```
<section>
	<h1>我是标题</h1>
	<p>段落</p>
	<p>段落2</p>
</section>
```

- 侧栏 ，摘要，插入，引用，  aside

```
它定义的是article以外的内容
<article>
<aside>
	<h1>我爱你</h1>
	<p>xxxx</p>
</aside>
</article>
```

- 导航部分，用于本页的导航，非外链  nav

```
<header>
	<nav>
		<ul>
			<li>当前页面1</li>
			<li>当前页面2</li>
			<li>当前页面3</li>
			<li>当前页面4</li>
		</ul>
	</nav>
</header>
```

- 大纲 hgroup

```
用于有多个标题的内容，如大纲，如果少于两个标题的就不用它
<hgroup>xxxx</hgroup>
```

- 时间  time

```
<time>2020-08-23</time>
```

#### 页脚

- 页脚  foooter

```
footer配合列表标签使用，不要使用table
<body>
<footer>
	<ul>
		<li>关于我们</li>
		<li>友情链接</li>
		<li>版权信息</li>
		<li>回到顶部</li>
	</1u>
</footer>
</body>

当然，footer也是写在body标签中
```

- 地址，联系方式 address 

```
addres包裹的内容以斜体呈现
<address>
	地址：广西玉林
	电话号码：177xxx
</address>
```

#### 多媒体

- 视频  video

```
<video width="700" height="400" controls>
     <source src="1.png" type="video/mp4">
</video>

video配合source元素使用，这是一对的，source代表资源
```

- 声音  audio

```
<audio controls>
     <source src="1.png" type="audio/mp3">
</audio>

同样配合source使用
```

- 嵌入内容，插件  embed

```
<embed src='xxx.swf'>swf后缀的文件是插件</embed>
```



#### 视觉效果

- 高亮显示  mark

```
mark默认以黄色背景为高亮，可以通过样式来更改它的背景
<mark style="background-color: red">
     猜猜我是谁
</mark>
```

- javasrcipt进程  progress

```
 <progress>我是进程</progress>
 会在页面中显示来回滚动的进度条，如果把value值改为0，进度条变成白色，随便一个值，会立即变成蓝色
```

- 显示度量衡，表现进度  meter

```
<meter value="900" max="1000">显示最大和最小度量</meter>
可以设置它的值，设置最大或者最小值，他会显示进度，进度是绿色。
```



#### 数据篇

- 输入框下拉列表  datalist

```
配合input标签使用，datalist的id需要绑定input的name
<input name='abc'>
<datalist id='abc'>
	<option value='xxx1'></option>
	<option value='xxx2'></option>
	<option value='xxx3'></option>
	<option value='xx33'></option>
	<option value='xx22'></option>
</datalist>

选择xxx2的时候，他会自带筛选出xx22，和2有关的数据会被筛选出，类似搜索框
```

- 文档描述，默认对用户不可见  details

```
<details> 可以配合<summary>标签使用
--- summary是用来更改detalis的标题，details默认标题是详细信息
--- summary 单击的时候会出现黑边框，影响美观，可以通过display的样式更改


<details>
        <summary style="display: inherit">查看详情</summary>
        
        <p>该条信息默认对用户不可见，除非你已经点开了</p>
	
	------------还可以嵌套使用------------------
        <details>
            <summary style="display: inherit">点我看看嵌套的标签</summary>
            <p>你好啊，这是第二层嵌套的</p>
        </details>
</details>
```

- 输出数据类型  outdata

```
测试到好像没什么用处
<outdata>xxxx</outdata>   正常输出xxxx
```

- 菜单列表(和普通列表差不多，相似的99%) 配合li标签使用

```
<menu>
	<li>菜单选项1</li>
	<li>菜单选项2</li>
</menu>
```



#### 表单功能

- 常用属性

```
max
min
step: 数字间隔
required：必填


```

- type类型

```
type='email'
type=''
```





