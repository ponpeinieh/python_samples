'''
多行注解：

(1) 列一個名單列表, 邀請他們來晚餐
至少三位客人
並對於每一個客人, 列印邀請訊息
'''
#建立清單list
guests = ['John','Mary','Wilson','Peter']
print(guests)
message = 'Please come to our dinner party!!!'
print(f'Dear {guests[0]},\n{message}')

'''
(2) 有一位客人無法參加, 請替換成另一位客人
重新發出邀請訊息
(3)
買了一張大餐桌, 可以邀請更多的客人
再多邀請三位客人
放置在列表的最前面, 中間, 及最後面 (insert, append)
重新發出邀請訊息
'''
