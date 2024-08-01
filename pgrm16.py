num=int(input("Enter the value :"))
n1,n2=0,1
count=0
if num<=0:
    print("please enter the positive integers")
elif num==1:
    print("Fibonacci sequence upto ",num,":")
    print(n1)
else:
    print("Fibonacci sequence :")
while count< num:
    print(n1)
    nth=n1+n2
    n1=n2n2=nth
    count+=1    