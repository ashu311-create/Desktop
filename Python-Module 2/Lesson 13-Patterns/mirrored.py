def print_mirrored_right_triangle(rows):
    """
    Prints a mirrored right-angle triangle pattern using asterisks.
    Args:
        rows (int): The number of rows for the triangle.
    """
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("*" * i)
try:
    num_rows = int(input("Enter the number of rows for the triangle: "))
    if num_rows > 0:
        print_mirrored_right_triangle(num_rows)
    else:
        print("Please enter a positive number of rows.")
except ValueError:
    print("Invalid input. Please enter an integer.")