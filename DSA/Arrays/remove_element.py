arr=[2,3,3,4,5,6,7,8]
t=3
i=0
for j in range(len(arr)):
    if arr[j]!=t:
        arr[i]=arr[j]
        i+=1
print(arr[:i])
