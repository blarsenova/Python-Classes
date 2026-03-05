def search(arr, x):
    n = len(arr)

    # Iterate over the array in order to
    # find the key x
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 100, 40]
    x = 10

    result = search(arr, x)
    if (result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)