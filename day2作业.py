'''class shifu(object):
    def __init__(self):
        self.hui = '煎饼果子配方'
    def zuo(self):
        print(f'我会用{self.hui}做煎饼果子')
class tudi(shifu):
    pass

aa = tudi()
aa.zuo()
'''


'''class shifu(object):
    def __init__(self):
        self.gongfu = '麻辣'
        self.__qian = 200

    def make(self):
        print(f'我会用{self.gongfu}做，我有{self.qian}')

    def get_money(self):
        return self.__qian

    def set_money(self):
        self.__qian = 500
class tudi(shifu):
    pass

a = tudi()
print(a.get_money())
a.set_money()
print(a.get_money())'''
'''class Master(object):
    def __init__(self):
        self.kongfu = '[五香]'
    def make_cake(self):
        print(f'用{self.kongfu}做煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '[香辣]'
    def make_cake(self):
        print(f'用{self.kongfu}做煎饼果子')
class Prentice(Master, School, ):
    def __init__(self):
        self.kongfu = '自己创造的麻辣'
    def make_cake(self):
        self.__init__()
        print(f'我会用{self.kongfu}做煎饼果子')

    def make_old_cake(self):
        super().__init__()
        super().make_cake()

aa = Prentice()
aa.make_cake()
aa.make_old_cake()'''

# class dog():
#     def word(self):
#         print('指哪打哪')
# class jdog():
#     def word(self):
#         print('追击绑匪')
# class ddog():
#     def word(self):
#         print('追击毒贩')
# class persen():
#     def witha(self,dog):
#         dog.word()
# a = jdog()
# b = ddog()
# c = dog()
# d = persen()
# d.witha(a)
# d.witha(b)
# d.witha(c)


'''class dog():
    gao = 10
b = dog()
c = dog()
print(b.gao)
print(c.gao)
dog.gao = 20
print(b.gao)
print(c.gao)'''


#2-http协议的组成，状态码含义；
'''常见的200 请求成功，但是不一定功能成功，
    300  重定向
    404  页面不存在    端的问题
    500  服务挂了  后端问题
'''

#3-完成手机app抓包
# 已完成，通过同一wifi下，手机设置代理ip信息，下载fiddler或者Charles连接进行抓包
#4-get和post区别
'''get: 不安全，会把用户输入的信息带到url，比如账号密码等私密信息。一般获取列表之类的接口使用get请求
   post:安全，不会带用户输入的信息 一般提交用户输入信息的接口使用post请求
'''
#-cookie和session区别
'''
COOKIE: cookie的数据会保存在客户端，而且可以通过f12在cookie存在的容器去篡改cookie的数据
SESSION:session的数据不会保存在客户端而是服务器，如果考虑安全用session，但是性能不如cookie
'''


