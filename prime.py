A= int(input("Enter the A value :"))
B= int(input("Enter the B value :"))
for num in range(A,B+1)
if num<=1:
    print(num)
continue
if num<=3:
    if num==1:
    print(num)
continue 
if num %2 ==0 or num%3==0:
    print(num)
    i=5
    is_primr=True
while i*i<=num:
if num%i==0 or num %(i+2)==0:
            is_prime =False
break
        i+=6
if not is_prime
        print(num)
