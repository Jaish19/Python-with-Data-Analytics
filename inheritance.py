# INHERITANCE: AN OBJECT ACQUIRING THE PROPERTIES OF AN ANOTHER CLASS

# SINGLE INHERITANCE: A DERIVED CLASS IS CREATED FROM THE SINGLE BASE CLASS

class A(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def add(self):
		return (self.a + self.b)

class firstChild(A):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def multiplication(self):
		print(self.x * self.y)

# 'Whenever we inherit A in firstChild, its not required to override all methods which Parent has.'
# 'In this above code, Add and Subract are the two methods.. ' \
# 'override only when there is a logic change, else no need to calling the method and returns nothing.'

if __name__ == '__main__':
myObj = firstChild(10, 20)
myObj.multiplication()
myObj.add()
# creating an another object for the same class
newObject = firstChild(10,10)
newObject.something()



# MULTILEVEL INHERITANCE: A DERIVED CLASS IS CREATED FROM ANOTHER DERIVED CLASS

class Father(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def behaviour(self):
		print ("I'm father! my behaviour is old.")

	def character(self):
		print "I've the attributes for my own character"

class FirstChild(Father):

	def __init__(self, a):
		self.a = a

	def behaviour(self):
		print ("I'm the child, but I feel responsible")


class SecondChild(FirstChild):
	def __init__(self):
		pass

'''
If method is uncommented, behaviour() will get call by its own class object.
if the method is not available, then it will contact the inherited class.
Even if the FirstChild class also doesn't have behaviour method, then it will contact
Father class for sure and calls behaviour method.
'''
# def behaviour(self):
#     print ("I have my own behaviour")

if __name__ == '__main__':
c = SecondChild()
c.behaviour()
c.character()
print (SecondChild.__mro__)


# MULTIPLE INHERITANCE: A DERIVED IS CREATED FROM MORE THAN ONE BASE CLASS

class Father(object):
	def __init__(self):
		pass

	def getUpEarlyMorning(self):
		print("Get up Early at 6 AM")


class Mother(object): # please don't mind the name of the class

	def __init__(self):
		pass

	def getUpEarlyMorning(self):
		print("Get up Early at 4 AM")


class ChildClass(Mother, Father):  # Method resolution order
# Child is ready to listen both Mother and Father behaviour, but priority goes to mom first.
# Because, we are inheriting "Mother" first. (Method Resolution Order)
	def __init__(self):
		pass

#def getUpEarlyMorning(self):
#print("I will get up at 5 AM")
# pass

if __name__ == '__main__':
b = ChildClass()
b.getUpEarlyMorning()
print (ChildClass.__mro__)


# HIERARCHICAL INHERITANCE: MORE THAN ONE DERIVED CLASS CREATED FROM A SINGLE BASE CLASS


class Father(object):
def __init__(self, x, y):
self.x = x
self.y = y

def myCharacter(self):
print ("Lets help as much as we can!")

def myBehaviour(self):
print ("Old is gold!")


class FirstChild(Father):

def __init__(self,a):
self.a = a

def myCharacter(self):
print ("I'm the first child, I'll get angry at times.")


class SecondChild(Father):  # Method resolution order
def __init__(self):
print("My father is all to me!")


if __name__ == '__main__':
secondObj = SecondChild()
secondObj.myCharacter()
secondObj.myBehaviour()

firstChildObj = FirstChild(10)
firstChildObj.myCharacter()
firstChildObj.myBehaviour() #firstchild doesn't contain myBehaviour method, so it has to contact base myBehaviour only.


# HYBRID INHERITANCE: A DERIVED CLASS IS CREATED FROM ANOTHER DERIVED CLASS AND THE SAME BASE CLASS OF ANOTHER DERIVED CLASS.

class GrandFather(object):
	def __init__(self, x, y):
	self.x = x
	self.y = y

def myCharacter(self):
	print ("Lets help as much as we can!")

def myBehaviour(self):
	print ("Old is gold!")


class Father(GrandFather):

	def __init__(self):
		pass

	def myCharacter(self):
		print ("I have my own Character! I'm a father of two child")


class FirstChild(Father):
def __init__(self):
pass

def myCharacter(self):
print ("I have my own character, May be because I behave like my dad.")


class SecondChild(Father):
def __init__(self):
print ("I dont need to be unique, My Father is already having good character and my grand father is having good"
       "behaviour")


if __name__ == '__main__':
firstChildObj = FirstChild()
firstChildObj.myCharacter()
firstChildObj.myBehaviour()
# firstchild doesn't contain myBehaviour method,
# it contacts father and search for myBehaviour, father also doesn't have
# o it has to contact base myBehaviour only.

secondChildObj = SecondChild()
secondChildObj.myCharacter()
secondChildObj.myBehaviour()


