def alphabet_pattern_concat(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Initialize an empty string for the row
        row = ""
        
        # Create the left half of the row
        for j in range(1, i + 1):
            row += chr(64 + j) + " "
        
        # Create the right half by reversing the left part (excluding the middle letter)
        for j in range(i - 1, 0, -1):
            row += chr(64 + j) + " "
        
        print(row.strip())  # Print the row, stripping trailing space

# Example usage
num_lines = int(input("Enter the number of lines: "))
alphabet_pattern_concat(num_lines)
