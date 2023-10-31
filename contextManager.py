'''
Context Managers - Used to manage the resources like file or db connection.

Once we opened the file, it's good to close them after usage in order to avoid some conflicts. With 
the help of context manager we can ensure that it'll closing the resource once they used.

'''
class FileContextManaging(object):
    def __init__(self,fileName, mode):
        self.fileName = fileName
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.fileName, self.mode)
        self.file.write("File created by contextManaging\n")
        return self.file
    
    def __exit__(self, *args):
        self.file.write("File closure initiated\n")
        self.file.close()
        
with FileContextManaging("jai.txt", "w") as file:
    file.write("Secret data will be written here!\n")
    
print(file.closed)