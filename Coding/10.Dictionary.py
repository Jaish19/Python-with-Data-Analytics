--------------------------------------------------------------
#     DICTIONARY: ITS A COLLECTION OF KEYS AND VALUES
-------------------------------------------------------------

d1={}

d1 = dict()
type(d1)

d1={'a':1,'b':2}
d2={'name':'Deepan','Age':18,'location':'chennai'}
d3={1:1,2:4,3:9}

len(d1)

d1.keys()
d1.values()


c=d1.keys()
type(c)
d=d1.values()
type(d)




# declare a dictionary
d = { "1" : "Ironman", 
      "2" : "Captain America", 
      "3" : "Thor",
      "4" : "Hulk"
    }

# loop over dictionary
for key in d:
    print(key)    # prints each key in d
    print(d[key]) # prints value of each key in d (unsorted)

# change values in the dictionary
d["2"] = "Hulk"
for key, value in d.items():
    print(key + " - " + value)

'''
prints
1 - Ironman
2 - Hulk
3 - Thor
'''

# check if key exists in a dictionary
if "3" in d:
    print("Yes! 3 is " + d["3"])
# prints 'Yes! 3 is Thor'

# get length of the dictionary
print(len(d)) # prints 3

# insert a key-value pair to a dictionary
d["4"] = "Thanos"

print (d.items())
# remove a key-value pair from the dictionary
d.pop("4")

# same thing using 'del' keyword
del d["2"]

# clear a dictionary
d.clear()
# delete a dictionary
del d


---------------------------------------------------------

# COUNTER
----------------------------------------------------------

from collections import Counter
l1='pppyyyytttthooonnnnn'
count=Counter(l1)
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