import datetime

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def find_anniversary_date(date_str):
   
    try:
        anniversary_date = datetime.datetime.strptime(date_str, "%m/%d/%Y")
        anniversary_year = anniversary_date.year

       
        is_leap_year = check_leap_year(anniversary_year)
        if is_leap_year:
            next_anniversary = anniversary_date + datetime.timedelta(days=366)
            output = f"Given Anniversary Year: Leap Year. Next Anniversary Date: {next_anniversary.strftime('%m/%d/%Y')}"
        else:
            previous_anniversary = anniversary_date - datetime.timedelta(days=365)
            output = f"Given Anniversary Year: Non Leap Year. Previous Anniversary Date: {previous_anniversary.strftime('%m/%d/%Y')}"

        return output

    except ValueError:
        return "Invalid date format. Please use format MM/DD/YYYY."

date_input = "04/11/1947"
result = find_anniversary_date(date_input)
print(result)