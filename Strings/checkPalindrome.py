# Check whether the given substring of string s is palindrome or not.
#  A palindrome is the sequence of characters that reads the same forward and backward.
# for example, "nayan", "madam", etc.

def checkPalindrome(S,startIdx,endIdx):
    n=len(S)

    while startIdx<=endIdx:
        if S[startIdx]!=S[endIdx]:
            return False
        startIdx+=1
        endIdx-=1  

    return True      

    

S="anamadamspe"
startIdx=3
endIdx=7
print(checkPalindrome(S,startIdx,endIdx))         


