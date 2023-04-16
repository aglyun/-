# encoding:utf-8
# 开发时间： 2022/7/6 16:48
# 开发者：小橘
# 加油！！！
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import sys
# 导入天气
from 天气爬取 import get_qitian

class TQ():
    def __init__(self):
        """ 初始化 """
        self.w = QtWidgets.QWidget()
        # 背景图
        self.w.setStyleSheet("background-image:url(碧珀绯影.jpg)")
        # 透明对象
        self.op1 = QtWidgets.QGraphicsOpacityEffect()
        self.op1.setOpacity(0.5)

        self.w.setGeometry(200, 200, 400, 600)
        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)
        self.w.setLayout(self.grid)    # 设置布局变成网格
        self.w.setWindowTitle("天气查询系统 v1.0")
        self.f = QtGui.QFont("Times", 21)
        self.zj()
        self.w.show()

    def zj(self):
        """ 组件 """
        l1 = QtWidgets.QLabel("天气查询")
        l1.setFont(self.f)
        l1.setAlignment(Qt.AlignCenter)    # 设置文本在中心

        city = QtWidgets.QLabel("城市")
        city.setFont(QtGui.QFont("Times", 16))
        city.setAlignment(Qt.AlignCenter)   # 文本中心

        self.i1 = QtWidgets.QLineEdit()   # 输入框
        self.i1.setStyleSheet("background-color:rgba(0,0,0,0.1); color:white")
        self.i1.setFont(QtGui.QFont("Times", 16))

        b1 = QtWidgets.QPushButton("查看今天天气")
        b1.setFont(QtGui.QFont("Times", 13))
        # 点击事件
        b1.clicked.connect(self.jintian)   # 0标记代表进行

        b2 = QtWidgets.QPushButton("查看未来七天天气")
        b2.setFont(QtGui.QFont("Times", 13))
        # 点击事件
        b2.clicked.connect(self.jintian2)   # 0标记代表进行

        self.t1 = QtWidgets.QTextBrowser()
        self.t1.setFont(QtGui.QFont("Times", 13))
        # 设置透明背景和红色字体
        self.t1.setStyleSheet("background-color:rgba(0,0,0,0.3); color:yellow")
        self.t1.setText("这里用来展示天气信息")

        self.grid.addWidget(l1, 0, 0, 1, 2)
        self.grid.addWidget(city, 1, 0)
        self.grid.addWidget(self.i1, 1, 1)
        self.grid.addWidget(b1, 2, 0)
        self.grid.addWidget(b2, 2, 1)
        self.grid.addWidget(self.t1, 3, 0, 1, 2)

    def jintian(self):
        # 这个方法实现点击后的处理方案
        # 点击按钮，获取输入框的内容
        t = self.i1.text()
        s = ""
        j = get_qitian(t)   # 放入一个t，代表城市
        for i in j[0]:
            s += i +'\n'
        print(s)
        self.t1.setText(s)
    def jintian2(self):
        t = self.i1.text()
        s = ""
        j = get_qitian(t)   # 传入文本
        for i in j:
            for k in i:
                print(k)
                s += k + '\n'
            s += '-'*20 + '\n'
        self.t1.setText(s)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tq = TQ()
    app.exec_()
