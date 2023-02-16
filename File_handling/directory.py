import os
if os.path.exists('myfile.txt'):
    print ("File exists")

else: 
      with open("myfile.txt", 'a') as fr:
        fr.write("new gen\n")
        fr.write("new gen1")
        fr.write("new gen2")

# import os
# print(os.getcwd()) # TO GET CURRENT WORKING DIRECTORY
# print(os.path.abspath('.')) # to get current working directory
# print(os.listdir('.')) # directory listdir
# # os.chdir("gum") # changing the directory
# # print(os.getcwd()) 
# # os.chdir("../")# go back to parent directory
# # print(os.getcwd())

# #os.mkdir("new", exist_ok = False)

# # os.mkdir("D:\\Petramount\\Courses\\Python\\New\\Final_Content\\File_handling\\new") # to create the new directory..if the directory is already exist it wil throw an error
# # print(os.getcwd())

# #os.rename('new','new_one')

# # os.remove('old.txt')

# # os.rmdir('new_one')

# import shutil
# shutil.rmtree('new_one')