## Example 1
try:
    print(s)
except: 
    print("Something is wrong!")
finally:
    print("Finally always execute after try-except.")

## Example 2

y =10
try:
    print (z)
    x = y/0
except NameError :
    print ("value error")
except Exception as e:
    print("Something is wrong!")
    print (e)


## Example 3
class Error(Exception):
    def __init__(self):
        pass

def func(x,y):
    try:
        if x==y:
            print("Both values are same")
        else:
            raise Error()
    except Error:
        print("Values are not equal....")
func(1,2)

## Example 4
class Error(Exception):
    def __init__(self,num):
        self.num=num
        print (num)
        pass

def func(x,y):
    try:
        if x<0:
            raise Error(x)
        else:
            print("Its positive value....")
        
    except Error:
        print(x,"is a negative value...")
        
func(-5,8)