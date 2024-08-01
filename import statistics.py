import statistics
numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
mean = sum(numbers) / len(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")