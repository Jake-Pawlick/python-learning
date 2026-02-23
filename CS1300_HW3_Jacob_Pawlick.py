# Problem 1: Boolean Expression Evaluator
'''
a = int(input("Please type in an integer to be a: "))
b = int(input("Please type in an integer to be b: "))
c = int(input("Please type in an integer to be c: "))
if a < b < c:
    check1 = True
else:
    check1 = False
if not (a > b or b > c):
    check2 = True
else:
    check2= False
if a <= b and b <= c:
    check3 = True
else:
    check3 = False
if check2 == check3:
    morgan = 1
else:
    morgan = 0
print("a < b < c                :",check1)
print("not (a > b or b > c)     :",check2)
print("a <= b and b <= c        :",check3)
if morgan == 1:
    print("\nDe Morgan's confirmed: Expressions 2 and 3 match!")
elif morgan == 0:
    print("\nDe Morgan's not confirmed: Expressions 2 and 3 DO NOT match")
'''
# Problem 2: Weather Advisory System
'''
temp = int(input("Please enter the curent temperature (°F): "))
rain = input("Is it currenty raining? (yes/no): ")
if rain == "yes":
    rain = 1
else:
    rain = 0
if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")
elif temp > 85 and rain == 1:
    print("Warm rain — watch for flash floods.")
elif temp > 85 and rain == 0:
    print("Hot and dry — stay hydrated.")
elif 60 <= temp <= 85 and rain == 1:
    print("Grab an umbrella!")
elif 60 <= temp <= 85 and rain == 0:
    print("Nice weather — enjoy your day!")
elif 32 <= temp <= 59:
    print("It's cold — bundle up!")
elif temp < 32:
    print("FREEZE WARNING: Roads may be icy!")
'''
# Problem 3: Student Grade Report
'''
name = input("Please enter your name: ")
ex1 = int(input("Enter your score for Exam 1: "))
ex2 = int(input("Enter your score for Exam 2: "))
ex3 = int(input("Enter your score for Exam 3: "))
avg = (ex1+ex2+ex3)/3
if 90 <= avg <= 100:
    grade = "A"
elif 87 <= avg <= 89:
    grade = "A-"
elif 83 <= avg <= 86:
    grade = "B+"
elif 80 <= avg <= 82:
    grade = "B"
elif 77 <= avg <= 79:
    grade = "B-"
elif 73 <= avg <= 76:
    grade = "C+"
elif 70 <= avg <= 72:
    grade = "C"
elif 67 <= avg <= 69:
    grade = "C-"
elif 63 <= avg <= 66:
    grade = "D+"
elif 60 <= avg <= 62:
    grade = "D"
elif avg < 60:
    grade = "F"
if avg>=90:
    status = "Dean's List"
elif avg>=70:
    status = "Good Standing"
elif avg>=60:
    status = "Academic Probation"
elif avg<60:
    status = "Academic Suspension Warning"
print(f"="*35)
print(f"Student Grade Report".center(35))
print(f"="*35)
print("Student:         ",name.title())
print("Exam 1 Score:    ",ex1)
print("Exam 2 Score:    ",ex2)
print("Exam 3 Score:    ",ex3)
print(f"-"*35)
print("Grade Average:   ",avg)
print("Letter Grade:    ",grade)
print("Status:          ",status)
print(f"="*35)
'''