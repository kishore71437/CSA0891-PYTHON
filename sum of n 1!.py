N = 5
total_sum = 0
for i in range(1, N + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    total_sum += factorial / i
print("The sum of the series is:", total_sum)