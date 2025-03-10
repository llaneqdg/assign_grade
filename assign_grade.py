assign_grade = int(input("Enter your score: "))

if assign_grade >= 90:
    print("Grade: A")
elif assign_grade >= 80:
    print("Grade: B")
elif assign_grade >= 70:
    print("Grade: C")
elif assign_grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")