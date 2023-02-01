# ENCAPSULATION: WRAPPING THE DATA AND FUNCTION INTO A SINGLE UNIT.
# DATA HIDING: IF THE INSULATED DATA CALLED BY THE PROGRAM FROM DIRECT ACCESS

#Access Specifiers : 
# publicMethod : Can be called within any childclass & classes and also can access while acting as packages(import)
# Protected Method : 
# 1. Can be called within any childClass & classes and not able to access as packages/imports
# 2. Can be accessed while inheriting
# privateMethod : Can be called within the class with the specific format.

class AccessSpecifiers(object):
    b=55
    _b=45
    __b=87
    def __init__(self):
        self.a = 1
        self._a= 2
        self.__a=3
        
    def publicMethod(self):
        print("hey hi I am public method")
        print(self.__a)
    
    def _protectedMethod(self):
        print("Buddy I am protected method")
    
    def __privateMethod(self):
        print("I am Damn private")
        print(self.__a)
        
        
        
c=AccessSpecifiers()
# To call private method or variable : object._ClassName__(var or methodName)
print(c.b,c._b,c._AccessSpecifiers__b)
# print(c.a,c._a,c._AccessSpecifiers__a)
#Method call
c.publicMethod()
c._protectedMethod()
c._AccessSpecifiers__privateMethod()


------------------------------------------------------------------------

class accessSpecifiers(object):
    def __init__(self):
        self.a=1
        self._b=2
        self.__c=3
    
    def publicMtd(self):
        print "Public method",self.a
    
    def _protectedMethod(self):
        print "Protected method"
    
    def __privateMethod(self):
        print "private method",self.__c
        
class TrialClass(accessSpecifiers):
    def __init__(self):
        super(TrialClass, self).__init__()
        self._protectedMethod()
        self._accessSpecifiers__privateMethod()
        

obj = TrialClass()
# obj._accessSpecifiers__privateMethod()

---------------------------------------------------------------


# DATA ABSTRACTION: REDUCTION OF PARTICULAR BODY OF DATA TO SIMPLIFIED REPRESENTATION OF THE WHOLE.


class Person(object):
    def __init__(self, first, last, id, email):
        self.firstName = first
        self.lastName = last
        self.id = id
        self.email = email
        self.friends = []

    def add_friend(self, friend):
        if len(self.friends) < 10 and len(friend.friends) < 10:
            self.friends.append(friend)
            print("P1 Friend List: {}".format(self.friends))
            friend.friends.append(self)
            print("P2 Friend List : {}".format(friend.friends))

    def getFriends(self):
        print(len(self.friends))
        for i in self.friends:
            print(i)


p1 = Person("David", "Wolber", "922-43-9873", "wolber@usfca.edu")
p2 = Person("Bob", "Jones", "902-38-9973", "jones@usfca.edu")
p1.add_friend(p2)

print (p1.firstName)
print (list(p1.friends))
print (p1.getFriends())




