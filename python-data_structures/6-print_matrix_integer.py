def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
        return

    for row in matrix:
        line = ""

        for i in range(len(row)):
            if i > 0:
                line += " "
            line += "{:d}".format(row[i])

        print(line)
