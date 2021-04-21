'''import time

try:
    f = open('test.txt')

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件的过程中，产生了了异常，那么就会捕获到
        # ⽐如 按下了 ctrl+c
        print('意外终⽌止了了读取数据')
    finally:
        f.close()
        print('关闭⽂文件')
except:
    print("没有这个⽂文件")'''

# class Xiyiji:
#     def dongci(self):
#         print(f'洗衣机的宽度是{self.width}')
#         print(f'洗衣机的高度是{self.right}')
#
#
# duixiang = Xiyiji()
# duixiang.width = 500
# duixiang.right = 800
# duixiang.dongci()


'''class Xiyiji():
    def __init__(self,gaodu,kuandu,pinpai):
        self.kuandu = kuandu
        self.gaodu = gaodu
        self.pinpai = pinpai
    def __str__(self):
        return f'这是{self.pinpai}洗衣机的说明书'
    def wash(self):
        print(f'洗衣机的高度是{self.gaodu}')
        print(f'洗衣机的宽度是{self.kuandu}')

        print(f'洗衣机的品牌是{self.pinpai}')
    def __del__(self):
        print('被删除了')
duixiang = Xiyiji(200,300,'海尔')
duixiang.wash()
duixiang2 = Xiyiji(100,200,'啊啊')
duixiang2.wash()
del duixiang
'''


# 定义一个老师类，老师又姓名，性别，课程 方法可以教学，
# 实现一段话：什么什么老师性别是什么什么，教什么什么课程
# 先定义一个老师类

class  laoshi():
    def __init__(self,xingming,age,course):
        self.xingming = xingming
        self.age = age
        self.course = course
    def dongci(self):
        print(f'姓名是:{self.xingming}，性别是{self.age},课程是{self.course}')
aa = laoshi('aaa',16,'yuwen')
aa.dongci()
print(aa)


'''class Teacher():
    def __init__(self, xingming, xingbie, course):
        self.xingming = xingming
        self.xingbie = xingbie
        self.course = course

    def __str__(self):
        return f'我会教学'

    def dongci(self):
        print(f'老师的姓名是{self.xingming},'
              f'老师的性别是{self.xingbie},'
              f'老师教的课程是{self.course}')


duixaing = Teacher('XXX', '男', '语文')
duixaing.dongci()
print(duixaing)'''

#房子类  属性：面积  剩余面积  家具列表
# class jiaju():
#     def __init__(self,jiajuname,mianji):
#         self.jiajuname=  jiajuname
#         self.mianji = mianji
# class fangzi():
#     def __str__(self):
#         return f'面积是{self.mianji},剩余面积是{self.shengyumianji}'
#     def __init__(self,mianji):
#         self.mianji = mianji
#         self.shengyumianji = mianji
#         self.list = []
#     def rongna(self):
#         if self.shengyumianji>self.mianji:
#             self.list.append(self.jiajuname)
#         else:
#             print('空间不足')
# bb = fangzi(100)
# bb.rongna()









