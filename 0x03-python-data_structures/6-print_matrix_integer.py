#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in rows:
            print("{:d}".format(columns), end="")
            if rows.index(columns) < len(rows) - 1:
                print(" ", end="")
        print("\n", end="")
