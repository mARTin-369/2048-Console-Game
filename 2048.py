import random

# Check board bounds during iteration
def check_in_bounds(lower, upper, size):
    return all([lower >= 0, lower < size, upper >= 0, upper < size])


def get_random_empty_cell(mat, empty_cell, size):
    empty_cells = []
    for i in range(size):
        for j in range(size):
            if mat[i][j] == empty_cell:
                empty_cells.append((i, j))
    x, y = empty_cells[random.randint(0, len(empty_cells) - 1)]
    return x, y


# Operation on combining tiles
def combine_tiles(num):
    return num * 2


# Print board
def print_board(mat, size):
    for i in range(size):
        for j in range(size):
            print("\t", mat[i][j], end="")
        print()


def main():
    # Size of board n x n
    size = 4
    # Empty cell symbol
    empty_cell = "."
    goal = 2048
    won = False

    # Game board
    mat = [[empty_cell] * size for i in range(size)]
    # Store combined cells to prevent merging of more than 2 cells with same value in a row
    fused_tiles = set()

    # Moves (left, right, up, down)
    d = ((0, -1), (0, 1), (-1, 0), (1, 0))

    x, y = get_random_empty_cell(mat, empty_cell, size)
    rand_num = random.choice((2, 4))
    mat[x][y] = rand_num

    # Game loop
    while True:
        x, y = get_random_empty_cell(mat, empty_cell, size)
        rand_num = random.choice((2, 4))
        mat[x][y] = rand_num

        print("\n")
        print_board(mat, size)

        if won:
            print("\nYou won!!!")

        # Get user input move
        n = int(input("\nNext move: "))
        if n not in (1, 2, 3, 4):
            if n != 5:
                print("\nInvalid input...")
            print("\nExiting...")
            break

        ip = d[n - 1]
        fr = to = inc = 0

        # Set direction of iteration
        fr, to, inc = (0, size, 1) if n in (1, 3) else (size - 1, -1, -1)

        # Board state transition logic
        for i in range(fr, to, inc):
            for j in range(fr, to, inc):
                m, n = i, j
                num = mat[i][j]

                # While adjacent cell is empty move in the given direction
                while (
                    check_in_bounds(m + ip[0], n + ip[1], size)
                    and mat[m + ip[0]][n + ip[1]] == empty_cell
                ):
                    m += ip[0]
                    n += ip[1]

                # If adjacent cell has same value combine
                if (
                    check_in_bounds(m + ip[0], n + ip[1], size)
                    and mat[m + ip[0]][n + ip[1]] == mat[i][j]
                    and ((m + ip[0], n + ip[1]) not in fused_tiles)
                ):
                    num = combine_tiles(mat[m + ip[0]][n + ip[1]])
                    if num == goal:
                        won = True

                    m += ip[0]
                    n += ip[1]
                    fused_tiles.add((m, n))

                mat[i][j] = empty_cell
                mat[m][n] = num

        fused_tiles.clear()


print("2048 Game")
print("Enter 1 to move left")
print("Enter 2 to move right")
print("Enter 3 to move up")
print("Enter 4 to move down")

if __name__ == "__main__":
    main()
