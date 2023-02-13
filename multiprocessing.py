'''
Multithreading is a technique where multiple threads are spawned by a 
process to do different tasks, at about the same time, just one after 
the other. This gives you the illusion that the threads are running in 
parallel, but they are actually run in a concurrent manner. 
In Python, the Global Interpreter Lock (GIL) prevents the threads from 
running simultaneously.

#
1. Multiprocessing is a technique where parallelism in its truest form is 
achieved. 
2. Multiple processes are run across multiple CPU cores, which do 
not share the resources among them. 
3. Each process can have many threads running in its own memory space. 
4. In Python, each process has its own 
instance of Python interpreter doing the job of executing the instructions.


Synchronization between processes

Process synchronization is defined as a mechanism which ensures that 
two or more concurrent processes do not simultaneously execute some 
particular program segment known as critical section.


'''

import multiprocessing
import os

def mtdA():
    print "ID mtdA:",os.getpid()
    print "Reaching the Mtd A here"

def mtdB():
    print "ID mtdB:",os.getpid()
    print "Reaching the Mtd B here"
    

if __name__ == '__main__':
    p1=multiprocessing.Process(target=mtdA)
    p2=multiprocessing.Process(target=mtdB)
    
    p1.start()
    p2.start()
    
    print "ID:",p1.pid
    print "ID:",p2.pid
    
    p1.join()
    p2.join()
    
    print "-I- Ending process"


----------------------------------------------------------------

import multiprocessing
import threading
import os

result=[]
def mtdA():
    global result
    for i in range(10):
        result.append(i)
        print "ID: {} | Value : {}".format(os.getpid(),i)
    print "MtdA:",result
    
def mtdB():
    global result
    for i in range(10,20):
        result.append(i)
        print "ID: {} | Value : {}".format(os.getpid(),i)
    print "MtdB:",result


if __name__ == '__main__':
    t1=multiprocessing.Process(target=mtdA)
    t2=multiprocessing.Process(target=mtdB)
    
    t1.start()
    t2.start()
    
    
    t1.join()
    t2.join()
    
    print "Outside:",result
    
        
    print "Ending the progress"    

    print("Process p1 is alive: {}".format(p1.is_alive())) 
    print("Process p2 is alive: {}".format(p2.is_alive())) 

    
--------------------------------------------------------------------


#MULTIPROCESS WITH CLASS IMPLEMENTATION

import multiprocessing
import time
import os


class ProcessLearning(multiprocessing.Process):
    def __init__(self,iterNum):
        multiprocessing.Process.__init__(self)
        self.iterNum = iterNum
        self.result=[]
    
    def run(self):
        for i in range(self.iterNum):
            self.mtdA()
            print("ID : {} and value is {}".format(os.getpid(), i))
            self.result.append(i)
            
        
    def mtdA(self):
        for i in range(self.iterNum):
            print("ID : {} and value is {}".format(os.getpid(), i))
            self.result.append(i)


if __name__ == '__main__':
    p1 = ProcessLearning(5,)
    p2 = ProcessLearning(6,)
    
    p1.start()
    p2.start()
    
    print("ID out:",p1.pid)
    print("ID Out:",p2.pid)
    
    p1.join()
    p2.join()
    
    print("Status p1:",p1.is_alive())
    print("Status p2:",p2.is_alive())
    
    print("Process Over!")


------------------------------------------------------------------------------------------