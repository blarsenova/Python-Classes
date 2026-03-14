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