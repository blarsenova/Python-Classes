def spiral_order(matrix):
    res = []

    if not matrix: return res

    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # Get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # Get every i in the right column
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # Get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # Get every i in the left column
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res

example_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = spiral_order(example_matrix)
print(result)
