#Given a string s, calculate the length of longest palindromic substring in s.

def findLength(s):
  if not s:
    return 0

  n=len(s)
  max_length=0

  for c in range(n):
    left=c
    right=c

    while left >=0 and right < n and s[left]==s[right]:
        left-=1
        right+=1

    max_length=max(max_length,right-left-1)

    left=c
    right=c+1

    while left>=0 and right<n and s[left]==s[right]:
      left-=1
      right+=1
    max_length=max(max_length,right-left-1)


  return max_length


S="anamadamm"
print(findLength(S))