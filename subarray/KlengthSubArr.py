# print the starting index and ending index of the all subarray whose length = K

def printSubArr(A,K):
    n=len(A)

    for i in range(n-K):
        s=i
        e=i++K-1
        print(s,e)

A=list(map(int,input("Enter Element : ").split()))
K=int(input("Enter K :"))
printSubArr(A,K)        
