'''POLYMORPHISM---PROCESS THE OBJECTS DIFFERENTLY BASED ON THEIR DATA TYPES
TWO METHODS:
1. METHOD OVERLOADING
2. METHOD OVER RIDING
'''

# METHOD OVERLOADING -DEVOLPING THE FUNCTION WITH THE SAME NAME AND DIFFERENT ARUGUMENTS
# BASED ON DATA TYPE
# based on sequence 
# based on number of arguments


class A(object):

    def __init__(self):
        pass

    def add(self, a, b):
        print self.a + self.b

    def add(self, a, b, c):
        print a + b + c

#Method overloading is not possible
# This is compile time polymorphism. 
x = A()
x.add(1,2)

# METHOD OVERRIDING - Inherting the method of super class and changing the 
# method implementation according  to the subclass specifications

class A(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def m1(self):
        print "inside A"

class B(A):

    def __init__(self):
        print ("b constructor")
    def m1(self):
        print "inside b"

bb = B()
bb.m1()


# SUPER METHOD- It's a method which helps to switch data's from one class to another.

class A(object):
    def __init__(self,a,y):
        self.a=a
        self.b=y
        print("A class is called")
        
    def add(self):
        print "addition from A class:%d"%(self.a,self.b)

# class B(A):
#     def __init__(self):
#         print("B class is called")
#         A.__init__(self,3,4)

class C(A):
    def __init__(self,x,y):
        print("C is called")
        self.x=x
        self.y=y
        super(C,self).__init__(x,y)
        
    
x=C(5,4)
print(x)
# y=B()
# print(y)
x.add()
-------------------------------------
#EG:2 # Accessing the local variables of child class
#without using super method
---------------------------------

class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print (self.x + self.y)  # accessing the child class local variables
    
class firstChild(A):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #super(firstChild,self).__init__(x,y)
    def multiplication(self):
        print(self.x * self.y)

if __name__ == '__main__':
    myObj = firstChild(10, 20)
    myObj.multiplication()
    myObj.add()
