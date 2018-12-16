import time
import threading
import philosophers

slock=threading.Lock()

startTime=time.time()

person=[1,2,3,4,5]
spoon =[1,1,1,1,1] #  1 - free spoon , 0 - busy spoon


phil =philosophers.eating(person,spoon)
phil.startTime=startTime
phil.eatTime=0.5

def eatProcess(pid):
        
        phil.personStartEat(pid)
        print("{} >> person {} start eat \n".format(time.time(),pid))

        
        time.sleep(phil.eatTime)
        

        phil.personEndEat(pid)
        print("{} >> person {} end eat \n".format(time.time(),pid))
        phil.eatCount+=1
        
        #time.sleep(0.30)
        #print("{}  ... person {} end thinking \n".format(time.time(),pid))



        
    

i=0
allThread=[]


while phil.timeout(5):  
    pindex=phil.getIndex(phil.person,phil.person[i])
    #if phil.checkSpoon(pindex) and phil.checkSecondSpoon(pindex):
    if phil.foo(pindex):
        # start threading
        #'''
        T=threading.Thread(target = eatProcess, args = (phil.person[i],))
        allThread.append(T)
        T.start()
        #'''
        
        #eatProcess(phil.person[i])
        


        
    # continue looping on person list
    i=phil.looping(i)
    
        


# wait for end threading
for t in allThread:    
    t.join()



#print('free spoons: ',countFeeSpoon())
print(phil.spoon)
print('process time: ',phil.interval())
print("{} people ate in this process \n".format(phil.eatCount))
