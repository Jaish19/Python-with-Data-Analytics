# GENERATORS:
# Generators simplifies creation of iterators. A generator is a function that produces a 
# sequence of results instead of a single value.

def foo():
    print "begin"
    for i in range(3):
        print "before yield", i
        yield i
        print "after yield", i
    print "end"

for i in foo():
	print(i)

-------------------------------------------------------------------
# Example 1.1:
'''
# Generator function:

A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of
a def contains yield, the function automatically becomes a generator function.
'''
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)


-----------------------------------------------------------
# Example 1.2:
'''
Generator object:
 Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).
 '''
# A Python program to demonstrate use of 
# generator object with next() 
 
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(x.next()); # In Python 3, __next__()
print(x.next());
print(x.next());

-----------------------------------------------------------

# EXAMPLE 2

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i
def norms():
    return 1

def take(n, seq):
    """Returns first n values from the given sequence."""
#     seq = iter(seq)
#     print(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

print take(5, squares()) # prints [1, 4, 9, 16, 25]

# EXAMPLE 3

import random

def lottery():
    # returns 6 numbers between 1 and 40
  for i in range(6):
    yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... ",  )



# EXAMPLE FOR FIBONACCI SERIES USING GENERATORS

def flow():
    i=1
    while True:
        yield i
        i+1
    
     
def operation():
    n1=0
    n2=1
    for i in flow():
        nth=n1+n2
        yield nth
        n1=n2
        n2=nth
        

def fib(n,jai):
    result=[]
    for i in range(n):
        result.append(jai.next())
        
    return result

    
        
print(fib(10,operation()))


# SIMPLE GENERATOR WITH DOUBLE METHODS

def validation(i):
    if i > 2:
        yield i
    else:
        yield 1

def func(value):
    for i in value:
        for j in validation(i):
            yield j
        
for i in func([1,2,3]):
    print(i)





















