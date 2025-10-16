# -The user types in the number of meters. Convert meters to centimeters, decimeters, millimeters, miles and display the result.
# meters = float(input("Mters: "))
# centimeters = 100 * meters
# decimeters = 10 * meters
# millimeters = 1000 * meters
# miles = meters / 1609.344
# choice = input(
#     "For centimeters type 'cm' , for decimeter type 'dm', for millimeters type 'mm', for miles type 'mil': "
# )
# if choice == "cm":
#     print("centimeters = meters * 100 =", centimeters)
#     print(f"Meters converted to centimeters is {centimeters}")
# elif choice == "dm":
#     print("decimeters = 10 * meters =", decimeters)
#     print(f"Meters converted to decimeters is {decimeters}")
# elif choice == "mm":
#     print("millimeters = 1000 * meters =", millimeters)
#     print(f"Meters converted to millimeters is {millimeters}")
# elif choice == "mil":
#     print("miles = meters / 1609.344 = ", miles)
#     print(f"Meters converted to miles is {miles}")
# else:
#     print("ERROR")


# Task 1
# The user types in a number. Check if it is even or odd. If the number is even, print the number and the text "Even number."
# If the number is odd, print the number and the text "Odd number."
# nr = int(input("Provide a number: "))
# if nr % 2 == 0:
#     print("The number", nr, "you provided is even because it divided perfectly by 2")
# else:
#     print(
#         "The number",
#         nr,
#         "you provided is odd because it does not divide perfectly by 2",
#     )


#  Task 2
# The user types in a number. Check if it is a multiple of 7. If it is, print
#  the number and the text "Your number is a multiple of 7." If it is not, print the number and the text
# "Your number is not a multiple of 7."
# number = int(input("Provide a number: "))
# if number % 7 == 0:
#     print(f"Your number  {number} is a multiple of 7")
# else:
#     print(f"Your number {number} is not a multiple of 7")

# Task 3
# The user types in two numbers. Find the maximum of two numbers and print it.
# num1 = int(input("Nr1: "))
# num2 = int(input("Nr2: "))
# if num1 > num2:
#     print(num1, "is the maximum")
# elif num1 < num2:
#     print(num2, "is the maximum")
# elif num1 == num2:
#     print("The numbers are equal")
# or
# number1 = int(input("Provide the first number: "))
# number2 = int(input("Provide the second number: "))
# maximum = max(number1, number2)
# minimum = min(number1, number2)
# choice = input("To get the maximum type 'max', and to get the minimum type 'min': ")
# if choice == "max":
#     print(maximum)
# elif choice == "min":
#     print(minimum)
# else:
#     print("Error")

# Task 5
# The user types in two numbers. Based on the user's choice, print the result of
# the sum, difference, product of these numbers or their arithmetic mean.

# try:
#     nr1 = int(input("First number: "))
#     nr2 = int(input("Second number: "))
#     sum = nr1 + nr2
#     difference = nr1 - nr2
#     product = nr1 * nr2
#     arithmetic_mean = (nr1 + nr2) / 2
#     choice = input("Type 'sum', 'difference', 'product', or 'arithmetic mean': ")
#     if choice == "sum":
#         print(sum)
#     elif choice == "difference":
#         print(difference)
#     elif choice == "product":
#         print(product)
#     elif choice == "arithmetic mean":
#         print(arithmetic_mean)
# except ValueError:
#     print("Invalid input")


# --------------------------------------------------------------------------------------

# lesson8!!!!!!!!!!!!!
# Concept of ranges and loops

# range(start, end + 1)
# This generates a sequence of numbers, starting at start
# and ending at end (inclusive, because we use +1).
# It does not create a list —
# it's a special object that behaves like a list but is more
# memory efficient.
# range(3, 7)  # means: 3, 4, 5, 6

# How to Count Numbers in a

# option1 : count = end - start + 1 - THIS just calculates how many numbers are in the range
# start = 3
# end = 6
# count = 6 - 3 + 1  # ➞ 4 (because 3, 4, 5, 6)

# option2: count = len(range(start, end + 1))- This builds a range object, then counts how many numbers are in it.
# It gives the same result as the formula above, but it's a tiny bit slower.
# count = len(range(3, 7))  # ➞ 4


# Creating a LIST of numbers

# Option1- create the list directly
# numbers = list(range(start, end + 1))- This gives you a list of all the numbers in the range.
# numbers = list(range(3, 7))  # ➞ [3, 4, 5, 6]
# print(numbers)(no loop)

# Option2 - Start an EMPTY list and fill it up yourself
# numbers = []
# for i in range(start, end + 1):
#     numbers.append(i)
# This creates an empty list and fills it one number at a time. with a loop
# numbers = [3, 4, 5, 6] - same result

# full list instantly vs build manually


# LOOPS

# In Python, a for loop lets you repeat code once for each item in a sequence.
# for i in range(1, 4):
#     print(i) =>
# 1
# 2
# 3

# Loops and lists

# 1. Building a list manually
# numbers = []
# for num in range(start, end + 1):
#     numbers.append(num)

# 2. Calculating a sum with a loop
# If we don't use sum(numbers), we can do this:
# total = 0
# for num in range(start, end + 1):
#     total += num  # same as total = total + num

# What happens:
# total starts at 0.
# Each num from the range is added to total.
# start = 3
# end = 6
# Loop steps:

# total = 0
# num = 3 → total = 0 + 3 = 3
# num = 4 → total = 3 + 4 = 7
# num = 5 → total = 7 + 5 = 12
# num = 6 → total = 12 + 6 = 18

# 3. Counting elements (manually, using a loop)
# count = 0
# for num in range(start, end + 1):
#     count += 1 same as count = count +1
# Each time the loop runs, we increase count by 1.

# Same result as:
# count = end - start + 1
# or count = len(range(start, end + 1))

# 4. Looping through a list
# Once you’ve created a list like this:
# numbers = list(range(start, end + 1))  # [3, 4, 5, 6]
# You can loop through the list directly:
# for num in numbers:
# print(num)
# This is the same as:
# for num in range(start, end + 1):
# print(num)

# -------------------------------------------------------------------------------------------------

# Task 1
# The user types in two numbers. Find the sum and average of numbers in the specified range.

# version 1 - list without loop
# nr1 = int(input("First number: "))
# nr2 = int(input("Second number: "))
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# choice = input(
#     "'sum' for the sum in the range , 'avr' for the average mean of the range: "
# )
# numbers = list(range(start, end + 1))
# #  sau
# count = end - start + 1
# # si la sfarsit impartim la count inloc de len
# if choice == "sum":
#     total = sum(numbers)
#     print(total)
# elif choice == "avr":
#     total = sum(numbers)
#     # average = total / len(range(start, end + 1))
#     average = total / count
#     print(average)

# version 2- using a loop
nr1 = int(input("First number: "))
nr2 = int(input("Second number: "))
start = min(nr1, nr2)
end = max(nr1, nr2)
choice = input(
    "'sum' for the sum in the range , 'avr' for the average mean of the range: "
)
numbers = []
if choice == "sum":
    for num in range(start, end + 1):
        numbers.append(num)
    total = sum(numbers)
    # The sum() function in Python requires an iterable — like a list or a range — not a single number like 'num'
    print(total)
elif choice == "avr":
    for num in range(start, end + 1):
        numbers.append(num)
    total = sum(numbers)
    average = total / len(range(start, end + 1))
    # or : average = total / len(numbers)
