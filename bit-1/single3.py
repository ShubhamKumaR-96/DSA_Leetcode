# given an array where all number appears thrice except one number which appear only once.
# find the single number A=5 7 5 7 11 11 9 11 7 5. 

def sigleNo(A):
    ans=0

    for i in range(32):
        bit_count=0
        for num in A:
            if (num>>i) & 1:
                bit_count+=1

        if bit_count%3!=0:
            ans|=(1<<i)
    if (ans & (1<<31)):
        ans-=(1<<32)

    return ans

A=[5,7,5,7,11,11,9,5,7,11]
print(f"single no : {sigleNo(A)}")        