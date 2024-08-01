array = [26,28,47,26,43,51,29]
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
print("Prime numbers in array:", non_composite_numbers)