#from restaurant import Restaurant
import restaurant
class IceScreamStand(restaurant.Restaurant): # 父類別(super class, parent class): Restaurant 
    def __init__(self,name,type,flavors):
        #呼叫父類別的建構子
        super().__init__(name,type)
        self.flavors = flavors # 冰淇淋口味
    def display_flavors(self):
        print('我們提供以下的冰淇淋口味:')
        for f in self.flavors:
            print(f'{f}')



s1 = IceScreamStand("我家冰品",'甜點',['香草','巧克力','薄荷','抹茶'])
s1.describe()
s1.open()
s1.display_flavors()
