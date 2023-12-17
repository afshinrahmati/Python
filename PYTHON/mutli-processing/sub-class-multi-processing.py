import time
from multiprocessing import Process,freeze_support

start = time.perf_counter()

def show(name,delay):
    print(f'starting {name}...')
    time.sleep(delay)
    print(f'Ending {name}...')

class ShowProcess(Process):
    def __init__(self,name,delay):
        super().__init__();
        self.name = name
        self.delay = delay
    def  run(self) -> None:
        print(self.name,self.delay)
        show(self.name,self.delay)
if __name__ == '__main__':
    freeze_support()        
    p1 = ShowProcess("One",3)
    p2 = ShowProcess("Two",3)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print(f'Time is {end - start}')        