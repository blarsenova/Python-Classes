
numbers = [42, 7, 19, 88, 3, 25]

if not numbers:
    print("Array is empty")
else:
    # Initialize with the first element
    min_val = max_val = numbers[0]

    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    print(f"Min: {min_val}, Max: {max_val}")