# Flask 分页
***
- views.py文件
```python
@app.route('/stu/')
def page():
    # 分页
    # 获取前端？后面的参数page
    page = int(request.args.get('page',1))  # 默认值1,转为数字类型

    # 查出需要的数据:以时间降序的方式查找数据，然后使用paginate进行分页处理
    m = Message.query.order_by(Message.timestamp.desc()).paginate(page,10)
    stus = m.items   # 获取当前页面记录

    return render_template('index.html',stus=stus,m=m)
```
- index.html文件
```html
<body>
<h1>分页测试</h1>
<hr>
<!--查看数据-->
<ul>
    {% for i in stus %}
        <li>姓名：{{ i.name }}</li>
        <li>内容：{{ i.body }}</li>
        <li>日期：{{ i.timestamp }}</li>
        <br>
    {% endfor %}
</ul>

<hr>
<!--判断是否有上一页,有就渲染上一页的文本-->
{% if m.has_prev %}
    <a href="/stu/?page={{ m.prev_num }}">上一页</a>
{% endif %}

<!--渲染按钮,指定一个参数可以让他不出现None-->
{% for i in m.iter_pages(left_edge=m.pages) %}
    <a href="/stu/?page={{ i }}">{{ i }}</a>
{% endfor %}

<!--下一页，指定stu路由，page是一个参数，后端会获取到-->
{% if m.has_next %}
    <a href="/stu/?page={{ m.next_num }}">下一页</a>
{% endif %}
<br>
</body>
```
