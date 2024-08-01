# Input marks for 5 subjects
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
mark4 = float(input("Enter marks for subject 4: "))
mark5 = float(input("Enter marks for subject 5: "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
average_marks = total_marks / 5
print(f"\nMarks entered:")
print(f"Subject 1: {mark1}")
print(f"Subject 2: {mark2}")
print(f"Subject 3: {mark3}")
print(f"Subject 4: {mark4}")
print(f"Subject 5: {mark5}")
print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")