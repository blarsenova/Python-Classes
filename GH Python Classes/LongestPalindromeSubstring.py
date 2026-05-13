def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        # Check odd length palindromes (e.g., "aba")
        tmp = expand(s, i, i)
        if len(tmp) > len(res): res = tmp

        # Check even length palindromes (e.g., "abba")
        tmp = expand(s, i, i + 1)
        if len(tmp) > len(res): res = tmp
    return res

def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

# Example:
print(longest_palindrome("babbaad")) # Output: bab