counter=[1 for i in range(10)]
par=[i for i in range(10)]                                       # ABCDEFGHIJ
print(par)

def find(u):
    if u==par[u]:
        return u
    par[u]=find(par[u])
    return par[u]

def connect(*args):
    for i in range(0,len(args)-1):
        print(f"args: {[i for i in args[i:i+2]]}")
        print(f"args: {[i-65 for i in args[i:i+2]]}")
        u=find(args[i]-65)
        v=find(args[i+1]-65)
        print(f"{args[i]-65} --> {v}")
        if u==v:
            print("Already members!")
        else:
            print(u,v)
            par[max(u,v)]=min(u,v)
            # counter[min(u,v)]+=1


            print(par)

connect(ord('A'),ord('D'),ord('B'))
connect(ord('C'),ord('D'))
connect(ord('E'),ord('G'))
connect(ord('D'),ord('J'))
connect(ord('G'),ord('I'))
connect(ord('F'),ord('H'),ord('G'))
print(par)
# n=int(input())
# blank=input()

# for i in n:
#     s=input()
#     idx_=[ord(s)-65 for i in s]

    
