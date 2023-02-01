'''
FUNCTION: A function is a block of organized, reusable code that is used
to perform a single, related action. Functions provide better modularity for
your application and a high degree of code reusing.

TYPE OF FUNCTION:
1. BUILT-IN FUNCTION
2. USER DEFINED FUNCTION

FUNCTION ARGUMENTS:
1.Required arguments
2.Keyword arguments
3.Default arguments
4.Arbitary arguments (args & kwargs)

'''


-----------------------------------------------------------------------------
# defining the functions by passing an arguments:(REQUIRED ARGUMENTS or USER-DEFINED ARGUMENTS)
-----------------------------------------------------------------------------
def func(a,b):
	c=a+b
	print c

func(5,8)

-----------------------------------------------------------------------------
        # defining the functions with default arguments:
-----------------------------------------------------------------------------

def func(a,b=5):
	c=a+b
	print c

func(5)
func(50,100)
-----------------------------------------------------------------------------
# defining the functions with Keyword arguments:
-----------------------------------------------------------------------------

def func(name,info):
	print name
	print info

func(name = "Python", info="keywords") # keyword argument
func(info = "Keyword", name="Python") # keyword with out of order
func("python",info="keyword") # positional argument follows keyword argument
-----------------------------------------------------------------------------
# defining the class:
-----------------------------------------------------------------------------

class abc(object):
    def a(self,val):
        print "Hi A!!",val
    def b(self,val2):
        print 'Hi B!!'
        
obj=abc()
obj.a(5)
obj.b()


-----------------------------------------------------------------------------

# objects: states and behaviour of the classs.
# class:states and behaviour of an object

# constructor: will help to create an object very effectively
-----------------------------------------------------------------------------

class alphabets(object):
	def __init__(self,a,b):
		self.a=a
		self.b=b
		pass
	def A(self):
		print self.a + self.b

	def B(self):
		print self.a*self.b

bb=alphabets(5,9)
bb.A()
bb.B()

-----------------------------------------------------------------------------

# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
# 
# The __init__ method for initialization is invoked without any call, when an instance of a class is created,

class EbookRoom():
    
    def __init__(self,a):
        self.a = a
    
    def __repr__(self):
        return "EBook representation"
    
    def Python(Trainee, Trainer='Jai'):
        print "Hello!",Trainee
        print "Trainer:",Trainer
    
    def MachineLearning(self):
        print "Hello!",Trainee
        print "Trainer:",Trainer
 
  
obj = EbookRoom("Mani")  
print obj  

--------------------------------------------------