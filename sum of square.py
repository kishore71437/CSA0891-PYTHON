N = 10
sum_of_squares = 0
square_of_sum = 0
for i in range(1, N + 1):
    sum_of_squares += i ** 2
    square_of_sum += i
square_of_sum = square_of_sum ** 2
difference = square_of_sum - sum_of_squares
print("The difference between the square of the sum and the sum of the squares is:", difference)