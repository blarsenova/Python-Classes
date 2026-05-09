from collections import defaultdict

def group_anagrams(strs):
    # Using defaultdict to avoid KeyErrors
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the word to create a unique key for anagrams
        # e.g., "eat" and "tea" both become "aet"
        sorted_word = "".join(sorted(word))

        # Append the original word to the list matching that key
        anagram_map[sorted_word].append(word)

    # Return only the grouped values
    return list(anagram_map.values())

# Example Usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))