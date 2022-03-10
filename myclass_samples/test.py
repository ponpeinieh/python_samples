message = "Welcome to \nRyan's python world" #這是注解
print(message)
print(message.upper())  #upper() to upper case
print(message.lower()) #lower() to lower case
#
first_name = 'Ryan'
last_name = 'Nieh'
print(first_name,last_name)
print(f"My name is {first_name} {last_name}") # f-string f'' f""
#string的方法
#strip(),rstrip(),lstrip()
message2 = '   python    '
print(message2.rstrip())
print(message2.lstrip())
print(message2.strip())
# numbers
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(10/3) #產生浮點數
print(10//3) #產生整數
print(10%3)
print(10**2) #指數
print(0.5**0.5)
#資料結構
#lists(清單，列表)，類似C/java的陣列
#集合資料
colors = ['red','blue','black','yellow'] #create
print(colors)
#使用某一個元素
print(colors[0])
print(colors[3])
print(colors[-1])
print(colors[-2])
colors[-1]='orange' #replace
print(colors)
colors.append('purple') #append
print(colors)
colors.insert(-2,'cyan') #insert
print(colors)
colors.pop(-3) # pop(): remove
print(colors)
removed = colors.pop(-1)
print(f'刪除掉的元素是{removed}')
removed = colors.pop() # 移除最後一個
print(removed)
del colors[0]
print(colors)
colors.remove('blue')
print(colors)
