num = int(input("Enter a number: "))
seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    num = sum(int(digit) ** 2 for digit in str(num))

if num == 1:
    print("The number is a Happy number.")
else:
    print("The number is not a Happy number.")