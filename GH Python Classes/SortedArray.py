# For lists
my_list = [3, 1, 4, 1, 5, 9, 2]
sorted_list = sorted(my_list)
print(sorted_list)


# For strings
chars = ['d', 'a', 'c', 'boy', 'girl']
sorted_chars = sorted(chars)
print(sorted_chars)

# Sort by length
words = ['apple', 'pears', 'peanuts', 'date', 'lime']
sorted_words = sorted(words, key=len)
print(sorted_words)