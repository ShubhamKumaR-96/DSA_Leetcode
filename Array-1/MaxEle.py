def countMaxGreaterEle(A):
    n=len(A)
    maxVal=max(A)
    cnt=0

    for num in A:
        if maxVal==num:
            cnt+=1

    totalMax=n-cnt
    return totalMax

A=list(map(int,input("Enter the elements : ").split())) 
print(f"Max Element : {countMaxGreaterEle(A)}")
