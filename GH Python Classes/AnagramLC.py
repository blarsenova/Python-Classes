s ='anagram'
t='nagaram'


# 1. First, check if lengths match exactly
if len(s) != len(t):
    print('Not anagrams: Lengths do not match')
else:
    # 2. Sort both strings and compare them
    # This is the simplest way to check if they have the same letters
    if sorted(s) == sorted(t):
        print('The words are anagrams')
    else:
        print('The words are NOT anagrams')


#2 Solution

s = "cat"
t = "dog"

if len(s) != len(t):
    print(False)
else:
    countS = {}
    countT = {}

    # Fill countS dictionary
    for char in s:
        # If 'a' is new, it takes 0 and adds 1. If 'a' exists, it adds 1 to the current count.
        countS[char] = countS.get(char, 0) + 1

    # Fill countT dictionary
    for char in t:
        countT[char] = countT.get(char, 0) + 1

    # Compare the two maps
    if countS == countT:
        print("Success: It is an anagram!")
    else:
        print("Fail: Not an anagram.")