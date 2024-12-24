def number_triangle_multiply(n):
    for i in range(1, n + 1):
        # Print leading spaces for alignment
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            print(j, end=" ")
        print()

# Example usage
num_lines = int(input("Enter the number of lines: "))
number_triangle_multiply(num_lines)
