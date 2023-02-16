def f(): 
    print (s)
s = "I hate spam"
f()

# The variable s is defined as the string "I hate spam", before we call the function f(). 
# The only statement in f() is the "print s" statement. As there is no local s, the value from the global s will be used. So the output will be the string "I hate spam". The question is, what will happen, if we change the 
# value of s inside of the function f()? Will it affect the global s as well? We test it in the following piece of code:

-------------------------------------------------------------------------------------------------------------------
# 2.

def f(): 
    s = "Me too."
    print (s) 

s = "I hate spam." 
f()
print (s)
----------------------------------------------------
3.

def f(): 
	print (s)
	s = "Me too."
	print (s)


s = "I hate spam." 
f()
print (s)
--------------------------------------------------------

# 4.Python "assumes" that we want a local variable due to the assignment to s inside of f(), 
# so the first print statement throws this error message. Any variable which is changed or created inside of a function is local, if it hasn't been declared as a global variable. To tell Python, 
# that we want to use the global variable, we have to use the keyword "global", as can be seen in the following example:

def f():
    global s
    print (s)
    s = "That's clear."
    print (s) 


s = "Python is great!" 
f()
print (s)


-----------------------------------------------------------------------------
# 5.Local variables of functions can't be accessed from outside, when the function call has finished:


def f():
    s = "I am globally not known"
    print (s) 

f()
print (s)


----------------------------------------------------------------
# 6. The following example shows a deliberate combination of local and global variables and function parameters:


def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print (a,b,x,y)

a,b,x,y = 1,15,3,4
foo(17,4)
print (a,b,x,y)

