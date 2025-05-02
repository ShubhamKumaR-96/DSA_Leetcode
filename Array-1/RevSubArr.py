# Given an array of n elements two indices start and end are also given.Reverse the array from starting index to ending indexs

def revSubArr(A,startidx,endidx):
    n=len(A)

    while startidx<=endidx:
        A[startidx],A[endidx]=A[endidx],A[startidx]
        startidx+=1
        endidx-=1

    return A


A=list(map(int,input("Enter the elements : ").split())) 
startIdx=int(input("Enter startidx : "))
endIdx=int(input("Enter endIdx: "))
print(f"Revsering from {startIdx} to {endIdx} : {revSubArr(A,startIdx,endIdx)}")    