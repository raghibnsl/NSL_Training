
def find(u):                                                                        #basic disjoint sets 
    if u==par[u]:
        return u
    par[u]=find(par[u])
    return par[u]
def union(u,v):                                                                     #basic disjoint sets 
    u=find(u)
    v=find(v)
    if u==v:
        # print("Already friends")
        pass
    else:
        a_idx_minus=max(u,v)
        par[max(u,v)]=min(u,v)
        a_idx_plus=min(u,v)
        counter[a_idx_plus]+=counter[a_idx_minus]                                   #subset parent represented by idx to which we tally total members of the subset after joining the two subsets
        counter[a_idx_minus]-=counter[a_idx_minus]                                  # subset parent represented by idx from which we negate its group members due to merging with smaller index subset     
if __name__=="__main__":
    while True:
        par=[]
        animals=[]
        counter=[] 
        cases,relations=list(map(int,input().split()))
        if cases==0 and relations==0:
            break
        for i in range(cases):
            animal=input().rstrip()
            animals.append(animal)
            par.append(i)
            counter.append(1)
            # print(f"\tanim_d: {animals},\n\tpar:{par},\n\tcounter: {counter}")
        for _ in range(relations):
            u,v=input().rstrip().split()
            if u==v:
                continue
            # print(f"inputs:{u,v}")
            union(animals.index(u),animals.index(v))
            # print(counter)
        print(max(counter))
        _=input()
        
            
