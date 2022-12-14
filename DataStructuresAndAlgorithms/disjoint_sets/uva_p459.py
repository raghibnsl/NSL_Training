par=[0, 0, 2, 0, 2]      #parents A for ABD and C for CE

def find(u):                                                                    #basic disjoint format
    """
    Finds the representitive node within a subset.

    Parameters:
        u <int>: provides the index mapped to the element in question
    """
    if u==par[u]:
        return u
    par[u]=find(par[u])
    return par[u]

# def connect(u,v):                                                             #basic disjoint format                     
#     """
#     Helps connect multiple nodes to a certain subset.

#     Parameters:
#         u,v <int>: The arguments are nodes that must be connected to the same subset
#     """
#     u=find(u)
#     v=find(v)
#     if u==v:
#         print("already chuddy buddies")
#     else:
#         par[max(u,v)]=min(u,v)

def count_sub(args,principle_case):                                   #Problem specific function
    """
    Counts the correct maximal substrings from our inputs
    Parameters:
        - args(string): Input string to be converted to index values and checked for maximal substring matching
                        according to principle case.
        - kwargs:
            - principle_case: Representitive index converted from principle_case string input for 
                            matching against input substrings.        
    """
    for i in [ord(i)-65 for i in args]:
        new_rep=find(i)
        if new_rep==principle_case:
            continue
        else:
            return False
    return True


if __name__=="__main__":
    cases=int(input())
    _=input()
    for i in range(cases):
        principle_case=find(ord(input())-65)
        counter=0
        while True:
            case=input()
            if case=="":
                break
            if count_sub(case,principle_case=principle_case):
                counter+=1
        print(counter)





