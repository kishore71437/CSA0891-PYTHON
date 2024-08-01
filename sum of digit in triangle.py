triangle = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]
total_sum = 0
for row in triangle:
    for num in row:
        str_num = str(num)
        for digit in str_num:
            total_sum += int(digit)
print("The sum of all digits in the triangle is:", total_sum)