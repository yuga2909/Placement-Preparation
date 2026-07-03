a1=[1,2,2,3]
a2=[2,2,4]
p1=0
p2=0
result=[]
while p1 < len(a1) and p2 < len(a2):
    if a1[p1]<a2[p2]:
        if not result or a1[p1]!=result[-1]:
            result.append(a1[p1])
        p1+=1
    elif a1[p1]>a2[p2]:
        if not result or a2[p2]!=result[-1]:
            result.append(a2[p2])
        p2+=1
    else:
        if not result or a1[p1]!=result[-1]:
            result.append(a1[p1])
        p1+=1
        p2+=1
while p1 < len(a1):
    if not result or a1[p1]!=result[-1]:
        result.append(a1[p1])
    p1+=1
while p2 < len(a2):
    if not result or a2[p2]!=result[-1]:
        result.append(a2[p2])
    p2+=1
print(result)
