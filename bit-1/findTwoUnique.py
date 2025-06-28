# In an array where every element occurs twice except two elements which occur once, 
# find the two unique numbers

def findTwoUnique(A):
    

    xor_all=0

    for num in A:
        xor_all^=num

    set_bit=xor_all & -xor_all    

    num1=0
    num2=0

    for nums in A:
        if nums & set_bit:
            num1^=nums
        else:
            num2^=nums

    return [num1,num2]

A=[3,6,4,4,6,8]
print(f"Two unique no : {findTwoUnique(A)}")            
