arr=[1,3,5,7,9]
target=12
left=0
right=len(arr)-1
while left<right:
    if arr[left]+arr[right]==target:
        print([left,right])
        break
    elif arr[left]+arr[right]<target:
        left+=1
    elif arr[left]+arr[right]>target:
        right-=1
else:
    print(-1)
