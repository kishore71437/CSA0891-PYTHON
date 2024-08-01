number = 153  
number_str = str(number)
num_digits = len(number_str)
sum_of_powers = 0
for digit in number_str:
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")