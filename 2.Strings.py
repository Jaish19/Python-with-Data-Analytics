------------------------------------------------------------
# STRINGS
------------------------------------------------------
a=5
b=6
c='python'
d='2.5'
e='20'

a+b  # will give addition of two numbers

a+c  # check it out - TypeError will occur

#Typecasting

a+int(c)    # Eg. 1 - ValueError will occur

str(a) + c  # Eg. 2 - converting int to str is possible


c + d # Eg. 3 - Both are string type and can expect no error

a+d # Eg. 4 - It should work? but How?

a + float(d) # Eg. 5 : converting d value to floating

float(d) + int(e)  # Eg. 6 : Output?

------------------------------------------------------------------
# 2. print statements
---------------------------------------------------------------

print 'Python'

print 'python's dominating the programming world'

print "python's dominating the programming world"

print "C:\Users\dell\notepad"   # will go to next line when it met \notepad '\n' --> next line place holder

print r"C:\Users\dell\notepad"  # will take as a directory now


-------------------------------------------------------------------
# FORMAT PRINTING
--------------------------------------------------------------

a= 5
b= 'Crash course'
c= 'will give great support'

print "Python",b

print "python {}".format(b)

print "python {0},{1}".format(a,b)

print '''Hi
welcome 'students' '''  # Using triple codes for documentation purposes



----------------------------------------------------------------------------
# 2. String Built-in functions
--------------------------------------------------------------------------

a= 'Python'

b= 123

a**2    # check it

a*2      # Repetion (check)

len(a)    # to find the length

max(a)   # to find max of 'a'  

min(a)   # to find min of 'a'

len(b), max(b), min(b)   # will give TypeErrors since integers has no attribute like these.

c='123python'

len(c), max(c), min(c)   # alphaNumeric (try it and get knowledge)


-------------------------------------------------------------------
# Join operator
-------------------------------------------------------------------

a= 'Python'

' '.join(a)

'-'.join(a)   # string will seperate by '-'

'*'.join(a)


---------------------------------------------------------------------
# String slicing
--------------------------------------------------------------------
a='Mathematic'

a[0]
a[5]
a[-1]
a[-3]
a[0:2]

a[1:5]
a[0:]
a[:10]

a[1:6:2]

a[::-1]    # Reversing the string

a[-1:-4]   # Reversing is not possible in slicing(will print empty list)

a[-1:3]   # Reversing is not possible in slicing(will print empty list)

a[3:-3]  # This will be possible because this action is happening towards the positive way

a[-3:-2]  # This will be possible because this action is happening towards the positive way

a[:-4]

a[-1:]

a[:]

a[::]   # will print complete string

a[:len(a)]

a[len(a)-2:len(a)]

---------------------------------------------------------------------------










 

















