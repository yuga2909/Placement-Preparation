arr=[1,2,3,0,3,0,5,0,9,1]
z=-1
for i in range(len(arr)):
    if arr[i]==0:
        z=i
        break
if z!=-1:
    for j in range(z+1,len(arr)):
        if arr[j]!=0:
            arr[z]=arr[j]
            arr[j]=0
            for i in range(z+1,len(arr)):
                if arr[i]==0:
                    z=i
                    break
print(arr)
