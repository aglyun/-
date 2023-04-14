# Vue学习记录

- 引入外部cdn

```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

- 测试

```
<div id="box">
	{{ 10+10 }}
</div>

<script>
    new Vue({
        el: "#box",    // vue开始渲染的地方
    })
</script>


>>> 结果是 20, 如果不使用vue渲染那么结果是 {{ 10+10 }}
```

- 三目表达式  (布尔类型)

```
条件?值1:值2
例如：
10>20?'yes':'no'    >>> 结果为 "no"
```



#### 指令

- 标签插入：v-html

```
<div v-html='name'></div>

data: {
	name: "<p>xxxxx</p>",
}
```

- 动态显示和隐藏： v-show

```
 <p v-show="isShow">动态显示和隐藏</p>
 data: {
 	isShow: true/false,
 }
```

- 动态创建和删除：v-if

```
<p v-if="isCreated">动态创建和删除：v-if</p>
data: {
	isCreated: true/false,
}
```

- 动态绑定class：:class
- 使用三木表达式切换，然后更换布尔值
- 在vue中，方法都是在methods中写，字典的形式

```
<div :class="isActive?'red':'blue'">动态绑定class</div>
<button @click="demo()">点击切换</button>
data: {
	isActive: true,
},
// 所有的方法都在methods中写
methods: {
	demo() {
		this.Active = !this.Active;
	}
}
```

