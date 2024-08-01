n=int(input("Enter an intager :"))
answer=[]
for i in range(1,n+1):
    if i % 3==0 and i % 5==0:
        answer.append("fizzBuzz")
    elif i%3==0:
        answer.append("fizz")
    elif i%5==0:
        answer.append("buzz")
    else:
        answer.append(str(i))
    print(answer)    