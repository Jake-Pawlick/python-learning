
# Unit 1: BEGINNER EXERCISE
'''

# Create your RGB color tuple here
rgb_color = (255, 128, 0)

# Print each color channel
print(rgb_color[0])
print(rgb_color[1])
print(rgb_color[2])

# Create palette list and add color
palette = []
palette.append(rgb_color)

# Print the palette
print(palette)


'''
# Unit 1: INTERMEDIATE EXERCISE
'''

# Create student tuples
student1 = ("Alice", 88, 20)
student2 = ("Bob", 92, 21)
student3 = ("Charlie", 85, 19)

# Store in classroom list
classroom = [student1, student2, student3]

# Print second student's name using double subscripting
print(classroom[1][0])

# Unpack first student's information
name, grade, age = classroom[0]

# Print formatted message
print(name + " is " + str(age) + " years old and has a grade of " + str(grade))

'''
# Unit 1: ADVANCED EXERCISE
'''
# Create original student tuple
student_name = "David"
exam_scores = [80, 85, 90]
final_grade = sum(exam_scores) / len(exam_scores)

student_tuple = (student_name, exam_scores, final_grade)

print(student_tuple)

# Add fourth exam score
exam_scores.append(95)

# Calculate new average
new_final_grade = sum(exam_scores) / len(exam_scores)

# Create new tuple with updated final grade
updated_student_tuple = (student_name, exam_scores, new_final_grade)

print(updated_student_tuple)
'''
# Unit 2: BEGINNER EXERCISE
'''

# Create a list of three homework grades
grades = [80, 85, 90]

# Create a tuple representing today's date (month, day, year)
today = (4, 21, 2026)

# Function to boost grades by 5 points
def boost_grades(grades_list):
    for i in range(len(grades_list)):
        grades_list[i] += 5
    return grades_list

# Call function with grades list
boosted = boost_grades(grades)

# Print result
print(boosted)

# We used a list for grades because grades need to be changed (mutable),
# and we used a tuple for the date because dates should not change (immutable)
'''

# Unit 2: INTERMEDIATE EXERCISE
'''

# Function using *args to find min and max
def find_range(*args):
    return (min(args), max(args))

# Test with 3 numbers
print(find_range(10, 20, 5))

# Test with 7 numbers
print(find_range(3, 8, 15, 6, 22, 1, 9))

# Given list of test scores
test_scores = [78, 92, 85, 88, 91]

# Use * to unpack list into function
print(find_range(*test_scores))
'''

# Unit 2: ADVANCED EXERCISE
'''

# Function to calculate statistics using *args
def calculate_statistics(*args):
    count = len(args)
    total = sum(args)
    average = total / count
    return (count, total, average)

# Function to update student records (creates NEW tuples)
def update_student_records(student_list, bonus):
    updated_list = []
    
    for name, grade in student_list:
        new_grade = grade + bonus
        updated_list.append((name, new_grade))
    
    return updated_list

# Test calculate_statistics
stats = calculate_statistics(80, 90, 100, 70)
print(stats)

# Original student records
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]

# Update student records with bonus
updated_students = update_student_records(students, 5)

# Print results
print(updated_students)
'''
# Unit 3: BEGINNER EXERCISE
'''

# Create a nested list (3x3 grid)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print entire grid
print(grid)

# Print center number using double indexing
print(grid[1][1])

# Print each row on a separate line using nested loops
for row in grid:
    for num in row:
        print(num, end=" ")
    print()
'''

# Unit 3: INTERMEDIATE EXERCISE
'''

# Given list of student scores
scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

# List comprehension for passing grades (60 or above)
passing_grades = [score for score in scores if score >= 60]
print(passing_grades)

# List comprehension for letter grades based on passing grades
letter_grades = [
    'A' if score >= 90 else
    'B' if score >= 80 else
    'C' if score >= 70 else
    'D'
    for score in passing_grades
]

print(letter_grades)
'''

# Unit 3: ADVANCED EXERCISE
'''

# Create 4x4 multiplication table using nested list comprehension
table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

# Print formatted table
for row in table:
    for val in row:
        print(val, end="\t")
    print()

# Function to sum diagonal elements
def sum_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

# Test diagonal sum
print(sum_diagonal(table))

# Generator expression for even numbers in table
even_numbers = (num for row in table for num in row if num % 2 == 0)

# Print first 5 even numbers
count = 0
for num in even_numbers:
    print(num)
    count += 1
    if count == 5:
        break
'''