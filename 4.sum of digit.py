number = int(input("Enter an n-digit number: "))
number = abs(number)
total = 0
while number > 0:
    total += number % 10
    number //= 10
print(f"The sum of the digits is {total}")

