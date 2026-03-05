def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        guess = arr[mid]

        if guess == target:
            return mid  # Found it!
        if guess > target:
            high = mid - 1  # Target is in the left half
        else:
            low = mid + 1   # Target is in the right half

    return -1  # Not found


my_data = [1000, 998, 32, 2,203, 769]
search_target = 203

result = binary_search(my_data, search_target)
print(f"{result}  is the location")