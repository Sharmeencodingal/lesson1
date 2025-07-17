# 1. Storing birthdays of three people
name1 = "Ali"
bday1 = "12 March"

name2 = "Sara"
bday2 = "5 July"

name3 = "Ahmed"
bday3 = "22 November"

print("🎂 Birthdays Stored:")
print(name1, "has birthday on", bday1)
print(name2, "has birthday on", bday2)
print(name3, "has birthday on", bday3)

print("\n")

# 2. Congratulation messages
print("🎉 Happy Birthday,", name1, "!")
print("🎉 Happy Birthday,", name2, "!")
print("🎉 Happy Birthday,", name3, "!")

print("\n")

# 3. Finding square root of a number
import math
num = float(input("Enter a number to find square root: "))
if num >= 0:
    root = math.sqrt(num)
    print("Square root of", num, "is", round(root, 2))
else:
    print("❌ Cannot find square root of a negative number.")

print("\n")

# 4. Checking if a character is an alphabet
char = input("Enter a character to check if it's an alphabet: ")

if char.isalpha():
    print("✅", char, "is an alphabet.")
else:
    print("❌", char, "is not an alphabet.")
