__author__ = 'Sanjay'

#calculating a sum of list of numbers.

def sumOfList(inp):
    s = 0
    for i in inp:
        s = s +i
    print (s)
    return s

#Recurssion methodology now
# three LAWS OF RECURSSION
# A recursive algorithm must have a base case.
# A recursive algorithm must change its state and move toward the base case.
# A recursive algorithm must call itself, recursively.


def sumRec(inp):
    if len(inp) == 1:
        return 1
    else:
        return inp[0] + sumRec(inp[1:])


def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])
   return numList

if __name__ == '__main__':
    sumOfList([1,2,3,6,7,8,9,65,6])
    sumRec([1,90,80,700]) # 3 RECURSSIVE CALLS WIL HAPPEN (TOTAL LENGTH - 1)
    listsum([1,90,80,700])


-------------------------------------------------------------------------------

# Recursion to print 0,1,2,3,4......100

def recursion(s):
    if s < 100:
        print(s) # General recursion value to print as 0,1,2,3...
        recursion(s+1)
        print(s) # post reversal 99,98,97,96,......1
        
recursion(s=0)

-------------------------------------------------------

# Recursion concept - Post reversal using (L & R) two pointers.

def postReversal(lst, L, R):
    if L >= R:
        return lst
    temp = lst[L]
    lst[L] = lst[R]
    lst[R] = temp
    
    return postReversal(lst, L+1, R-1)


l1=[1,2,3,4,5,6,7,8,9]
print(postReversal(l1, L=0,R=len(l1)-1))


--------------------------------------------------------