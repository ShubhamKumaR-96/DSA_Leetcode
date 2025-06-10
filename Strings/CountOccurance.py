def cntOccurence(A):
  if len(A)==0:
    return 0

  cnt=0


  for i in range(len(A)-2):
    if A[i]=='b' and A[i+1]=='o' and A[i+2]=='b':
      cnt+=1

  return cnt

# A= "abobc"
A="bobob"
print(cntOccurence(A))
