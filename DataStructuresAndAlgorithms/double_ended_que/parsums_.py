def is_neg(arr):
    for i in arr:
        if i<0:
            return 1
    return 0
if __name__=="__main__":
    while True:
        n=int(input())                                      #sequence size
        if n==0:                
            break
        arr=list(map(int,input().split()))                  # sequence
        if len(arr)==1:                                     # if length is one, then there is only one cyclical sequence
            if arr[0]>0:                                    
                print(1)
            else:
                print(0)
            continue
        sum_arr=[sum(arr[:i+1]) for i in range(len(arr))]   #cumulative sum
        if is_neg(sum_arr)==False:    
            shifts=1
        else:
            shifts=0
        shift_n=0
        for _ in range(n-1):
            last_=arr.pop()
            shift_n+=1
            sum_arr.insert(0,last_)
            for i in range(1,n-1):
                sum_arr[i]+=last_
            if is_neg(sum_arr)==0:
                shifts+=1
        print(shifts)