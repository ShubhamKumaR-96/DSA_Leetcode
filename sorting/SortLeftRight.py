 # Given an array of N elements you need to re-arrange the array, arr[0]
#  should go it's sorted position. All the elements which are smaller than arr[0] =>
#  go it's left side and if greater than go it's right side

# A = 10 3 8 15 6 12 2 18 7 1

def sortLeftRight(A):
    n=len(A)
    temp=[0]*n
    p1=0
    p2=n-1
    pivot=A[0]

    i=1
    while i<n:
        if A[i]>A[0]:
            temp[p2]=A[i]
            p2-=1
        else:
            temp[p1]=A[i]
            p1+=1

        i+=1

    temp[p1]=A[0]    

    return temp


def partionPlace(A):
    n=len(A)
    pivot=A[0]

    A[0],A[n-1]=A[n-1],A[0]


    startIdx=0

    for i in range(n-1):
        if A[i]<pivot:
            A[i],A[startIdx]=A[startIdx],A[i]
            startIdx+=1

    A[startIdx],A[n-1]=A[n-1],A[startIdx]  

    return A      
    
    



A=[10,3,8,15,6,12,2,18,7,1]
result=partionPlace(A)
print(f" Sort Array : {result}")    




