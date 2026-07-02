arr=[1,1,3,3,3,5,6,6]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
low=float('inf')
ele=None
for i in freq:
    if freq[i]<low:
        low=freq[i]
        ele=i
print("Lowest frequent element : ",ele)
print("Lowest frequency : ",low)
