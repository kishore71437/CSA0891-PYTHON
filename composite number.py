array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
non_composite_numbers = []
for num in array:
    if num == 1:
        non_composite_numbers.append(num)
        continue
    is_prime = True
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            non_composite_numbers.append(num)
print("Original array:", array)
print("Non-composite numbers:", non_composite_numbers)