# 破解js加密的一篇过程记录（考拉解析网站）

- url是：http://www.zanqianba.com/ 

- 输入抖音链接后自动解析无水印，我要做的就是获取考拉的接口（但最主要的不是接口，而是用来学习js解密）

  ------

  

1、输入链接后点击‘解析’按钮获得一个表单的数据

```
pageUrl: https://v.douyin.com/
t:1590129613662
s:ntoqz93an6snzardonoj0tbaytgjz9klz9wlodknot
```

- pageurl是抖音的链接
- t是时间戳
- s是一个加密后的对东西

【其实所谓的破解js加密无非就是揣测人心，模拟对方程序员的想法，看看对方是如何加密的，然后自己也尝试做同样的做法】



2、下面要做的事情是：s是用什么加密的？

1)、既然有s，那么它一定有定义了一个名为‘s’的变量

2)、利用浏览器开发工具搜索var s var是js中定义变量的声明词

3)、var s的结果不是很多，可以点击进去看看代码的写法



<hr>

选择哪个s什么的不说了，随便选一个看看内部代码

- 其中代码是这样：

```
 parseVideo: function(code) {
            //服务端处理
            this.submitBtnClass.disabled = true;
            var token = Cookies.get("token");
            this.requestSuccess = false;
            
            var tt = new Date().getTime();
            var ss = this.link;
            var s = "";
            if (ss) {
                var s = bb(cc.m(ss + tt))
            }
```

- 开始分析代码

```
上面的是一个函数，定义了tt，ss，s的变量，tt，ss和s是啥玩意？

- 打上断点进行调试：然后再点击一次‘解析’后可以看到了结果
```

![image-20200522145849840](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200522145849840.png)

```
看到上面的代码确实变了很多：
原来：tt是时间戳，ss是抖音的短视频链接，s是空变量，就是用来保存加密后的js
```



- 接下来要分析的是bb(cc.m(ss + tt)) 这行代码

```
1、分析代码先看最里面的括号的内容，(ss + tt)  = （抖音链接 + 时间戳） 这个还好
2、再看外层的cc.m 是什么，也就是说cc也许是一个函数，它调用了m的方法，把ss和tt相加的结果进行了xxx
3、最外层的bb是啥也不知道，看起来就是bb把cc的结果再次进行了‘加密’，然后结果就是 s 了

4、我要做的就是先知道cc是啥，然后再看bb是啥
```



- 再次搜索‘var cc ‘，查找结果

```
1、先在最外面搜索cc，然后点进js的源码文件
2、在源码文件里面搜索’cc‘变量

看到这个结果：
var cc = {
    b: aa.enc.Base64,
    m: aa.MD5,
    u: aa.enc.Utf8
};
```

-- 还是分析一下变量里面的对象都是啥，还是一样的方法，不知道aa是什么就在里面搜索一下

-- aa是js的加密库，类似python的hashlib库

-- aa.md5： 调用了md5加密，aa.enc.base64 调用了base加密，后面的utf8是编码格式

- 分析好就知道了，cc.m 就是调用md5加密

```
cc.m(ss + tt) = cc.md5(抖音链接 + 时间戳)  >>> 也就是把抖音和时间戳组合的结果进行了md5加密
```

- 还有一个bb，看来bb也是将md5加密的结果再进行加密

```
把鼠标放在bb上可以看到提示，它是一个函数，点击进去就看到了它的源代码
- 接下来分析bb的源代码做了什么事情：

function bb(i) {
    return cc.b.stringify(cc.u.parse(i), true).toLowerCase()
};

它接收一个参数i，然后调用了cc.b >>> 很明显，cc.b 不就是上面分析的的东西吗

看来就是调用了base64库进行加密md5(双重加密了）
```

-- 然后，.stringify是啥意思我不知道，看字眼是 字符串格式化好像(老师说的，不知道就意淫一下)，然后在括号的后面也调用了.toLower。。。什么方法，这些方法是啥我也不知道，都是js里面的东西

-- 括号里面有一个cc.u.parse(i)，好像就是做了一个utf8的编码，，，，然后为true，老师说过base64里面是没有bool值的，看来对方重写了base64的规则，这时候自己也模仿一下里面的规则就好了...





- 大致流程记录，就是一条一条分析，模仿对方的加密方式，然后就可以发送相同的加密后的字符串发给服务器