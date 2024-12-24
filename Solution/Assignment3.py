def fibonacci_recursive(n, fib_sequence=None):
    if fib_sequence is None:
        fib_sequence = [0, 1]
    if len(fib_sequence) >= n:
        return fib_sequence[:n]
    else:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fibonacci_recursive(n, fib_sequence)

# Example usage
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_recursive(num_terms)}")
