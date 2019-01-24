import threading, time

shared_resource = 0


class myThread(threading.Thread):


    def __init__(self, name, counter, algorithm):
        threading.Thread.__init__(self)
        self.threadID = counter; self.name = name; self.algorithm = algorithm; self.counter = counter

    def run(self):
        global shared_resource
        print("Starting " + self.name)
        threadLock.acquire()
        if self.algorithm:
            for i in range(3):
                time.sleep(1)
                shared_resource += 1
                print('{}[{}]: resource is {}\n'.format(self.name, self.counter, shared_resource))
        else:
            ...
        threadLock.release()
        print("Exiting " + self.name)


threadLock = threading.Lock()
thread1 = myThread("Thread", 1, True); thread2 = myThread("Thread", 2, False)
thread1.start(); thread2.start()
thread1.join(); thread1.join()
print("Exiting the Program!!!")