#if
num = 50
if num>0: # <,>=,<=,==,!=
    print('positive number')
    print('finished')
print('not included in the if block')
# and , or
if num>0 and num<101:
    print(f'{num}介於0到100之間')
#
cars = ['toyota','bmw','audi','sukuki']
if 'BMW' in cars:
    print('BMW is in the list')
else:
    print('BMW is not in the list')

if 'honda' not in cars:
    print('honda is not in the list')

#
available_toppings = ['ham','corn','pineapple',
                      'extra cheese','green pepper','chicken']
ordered_toppings = ['pineapple','extra cheese','tomato']
for t in ordered_toppings:
    if t in available_toppings:
        print(f'you can have {t}')
    else:
        print(f"we don't offer {t}")

#
age = 20
if age<12:
    print('小朋友你好!')
elif age<18:
    print('同學你好!')
elif age<60:
    print('先生或女士你好!')
else:
    print('爺爺或奶奶您好!')
