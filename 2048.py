size = 4

# Game board
mat = [[0, 0, 2, 4], [0, 0, 4, 8], [0, 2, 16, 32], [0, 2, 2, 16]]

# Moves
d = ((0, -1), (-1, 0), (0, 1), (1, 0))
ip = d[0]

# Check board bounds during iteration
def inbounds(i, j):
    return all([i >= 0, i < size, j >= 0, j < size])


# Print board
def printMat(mat):
    for i in range(size):
        for j in range(size):
            print("\t", mat[i][j], end="")
        print()


printMat(mat)

# Logic on move
for i in range(size):
    for j in range(size):
        m = i
        n = j
        num = mat[i][j]
        while inbounds(m + ip[0], n + ip[1]) and mat[m + ip[0]][n + ip[1]] == 0:
            m += ip[0]
            n += ip[1]

        if inbounds(m + ip[0], n + ip[1]) and mat[m + ip[0]][n + ip[1]] == mat[i][j]:
            num = mat[m + ip[0]][n + ip[1]] * 2
            m += ip[0]
            n += ip[1]

        mat[i][j] = 0
        mat[m][n] = num

print("\n")
printMat(mat)
