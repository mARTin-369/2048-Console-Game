import random

# Check board bounds during iteration
def inbounds(i, j, size):
    return all([i >= 0, i < size, j >= 0, j < size])


def get_random_empty_cell(mat, empty_cell, size):
    emptyCells = []
    for i in range(size):
        for j in range(size):
            if mat[i][j] == empty_cell:
                emptyCells.append((i, j))
    x, y = emptyCells[random.randint(0, len(emptyCells) - 1)]
    return x, y


# Print board
def printMat(mat, size):
    for i in range(size):
        for j in range(size):
            print("\t", mat[i][j], end="")
        print()


def main():
    size = 4
    emptyCell = "."

    # Game board
    mat = [[emptyCell] * size for i in range(size)]
    fused = [[0] * size for i in range(size)]

    # Moves (left, right, up, down)
    d = ((0, -1), (0, 1), (-1, 0), (1, 0))

    x, y = get_random_empty_cell(mat, emptyCell, size)
    randNum = random.choice((2, 4))
    mat[x][y] = randNum

    # Logic on move
    while True:
        x, y = get_random_empty_cell(mat, emptyCell, size)
        randNum = random.choice((2, 4))
        mat[x][y] = randNum

        print("\n\n")
        printMat(mat, size)

        # Get user input move
        n = int(input("\n\nNext move: "))
        if n not in (1, 2, 3, 4):
            if n != 5:
                print("\n\nInvalid input...")
            print("\nExiting...")
            break

        ip = d[n - 1]

        # Board state transition logic
        for i in range(size):
            for j in range(size):
                m = i
                n = j
                num = mat[i][j]
                while (
                    inbounds(m + ip[0], n + ip[1], size)
                    and mat[m + ip[0]][n + ip[1]] == emptyCell
                ):
                    m += ip[0]
                    n += ip[1]

                if (
                    inbounds(m + ip[0], n + ip[1], size)
                    and mat[m + ip[0]][n + ip[1]] == mat[i][j]
                    and fused[m + ip[0]][n + ip[1]] != 1
                ):
                    num = mat[m + ip[0]][n + ip[1]] * 2
                    m += ip[0]
                    n += ip[1]
                    fused[m][n] = 1

                mat[i][j] = emptyCell
                mat[m][n] = num

        fused = [[0] * size for i in range(size)]


if __name__ == "__main__":
    main()
