EXAMPLE 1:

def sum(*args):
	s=0
	for i in args:
		s+=i
	print('sum is:',s)

sum(1,22,3)

---------------------------------------

def sum(a,b,c):
    print(a,b,c)
          
c=[1,2,3]        
sum(*c)

----------------------------------------

def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i, j)
 
my_func(name='tim', sport='football', roll=19)

--------------------------------------------------------

def test_var_args_call(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

kwargs = {"arg3": 3, "arg2": "two"} 
test_var_args_call(1, **kwargs)
-------------------------------------------------

def test_var_args_call(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

args = ("two", 3)
test_var_args_call(1, *args)
---------------------------------------------------

def test_var_kwargs(farg, **kwargs):
    print ("formal arg:", farg)
    for key in kwargs:
        print ("another keyword arg: %s: %s" % (key, kwargs[key]))

test_var_kwargs(farg=1, myarg2="two", myarg3=3)

-------------------------------------------------------

