number = int(input("Enter a number: "))
sum_of_digits = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10
if number % sum_of_digits == 0:
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")