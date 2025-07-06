def printN(n):
    if n==0:
        return

    printN(n-1)
    print(n) 

n=5
print(f"Printing 1 to {n} :")
print(printN(n))