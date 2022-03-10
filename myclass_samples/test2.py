#list可以取得部分的元素
#slice的語法
players = ['Henry','Steward','Kevin','David','Albert']
slice1 = players[1:4]
print(slice1)
slice2 = players[:4]
print(slice2)
slice3 = players[:-3]
print(slice3)
slice4 = players[2:]
print(slice4)
#指定間隔
slice5 = players[1:-1:2]
print(slice5)
#可以使用slice來建立list的copy
players2 = players[:]
players[1]='Teddy'
print(players)
print(players2)
#使用=，不會產生新的list
players3=players
players[2]='Raul'
print(players)
print(players3)
# Tuple (類似list，但是内容不能改變）
sizes = (100,200,500)
print(sizes)
for s in sizes:
    print(s)
#sizes[1]=350 #error
print(sizes[0])
#tuple可以省略小括號
position = 50,60
print(position[1])
print(len(position)) #len()元素個數
#tuple包含一個元素
scores = (10,)
print(type(scores)) #type()取得形態
'''
1. 列表中包含5個最希望旅行的國家
2. 列印"列表中前3個最希望去的國家是XXX,YYY,ZZZ" (使用slice取得最前面3個items)
3. 列印"列表中間3個最希望去的國家是XXX,YYY,ZZZ" (使用slice取得中間3個items)
4. 列印"列表中後3個最希望去的國家是XXX,YYY,ZZZ" (使用slice取得最後面3個items)
5. 從這個列表產生一個copy列表
   - 在copy列表中加入一個新的國家
   - 列印原本列表,以及copy列表內容, 確認copy列表與原本列表內容是不相同的
   '''


