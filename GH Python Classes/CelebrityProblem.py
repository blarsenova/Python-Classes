
# A simple "Following" matrix
# Person 0 knows 1
# Person 1 knows no one (The Celebrity!)
# Person 2 knows 1
matrix = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]


def knows(a, b):
    return matrix[a][b] == 1

# Now the algorithm works:
def find_celebrity(n):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    return candidate

print(f"The celebrity is person: {find_celebrity(3)}")