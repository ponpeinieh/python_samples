age =10
if age == 10 :
    print(f"I am 10 years old")
else:
    print(f"...")
#
if age<10:
    pass
elif age<18:
    pass
elif age<65:
    pass
else:
    pass

'''
1. 列表(list)中包含一系統的5名使用者id, 包含admin(管理者). 然後寫一個loop, 尋訪每一個user, 列印問候訊息.

   - 若登入人爲admin, 列印特別的訊息:"您好admin, 歡迎登入. 是否要看系統狀態報告?"
   - 若爲其他user, 列印:"您好xxx, 歡迎來到本站!"

2. 在尋訪之前, 先判斷這個列表不是空的內容. 

3. 檢查user ID是否有重復

   - 第一個列表(current_users)包含5位系統已經有的user ids.
   - 第二個列表(new_users)包含5位系統想要加入的新的user ids(與current_users有部分重復).
   - 尋訪new_users列表, 看是否有與current_users內容相同(不考慮大小寫, 亦即"Tom"與"TOM"視爲相同)
   
      - 若重復則列印"user id相同, 請輸入新的id!"
      - 若不重復則列印"user id可以使用!"
   
'''
#
a=[]
if a:
    print(f'a is not empty')
else:
    print(f'a is empty')
'''
### 練習: Ordinal numbers

1. 英文的序數規則爲: 第一稱爲First(1st), 第二稱爲Second(2nd), 第三稱爲Third(3rd), 第四以後爲number+th(4th,5th,...)
2. 將1-9存入一個list
3. 尋訪這個列表, 利用if-elif-else來將數字轉成序數.亦即1st 2nd 3rd 4th 5th 6th 7th 8th 9th.
'''
# A?B:C
gender = 'F'
msg = 'Good evening Mr.!' if gender == 'M' else 'Good evening Ms.!'
print(msg)



