class Master(object):
 def __init__(self):
    self.kongfu = '[五香ᆔ᷾ຎৼᯈො]'
 def make_cake(self):
    print(f'ᬩአ{self.kongfu}ګ֢ᆔ᷾ຎৼ')

class School(object):
 def __init__(self):
    self.kongfu = '[香辣ᆔ᷾ຎৼᯈො]'
 def make_cake(self):
    print(f'ᬩአ{self.kongfu}ګ֢ᆔ᷾ຎৼ')
class Prentice(School, Master):
 def __init__(self):
    self.kongfu = '[ᇿڠᆔ᷾ຎৼᯈො]'
 def make_cake(self):
     self.__init__()
     print(f'ᬩአ{self.kongfu}ګ֢ᆔ᷾ຎৼ')
 def make_master_cake(self):
    Master.__init__(self)
    Master.make_cake(self)
 def make_school_cake(self):
     School.__init__(self)
     School.make_cake(self)

class Tusun(Prentice):
 pass
xiaogang = Tusun()
xiaogang.make_cake()
xiaogang.make_school_cake()
xiaogang.make_master_cake()