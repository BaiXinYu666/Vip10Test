class Furniture():
    def __init__(self, name, area):
        # 家具名字
        self.name = name
        # 家具占地⾯积
        self.area = area
class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋⾯积
        self.area = area
        # 剩余⾯积
        self.free_area = area
        # 家具列表
        self.furniture = []
    def __str__(self):
        return f'房⼦坐落于{self.address}, 占地⾯积{self.area}, 剩余⾯积    {self.free_area}, 家具有    {self.furniture}    '

    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬⼊后，房屋剩余⾯积 = 之前剩余⾯积 - 该家具⾯积
            self.free_area -= item.area
        else:
            print('家具太⼤，剩余⾯积不⾜，⽆法容纳')
bed = Furniture('双⼈床', 6)
jia1 = Home('北京', 1200)
print(jia1)
jia1.add_furniture(bed)
print(jia1)
sofa = Furniture('沙发', 10)
jia1.add_furniture(sofa)
print(jia1)
ball = Furniture('篮球场', 1500)
jia1.add_furniture(ball)
print(jia1)