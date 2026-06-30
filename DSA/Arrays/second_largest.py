Arr=[10,20,20,5]
lar=Arr[0]
sec=float('-inf')
for i in Arr:
    if i>lar:
        sec=lar
        lar=i
    elif i>sec and i!=lar:
        sec=i
print("Second Largest Num :: ",sec)
