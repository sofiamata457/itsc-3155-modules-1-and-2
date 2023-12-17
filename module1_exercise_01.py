gradeNumber = input("Enter a grade from 0 to 100:")
if int(gradeNumber) in range(0,100):
    if int(gradeNumber) in range(90,100):
        print("Your grade is A")
    elif int(gradeNumber) in range(80,90):
        print("Your grade is B")
    elif int(gradeNumber) in range(70,80):
        print("Your grade is C")
    elif int(gradeNumber) in range(60,70):
        print("Your grade is D")
    else :
        print("Your grade is F")
else:
    print("Invalid Number")