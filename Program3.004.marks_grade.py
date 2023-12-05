# Write a python program to compute grade of students using if else ladder. 
#The grades are assigned as followed:
# a. Marks Grade

# b. marks<50 F
# c. 50≤marks< 60 C
# d. 60≤marks<70 B
# e. 70≤marks<80 B+
# f. 80≤marks<90 A
# g. 90≤marks≤ 100 A+ 

marks = float(input("Enter your marks: "))

if marks < 50:
    print("Grade F")
elif 50 <= marks < 60:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade B") 
elif 70 <= marks < 80:
    print("Grade B+")
elif 80 <= marks < 90:
    print("Grade A")
elif 90 <= marks <= 100:
    print("Grade A+")
