import sys

def factorize_number(n):
    factors = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            factors.append((i, n//i))
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()
        for number in numbers:
            n = int(number)
            factorizations = factorize_number(n)
            for factorization in factorizations:
                print(f"{n}={factorization[0]}*{factorization[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    factorize_file(file_path)

