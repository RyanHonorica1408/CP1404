"""
CP1404 Practical 10 - Ryan Honorica
Recursion code
"""

def calculate_blocks(rows):
    """Calculate blocks needed for a given number of rows of a 2D pyramid."""
    if rows <= 0:
        return 0
    else:
        blocks = rows + calculate_blocks(rows - 1)
        return blocks


def do_it(n):
    if n <= 0:
        return 0
    else:
        return n % 2 + do_it(n - 1)

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    else:
        print(n ** 2)
        do_something(n - 1)


def build_pyramid():
    """Get user's pyramid size in rows and output the blocks needed."""
    chosen_rows = int(input("How many rows is your pyramid: "))
    print("For {} rows, you need {} blocks".format(chosen_rows, calculate_blocks(chosen_rows)))


build_pyramid()
do_something(4)
print(do_it(5))


