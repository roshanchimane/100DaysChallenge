# missing number
def findnumber(arr):
    n=len(arr)
    totalsum=(n+1)*(n+2)//2
    actual=0
    for x in arr: 
        actual+=x
    return totalsum-actual

arr=[1,3,4,5]
print("Missing number is:",findnumber(arr))
