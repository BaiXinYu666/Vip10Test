# 提示：先去分析要定义的类，属性，方法，对象作为一个参数来传递，一定要先写逻辑分析，再写代码。

# 1、打印小猫爱吃鱼，小猫要喝水
# 定义一个类 小猫
'''class mao():
    #猫的属性：爱吃鱼，要喝水
    def __init__(self,eat,he):
        self.eat = eat
        self.he = he
    def dongci(self):
        print(f'猫要吃{self.eat},要喝{self.he}')
#定义对象
maomi = mao('鱼','水')
maomi . dongci()
print(maomi)
'''
'''2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤'''


# 定义类:小明
'''class xiaoming():
    # 属性：爱吃东西，爱跑步 体重75 跑步会减，吃东西会增
    def __init__(self, eat, yundong):
        self.eat = eat
        self.yundong = yundong
        self.tizhong = int(75)
    def tizhong1(self):
        print(f'小明爱{self.eat},小明爱{self.yundong}')
    def tizhong2(self):
        if self.yundong:
            self.tizhong  -=1
        elif self.eat:
            self.tizhong +=2
    def __str__(self):
        return  f'体重为{self.tizhong}'
#创建对象
xmtz = xiaoming('吃','运动')
xmtz.tizhong1()
print(xmtz)
yundong = xiaoming('吃','运动')
yundong.tizhong2()
print(yundong)'''

'''3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表'''
class jj():
    def __init__(self, name, mj):
        self.name = name
        self.mj = mj
class house():
    def __init__(self,huxing,mj):
        self.huxing = huxing
        self.mj = mj
        self.shengyu = mj
        self.jiayulist = []
    def __str__(self):
        return f'户型为{self.huxing},总面积为{self.mj},家具有{self.jiayulist}'
    def add(self,jiaju):
        if self.shengyu >=self.mj:
            self.jiayulist.append(jiaju.name)
        else:
            continue
        self.shengyu -= jiaju.mj
jia =jj('床',4)
fangzi = house('四合院',100)
print(fangzi)

def b():
    a = []
    for b in range(10):
        if b>5:
            a.append(b)
        else:
            continue