--------------------------------------------------------------
#                 LIST COMPREHENSION
--------------------------------------------------------------

l1= [i for i in range(10)]

# l1= []
# for i in range (10):
# 	l1.append(i)

l1 = [i**2 for i in range(0,10,2)]

l2=[]


l1=[i for i in range(10) if i%2==0]

# l1 = [0,2,4,6,8]

# l1 = []
# for i in range(10):
# 	if i%2==0:
# 		l1.append(i)

l2=[[1,2,3],[4,5,6]]


l1 =[j for i in l2 for j in i if j > 4]

# l1 =[]
# for i in l2:
# 	for j in i:
# 		if j>4:
# 			l1.append(j)

--------------------------------------------------------------
#                 TUPLE COMPREHENSION
--------------------------------------------------------------

t1= (i for i in range(10))

l1=[1,2,4,'a','b']

t1=(i for i in l1 if type(i)==str)

t1=tuple(i for i in l1 if type(i)==str)

# Though tuple comprehension is avail for tuple, final output will be in generator object. 

--------------------------------------------------------------
#                 DICTIONARY COMPREHENSION
--------------------------------------------------------------
l1=[1,2,1,1,1,2,2,2,3,4,5,5]

d4={i:i**2 for i in l1}

d4={i:l1.count(i) for i in l1}

d4 ={i:l1.index(i) for i in l1}

--------------------------------------------------------------------
