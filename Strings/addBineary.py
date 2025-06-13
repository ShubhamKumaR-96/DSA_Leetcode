# Add binary strings

def bineayString(A,B):
  num1=int(A,2)
  num2=int(B,2)

  total_sum=num1+num2

  ans=bin(total_sum)[2:]

  return ans

A = "10"
B = "110"
print(bineayString(A,B))