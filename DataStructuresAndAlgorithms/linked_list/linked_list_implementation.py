class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None
class ll(Node):
    def __init__(self,data=None):
        self.head=super().__init__(data)
        
    def insert(self,idx,x):
        temp=Node(x)
        temp1=self.head
        if idx==1:
            temp.next=self.head
            self.head=temp
            return 
        else:
            for i in range(idx-2):
                temp1=temp1.next
            temp.next=temp1.next
            temp1.next=temp
    def remove(self,idx):
        temp1=self.head
        if temp1.next==None:
            print('Linked List is already empty')
            return
        if idx==1:
            self.head=self.head.next
            return
    
        for i in range(idx-2):
            temp1=temp1.next
        temp1.next=temp1.next.next
    def print_(self):
        gg=[]
        temp1=self.head
        while temp1!=None:
            gg.append(str(temp1.data))
            temp1=temp1.next
        print('->'.join(gg)) 
        return
    def reverse_print(self):
        temp1=self.head
        print(reverse_print())
           
        

                
                




if __name__=="__main__":
    n=ll()
    n.insert(1,41)
    n.print_()
    n.insert(2,45)
    n.print_()
    n.insert(3,23)
    n.print_()
    n.insert(3,44)
    n.print_()
    n.remove(2)
    n.print_()