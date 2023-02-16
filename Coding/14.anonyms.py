-----------------------------------------------------------------------------------------
# MAPPING : MAPPING IS FUNCTION WHICH HELPS TO MAPPING THE FUNCTION AND INPUTS
-----------------------------------------------------------------------------------------


def square(x):
    return x**2

l3 = (list(map(square, [1,2,4,5,654,5,65,778])))
print (l3)


-----------------------------------------------------------------------------------------
# LAMBDA: ANONYMS FUNCTION IS A FUNCTION THAT IS DEFENIED WITHOUT FUNCTION
-----------------------------------------------------------------------------------------

#example 1
x = lambda a, b : a * b
print(x(5, 6))


#example 2
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#example 3
def testfunc(num):
    return lambda x : x * num

result = testfunc(2)

print(result(9))

#example 4
def testfunc(num):
    return lambda x : x * num

doubler = testfunc(2)
tripler = testfunc(3)

print(doubler(9))
print(tripler(9))

#example 5
l1=[1,2,3,4,5]
l4=[7,8,9,9,3]

print(list(map(lambda x,y: x*y, l1, l4)))


print(list(map(lambda x,y: x/y, l1, l4)))


-----------------------------------------------------------------------------------------
# FILTER: FILTER WILL HELP TO FILTERING THE VALUES
-----------------------------------------------------------------------------------------

print(list(filter(lambda x: x%2==0, [1,2,3,5])))

print(list(filter(lambda x: x<=10 , list(range(1,20)))))


-----------------------------------------------------------------------------------------
# REDUCE: ITS AN FUNCTION WILL HELP TO REDUCE THE SET OF INPUTS
-----------------------------------------------------------------------------------------
from functools import reduce
print(reduce(lambda x,y: x*y, [1,2,3,4,5]))

from functools import reduce
print(reduce(lambda x,y: x*y, list(range(1,6))))

    '''
    [1,2,3,4,5]
    [(1,2),3,4,5]
    [(3),3,4,5] --> [(3,3),4,5]
    [(6),4,5] ---> [(6,4),5]
    [(10),5] --> [(10,5)]
    [15]
    '''
