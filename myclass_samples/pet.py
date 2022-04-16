def make_pet(species, name, **kwargs):
    information ={'species':species, 'name':name}
    information.update(kwargs)
    return information

def user_profile(firstname, lastname, **user_info): # user_info is a dict
    user_info['fname']=firstname
    user_info['lname']=lastname
    return user_info
