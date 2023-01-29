''' Tuple : is a collection of Immutable python objects
----------------------------
In-built functions:
------------------------------
Length
Concatenation
Repetion
Membership
Iteration

-------------------------------
Other Built-In functions:
-------------------------------
min
max
tup(seq)
count
index
del

----------------------------------------'''
-----------------------------------------------
#     REPRESENTATION AND BUILT-IN FUNCTIONS
----------------------------------------------

t1=tuple()

t1=()

t1=(1,2,3,4,5,6,'python')

t2 = 5,2,8,'xyz'

t3= 3, # way of another tuple repr.

type(t1)

t1=(1,2,'a','b',2.555)

t1[0]    # capturing the values based on indexing

t1[1]

t1.index('python')  # will give index value of given object

t1.index(6)

-----------------------------

# 1. Length

t1=(1,2,5,8,7,4,9,'a','z')

len(t1)


-----------------------------------------

#2. Concatenation

t2=(99,74,'python')

a=5

t1 + a  # will throw error concatenation possible between two lists


t1 +t2  # will work

-----------------------------------------

# 3. Repetion

l3=(1,2)

l3*2

a= 'python'

a*2

--------------------------------------

#4. Member ship

t1=(1,2,5,8,7,4,9,'a','z')

4 in t1

'a' in t1

-----------------------------------------

# 5. Iteration

for i in t1:
     print i


#5.1 Eg.
     
for i in t1:
     print i*2

# 5.2 Eg.

for i in t1:
     print t1.index(i), i

# 5.3 Eg. Enumerate

for i in enumerate(t1):
     print i


---------------------------------------------
#         OTHER BUILT-IN FUNCTION
---------------------------------------------

'''

count - will get the no. of occurrences of given python objects
min - will get minimum value from list
max - will get maximum value from list
del - will delete the complete list
'''


t1.count(4)

min(t1)

max(t1)


del t1

del t1[2]   # check it

del t1[len(t1)-2]   # check it


----------------------------------------------------
#     LIST AND TUPLE SEQUENCE
---------------------------------------------------

t2=(1,2,4,5,8,7)

list(t2)   # convert tuple into list(tuple sequence)


l1=[1,2,4,7,8,9,(4,8,'a')]

tuple(l1)


-----------------------------------------
#           NESTED TUPLE
------------------------------------------

t1=(1, 2, 3, 4, 5, 7, 8, 'abc', (100, 90, 80), (10, 20, 30))

# output : [1, 2, 3, 4, 5, 7, 8, 'abc', [100, 90, 80], [10, 20, 30]]

for i in enumerate(t1):
     print i


-------------------------------------------------


#tuples are faster

#python -mtimeit -s"x,y,z=1,2,3" "[x,y,z]"
#python -mtimeit -s"x,y,z=1,2,3" "(x,y,z)"

# Tuples doesnt need copies

a = (1, 2, 3)
b = tuple(a)
a is b

a = (1, 2, 3)
b = list(a)
a is b


#Less memory than list
import sys
sys.getsizeof(tuple((range(10))))
sys.getsizeof(list((range(10))))






