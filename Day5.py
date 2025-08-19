# day 5
# finding leader
def findleaders(arr):
    n=len(arr)
    leaders=[]
    rightmost=arr[-1]
    leaders.append(rightmost)
    for i in range(n-2,-1,-1):
        if arr[i]>rightmost:
            leaders.append(arr[i])
            rightmost=arr[i]
    leaders.reverse()
    return leaders
arr=[5,12,5,9,4,1]
print(findleaders(arr))
