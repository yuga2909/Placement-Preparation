arr=[1,1,3,3,3,5,6,6]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
high=0
ele=None
for i in freq:
    if freq[i]>high:
        high=freq[i]
        ele=i
print("Highest frequent element : ",ele)
print("Highest frequency : ",high)
