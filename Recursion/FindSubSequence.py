# Write a recursive function that, given two strings A and B, return 1 
# if the first string A is a subsequence of the second string B.

# For example, given "hac" and "cathartic", you should return 1, 
# but given "bat" and "table", you should return 0.

def checkSubSeq(A,B):
    if len(A)==0:
        return 1

    if len(B)==0:
        return 0

    if A[0]==B[0]:
        return checkSubSeq(A[1:],B[1:])
    else:
        return checkSubSeq(A,B[1:])   

A = "hac"
B = "cathartic"     

print(f" Subsequence: {checkSubSeq(A,B)}")