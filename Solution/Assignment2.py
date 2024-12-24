def is_prime_while(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime_while(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
