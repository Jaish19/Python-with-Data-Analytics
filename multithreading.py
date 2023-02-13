'''
MULTITHREADING: It's process where it allows the multiple threads to do 
their same process in parellely or concurrently using the single processors 
and using the same memory space.

It can be simulated using time.sleep function.

threading.activeCount() − Returns the number of thread objects that are active.

threading.currentThread() − Returns the number of thread objects in the caller's thread control.

threading.enumerate() − Returns a list of all thread objects that are currently active.

run() − The run() method is the entry point for a thread.

start() − The start() method starts a thread by calling the run method.

join([time]) − The join() waits for threads to terminate.

isAlive() − The isAlive() method checks whether a thread is still executing.

getName() − The getName() method returns the name of a thread.

setName() − The setName() method sets the name of a thread.

'''
# Example 1 : Creating the thread & starting and joining it until it finishes the 
#execution and capturing the threadID

import threading 
import time
  
def list_outputs(num, val): 

    mtd_1=list()
    print('Current thread ID from list_outputs: {}'.format(threading.current_thread().name))
    for i in range(num):
        time.sleep(2)
        print("List: Iteration : {0} = {1}".format(i, val))
        mtd_1.append(i)
    print("List output here: ",mtd_1) 
  
def set_outputs(num,val):  

    mtd_2 = set()
    print('Current thread ID from set_outputs: {}'.format(threading.current_thread().name))
    for i in range(num):
        time.sleep(3)
        print("Set: Iteration : {0} = {1}".format(i, val))
        mtd_2.add(i)
    print("Set output here:",mtd_2) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=list_outputs, args=(5,'thread_1'), name = 't1') 
    t2 = threading.Thread(target=set_outputs, args=(5,'thread_2'), name='t2') 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start()
    
  
    # waiting to finish up the thread 1 process completely 
    t1.join() 
    # waiting to finish up the thread 1 process completely 
    t2.join() 
    

    # both threads are done  
    print("Operation ends here now!") 

#------------------------------------------------------------------

'''
Example 2: Creating the thread using class.
Threading using class and starting it without using any additional user defined function.

'''

import threading 
import time

class newThread(threading.Thread):
    def __init__(self, threadID, iterNum, holdTime):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.iterNum = iterNum
        self.holdTime = holdTime
        pass
    
    def run(self): 
        mtd_1=set()
        print(threading.current_thread())
        for i in range(self.iterNum):
            time.sleep(self.holdTime)
            result = self.set_outputs(i,mtd_1)
        print("Set output here: ",result) 
      
    def set_outputs(self, num, result_list):  
    
        print("Set: Iteration : {0} = {1}".format(num, self.threadID))
        result_list.add(num)
        return result_list
        
  
if __name__ == "__main__": 
    # creating thread 
    t1 = newThread('Thread_1', 5, 3)
    t2 = newThread('Thread_2', 5, 2)

    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start()
    
  
    # waiting to finish up the thread 1 process completely 
    t1.join() 
    # waiting to finish up the thread 1 process completely 
    t2.join() 
    

    # both threads are done  
    print("Operation ends here now!") 

#----------------------------------------------------------------------------------

'''
Example : 3 - Creating the thread using the class and accessing the methods of class

'''

import threading 
import time

class newThread(threading.Thread):
    def __init__(self, threadID, iterNum, holdTime):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.iterNum = iterNum
        self.holdTime = holdTime
        pass
    
    def run(self): 
    
        mtd_1=list()
        print(threading.current_thread())
        for i in range(self.iterNum):
            time.sleep(self.holdTime)
            print("List: Iteration : {0} = {1}".format(i, self.threadID))
            mtd_1.append(i)
        print("List output here: ",mtd_1) 
      
    def set_outputs(self):  
    
        mtd_2 = set()
        print(threading.current_thread())
        for i in range(self.iterNum):
            time.sleep(self.holdTime)
            print("Set: Iteration : {0} = {1}".format(i, self.threadID))
            mtd_2.add(i)
        print("Set output here:",mtd_2) 
    
    def dict_outputs(self):
        
        mtd_3 = dict()
        print(threading.current_thread())
        for i in range(self.iterNum):
            time.sleep(self.holdTime)
            print("Dictionary: Iteration : {0} = {1}".format(i, self.threadID))
            mtd_3[i] = i*5
        print("Dictionary output here:",mtd_3)
  
