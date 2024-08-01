principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))
is_senior_citizen = input("Is the customer a senior citizen (yes/no)? ").strip().lower() == "yes"
roi = 0.15 if is_senior_citizen else 0.12 if is_senior_citizen else 0.10
simple_interest = (lambda p, r, t: p * r * t / 100)(principal, roi * 100, time)
print(f"The simple interest is: {simple_interest}")