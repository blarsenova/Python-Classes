### 1. The List & Tuple Challenge: "The Secure Sorter"

# **Goal:** Practice the difference between mutable (Lists) and immutable (Tuples) structures.

# * **Task:** Create a list of tuples, where each tuple contains a name and a score (e.g., `[("Alice", 85), ("Bob", 75)]`).
# * **Requirement:** 1. Sort the list based on the scores in descending order.
# 2. Attempt to change a score inside one of the tuples and observe the error.
# 3. Then, "update" a score by replacing the entire tuple at that index.


tuple1 = [("Alice", 85), ("Bob", 75), ("Kurmanjan", 100), ("KeroKero", 99)]

from operator import itemgetter

# Sorts by the item at index 1
result = sorted(tuple1, key=itemgetter(1), reverse=True)
print(result)
tuple1[1] = 'nei', 55
print(tuple1)
# tuple1[0][1] = 95  # This will trigger the TypeError

# 2
text = "I am at 10th grade. Want to graduate and enter a college, and then graduate from there, and find a job"

# 1. Clean the string (remove commas/periods and make lowercase)
clean_text = text.replace(".", "").replace(",", "").lower()

# 2. Split into a list of words
words = clean_text.split()

# 3. Create the frequency dictionary
word_counts = {}
for word in words:
    # .get(word, 0) checks if the word exists; if not, it starts at 0
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)

# Set

setA = {'movie', 'cinema', 'theater', 'football'}
setB = {'cinema', 'ball', 'skating'}
print(setA | setB)
print(setA & setB)
print(setA - setB)
