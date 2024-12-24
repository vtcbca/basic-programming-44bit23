def star_pattern_string_multiplication(n):
    for i in range(1, n + 1):
        print(" ".join(['*'] * i))

# Example usage
num_rows = int(input("Enter the number of rows: "))
star_pattern_string_multiplication(num_rows)
