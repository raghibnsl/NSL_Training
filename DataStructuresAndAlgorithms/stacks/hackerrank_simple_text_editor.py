# Enter your code here. Read input from STDIN. Print output to STDOUT

q=int(input())
ops=[]
for i in range(q):
    ops.append(input().rstrip())
def str_operate(ops):
    str_=''
    last_1_2=[]
    for i in range(len(ops)):
        ins=ops[i][0]
        if ins=='1':
            rest=ops[i][2:]
            last_1_2.append(str_)
            str_+=rest
        elif ins=='2':
            delidx=int(ops[i][2:])
            last_1_2.append(str_)
            str_=str_[:len(str_)-delidx]
        elif ins=='3':
            prntidx=int(ops[i][2:])
            print(str_[prntidx-1])
        elif ins=='4':
            str_=last_1_2.pop()
    
str_operate(ops)

