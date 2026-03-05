# Problem 1: BMI Calculator
'''
weight = float(input("Enter weight: "))
checku = input("Enter unit system: ")
if checku == "m" or checku == "M":
    system = "metric"
    height = float(input("enter your height (in meters): "))
elif checku == "i" or checku == "I":
    system = "imperial"
    height = float(input("enter your height (in inches): "))
else:
    print("Invalid unit system.")
    exit()
if system == "metric":
    bmi = weight / (height ** 2)
elif system == "imperial":
    bmi = (weight * 703) / (height ** 2)
if bmi < 18.5:
    cat = "underweight"
elif 18.5<=bmi<=24.9:
    cat = "normal weight"
elif 25.0<=bmi<=29.9:
    cat = "overweight"
elif bmi>=30:
    cat = "obese"
print(f"your bmi is {bmi:.1f}")
print("Category:", cat)
'''
# Problem 2: Password Strength Checker
'''
password = input("Please enter your password: ")
criteria = 0

if len(password) >= 8:
    lencheck = "PASS"
    criteria += 1
else:
    lencheck = "FAIL"

uppercheck = "FAIL"
lowercheck = "FAIL"
digitcheck = "FAIL"
specialcheck = "FAIL"

for char in password:
    if char.isupper():
        uppercheck = "PASS"
    elif char.islower():
        lowercheck = "PASS"
    elif char.isdigit():
        digitcheck = "PASS"
    else:
        specialcheck = "PASS"

if uppercheck == "PASS":
    criteria += 1
if lowercheck == "PASS":
    criteria += 1
if digitcheck == "PASS":
    criteria += 1
if specialcheck == "PASS":
    criteria += 1

print("Length:", lencheck)
print("Uppercase:", uppercheck)
print("Lowercase:", lowercheck)
print("Digit:", digitcheck)
print("Special:", specialcheck)

if password == "":
    rating = "No password entered"
elif criteria == 5:
    rating = "Strong"
elif criteria == 3 or criteria == 4:
    rating = "Moderate"
elif criteria == 1 or criteria == 2:
    rating = "Weak"

print("Password Strength:", rating)
'''
# Problem 4: Parking Fee Calculator
'''
type = input("Enter vehicle type (car/motorcycle/truck): ").strip().lower()
hours = float(input("Enter the number of hours your vehicle has been parked: "))
passholder = input("Monthly pass? (yes/no): ").strip().lower()
if passholder == "yes":
    fee = 0
elif type == "motorcycle" and hours<=2:
    fee = 1
elif type == "motorcycle" and hours>2:
    fee = (1 + (0.5 * (hours - 2)))
elif type == "car" and hours<=2:
    fee = 3
elif type == "car" and hours>2:
    fee = (3 + (1.5 * (hours - 2)))
elif type == "truck" and hours<=2:
    fee = 5
elif type == "truck" and hours>2:
    fee = (5 + (2.5 * (hours - 2)))
else:
    print("Invalid vehicle type.")
    exit()
print("--- Parking Receipt ---")
print("Vehicle:", type.title())
print(f"Duration: {hours} hours")
print("Pass Holder:", passholder.title())
print(f"Fee: ${fee:.2f}")
print("-"*23)
'''
# Problem 5: Word Frequency Counter
'''
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split()
print("Total words:", len(words))
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print("Unique words:", unique)
print("--- Word Frequencies ---")
maxword = ""
maxcount = 0
for u in unique:
    count = 0
    for w in words:
        if w == u:
            count += 1
    print(f"{u}: {count}")
    if count > maxcount:
        maxcount = count
        maxword = u
print(f'Most frequent word: "{maxword}" ({maxcount} times)')
'''