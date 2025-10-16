# lesson 5
# Task 1
# # Print the multiplication table for the user-defined number. If the user typed in 7, the output should be as follows:
# # 7 * 1 = 7
# # 7 * 2 = 14
# # 7 * 3 = 21
# # …
# number = int(input("Provide a nr: "))
# for num in range(1, 11):
#     total = number * num
#     print(f"{number} * {num} = {total}")


# Task 3
# # The user types in the start and end points of the range and a number.
# # If the number is not in the range, the program asks the user to re-enter the number,
# # and so on until the user enters the number correctly. The program displays all numbers in the range,
# # highlighting the number with exclamation marks. For instance: 1 2 3 !4! 5 6 7.
# nr1 = int(input("Write the first number: "))
# nr2 = int(input("Provide the last number: "))
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# nr = int(input("Number in the range: "))
# while nr not in range(start, end + 1):
#     print("Please provide a number within the range")
#     nr = int(input("Number in the range: "))
# for num in range(start, end + 1):
#     if num == nr:
#         print(f"!{num}!", end=" ")
#     else:
#         print(num, end=" ")

# print("\n")
# tema 9
# Task 2
# Count the number of integers in the range from 100 to 999 that have two identical digits.
# count = 0
# for num in range(100, 999 + 1):
#     digit = str(num)
#     if digit[0] == digit[1] or digit[1] == digit[2] or digit[2] == digit[0]:
#         count = count + 1
# print(count)


# My exercise:
# # # Vreau sa cumpar 5 chitari a cate 1 costa 100 de lei. Eu am 400 de lei.
# # # Trebuie sa ii spun calculatorului asta si sa imi spuna cate chitari as putea sa cumpar.
# # # Daca introduc numar de chitari care va fi peste buget atunci trebuie sa imi spuna asta
# # # si sa ma roage sa introduc alt numar de chitari:
# chitara = 100
# buget = 400
# chitari_dorite = int(input("Cate chitari doresti: ")) * chitara
# while chitari_dorite > buget:
#     print(
#         f"Suma totala a atatea chitari este {chitari_dorite} , deci peste buget \nte rog introdu alra cantitate."
#     )
#     chitari_dorite = int(input("Cate chitari doresti: ")) * chitara
# total = buget - chitari_dorite
# print(f"Restul dumneavoastra este: {total}")

# lesson 7
# 2
# The user types in two numbers.
# Print the whole range first
# Print all odd numbers in the specified range after.
# nr1 = int(input("Provide the first nr of the range: "))
# nr2 = int(input("Provide the last nr of the range: "))
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# for nr in range(start, end + 1):
#     print(nr, end=" ")
# print("\n")
# for nr in range(start, end + 1):
#     if nr % 2 != 0:
#         print(nr, end=" ")


# Task 1
# The user types in two numbers (start and end points of the range). Analyze all the numbers in this range as follows:
# if the number is a multiple of 7, print it. (Let s try it with a list)

# nr1 = int(input("Provide the first nr of the range: "))
# nr2 = int(input("Provide the last nr of the range: "))
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# multiples = []
# for num in range(start, end + 1):
#     if num % 7 == 0:
#         multiples.append(num)
# print(multiples)

# tema 10
# Task 2
# Print the multiplication table for all numbers from 1 to 10. For example:
# 1*1 = 1 1*2 = 2 ….. 1*10 = 10
# ..................................
# 10*1 = 10 10*2 = 20 …. 10*10 = 100
# nr_to_multiply = range(1, 11)
# nr_to_multiply_with = range(1, 11)
# for nr in nr_to_multiply:
#     for num in nr_to_multiply_with:
#         total = nr * num
#         print(f"{nr} * {num} = {total}")


# Task 3
# Print the multiplication table in the user-specified range.
# If the user specified 3 and 5, the multiplication table might look like this:
# 3*1 = 3 3*2 = 6 3*3 = 9 … 3*10 = 30
# .....................................
# 5*1 = 5 5*2 = 10 5*3 = 15 … 5*10 = 50

# nr1 = int(input("Provide the first nr of the range: "))
# nr2 = int(input("Provide the last nr of the range: "))
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# for num in range(start, end + 1):
#     for nr in range(1, 11):
#         total = num * nr
#         print(f"{num} * {nr} = {total}", end=" ")


# lesson 10
# Task 1
# The user types in the size of the square's sides. Print a solid square. The size is equal to the typed in square's side.
# Say the user typed in 3, the output will be as follows:
# ***
# ***
# ***
# size = int(input("Provide the size : "))
# for _ in range(size):
#     print("*" * 3)


# Task 2
# The user types in the width and height of a rectangle. Print a solid rectangle of the specified height and width.
# Say the user typed in the height equal to 3, and width 5, the output should be as follows:
# *****
# *****
# *****

# height = int(input("Type in the height: "))
# width = int(input("Type in the width: "))
# for _ in range(height):
#     print("*" * width)


# Task 3
# The user types in the size of the square's sides. Print an empty square (only its sides are displayed).
# The side is equal to the typed in size.
# side_size = int(input("Type in the size of the sides of the square: "))
# print("*" * (side_size + 2))
# for _ in range(side_size):
#     print("*" + (" " * side_size) + "*")
# print("*" * (side_size + 2))
# KINDA BUT NO _ YOU LL NOT HAVE the same amount of * as the input

