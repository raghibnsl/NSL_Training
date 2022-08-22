# Enter your code here. Read input from STDIN. Print output to STDOUT
class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enque(self,x):
        self.s1.append(x)
        return self.s1
    def deque(self):
        if len(self.s2)==0:
            if len(self.s1)==0:
                print("Queue is empty!")
                return
            else:
                while len(self.s1)!=0:
                    n_=self.s1.pop()
                    self.s2.append(n_)
        self.s2.pop()
        return self.s1,self.s2
que=queue()
q=int(input())
for i in range(q):
    ins=input().rstrip()
    if ins[0]=='1':
        input_=int(ins[2:])
        que.s1=que.enque(input_)
    if ins[0]=='2':
        que.s1,que.s2=que.deque()
    if ins[0]=='3':
        if len(que.s2)==0:
            print(que.s1[0])
        else:
            print(que.s2[-1])

