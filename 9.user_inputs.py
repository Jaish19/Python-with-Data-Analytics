-----------------------------------------------
#              USER-INPUTS
-----------------------------------------------

user_input= raw_input("Enter the value:")

user_input_one= int(raw_input("Enter the value:"))

user_input_two= str(raw_input("Enter the value:"))

---------------------------------------------------
# Getting the input as list type


val= str(raw_input("Enter the value:")).split()

val = map(int, raw_input("Enter:").split()) # collecting int input

-----------------------------------------------------
# striping the empty space from the user input

val_one= str(raw_input("Enter the value:")).strip()

val_one = raw_input("Enter the input:").strip('val')
'''
val_one = 'ue'  ----> 'val' will be striped here:)
'''
val_one = raw_input("Enter the input:").split().strip('ue')
'''
Here, it'll throw an attribute error because list don't
have the strip() attribute.
'''
val_one = raw_input("Enter the input:").split()[0].strip('ue')
'''
input = 'value error'
val_one = 'val'
'''

----------------------------------------------------

# Eg. 1

for i in range(int(raw_input("Enter the iteration count:"))):
     print "Count is {}".format(i)

-----------------------------------------------------
#                   RANDOM MODULE
---------------------------------------------------

import random

print random.randint(0, 5)

random.random() * 100

random.choice( ['red', 'black', 'green'] )


myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
random.choice(myList)

random.shuffle(list)

-------------------------------------------------
# Eg. 1

import random
for i in range(3):
    print random.randrange(0, 101, 5)
------------------------------------------------------
# Eg. 2

from random import shuffle
x = [[i] for i in range(10)]
shuffle(x)

--------------------------------------------------

