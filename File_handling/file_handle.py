
# fw=open('sample.txt','w')
# fw.write('Write a new text\n')
# fw.write('and save it\n')
# fw.close()

# fr=open('sample.txt','r')
# view=fr.read() # To read entire contents from the file
# print(view)
# fr.close()


fo = open("sample.py", "a")
fo.write('print ("hello world")\n')
# fo.write("welcome\n")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
fo.close()

with open('sample.py','r') as f:
    contents=f.readlines() 
    print (contents)
for i in contents:
    print(i)


# # f = open("myfile.txt", "x")