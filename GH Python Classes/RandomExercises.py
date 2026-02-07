### 1. The List & Tuple Challenge: "The Secure Sorter"

#**Goal:** Practice the difference between mutable (Lists) and immutable (Tuples) structures.

#* **Task:** Create a list of tuples, where each tuple contains a name and a score (e.g., `[("Alice", 85), ("Bob", 75)]`).
#* **Requirement:** 1. Sort the list based on the scores in descending order.
#2. Attempt to change a score inside one of the tuples and observe the error.
#3. Then, "update" a score by replacing the entire tuple at that index.


tuple1 = [("Alice", 85), ("Bob", 75), ("Kurmanjan", 1), ("KeroKero", 99)]

from operator import itemgetter
# Sorts by the item at index 1
result = sorted(tuple1, key=itemgetter(1))
print(result)
