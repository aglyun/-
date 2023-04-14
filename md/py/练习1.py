import turtle as t
import random

t.speed(100)
t.dot(100000,'black')
t.color("white")

# # 自定义跳转的函数
def goto(a,b):
    t.up()
    t.goto(a,b)
    t.down()
# # 使用函数
# # gt(1,9)
# # gt(100,100)
# # gt(-200,200)
# # gt(300,-300)
# # t.done()

# # 一、学会并且了解列表

# # 列表
# # a = ["刘鼎杰","李焱辉","龚梓博",1,2,3]

# # print(a[1])
# # # a[开始:结束]
# # print(a[0:3])

# # a = ["刘鼎杰","李焱辉","龚梓博",1,2,3,True, False, 100.0]
# # # 1.打印出龚梓博或者刘鼎杰或李焱辉
# # # 2.打印出 True 和 False 比如输出结果是：["True","False"]


# # 二、结合列表使用，自定义函数，setheading(方向) 的用法，以及方向(注意不是坐标)
# # 这个是自定义的函数命名为yi，然后需要传入a和b列表
def yi(a,b,c=""):
    # 注意 c=""代表空值
    t.fillcolor(c)   # 填充颜色的c
    t.begin_fill()    # 开始填充
    for i in range(len(a)):   # 循环次数是len(a)的长度
        t.setheading(a[i])    # 方向是从a中的第i项，i就是从0到某某某
        t.fd(b[i])            # 前进的步数，也是从b列表中的第i项，i也就是0到某某某
    t.end_fill()      # 结束填充


# t.dot(10000,'black')
# t.color("white")
# a = [0,-90,180,90,  0,-90,0,90,0,-90,180]
# b = [100,50,100,50,  40,50,40,50,20,25,130]
# yi(a[0:4],b[0:4],"blue")
# yi(a, b)
# # 圆柱
# a = [45,-90,145]
# b = [40,50,40]
# yi(a, b)




def gq():
    t.color("red")
    goto(-75, -276)
    a = [180,90,0,-90] 
    b = [35,66,35,66]
    yi(a, b,"red")
    # 星星
    t.color("yellow")
    goto(-90,-260)
    t.setheading(110)
    t.begin_fill()
    t.circle(8, 720, 5)
    t.end_fill()
    # 小星星1
    goto(-96,-249)
    t.circle(3, 720, 5)
    # 2
    goto(-90,-247)
    t.circle(3, 720, 5)
    # 3
    goto(-84,-249)
    t.circle(3, 720, 5)
    # 4
    goto(-80,-253)
    t.circle(3, 720, 5)
    
    t.hideturtle()

t.setheading(0)
for i in range(0,201,50):
    t.write(i)
    t.fd(50)
t.home()


t.setheading(180)
for i in range(0,201,50):
    t.write(i)
    t.fd(50)
t.home()


t.setheading(90)
for i in range(0,201,50):
    t.write(i)
    t.fd(50)
t.home()


t.setheading(-90)
for i in range(0,201,50):
    t.write(i)
    t.fd(50)
t.home()
# # 星星
for i in range(200):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    r = random.randint(1,5)   # 实心圆的大小1~5
    goto(x,y)   # 跳转到随机的x和y
    color = ['yellow','gray','blue','red','white','white','white']
    c = random.choice(color)    # 随机从列表中抽取一个元素
    t.dot(r,c)   # r是大小，c是颜色
# 地球
goto(-200,-300)
t.color('#0c6a8f')   
t.dot(700)
# 大陆
t.color('green')
t.pensize(100)
t.fd(10)
t.setheading(50)
t.fd(200)
t.setheading(135)
t.fd(80)
t.setheading(-90)
t.fd(50)
goto(-250,-110)
t.setheading(180)
t.fd(100)
t.setheading(67)
t.fd(50)

# 创建一支笔
# t.colro("white")
a = 0b110110110
t.write(oct(a))


t.done()