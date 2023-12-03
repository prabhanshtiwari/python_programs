# Write a program to take input of name, rollno and marks obtained by a student in 4 subjects of 100 marks each and display the name, rollno, total marks with percentage score secured 

name = input("Enter name of the student: ")
roll_no = int(input("Enter roll number: "))
maths = int(input("Enter marks obtained in Mathematics(out of 100): "))
english = int(input("Enter marks obtained in English(out of 100): "))
computer_science = int(input("Enter marks obtained in Computer Science(out of 100): "))
hindi = int(input("Enter marks obtained in Hindi(out of 100): "))

marks_obtained = maths + english + computer_science + hindi
maximum_marks = 400
percentage = (marks_obtained / maximum_marks) * 100

print("Name: ", name)
print("Roll number: ", roll_no)
print("Total marks obtained by student: ", marks_obtained)
print("Percentage: ", percentage)
