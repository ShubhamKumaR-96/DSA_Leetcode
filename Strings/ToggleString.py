# Given a string consisting of only alphabets(either lowercase or uppercase).
#  Print all the characters of string in such a way that for all lowercase character,
#  print its uppercase character and for all uppercase character, print its lowercase character.

def toggle(s):
    n=len(s)

    result=[]

    for ch in s:
        if ord(ch)>= ord('a') and ord(ch) <= ord('z'):
            result.append(chr(ord(ch)-32))
        elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            result.append(chr(ord(ch)+32))

    return ''.join(result)


def toggleCase(s):
    n=len(s)
    result=[]

    for ch in s:
        if 'a' <= ch  <= 'z' :
            result.append(chr(ord(ch)-32))
        elif 'A' <= ch <= 'Z' :
            result.append(chr(ord(ch)+32))  

    return ''.join(result)        


s="aDgbHJe"    
print(f"After toggle: {toggleCase(s)}")        

