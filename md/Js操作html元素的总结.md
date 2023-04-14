# JavaScript总结

[TOC]

## 1、js语法

```
1）变量定义
var变量\let变量\const常量
如： 
var a = 1;
let b = 2;
const C = 3;
```



## 2、 获取元素的方法

```
1、document.getElementById("id属性的值");

2、document.getElementsByTagName("标签的名字");

3、document.getElementsByName("name属性的值");

4、document.getElementsByTagName("标签的名字");

5、document.getElementsByClassName("类样式的名字");
- 解析：
- document 文档流
- get 获取
- Element  元素
- By 通过
- id、TagName 标签名字 等等



根据选择器获取元素

6、document.querySelector("选择器");  
   如: <div class='div1'></div>
       var d = document.querySelector(".div1")

7、document.querySelectorAll("选择器");
```

- 页面输出数据

```
window.alert("警告")  // 弹窗
document.write("内容")  // 将内容写到html文档中
console.log("内容")   // 将内容展示在浏览器的控制台
```

- 元素内部写入数据

```
innerHTML: 可以修改html的标签
innerText: 页面获取内容的时候，会把标签过滤掉，会对标签进行转义(可以修改html元素的文字)
```



## 3、函数部分

- 有名函数

```
function demo(){
	代码
}

- 调用：demo()
```

- 函数表达式

```
var demo = funtion(){
	代码
}
- 调用：demo()
```

- 匿名函数

```
(function(){
	代码
});
- 调用：()

(function(){
	代码
}())
- 自动调用，被称为自执行函数
```

- 函数中的关键词

```
return、形参和实参、
```



## 4、css样式

- 内部样式

```
<div class="div1"></div>

<style>
	.div1 {
		width: 100px;    // 宽度
		background-color: red;	// 背景颜色
	}
</style>
```

- 外部样式

```
<link rel="stylesheet" type="text/css" href="样式.css">
```

- 操作css

```
// 先获取到标签的id
// 使用对象进行样式操作
var d = document.getElementById("div1");   // 获取到id，如果是class就用ClassName
d.style.background = "red";
d.style.width = 100 + "px";    // 拼接字符串
d.style.height = "100px";	   // 直接写字符串也可以

---------------------------
- 一次性操作多个样式
d.style.cssText = "width:100px; heigth:200px; background:yellow;"
```



## 5、Js操作html元素

- 关键词：querySelector("标签")

```
<img src="1.png" alt="">

<script>
	var oimg = document.querySelector("img")    // 获取到图片的标签
	oimg.src = "2.png"    // 通过对象.属性改变标签的属性
</script>
```

- 同用的方法操作元素

```
// 有时候直接使用对象.属性无法修改标签的属性如：
// div标签的属性是name="wap",odiv.name='xxx'是无法改变的

// 可以使用querySelector内置的方法进行修改

1、getAttribute("属性名")
  例如：对象.getAttribute("name")  // 获取到name的值

2、设置值：setAttribute("属性名", "新值")
  例如：对象.setAttribute("name", "xxx")
 
3、删除值：removeAttribute("属性名")
  例如：对象.removeAttribute("属性名")
```

- 自定义属性

```
<div xxx="123"></div>    其中 xxx就是自定义的属性
<div aaa="123"></div>    aaa也是自己定义的属性，以此类推
```



## 6、浏览器事件

- 鼠标事件

| 事件          | 事件名称               |
| ------------- | ---------------------- |
| onclick       | 单击事件               |
| ondblclick    | 双击事件               |
| onmouseover   | 鼠标移入               |
| onmouseout    | 鼠标移出               |
| onmousedown   | 鼠标按下               |
| onmousemove   | 鼠标移动               |
| oncontextmenu | 右键单击               |
| onmouseup     | 鼠标抬起(先点击再抬起) |
|               |                        |

```
例如：
<div class="div1"></div>

js代码：
var odiv = document.querySelector(".div1");

// 点击事件
odiv.onclick = function() {
	console.log("点击了div");
}

// 鼠标移动事件
odiv.onmousemove = function() {
	console.log("xxx");
}

- 以此类推
```



- 表单事件

| 事件     | 事件名称     |
| -------- | ------------ |
| onfocus  | 获取焦点后   |
| onblur   | 失去焦点     |
| onchange | 内容发生改变 |
| onreset  | 重置后       |
| onselect | 选择后       |
| onsubmit | 提交后       |
|          |              |

- 键盘事件

| 事件      | 事件名称 |
| --------- | -------- |
| onkeydown | 按键按下 |
| onkeyup   | 按键松开 |
|           |          |

```
document.onkeydown = function() {
	alert('键盘被按下');
}
```



- BOM(浏览器)事件，BOM事件都是window下的属性

| 事件     | 事件名称·    |
| -------- | ------------ |
| onload   | 加载完毕后   |
| onerror  | 加载出错后   |
| onresize | 窗口改变时   |
| onscroll | 操作滚动条时 |
|          |              |

```
如：
window.onload = function() {
	console.log("页面加载完毕")
}

window.onerror = funciton() {
	console.log("页面加载出错")
}
- 以此类推
```



## 7、typeof关键词

```
	// typeof 关键词返回数据类型
    // 格式：typeof 123; 返回number 类型
    var num = 1234;    // number
    var str = '123';    // string
    var bool = true;  // boolean
    var nulls = null;   // object
    var undefieds = undefined;  // undefined
    var json = {};  // object
    var list = [];  // object
    var fun = function(){}; // function

    console.log(typeof fun);    // 测试各种数据的类型
    
    
   
```



## 8、算术运算符

```
 	// 余数
    var t1 = 100%22;
    console.log(t1)    // 余数是12
    
    - 余数的计算步骤是：先计算多个22相加最接近100的数，不能超出，剩下的便是余数。
    - 如：22+22+22+22=88，如果再加一次22便超出了100，所以答案是100-88=12
    
    // a++
    var a = 10;
    a++  // 相当于a = a+1
    console.log(a)   // 11
    
    var a = 10;
    var b = a++;    // 先赋值，后自增，也就是说先打印了值是10的b，然后再自增+1
    console.log(b)  // 10
    
    var c = a--;
    console.log(c) // 10
    
    
    // ++a
    var a = 10;
    var b = ++a;  // 先自增，后赋值（先计算后数值，然后赋值给b）
    console.log(b)  // 11
    
    var c = --a;
    console.log(c)   // 9
```

