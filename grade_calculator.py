print("Welcome to the Grade Calculator!")
grade = int(input("Please insert here your grade: "))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F" 
if grade >= 70:    
    print(f"Congratulations! You have passed. you grade is: {letter} ") 
else:
    print(" I am sorry, You need to work harder next time.")     

