date = input("Enter the date to be checked (dd/mm/yyyy): ")
c = date.split("/")
b = list(map(int, c)) #[12/2/2020]
input_year = b[2]
if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    is_leap = True
    print("%d is a Leap Year" % input_year)
else:
    is_leap = False
    print("%d is not a Leap Year" % input_year)

if is_leap:
    next_anniversary_year = input_year + 1
    print("Next anniversary year:", next_anniversary_year)
else:
    previous_anniversary_year = input_year - 1
    print("Previous anniversary year:", previous_anniversary_year)