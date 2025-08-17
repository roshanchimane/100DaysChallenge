# day 3
# finding dupliate from the array

def findduplicate(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i):
            if arr[i]==arr[j]:
                print("Duplicate number:",arr[i])
    
arr=[3,2,4,6,5,3]
ans=findduplicate(arr)
