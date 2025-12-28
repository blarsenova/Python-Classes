#1
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print(reversed_arr)

#2 w reversed w list
arr = [11, 4, 3, 68, 5]
reversed_arr = list(reversed(arr))
print(reversed_arr)

#3 method (in-place)
arr = [42,32,66]
arr.reverse()
print(arr)