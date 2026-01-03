def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    # Method 1: Loop
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

    # Method 2: Comprehension
    # return sum(1 for char in s if char in vowels)

print(count_vowels("It's rainy today, but sun is coming up"))