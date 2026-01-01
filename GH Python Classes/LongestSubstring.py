def longest_substring_without_repeating(s: str) -> tuple:
    """
    Returns: (length of longest substring, the substring itself)
    """
    if not s:
        return 0, ""

    char_index = {}  # Store the last seen index of each character
    start = 0
    max_length = 0
    max_start = 0

    for end, char in enumerate(s):
        # If char is seen and its last index is >= start, move start
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        # Update the character's latest index
        char_index[char] = end

        # Update max length if current window is longer
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            max_start = start

    return max_length, s[max_start:max_start + max_length]

# Test it
result = longest_substring_without_repeating("wheelsonwheel")
print(result)  # Output: (3, 'abc')

