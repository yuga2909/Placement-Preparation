Arr=[1,2,3,4,5]
a=True
for i in range(len(Arr)-1):
      if Arr[i]>Arr[i+1]:
         a=False
         break
print(a)
