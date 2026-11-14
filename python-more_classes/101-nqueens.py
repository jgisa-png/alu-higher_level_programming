#!/usr/bin/python3
"""Print every solution to the N queens puzzle."""
import sys


def solve(n):
    """Place one queen per row and print each complete solution."""
    queens = []
    columns = set()
    rising = set()
    falling = set()

    def place(row):
        """Try each column that is safe in this row."""
        if row == n:
            print([[r, c] for r, c in enumerate(queens)])
            return

        for col in range(n):
            up, down = row + col, row - col
            if col in columns or up in rising or down in falling:
                continue

            queens.append(col)
            columns.add(col)
            rising.add(up)
            falling.add(down)
            place(row + 1)
            falling.remove(down)
            rising.remove(up)
            columns.remove(col)
            queens.pop()

    place(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(size)
