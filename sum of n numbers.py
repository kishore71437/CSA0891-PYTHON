n=4
factorial=1
sum_of_fact=0
for i in range(1,n+1):
    factorial *=i
    sum_of_fact+=factorial
print("the factorial of n:",sum_of_fact)