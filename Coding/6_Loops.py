# while loop
c = 0
while (c < 10):  # while True:
    print(c,end='')
    c += 1  # c = c+1

# prints 0good1good2good3god456789

# for loop
print ("\n For loop enumeration")
numbers = [1, 2, 4]
#for (i=0;i<len(numbers);i++)

for x in numbers:
    print(x)

# prints 1
#        2
#        4


for i,x in enumerate (numbers):
    print(i,x)

# prints 0 1
#        1 2
#        2 4

print ("For loop range")
x = 5
for c in range(x):  # for (i=0,i<5,i++)
    print(c)

# prints 0
#        1
#        2
#        3
#        4

print ("For loop with steps")

for c in range (0,10,2):  #for (i=1,i<10,i+2)
	print (c)

# prints 0  1
#		 2  3
# 		 4  5
# 		 6  7
# 	     8  9

print ("For loop with negative steps")
for c in range (10,0,-2):
	print (c)
	#cal = c * .5

# prints 10
#		 8
# 		 6
# 		 4
# 	     2