if __name__ == "__main__": 
    # creating thread 
    t1 = newThread('Thread_1', 5, 3)
    t2 = newThread('Thread_2', 5, 2)
  
    # starting thread 1 
    t1.dict_outputs() 
    # starting thread 2 
    t2.set_outputs()
    
  
    # waiting to finish up the thread 1 & 2process completely (Here it doesn't require since we're accessing the user-define method instead of run()) 
#     t1.join() 
#     t2.join() 
    

    # both threads are done  
    print("Operation ends here now!") 

# -------------------------------------------------------------------------------

'''
THREADING LOCKING
Example 4: Synthronization Technique

Syncthronization is a process will happen between two or more threads.
Critical section: When two are more concurrent threads are trying to access the particular
segment of the program, that's called Critical section.

Race condition: Concurrent access on the particular segment of program will lead to Race condtion.
when two or more threads are accessing the critical 
section and they try to change it at same time, due to that values of the variable 
may be unpredictable and vary depending on the timings.
'''

import threading 
  
# global variable x 
x = 0
  
def increment(): 
    """ 
    function to increment global variable x 
    """
    global x 
    x += 1
  
def thread_task(lock): 
    """ 
    task for thread 
    calls increment function 100000 times. 
    """
    for _ in range(100000): 
        lock.acquire() 
        increment() 
        lock.release() 
  
def main_task(): 
    global x 
    # setting global variable x as 0 
    x = 0
  
    # creating a lock 
    lock = threading.Lock() 
  
    # creating threads 
    t1 = threading.Thread(target=thread_task, args=(lock,)) 
    t2 = threading.Thread(target=thread_task, args=(lock,)) 
  
    # start threads 
    t1.start() 
    t2.start() 
  
    # wait until threads finish their job 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x))

-----------------------------------------------------------------
'''
THREADING LOCK : 2
'''

import threading
import os
    
def toFind(l1,lock):
    lock.acquire()
    l1=map(int, raw_input("Enter the input values:").split())
    lock.release()
    print("Max value:{},{}".format(max(l1), threading.current_thread().name))
    

lock = threading.Lock()
t1 = threading.Thread(target=toFind, args=(list(),lock), name='t1')
t2 = threading.Thread(target=toFind, args=(list(),lock), name='t2')

t1.start()
t2.start()


t1.join()
t2.join()

print("Ending the progress!")

--------------------------------------------------------------------

'''
OWN TRY: MULTITHREADING WITH FILEHANDLING TECHNIQUE

'''
import threading 
import os
def file_open(mode, list_to_write, lock, threadName):
    global file
    if os.path.exists(file):
        with open(file,mode) as fw:
            for i in list_to_write:
                lock.acquire()
                print "Thread Name :", threading.current_thread().name, i
                fw.write(i)
                fw.write("\n")
                lock.release()
                
    else:
        print("Path not available")
    file_read(file, threadName)
    

def file_read(file, threadName):
    for lines in open(file, 'r').readlines():
        print "From the file :", threadName
    
    


print("Hi Everyone!")
global file

file = raw_input("Please enter your file path here:")
mode = raw_input("Please enter the file mode operation here:")
line_to_write_one = ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y', 'b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
line_to_write_two = ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z', 'a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y']

lock = threading.Lock()

t1 = threading.Thread(target=file_open, args=(mode, line_to_write_one, lock, 'Thread-1'), name='t1')
t2 = threading.Thread(target=file_open, args=('a', line_to_write_two, lock, 'Thread-2'), name='t2')

t1.start()
t2.start()

t1.join()
t2.join()

print "Operarion ends here!"

--------------------------------------------------------------------------