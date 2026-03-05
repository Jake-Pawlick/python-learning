#problem 1 - Temperature Converter
'''
temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F): ").strip().upper()

if scale == "C":
    f = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {f:.1f}°F")
elif scale == "F":
    c = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {c:.1f}°C")
else:
    print("Invalid scale.")
'''
#problem 2 - String Analyzer
'''
sentence = input("Enter a sentence: ")

total_chars = len(sentence)
upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

for ch in sentence:
    if ch.isupper():
        upper_count += 1
    if ch.islower():
        lower_count += 1
    if ch.isdigit():
        digit_count += 1
    if ch == " ":
        space_count += 1

print(f"Total characters: {total_chars}")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Reversed: {sentence[::-1]}")
'''
#problem 3 - List Operations Toolkit
'''
numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

print("Original:", numbers)
print(f"First: {numbers[0]}, Last: {numbers[-1]}")
print("Middle 4:", numbers[3:7])

numbers.append(99)
print("After append 99:", numbers)

numbers.insert(0, 0)
print("After insert 0:", numbers)

numbers.remove(42)
print("After remove 42:", numbers)

removed = numbers.pop()
print("Popped:", removed)
print("After pop:", numbers)

print(23 in numbers)
print("Index of 16:", numbers.index(16))

print("Final:", numbers)
print("Length:", len(numbers))
'''
#problem 4 - Course Eligibility Checker
'''
gpa = float(input("Enter GPA (0.0-4.0): "))
credits = int(input("Enter credit hours completed: "))
prereq_input = input("Prerequisite completed? (yes/no): ").strip().lower()
prereq_done = (prereq_input == "yes")

if gpa >= 3.5 and credits >= 60 and prereq_done:
    status = "Approved: You meet all requirements."
elif gpa >= 3.5 and credits >= 60 and not prereq_done:
    status = "Conditionally approved: Complete the prerequisite first."
elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."
elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."
else:
    status = "Denied: GPA is below minimum threshold."

print("--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print(f"Credits: {credits}")
print(f"Prerequisite: {'Yes' if prereq_done else 'No'}")
print(f"Status: {status}")
print("----------------------------")
'''
#problem 5 - Student Roster Manager
'''
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

print("=== CLASS ROSTER ===")
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {scores[i]}")
print("====================")

hi_i = 0
lo_i = 0
for i in range(1, len(scores)):
    if scores[i] > scores[hi_i]:
        hi_i = i
    if scores[i] < scores[lo_i]:
        lo_i = i

print(f"Highest: {names[hi_i]} - {scores[hi_i]}")
print(f"Lowest: {names[lo_i]} - {scores[lo_i]}")

total = 0
for s in scores:
    total += s
avg = total / len(scores)
print(f"Average: {avg:.2f}")

print("--- Grade Report ---")
for i in range(len(names)):
    s = scores[i]
    if 90 <= s <= 100:
        grade = "A"
    elif 80 <= s <= 89:
        grade = "B"
    elif 70 <= s <= 79:
        grade = "C"
    elif 60 <= s <= 69:
        grade = "D"
    else:
        grade = "F"
    print(f"{names[i]}: {s} -> {grade}")

names.append("Frank")
scores.append(77)

drop_index = names.index("Diana")
names.pop(drop_index)
scores.pop(drop_index)

print("Updated roster length:", len(names))
'''