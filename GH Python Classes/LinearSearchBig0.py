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


        ###### HomeWork####

def linear_search(data_list, target):
    """
    Search for a target value within a list.
    Returns the index of the target if found, otherwise -1.
    """
    # Loop through the list using the index
    for index in range(len(data_list)):
        # Check if the current element matches the target
        if data_list[index] == target:
            return index  # Target found, return the current index

    return -1  # Target not found after checking the whole list

# --- Testing the implementation ---
my_data = [15, 23, 8, 42, 42, 16]
search_target = 16

result = linear_search(my_data, search_target)

if result != -1:
    print(f"Target {search_target} found at index: {result}")
else:
    print(f"Target {search_target} was not found in the list.")


    #It is Big O(n), bcoz it has to go thru n times, it would be 0(1), if we knew the index already like arr [1].