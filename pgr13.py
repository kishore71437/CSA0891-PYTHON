num=int(input("Enter the number :"))
factor=[i for i in range (1,num +1) if num % i==0]
print(f"the factor {num} are {factor} ")