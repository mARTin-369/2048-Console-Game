import random

# Check board bounds during iteration
def inbounds(i, j, size):
    return all([i >= 0, i < size, j >= 0, j < size])


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

    # Moves (left, right, up, down)
    d = ((0, -1), (0, 1), (-1, 0), (1, 0))

    x, y = random.randint(0, size - 1), random.randint(0, size - 1)
    randNum = random.choice((2, 4))
    mat[x][y] = randNum

    # Logic on move
    while True:
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
                ):
                    num = mat[m + ip[0]][n + ip[1]] * 2
                    m += ip[0]
                    n += ip[1]

                mat[i][j] = emptyCell
                mat[m][n] = num


if __name__ == "__main__":
    main()
