# dict裏面包含list
# example: pizza 包含餅皮（crust), 加料（toppings):list)
pizza = {'crust':'thick', 'toppings': ['tomato','ham','corn']}
#print
print(f"你訂了一個{pizza['crust']}披薩，裏面有加料")
for t in pizza['toppings']:
    print(t,end=',')
print()
#
favorite_languages = {
    'John':['C','Java'],
    'Steve':['Python','C','Java'],
    'Eddy':['Go'],
    'Philips':['VB','C#']}
#print
for key,value in favorite_languages.items():
    print(f"{key}'s favorite languages are:")
    for lang in value:
        print(f"{lang}",end=",")
    print()
