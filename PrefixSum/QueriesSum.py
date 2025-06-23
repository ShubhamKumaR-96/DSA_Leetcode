# Given with array of size N : 
# Q queries start with i and end with j => return the sum of the range of sub array
# -3 6 2 4 5 2 8 -9 3 1 

# PrefixSum Way
def queriesSubArrSum(A,queries):
      n=len(A)
      ps=[0]*n
      ps[0]=A[0]
      
      for i in range(1,n):
            ps[i]=ps[i-1]+A[i]

      while queries>0:
            startIdx=int(input("Enter start index: ")) 
            endIdx=int(input("Enter end index: "))  
            if startIdx>n:
                  print("Indicies not valid")          
              
            if startIdx==0:
                  psSum=ps[endIdx]
            else:              
                  psSum=ps[endIdx]-ps[startIdx-1]
                     
            print(f"Total sum:  {psSum}")
            queries-=1                  

A=list(map(int,input("Enter elements:").split()))
queries=int(input("Enter queries: "))    
queriesSubArrSum(A,queries)        


