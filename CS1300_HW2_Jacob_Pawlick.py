# Problem 1: User Profile Generator 
"""
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
year = input("Please enter your birth year: ")
hobby = input("Please enter your favorite hobby: ")
print(f"="*50)
print(f"User Profile".center(50))
print(f"="*50)
print(f"Name:       ",first_name.title(),last_name.title(),"\nAge:        ",2026-int(year),"\nHobby:      ",hobby)
print(f"-"*50)
print(f"Thank you for creating your profile :)".center(50))
print(f"="*50)
"""
# Problem 2: Text Analyzer
"""
print(f" Text Analyzer ".center(30,"="))
sentence = input("Please type a sentence: ")
sentence = sentence.lower()
vowels = (
    sentence.count("a") +
    sentence.count("e") +
    sentence.count("i") +
    sentence.count("o") +
    sentence.count("u")
)
if sentence[0].isupper():
    cap = "True"
elif sentence[0].islower():
    cap = "False"
if sentence[-1] == "!" or "." or "," or "?" or ";" or ":":
    punc = "True"
else:
    punc = "False"
print(f"Analysis Results".center(30,"-"))
print(f"Total Characters (with spaces):",len(sentence))
print(f"Total Characters (without spaces):",len(sentence)-sentence.count(" "))
print(f"Number of Words: ",len(sentence.split()))
print(f"Number of vowels: ",vowels)
print(f"Uppercase version: ",sentence.upper())
print(f"Lowercase version: ",sentence.lower())
print(f"Reversed: ",sentence[::-1])
print(f"Starts with capital?: ",cap)
print(f"Ends with punctuation?: ",punc)
"""
# Bonus Question! Palindrome Checker
"""
original_string = input("Please enter a word or phrase to see if it's a palindrome: ")
string = original_string.lower()
string = string.replace(" ", "")
palin = string[::-1]
print("="*20)
if string == palin:
    print("Yes!",string,"is a palindrome!")
    print("What you typed, but all lowercase and no spaces:",string)
    print("The reverse of what you typed is:",palin)
else:
    print("No,",string,"is not a palindrome")
"""