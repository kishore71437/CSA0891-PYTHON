numbers = [14,67,48,23,5,62]
n = 4  
sorted_numbers = sorted(numbers, reverse=True)
if 1 <= n <= len(sorted_numbers):
    nth_largest = sorted_numbers[n - 1]  
    print(f"The {n}th largest number is: {nth_largest}")
else:
    print(f"Invalid input. Please provide a valid value of n.")