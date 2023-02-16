-----------------------------------------------
#              USER-INPUTS
-----------------------------------------------


user_input= raw_input("Enter the value:")

user_input_one= int(raw_input("Enter the value:"))

user_input_two= str(raw_input("Enter the value:"))

---------------------------------------------------
# Getting the input as list type


val= str(raw_input("Enter the value:")).split()

-----------------------------------------------------
# striping the empty space from the user input

val_one= str(raw_input("Enter the value:")).strip()

----------------------------------------------------

# Eg. 1

for i in range(int(raw_input("Enter the iteration count:"))):
     print ("Count is {}".format(i))

-----------------------------------------------------
#                   RANDOM MODULE
---------------------------------------------------

import random

print (random.randint(0, 5))

random.random() * 100

random.choice( ['red', 'black', 'green'] )


myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
random.choice(myList)

-------------------------------------------------
# Eg. 1

import random
for i in range(3):
    print (random.randrange(0, 101, 5))
------------------------------------------------------
# Eg. 2

from random import shuffle
x = [[i] for i in range(10)]
shuffle(x)

--------------------------------------------------

