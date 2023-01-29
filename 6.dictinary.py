--------------------------------------------------------------
#     DICTIONARY: ITS A COLLECTION OF KEYS AND VALUES
--------------------------------------------------------------

d1={}

d1 = dict()
type(d1)

d1={'a':1,'b':2}
d2={'name':'jai','Age':24,'location':'chennai'}
d3={1:1,2:4,3:9}

len(d1)

d1.keys()
d1.valus()


c=d1.keys()
type(c)
d=d1.values()
type(d)


for i in d1:
	print i


d1['c']=3
d1['d']=4

d1.update({'e':5,6:7})

d1.copy()

d1.clear()

-----------------------------------------------------
# Dictionary with Iterations
-----------------------------------------------------
# Eg.1

for k,v in d1.items():
    print k,v


# Eg. 2    
for k,v in d1.items():
    print(k,v**2)


# Eg.3
l1=[1,1,1,1,2,2,3,3,3]
d4={}
for i in l1:
    d4[i]=l1.count(i)

# Eg. 4

l1=[1,2,4]
d1={}
for i in l1:
        d1[i]=[]
        for i in l1:
                d1[i] = i

print d1

# output : {1: 1, 2: 2, 4: 4}   ---> dictionary won't assign the same key to another key

---------------------------------------------------------

# COUNTER
----------------------------------------------------------

from collections import Counter
var_one='pppyyyytttthooonnnnn'
count=Counter(var_one)
print(count)

---------------------------------------------------------------
# SORTED AND ZIP
---------------------------------------------------------------

d1={'A':1,'B':2,'C':3}

sorted(d1.keys())
sorted(d1.values())

# ZIP

l1=['a','b','c','d']
l2=[1,2,3]

zip(l1,l2)
dict(zip(l1,l2))

-----------------------------------------------------------------
#Ordered Dictionary
---------------------------------------------------------------


from collections import OrderedDict
 
print("This is a Dict:")
d = {}
d['a'] = 1
d['b'] = 2
d['d'] = 3
d['c'] = 4
 
for key, value in d.items():
    print(key, value)
 
print("This is an Ordered Dict:")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
for key, value in od.items():
    print(key, value)

print("After changing:")
od['c'] = 5
for key, value in od.items():
    print(key, value)

print("After deleting:")
od.pop('c')
for key, value in od.items():
    print(key, value)
 
print("After re-inserting:")
od['c'] = 3
for key, value in od.items():
    print(key, value)