arr = [5, 2, 8, 19, 9, 3]

smallest = arr[0]  # Assume first element is smallest
for num in arr:
    if num < smallest:
        smallest = num

print(f"Smallest number: {smallest}")