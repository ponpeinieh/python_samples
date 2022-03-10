# dict裏面可以放置list
# list裏面放dict
favorite_languages = {'jane':['python','java'],
                      'john':['c','c++'],
                      'edward':['javascript','vb'],
                      'philips':['go','dart'],
                      'steve':['python']                   
                      }
#loop
#for name,languages in favorite_languages.items():
#for item in favorite_languages.items(): #tuple
for name in favorite_languages.keys():
    if len(favorite_languages[name])>1:
        #顯示複數訊息
        print(f"{name.title()}'s favorite languages are:")
    else:
        #顯示單數訊息
        print(f"{name.title()}'s favorite language is:")
    for a in favorite_languages[name]:
        print(f"{a.title()}")
# dict裏面放入dict
# 使用者資料(dict): key: username, value: dict(firstname, lastname,location)
users ={'aeinstein': {'firstname': 'albert',
                      'lastname':'einstein',
                      'location':'prinston'},
        'mcurie':{'firstname':'marie',
                  'lastname':'curie',
                  'location':'paris'},
        }
# for .... in users.items():
# for .... in users.keys():
# 印出username,firstname,lastname,location
