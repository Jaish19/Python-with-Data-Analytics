# Bounding methods (class method) : which is present inside class and 
#eligible to access global variable and not a local variable or method of a class which is appeared 
#inside the class
'''
Use of Class method

A class method is a method which is bound to the class and not the object of the class.

They have the access to the state of the class as it takes a class parameter that points to the 
class and not the object instance. It can modify a class state that would apply across all the 
instances of the class
'''

# Un-bounding methods (Static method) impressivly called as "Utility function" : which is present inside 
# class and not eligible to access global variable and local variable which 
# is appeared inside the class.
# Static method not required the class object to create the method and it can be called with jus class name
# Eg. class car: -> Car.staticMethodName()
'''
use of static:

We can use static utility method when it has simple or single use implementation.
'''

# What are the differences between Classmethod and StaticMehtod?
# Class Method    Static Method
# The class method takes cls (class) as first argument.   The static method does not take any specific parameter.
# Class method can access and modify the class state. Static Method cannot access or modify the class state.
# The class method takes the class as parameter to know about the state of that class.    Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
# @classmethod decorator is used here.    @staticmethod decorator is used here.

# The Static methods are used to do some utility tasks, and class methods are used for factory methods. The factory methods can return class objects for different use cases.

class abc:
    outOne = 1  # Class variable - can able to access this variable using any of the instance.
    outTwo = 2  # class variable
    def __init__(self,val1,val2):
        self.val1 = val1  # Instance variable - Can able to access only using the specific instance
        self.val2 = val2  # Instance variable

    def newFactor(self):
        print "inside new factor"
# Bound methods
    @classmethod
    def classmethod(ref,sep):
        print "Inside method now"
        print ref.outOne
# Unbound method (Cannot call class abc's global variable inside static method)
    @staticmethod
    def smalA():
        print "Terms and conditions"

class xyz(abc):
    def __init__(self):
        pass

obj = abc(10,234)
obj.classmethod(8)
obj.smalA()
print dir(obj)
print(obj.outOne)
print obj.val1
print "Document:",abc.__doc__
print "Dict:",abc.__dict__
print "Module:",abc.__module__
print "Base:",abc.__base__
print "Name:",abc.__name__

print getattr(abc,"new_world","Not present")
print setattr(abc,"file","newname")
print obj.file
print setattr(abc,"id","termOne")
print obj.id
print issubclass(xyz, abc)



----------------------------------------------------------------------------------------------

# CLASS & STATIC METHOD

class JaiException(Exception):
    def __init__(self, error):
        Exception.__init__(self)
        self.Error = error
    
    def __str__(self):
        print "OH Gosh! It's JaiException error cart! Reason:",self.Error       

class BOUND_AND_UNBOUNDCLASS(object):
    CLASS_NAME = 'Bound&Unbound'
    CLASS_OWNER = 'Jai Ganesh'
    
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    @classmethod
    def boundMethod(self):
        try:
            print "You're inside of bound method!"
            if self.CLASS_NAME == 'Bound&Unbound':
                raise JaiException("Not expected operation!")
            else:
                print "Nothing here!"
        except AttributeError:
            print "Seems like you're handling bounding method or bounding method trying to hold instance variable"
    
    @staticmethod
    def unboundMethod(a,b):
        print "You're inside of unbound method",(a**b)
        
    
    def normalMethod(self): #instance method
        print "I'm a generic fella!"
        

objBU = BOUND_AND_UNBOUNDCLASS(10,20,30)
objBU.boundMethod()
# objBU.unboundMethod(1,2)
        
    
    





