#test method override
class Superclass:
    
    def aM(self, id):
        print(f"In Superclass: id = {id}")
    

class Subclass(Superclass):
    def aM(self, id, dummy):
        #super().aM(id)
        print(f"In Subclass id = {id}")
        print(f"In Subclass dummy = {dummy}")

def main():
    s = Subclass()
    s.aM(101,1)

if __name__ == '__main__':
    main()
    
