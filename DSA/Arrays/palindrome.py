def palind(a):
    left=0
    right=len(a)-1
    while left<right:
        if not a[left].isalnum():
            left+=1
        elif not a[right].isalnum():
            right-=1
        elif a[left].lower()!=a[right].lower():
            return "Not palindrome"
        else:
            right-=1
            left+=1
    return "palindrome
