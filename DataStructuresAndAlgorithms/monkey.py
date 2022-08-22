import math

def small_darlings_search(arr,x):
    beg=0
    end=len(arr)
    mid=None
    while beg<=end:
        mid=(beg+end)//2
        if arr[mid]>x:
            end=mid-1
        elif arr[mid]<x:
            beg=mid+1
        elif arr[mid]==x:
            end=mid-1
        print(arr,beg,end)
    if end==-1:
        end=0
    first_small=end
    while end>0 and arr[end]==arr[end-1]:
        end=end-1
    if arr[end]>=x:
        return (first_small,'X')
    else:
        return (first_small,arr[end])


if __name__=="__main__":
    n=13
    arr=[1,4,6,10,11,11,11,11,12,13,13,13,14,16,17]
    first_small_idx,small=small_darlings_search(arr,n)
    while first_small_idx<len(arr) and arr[first_small_idx]<=n:
        first_small_idx+=1
    if arr[first_small_idx]<=n:
        large="X"
    else:
        large=arr[first_small_idx]
    print(f"{large} {small}")