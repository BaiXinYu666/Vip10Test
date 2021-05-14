'''class shifu():
    def __init__(self):
        self.gongfu = '[大师傅教的方式]'
    def aa(self):
        print(f'会使用{self.gongfu}的方式做杂粮煎饼')
class shifu2():
    def __init__(self):
        self.gongfu = '[二师傅教的方式]'
    def aa(self):
        print(f'会使用{self.gongfu}的方式做杂粮煎饼')

class tudi1(shifu,shifu2):
    def __init__(self):
        self.gongfu = '[自己研究的方式]'
    def aa(self):
        print(f'会使用{self.gongfu}的方式做杂粮煎饼')
    def fulei1(self):
        shifu.__init__(self)
        shifu.aa(self)
    def fulei2(self):
        shifu2.__init__(self)
        shifu2.aa(self)
duixiang = tudi1()
duixiang.aa()
duixiang.fulei1()
duixiang.fulei2()'''

'''class shifu():
    def __init__(self):
        self.gongfu = '[大师傅教的方式]'
    def aa(self):
        print(f'会使用{self.gongfu}的方式做杂粮煎饼')
class shifu2():
    def __init__(self):
        self.gongfu = '[二师傅教的方式]'
    def aa(self):
        print(f'会使用{self.gongfu}的方式做杂粮煎饼')

class tudi1(shifu,shifu2):
    def __init__(self):
        self.gongfu = '[自己研究的方式]'
    def aa(self):
        print(f'会使用{self.gongfu}的方式做杂粮煎饼')
    def fulei1(self):
        shifu.__init__(self)
        shifu.aa(self)
    def fulei2(self):
        shifu2.__init__(self)
        shifu2.aa(self)
class tusun(tudi1):
    pass
duixiang =tusun()
duixiang.aa()
duixiang.fulei1()
duixiang.fulei2()'''


class Master(object):
    def __init__(self):
        self.kongfu = '[五香的]'
    def make_cake(self):
        print(f'会{self.kongfu}做煎饼')
class School(Master):
    def __init__(self):
        self.kongfu = '[香辣的]'
    def make_cake(self):
        print(f'会{self.kongfu}做煎饼')
        super().__init__()
        super().make_cake()
duixiang = School()
duixiang.make_cake()