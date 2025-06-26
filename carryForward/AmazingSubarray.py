# You are given a string S, and you have to find all the amazing substrings of S.
# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
# Input
# Only argument given is string S. Output
# Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
# Input: ABEC

# Output: 6

# Explanation
# Amazing substrings of given string are :
# 1. A
# 2. AB
# 3. ABE
# 4. ABEC
# 5. E
# 6. EC
# here number of substrings are 6 and 6 % 10003 = 6.

# Brute force way
def amazingSubArr(S):
    n=len(S)

    vowels=set("aeiouAEIOU")
    cnt=0
    for i in range(n):
        if S[i] in vowels:
            for j in range(i,n):
                cnt+=1

    return cnt%10003



# optimized way
def amazingSubrrcnt(S):
    n=len(S)
    cnt=0

    vowels=set("aeiouAEIOU")
    for i in range(n):
        if S[i] in vowels:
            cnt+=(n-i)
    return cnt        
              

S="ABEC"
print(f"Amazing subArr: {amazingSubrrcnt(S)}")



                
