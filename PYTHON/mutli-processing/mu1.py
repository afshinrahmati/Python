# Multi_Processing that mean when the program is sleep or that time wait untill Do some work my program do an other work to this time
import time
from multiprocessing import Process , freeze_support , current_process

start = time.perf_counter()

# 1)) if we dont use multi proccesing ==> it run 6s Because it sleep 3 time and we call 2 time the function 3 + 3 = 6
# def show(name):
#     print("what is your name ?")
#     time.sleep(3)
#     print(name,print)
    
# show("afshin Rahmari")    
# show("amir Rahmari")    
# end = time.perf_counter()

# print(end-start) # ==> 6 second

# 2)) when it run just happend in 3 second becasue we use process and process that mean when programing is sleep go and do an other work

def showProcess(name):
    print("What is your name?")
    # this show with process in runing
    print(current_process())
    time.sleep(3)
    print(name)

if __name__ == '__main__':
    freeze_support()
    start = time.perf_counter()
    
    p1 = Process(target=showProcess, args=("Afshin Rahmati",),name="First")
    p2 = Process(target=showProcess, args=("Amir Rahmati",),name="Second")
    
    p1.start()
    p2.start()
    
    p1.join()  # Wait for p1 to finish
    p2.join()  # Wait for p2 to finish
    print(p1.is_alive()) # still exist
    end = time.perf_counter()
    print(f"Total time taken: {end - start} seconds") # 3 second because it work untill even the program is wait for do an other work