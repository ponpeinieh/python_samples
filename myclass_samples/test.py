#import pet

#from pet import make_pet
#from pet import make_pet as mp
from pet import *
print(make_pet('dog','Lucky',age=10, hair='white',tail='no'))
print(make_pet('cat','kitty'))

result = user_profile('Steven','Hawking', age=20, gender='M', email='js@email.com')
print(result)
