count = str(input("Enter an n-digit number: "))
count = abs(count)
total = 0
while count > 0:
    total += count % 10
    count //= 10
print(f"The sum of the digits is {total}")

