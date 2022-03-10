#list

cars = ['bmw','audi','toyota','honda']
# 排序 sort() : 方法（list 裏面的方法）
cars.sort()
print(cars)
# 反向排序 sort(reverse=True)
cars.sort(reverse=True)
print(cars)
# sorted() ： 函數
print(sorted(cars))
print(cars)
#
cars = ['bmw','audi','toyota','honda']
cars.reverse()
print(cars)
# for-each loop
for car in cars:
    print(car)
    
'''
### 練習: Seeing the world

1. 列表中包含5個最希望旅行的國家(按照希望的優先順序)
2. 按照原本的順序列印列表內容
3. 按照字母順序列列印列表內容, 但不要改變原本的列表順序
4. 改變原本的列表順序, 最希望的國家排在最後面
5. 改變原本的列表順序, 按照字母順序排列
6. 改變原本的列表順序, 按照字母相反的順序排列
'''

#產生一系列數字 : range()
numbers = [1,2,3,4,5]
numbers = list(range(1,6))
print(numbers)
#for n in range(1,101):
#    print(n)
for n in range(1,11):
    print('hello world')
#range()
print(list(range(10)))
print(list(range(0,20,2))) #0,2,4,6,...18

#產生0,1,4,9,16,25,36,...,100,121
squares=[]
for n in range(12):
    squares.append(n**2)
print(squares)


#min(), max()
numbers=[2,9,11,5,10,1,100,76]
print(min(numbers))
print(max(numbers))
#sum() : 總和
print(sum(numbers))

'''
### 練習

1. 使用for in loop 列印1到20的數字
2. 建立一個list, 包含1到20的數字, 然後再印出
3. 建立一個list, 包含1到1000的數字, 然後列印最大值與最小值以及總和
4. 使用for in loop 列印1到21的奇數
5. 建立一個list, 包含3到30內的3的倍數, 然後印出這個list
6. 建立一個list, 包含1到10的立方值, 然後印出這個list
'''
