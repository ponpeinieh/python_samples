
'''
產生52張撲克牌（0x2660, 0x2661, 0x2662, 0x2663)
♠A ♠2 ♠3 ♠4 ♠5 ♠6 ♠7 ♠8 ♠9 ♠10 ♠J ♠Q ♠K
♡A ♡2 ♡3 ♡4 ♡5 ♡6 ♡7 ♡8 ♡9 ♡10 ♡J ♡Q ♡K
♢A ♢2 ♢3 ♢4 ♢5 ♢6 ♢7 ♢8 ♢9 ♢10 ♢J ♢Q ♢K
♣A ♣2 ♣3 ♣4 ♣5 ♣6 ♣7 ♣8 ♣9 ♣10 ♣J ♣Q ♣K
'''
suits = [0x2660, 0x2661, 0x2662, 0x2663]
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
for s in suits:
    print(f"{chr(s)}")

numbers = list(range(52))
print(numbers)
import random
random.shuffle(numbers)
print(numbers)
cards=[]
for n in numbers:
    cards.append({'suit':chr(suits[n//13]),'rank': ranks[n%13]})
for n in cards:
    print(f"{n['suit']}{n['rank']}", end=',')


