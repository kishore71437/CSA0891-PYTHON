num = int(input("Enter a number: "))
n = int(input("Enter the value of n to find the nth factor: "))
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"The number of factors of {num} is: {len(factors)}")
if n <= len(factors) and n > 0:
    print(f"The {n}th factor of {num} is: {factors[n - 1]}")
else:
    print(f"There is no {n}th factor for the number {num}.")