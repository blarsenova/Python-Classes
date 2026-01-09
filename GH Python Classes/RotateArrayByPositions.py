def reverse_section(arr, start, end):
    """Helper function to reverse a portion of array"""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_in_place(arr, k):
    n = len(arr)
    k = k % n

    if k == 0:
        return arr

    # Step 1: Reverse the entire array
    reverse_section(arr, 0, n - 1)
    # Step 2: Reverse first k elements
    reverse_section(arr, 0, k - 1)
    # Step 3: Reverse remaining elements
    reverse_section(arr, k, n - 1)

    return arr

if __name__ == "__main__":
    # Test case 1
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original array:", arr)
    print("Rotated array:", rotate_array_in_place(arr.copy(), k))