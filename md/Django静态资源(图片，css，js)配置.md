# Django静态资源(图片，css，js)配置



- 假如djang项目下有这样的文件结构

```
demo （项目）
----demo
----static
    ----statics
        ----img
            ---- 1.png
----manage.py
```



- 在settings.py 中指定静态文件的存放目录

```
STATIC_URL = '/static/'    # 图片的URL，可以自定义，如 xxx，bbb

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')    # 存放图片的文件夹
    # 访问静态资源方式
    # 域名 + /static/image/1.png 
    # 或者还有其他的文件夹 
    # 域名 + /static/css/1.css
]
```



- 通过：域名/static/image/1.png 便能访问到静态资源

![](F:\Desktop\md\img\static_setting_img.png)

