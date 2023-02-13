'''
DECORATOR

a function that takes another function and extends the behavior of the latter 
function without explicitly modifying it.
'''
# Assigning the function to varialble

def greetings(name):
    return "hi Mr." + name
super=greetings
print(super("Jai"))

# Define functions inside other functions

def greetings(name):
    def inside_function():
        return "hi Mr."
    
    result= inside_function() + name
    return result

print(greetings("suresh"))

# Functions can be passed as parameters to other functions

def greet(name):
    return "hi Mr." + name

def call_func(func):
    need_name="Suresh"
    return func(need_name)
    

print(call_func(greet))

# Functions can return other functions

def initialFunction():
    def call_function():
        return "super I am decorator method"
    
    return call_functionz

start=initialFunction()
print(start())


# inner functions have access to the enclosing scope

def initial_calling(name):
    def second_method():
        return "hi Mr." + name +"!"
    
    return second_method()


start=initial_calling("Suresh")
print(start)

# Composition of Decorators

# EXAMPLE I:
def holdAMobile(name):
     print "Your gadget is ready to proceed..."
     return name
     
@holdAMobile
def takeAPicture():
     print "Hey Champ!!! Here your snap... "
     
takeAPicture()


# EXAMPLE 1:

def get_text(name):
    return "hello Mr." + name


def p_decorator(func):
    def func_wrapper(name):
        return func(name)
    
    return func_wrapper


start=p_decorator(get_text)
print(start("suresh"))

# EXAMPLE 2

def get_text(name):
    return "hello Mr. {0} welcome to the party".format(name)


def p_decorator(func):
    def func_wrapper(name):
        return "{0}".format(func(name))
    
    return func_wrapper


start=p_decorator(get_text)
print(start("suresh"))

# PYTHON DECORATOR SYNTAX

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        print(name)
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("John")




# Composition of Decorators

# EXAMPLE 1:

def get_text(name):
    return "hello Mr." + name


def p_decorator(func):
    def func_wrapper(name):
        return func(name)
    
    return func_wrapper


start=p_decorator(get_text)
print(start("suresh"))

# EXAMPLE 2

def get_text(name):
    return "hello Mr. {0} welcome to the party".format(name)


def p_decorator(func):
    def func_wrapper(name):
        return "{0}".format(func(name))
    
    return func_wrapper


start=p_decorator(get_text)
print(start("suresh"))

# PYTHON DECORATOR SYNTAX

# EXAMPLE 1

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("John")



# EXAMPLE 2


def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        print(name)
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("John")

# EXAMPLE 3

def mtd_one(func):
    def game(name):
        return func(name)
    return game

def mtd_two(func):
    def game(name):
        return func(name)
    return game

def mtd_three(func):
    def game(name):
        return func(name)
    return game

@mtd_three
@mtd_one
@mtd_two
def call_method(name):
    return "Hi Mr." + name


print(call_method("suresh"))

# DECORATING METHOD

def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print my_person.get_fullname()

--------------------------------------------
SIMPLE UNDERSTAND
-------------------------------------------------

def starting(func2):
    def checking(oneBack):
        print("Initiated!")
        return func2(oneBack)
    return checking

@starting
def stateHere(func1):
    def crossVal(temp):
        print("Output on the way!")
        return func1(temp)
    return crossVal

@stateHere
def FinalResult(func):
    def getBack(a,b):
        if a and b != 0:
            print("Final Output here:",func(a,b))
    return getBack

    
@FinalResult    
def add(a,b):
    return a**b


add(5,2)

--------------------------------------------------



def holdAMobile(func1):
    def createNew(name):
        if type(name) is str:
            print("Logic works")
            return func1(name)
        else:
            print("Logic not works here. So killing the process!")
    return createNew
     
@holdAMobile
def takeAPicture(name):
     print ("Hey Champ!!! Here your snap... ",name)
     
takeAPicture(555)