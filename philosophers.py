import time
import threading

lock=threading.Lock()

class eating:
    def __init__(self,person,spoon):
        self.person=person
        self.spoon=spoon
        self.eatCount=0
        self.eatTime=0.5
        self.personNum=len(person)
        self.startTime=0

    def interval(self):
        currentTime=time.time()
        return currentTime-self.startTime

    def timeout(self,time):
        if self.interval()>= time:
            return False
        return True

    def getIndex(self,arr,var):
        i=0
        for a in arr:
            if a==var:
                return i
            i+=1
        return -1


    def looping(self,i):
        i+=1
        if self.personNum <=i:
            return False
        return i

    def checkSpoon(self,index):
        if self.spoon[index]:
            return 1
        return 0


    def checkSecondSpoon(self,index):
        if self.spoon[index-1]:
            return 1
        return 0


    def foo(self,index):
        lock.acquire()
        if self.checkSpoon(index) and self.checkSecondSpoon(index):
            lock.release()
            return 1
        lock.release()
        return 0
        

    def setBusySpoon(self,index):
        if self.spoon[index]:
            self.spoon[index]=0
        else:
            print('error : person index- ',index,'using virtual spoon')

    def setFreeSpoon(self,index):
        if not self.spoon[index]:
            self.spoon[index]=1
        else:
            print('error: set free spoon as already free')

    def personStartEat(self,pid):  # pid - person id
        lock.acquire() # ***********************************   lock up
        index=self.getIndex(self.person,pid)
        #time.sleep(0.80)  # A
        if index>=0:
            self.setBusySpoon(index)
            self.setBusySpoon(index-1)
        else:
            print('there is not ',pid,' person on the table')
        lock.release() # ***********************************   lock down
        #time.sleep(0.80)  # B

    def personEndEat(self,pid):  # pid - person id
        lock.acquire() # ***********************************   lock up
        index=self.getIndex(self.person,pid)
        if index>=0:
            self.setFreeSpoon(index)
            self.setFreeSpoon(index-1)
        else:
            print('there is not ',pid,' person on the table')
        lock.release() # ***********************************   lock down