#  OR better:

# square_size = int(input("Provide the square size: "))
# # top row
# print("*" * square_size)
# # middle rows
# for _ in range(square_size - 2):
#     print("*" + " " * (square_size - 2) + "*")
#     # bottom row
# print("*" * square_size)


# Lesson 11
# Task 1
# # The user types in a number. Determine how many digits this number has,
# # find their sum and average. Determine how many zeros this number has. Implement a dialog with the user through a menu.
# while True:
#     number = input("Provide a number, or 'quit': ")
#     if number == "quit":
#         print("Goodbye!")
#         break
#     if not number.isdigit():
#         print("Please provide a proper number")
#         continue
#     print(f"The inserted number {number} has {len(number)} digits")
#     count = 0
#     for num in number:
#         if num == "0":
#             count = count + 1
#     print(f"The number has {count} zeros")
#     lst = []
#     for num in number:
#         lst.append(int(num))
#         total = sum(lst)
#     print(total, "is the sum")
#     average = total / len(number)
#     print(average, " is the average")


# ! TINE MINTE = LISTA.APPEND(INT(NR)) PENTRU A TRANSFORMA LISTA IN INT!!

# lsttt = ["Comedy", "North", "Star"]
# print(lsttt)
# lsttt2 = ["Comedy", "North", "Star"]
# for i in lsttt2:
#     print(i, end=", ")
# lst3 = [nr * nr for nr in range(10) if nr != 4]
# print(lst3)


# Task 2
# Write a program that displays a chessboard with a set cell size. For example, three,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***
# cellsize = int(input("Provide the cell size: "))

# # The chessboard has 8 rows, but each row must be expanded by `cellsize`
# for row in range(8):
#     for _ in range(cellsize):  # repeat each row 'cellsize' times vertically
#         line = ""
#         for col in range(8):
#             if (row + col) % 2 == 0:  # even = stars, odd = dashes
#                 line += "*" * cellsize
#             else:
#                 line += "-" * cellsize
#         print(line)


# Task 3
# Write a program that tests users for their multiplication table skills.
# The program prints two numbers, and the user must enter their product.
# Develop several levels of difficulty (they should differ in complexity and number of questions).
#  Print the points that represent the user's skills.


import random

print("Welcome to the Multiplication Quiz! 🧮")

score = 0

# Define levels (range of numbers and number of questions)
levels = {
    1: {"range": (1, 10), "questions": 5},
    2: {"range": (5, 20), "questions": 7},
    3: {"range": (10, 50), "questions": 10},
}
# {} means dictionary in Python.
# A dictionary is like a real-world dictionary:
# In a real dictionary: word → definition
# In Python dictionary: key → value
# So {} is used when we want to group together pairs of information.

# Loop through levels
for level, data in levels.items():
    # for ... in ... → a loop: it repeats the code inside it for each item.
    # level, data → unpacking the tuple:
    # On the first loop: level = 1, data = {"range": (1, 10), "questions": 5}
    # On the second loop: level = 2, data = {"range": (5, 20), "questions": 7}
    # On the third loop: level = 3, data = {"range": (10, 50), "questions": 10}
    # Unpacking means Python automatically splits the tuple into two variables.
    # levels = big dictionary <=> the key and the inside are the values
    # level = 1/2/3 =dictionaries just like the outer "levels"
    # data = value dictionary for level = > so range and question are the values of data
    # range and question is the value of data dictionary
    # which is the value of level dictionary
    # which is the value of levels dictionary
    print(f"\n=== Level {level} ===")
    print(f"Numbers from {data['range'][0]} to {data['range'][1]}")
    # data['range'] = (1, 10) a tuple of min and max number for lvl 1 as example
    # [0] and [1]
    # A tuple (1, 10) is like a list with two elements: index 0 = 1, index 1 = 10
    # data['range'][0] → first number → 1 (the minimum number for this level)
    # data['range'][1] → second number → 10 (the maximum number for this level)
    for _ in range(data["questions"]):
        # Command: _
        # _ is a placeholder variable.
        # We don’t care about the number, we just want the loop to repeat data["questions"] times.
        # Command: range(data["questions"])
        # data["questions"] → number of questions for this level
        # range(n) → creates a sequence of numbers 0, 1, 2, ..., n-1
        # The loop repeats once for each number in this sequence
        # Example
        # If Level 1 has 5 questions, the loop will run 5 times.
        a = random.randint(*data["range"])
        b = random.randint(*data["range"])
        total = a * b
        print(f"\nWhat is {a} × {b}?")

        try:
            answer = int(input("Your answer: "))
            if answer == total:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is {total}")
                score -= 1
        except ValueError:
            print("⚠️ Please enter a number!")
            score -= 1

print("\n=== Quiz Finished ===")
print(f"Your final score: {score}")

# Skill evaluation
if score > 15:
    print("🌟 Excellent multiplication skills!")
elif score > 5:
    print("👍 Good job, keep practicing!")
else:
    print("😅 You need more practice!")
