import sys

def factorize(number):
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()

    for number in numbers:
        number = int(number)
        factors = factorize(number)
        print(f"{number}={'*'.join(map(str, factors))}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_file(file_path)

