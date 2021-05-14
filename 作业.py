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
'''class mingz():
    # 属性：爱吃东西，爱跑步 体重75 跑步会减，吃东西会增
    def __init__(self, name, gansm):
        self.name = name
        self.gansm = gansm
        self.tizhong = int(75)
        self.tizhong2 = int(45)

    def chi(self):
        if self.name == '小明':
            self.tizhong += 1
        elif self.name == '小红':
            self.tizhong2 += 1

    def ydd(self):
        if self.name == '小明':
            self.tizhong -= 2
        elif self.name == '小红':
            self.tizhong2 -= 2

    def __str__(self):
        if self.name == '小明':
            return f'我的名字叫{self.name},{self.gansm}后的体重为{self.tizhong}'
        elif self.name == '小红':
            return f'我的名字叫{self.name},{self.gansm}后的体重为{self.tizhong2}'


xmm = mingz('小明', '运动')
xmm2 = mingz('小明', '吃')
xmm2.chi()
xmm.ydd()
print(xmm)
print(xmm2)

xhh = mingz('小红', '运动')
xhh2 = mingz('小红', '吃')
xhh2.chi()
xhh.ydd()
print(xhh)
print(xhh2)
'''
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

'''class jj():
    def __init__(self, name, mj):
        self.name = name
        self.mj = mj
class house():
    def __init__(self, huxing, mj):
        self.huxing = huxing
        self.mj = mj
        self.shengyu = mj
        self.jiayulist = []
    def __str__(self):
        return f'户型为{self.huxing},总面积为{self.mj},剩余面积为{self.shengyu},家具有{self.jiayulist}'

    def add(self, jiaju):
        if self.shengyu >= jiaju.mj:
            self.jiayulist.append(jiaju.name)
            self.shengyu -= jiaju.mj
        else:
            print('放不下了')
bad = jj('床', 4)
jia1 = house('四合院', 100)
print(jia1)
jia1.add(bad)
print(jia1)
sofa = jj('沙发',2)
jia1.add(sofa)
print(jia1)
cz = jj('餐桌',1.5)
jia1.add(cz)
print(jia1)
'''

'''4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
'''
# 类 ：士兵#属性：有ak#动作：开火
# 类:枪 属性：有子弹  动作：装子弹
# 士兵类
'''class shibin():
    def __init__(self,name,q):
        self.name = name
        self.q = q
    def __str__(self):
        return  f'我是一名{self.name}我有{self.q}'
# 枪类
class qiang():
    def __init__(self,name,kh,z):
        self.name = name
        self.kh = kh
        self.z = z
    def __str__(self):
        return  (f'ak里有{self.name},我会{self.kh},没子弹了我还会{self.z}')
aa = shibin('士兵','ak')
print(aa)
zid = qiang('子弹','biubiubiu','装子弹')
print(zid)
'''


'''2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤'''

class mingz():
    def __init__(self, name, tz):
        self.name = name
        self.tz = tz
    def chi(self):
        self.tz +=1
        print(f'{self.name}吃东西后的体重是{self.tz}')
    def yd(self):
        self.tz -=0.5
        print(f'{self.name}运动后的体重是{self.tz}')

xm = mingz('小明',75)
xm.chi()
xm.yd()

xh = mingz('小红',45)
xh.chi()
xh.yd()


