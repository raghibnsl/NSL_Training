class circular_que:
    def __init__(self,capacity,sp):
        self.capacity=capacity
        self.q=[None for _ in range(self.capacity)]
        self.head=-1
        self.tail=-1
        self.starting_point=sp
    def enque(self,x):
        if (self.tail+1)%self.capacity==self.head:
            print("Q is full")
            return
        if self.head==-1:
            self.head=self.tail=self.starting_point
            self.q[self.head]=x
        else:
            self.tail=(self.tail+1)%self.capacity
            self.q[self.tail]=x
    def deque(self):
        if self.head==-1:
            print("Q is already empty!")
            return
        self.q[self.head]=None
        if self.head==self.tail:
            self.head=self.tail=-1
        else:
            self.head=(self.head+1)%self.capacity

if __name__=="__main__":
    que=circular_que(6,4)
    print(que.q)
    for i in range(10):
        que.enque(i)
        print(que.q)
    print(que.q)
    for i in range(10):
        que.deque()
        print(que.q)
    