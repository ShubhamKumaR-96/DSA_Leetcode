# Check anagram

def checkAnagram(A, B):
    if len(A) != len(B):
        return 0

    freq = [0] * 26

    # First count characters in A
    for char in A:
        freq[ord(char) - ord('a')] += 1

    # Then decrement counts for characters in B
    for char in B:
        freq[ord(char) - ord('a')] -= 1

    # Finally check all counts
    for count in freq:
        if count != 0:
            return 0

    return 1

# Test cases
print(checkAnagram("cat", "bat"))      # Output: 0
print(checkAnagram("secure", "rescue"))  # Output: 1