------------------------------------------------------------
#            CONTROL STRUCTURES  AND LOOPS
-----------------------------------------------------------

# if - else statements

# Eg. 1

val = 5

if val==5:
     print "Expected Value"
else:
     print "Unexpected Value"

-------------------------------------------

# Eg. 2

var=15

if val > 20:
     print "Value One"
elif val >10:
     print "Value two"
elif val==8:
     print "Value three"
else:
     print "None"

-------------------------------------------

# Eg. 3

l1=[4,7,8,5,9,65,100]

if 5 in l1:
     print "Hi Buddy"
else:
     print "Exit"

-------------------------------------------------
# Eg. 4 Based on address comparision
l1=[4,7,8,5,9,65,100]
l2 =[4,7,8,7,8,9]

if l1 is l2:
     print "Hi Buddy"
else:
     print "Exit"

-----------------------------------------------------
# Eg. 5

l1=[1,2,3]
a,b=100,30

if a and b not in l1:
     l1.extend([a,b])
else:
     print "It's Exist"


------------------------------------------------------------
#                 WHILE LOOP
----------------------------------------------------------

# Eg. 1 : Infinite loop execution

while True:
     print "Hello Guys"


--------------------------------------------
# Eg. 2:

val = 1

while val ==1:
     print "This is available"

---------------------------------------------

# Eg. 3 : Else statement with loop

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"


------------------------------------------------------- 
# Eg. 4 : Single line statement

flag = 1
while (flag): print 'Given flag is really true!'


---------------------------------------------------------
#             RANGE FUNCTION
----------------------------------------------------------

type(range(10))
l1=list(range(0,20))

range(5)
range(-5,0)

range(0,10)
range(5,15)

range(0,20,2)
range(0,5,-1)  # check it
range(5,0,-1)
range(10,0,-2)


-------------------------------------------------------------
#                 FOR LOOP ITERATION
-----------------------------------------------------------------
#Eg. 1

for i in range(10):
     print i

--------------------------------------------------

# Eg. 2

a = 'Python'
l1=[]
for i in a:
     if i in ['a','e','i','o','u']:
          l1.append(i)
     else:
          print "No vowels"

--------------------------------------------------

# Eg. 3

l1=[]

for i in range(1,15):
     if i%2 == 0:
          l1.append(i)
     else:
          print "Not an even number"

--------------------------------------------------------------------
# Eg. 4 FOR LOOP WITH BREAK STATEMENT AND ELSE STATEMENT
---------------------------------------------------------------------

for i in b:
     if i not in b:
	     print "Not exist"
	     break
else:
	print "Came out from loop"

----------------------------------------------------------------

