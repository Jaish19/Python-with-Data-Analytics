-------------------------------------------------------------------------
#                 SET: ITS A COLLECTION OF NON-DUPLICATE ELEMENTS
----------------------------------------------------------------------------
s1=set()
type(s1)

l1=[1,1,1,2,2,1,2,3,4,5]

set(l1)

s2=set(l1)

s2.add(9)
s2.add(100)
s2


s1=s2

del s1

len(s1)

s1.pop()

s4=s2.copy()


s2.clear()


s1={1,2,3,4,5}
s2={1,8,9,7,6}


s1.difference(s2)

s1.difference_update(s2)

s2.discard(8)

s2.discard(1)

s2.intersection(s1)

s2.intersection_update(s1)




s1.symmetric_difference(s2)

s1.symmetric_difference_update(s2)

s1.union(s2)   # combining two sets

s1.issuperset(s2)  # both should equal to return True


