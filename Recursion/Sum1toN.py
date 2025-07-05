def printSum(n):
    if n==1:
        return 1

    return printSum(n-1)+n

n=5
print(f"Sum : {printSum(5)}")        