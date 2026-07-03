arr=[-7,-3,2,3,11]
left = 0
right = len(arr) - 1
k = len(arr) - 1
result = [0] * len(arr)
while left<=right:
    if abs(arr[left])>abs(arr[right]):
        result[k]=(arr[left])**2
        left+=1
        k-=1
    else:
        result[k]=(arr[right]**)2
        right-=1
        k-=1
print(result)
