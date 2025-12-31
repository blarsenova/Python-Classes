
def is_palindrome(s):
    # Case insensitive, ignore non-alphanumeric
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Optimized two-pointer
def is_palindrome_optimized(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome_optimized("race a car"))  # False