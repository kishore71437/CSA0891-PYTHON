numbers = [10, -1, -20, 15, 0, -5, 30, -10]
negative_count = 0
for num in numbers:
    if num < 0:
        negative_count += 1
print("Original list:", numbers)
print("Number of negative numbers:", negative_count)