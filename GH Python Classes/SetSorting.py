# A list of orders that has some duplicates
orders = ["croissant", "baguette", "croissant", "macaron", "baguette"]

# Convert the list to a set to automatically remove duplicates
unique_orders = set(orders)

print(unique_orders)
# Output: {'baguette', 'macaron', 'croissant'} (The order might vary!)