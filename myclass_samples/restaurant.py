class Restaurant:
    def __init__(self, name, type): #建構子
        self.name=name
        self.type=type
    def describe(self):
        print(f'餐廳名字:{self.name},型態:{self.type}')
    def open(self):
        print(f'營業中')
