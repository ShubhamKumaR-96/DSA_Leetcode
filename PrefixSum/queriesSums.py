# Brute force way

def queries(A,Q,startIdx,endIdx):

    queriesSum=0
    for i in range(startIdx,endIdx+1):
        queriesSum+=A[i]

    print(f" Queries sum : {queriesSum}")


A=[-3, 6,2,4,5,2,8,-9,3,1]    

q=int(input("Enter queries: "))

while q>0:
    s=int(input("Enter startIdx: "))
    e=int(input("Enter endIdx: "))
    queries(A,q,s,e)
    q-=1


    