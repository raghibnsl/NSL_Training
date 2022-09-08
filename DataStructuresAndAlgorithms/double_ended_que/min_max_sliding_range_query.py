##deque

##Sliding Range Minimum Query:
from collections import deque

class deque:
    def __init__(self):
        self.result=[]
        self.dq=[]

    def min_query(self,arr:list ,i:int):                
        
        if arr[self.dq[-1]]<=arr[i]:
            self.dq.append(i)
            return 
        else:
            while True:
                self.dq.pop()
                if not self.dq or arr[self.dq[-1]]>arr[i]:
                    self.dq.append(i)
                    break
            return

    def max_query(self,arr:list ,i:int):
        if arr[self.dq[-1]]>=arr[i]:
            return
        else:
            while True:
                self.dq.pop()
                if not self.dq or arr[self.dq[-1]]<arr[i]:
                    self.dq.append(i)
                    break
            return
    

            
            



    def process(self,arr:list,max_min:str,range_:int)->list:
        for i in range(len(arr)):
            if len(self.dq)==0:
                self.dq.append(i)
            range_diff=i-range_
            while self.dq:
                if self.dq[0]<range_diff:
                    self.dq.pop(0)
                else:
                    break
            if max_min=="min":
                self.min_query(arr=arr,i=i)
            else:
                self.max_query(arr=arr,i=i)
            self.result.append(arr[self.dq[0]])
        return 
                    

if __name__=="__main__":
    deq=deque()
    arr=[10,20,5,6,2,30,21]
    deq.process(arr=arr,max_min='max',range_=3)


