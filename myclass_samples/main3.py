# list裏面包含多個dict
monster_0 = {'color':'blue', 'score':5} #dict
monster_1 = {'color':'green', 'score':8}
monster_2 = {'color':'red', 'score':10}
monsters = [monster_0, monster_1, monster_2] #list
#loop through monsters
for m in monsters:
    print(f"怪物顔色：{m['color']},分數：{m['score']}")
# 建立空的list
monsters2 = []
# 加入30 monsters
for n in range(30):
    m = {'color':'black','score': 3}
    monsters2.append(m)
# 列印出前面的10個monster
for m in monsters2[:10]: #slice(片段)
    print(f"怪物顔色：{m['color']},分數：{m['score']}")
#len() 回傳list的内容個數
print(len(monsters2))
#使用亂數函數
import random #匯入函數庫
colors = ['red','yellow','green','blue','purple','black','orange','cyan','grey','pink']
# 加入30 monsters
monsters3=[]
for n in range(30):
    m={'color':colors[random.randint(0,9)],'score':random.randint(1,20)}
    monsters3.append(m)
# 列印出前面的10個monster
for m in monsters3[:10]: #slice(片段)
    print(f"怪物顔色：{m['color']},分數：{m['score']}")
'''
產生52張撲克牌（0x2660, 0x2661, 0x2662, 0x2663)
'''
suits = [0x2660, 0x2661, 0x2662, 0x2663]
for s in suits:
    print(f"{chr(s)}")
