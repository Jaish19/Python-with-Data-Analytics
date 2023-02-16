# Example 1:

# Python program to handle simple runtime error
 
a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]) )
 
except IndexError:
    print ("An error occurred")

finally:
    print ("Finished the above case successfully...")
'''
#output:
    Second element = 2
An error occurred
'''
---------------------------------------------------------------

# Example 2:

# Program to handle multiple errors with one except statement
try : 
    a = 3
    if a < 4 :
 
        # throws ZeroDivisionError for a = 3 
        b = a/(a-3)
     
    # throws NameError if a >= 4
    print ("Value of b = ", b)
 
# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print ("\nError Occurred and Handled")

'''
OUTPUT:

Value of b =  
Error Occurred and Handled
'''
-------------------------------------------------------------------

# Example 3 Raising an exception

# Program to depict Raising Exception
 
try: 
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not

----------------------------------------------------------------

# Example 4:

def isDivide(x,y):
    try:
    	x/y
    except Exception as e:
    	print (e)
    else:
    	print ("inside else")
    finally:
    	print ("inside finally")

isDivide(1, 10)
isDivide(10, 0)



#METHOD 2
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")




