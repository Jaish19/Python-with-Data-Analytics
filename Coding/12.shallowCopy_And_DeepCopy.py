#SHALLOW_COPY
# A shallow copy creates a new object which stores the reference of the original elements.

# So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.

l1=[1,2,3,4,5,6,7,8]

l2=l1
l2.append(9)
l2.append(60)
print (l1)
print (l2)

# [1,2,3,4,5,6,7,8]
# [1,2,3,4,5,6,7,8,9,60]


import copy

l1=[1,2,3,4,5,6,7,8]
l2=copy.copy(l1)
l2.append(9)
l2.append(60)
print (l1)

---------------------------------------------------------------------
# DEEP_COPY
# A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

import copy

l1=[1,2,3,4,5,6,7,8]

l2=copy.deepcopy(l1)
l2.append(9)
l2.append(60)
print (l1)