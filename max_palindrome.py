max_palindrome = 0
num1 = 0
num2 = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > max_palindrome:
                max_palindrome = product
                num1 = i
                num2 = j

print(f"The largest palindrome made from the product of two 3-digit numbers is {max_palindrome} = {num1} * {num2}")