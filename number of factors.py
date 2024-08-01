num = int(input("Enter a number: "))
N = int(input("Enter the number of factors to print: "))
factors = [i for i in range(1, num + 1) if num % i == 0]
num_factors = len(factors)
print(f"The number of factors of {num} is: {num_factors}")
print(f"The first {N} factors are: {factors[:N]}")