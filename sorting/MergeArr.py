# Given an array A, (x,y,z) Array is sorted from x => y-1 amd y=>z  sort the array from x=>z 
#  A= 8 1 3 6 11 2 4 9 7 6
# x=2 y = 5 z= 7

def mergrTwoArr(A, x,y,z):

    left=A[x:y]
    right=A[y:z+1]

    i=j=0
    temp=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])  
            j+=1

    while i<len(left):
        temp.append(left[i])
        i+=1

    while j<len(right):
        temp.append(right[j])
        j+=1


    A[x:z+1]=temp

    return A

A=[8,1,3,6,11,2,4,9,7,6]
x=2
y=5
z=7
result = mergrTwoArr(A, x, y, z)
print(result)
                    