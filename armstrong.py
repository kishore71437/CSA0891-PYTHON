num=int(input("Enter the number :"))
num_str=str(num)
num_len=len(num_str)
sum_of_powers=sum(int(digit)*num_len for digit in num_str)
if sum_of_powers==num:
    print(f"{num} is an Armstrong number .")
else:
    print(f"{num} is not an armstrong number.")