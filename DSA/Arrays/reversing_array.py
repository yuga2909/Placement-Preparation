Arr=[1,2,3,4,5,6]
r=len(Arr)-1
for i in range(len(Arr)//2):
    Arr[i],Arr[r]=Arr[r],Arr[i]
    r-=1
print(Arr)
