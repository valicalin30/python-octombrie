# TEMA 5
# Task 1- Aurelian
# # The user types in a number from 1 to 7 that represents a day of the week.
# # Print its name. For example, if the number is 1,
# # then you should display "Monday"; if 2, display "Tuesday," etc.
# exercitiu de index + cum sa ii spunem programului sa incerce din nou cu while:

# day_number = int(
#     input("Enter a number between 1 and 7 coresponding to the days of the week: ")
# )
# week_days = [
#     "Monday",
#     "Tuesday",
#     "Wendsday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday",
# ]
# while day_number not in range(1, 8):
#     print("Please provide a number within the range of 1 to 7")
#     day_number = int(
#         input("Enter a number between 1 and 7 coresponding to the days of the week: ")
#     )
# if day_number in range(1, 8):
#     print(week_days[day_number - 1])

# -----------------------------------------------------------------------------------------------------------------------------

# lesson 9
# Task 3
# # The user types in the start and end points of the range and a number.
# # If the number is not in the range, the program asks the user to re-enter the number,
# # and so on until the user enters the number correctly. The program displays all numbers in the range,
# # highlighting the number with exclamation marks. For instance: 1 2 3 !4! 5 6 7.
# way 1:
# try:
#     nr1 = int(input("First nr of the range: "))
#     nr2 = int(input("Last nr of the range: "))
#     start = min(nr1, nr2)
#     end = max(nr1, nr2)
#     print(f"The respective range is between {start} and {end}")
#     user_number = int(input("Provide a number in the specified range: "))
#     while user_number not in range(start, end + 1):
#         print("Please enter a number in the specified range")
#         user_number = int(input("Provide a number in the specified range: "))
#     the_range = []
#     for num in range(start, end + 1):
#         if num == user_number:
#             the_range.append(f"!{num}!")
#         else:
#             the_range.append(str(num))
#     print(" ".join(the_range))
# end=' ' face ca loop ul sa fie orizontal , nu vertical
# explanation: we build a list of strings, converting each number to: '!x!' if its the specific nr
# 'x' if not
# Fill the list using a for loop:
# The loop goes through every number in the range (from start to end).
# For each number:
# If it matches the user's number, we convert it to a string wrapped with ! (e.g., "!4!") and append it to the list.
# If it doesn't match, we just convert it to a normal string (e.g., "2") and append that.

# then :' '.joint(list) to make a single string= print # This is a function that outputs whatever is inside the parentheses to the screen.
# Here, it will print the final string produced by the " ".join(the_range) expression.
# . " ":
# A string literal consisting of a single space character.
# This is the separator we want to insert between each element
# when joining.

# join
# This is a string method that takes a list (or any iterable) of strings as an argument.
# It returns a new string consisting of each item joined together, separated by the string " " (a space).
# For example: " ".join(["a", "b", "c"]) returns "a b c".

# the_range
# This is the list variable containing strings (like '1', '!3!', '4', etc.).
# join will iterate through this list and combine all items into one string with spaces in between.

# Why is the print-join command outside the loop?
# The loop’s job is only to build the list — gathering all numbers formatted correctly.
# The print(" ".join(the_range)) outside the loop combines all these strings into one single string separated by spaces, then prints it.
# If you put the print inside the loop, you’d print each element separately on its own line or piece, resulting
# in many separate outputs — not the nice one-line display you want.


# The else in the first version handles all numbers
# that aren’t the user’s chosen one, just appending them as strings.

## if num == user_number:
# the_range.append(f"!{num}!" if num == user_number else str(num))


# or way #2 without a [] list:
# for num in range(start, end +1):
#     if num == user_number:
#         print(f'!{num}!', end=' ')
#     else:
#         print(num,end=' ')

# except ValueError:
#     print("Error")

# vs a basic range version with no highlight
# try:
#     nr1 = int(input("First number of the range: "))
#     nr2 = int(input("Last number of the range: "))
#     start = min(nr1, nr2)
#     end = max(nr1, nr2)

#     number = int(input("Provide a number within the specified range: "))
#     while number not in range(start, end + 1):
#         number = int(input("Number not in range, try again: "))

#     # the_range = list(range(start, end + 1))
#     # print(the_range)
#     # or
#     the_range = []
#     for num in range(start, end + 1):
#         the_range.append(num)
#     print(the_range)
# except ValueError:
#     print("Please enter a valid number.")


# -------------------------------------------------------------------------------------
# Tema 9
# Task 2
# Count the number of integers in the range from 100 to 999 that have two identical digits.
# count = 0
# number_list = []
# for num in range(100, 1000):
#     digit = str(num)
#     # This line converts the integer num into a string, so that you can easily access each digit by position, like this:
#     # digit[0]: the hundreds digit
#     # digit[1]: the tens digit
#     # digit[2]: the units digit
#     if (
#         digit[0] == digit[1] != digit[2]
#         or digit[1] == digit[2] != digit[0]
#         or digit[0] == digit[2] != digit[1]
#     ):
#         count += 1
#         number_list.append(num)
# print(len(number_list), end=" ")
# print(count)
# can t do it without a loop

# Task 3
# Count the number of integers in the range from 100 to 9999 that have different digits.
# count = 0
# for num in range(100, 10000):
#     digit = str(num)
#     if len(set(digit)) == len(digit):  # All digits are different
#         count += 1
# print(count)

# # or more simple:
# count = len([num for num in range(100, 10000) if len(set(str(num))) == len(str(num))])
# print(count)

# Task 4
# The user types in an integer value. Remove all 3s and 6s from this integer and print it.
# integer = int(input("Provide a nr: "))
# integer = str(integer)
# for digit in integer:
#     digit = str(digit)
#     if digit == "3" and "6":
#         integer = int(integer)
#         digit = int(digit)
#         finalnr = integer - digit
#         print(finalnr)
# # not like this but close......
# # here is how it s supposed to be:
# integer = input("Provide a number: ")  # Keep it as a string
# result = ""

# for digit in integer:
#     if digit not in ("3", "6"):
#         result += digit

# # Handle case where all digits are removed
# if result == "":
#     print("No digits left after removing 3s and 6s.")
# else:
#     print(int(result))  # Convert to int to remove any leading zeros
# ----------------------Sa recapitulam din nou aceste exercitii:
# Tema 9
# Task 2
# Count the number of integers in the range from 100 to 999 that have two identical digits.
# count = 0
# identical_nr = []
# for digit in range(100, 1000):
#     digit = str(digit)
#     if digit[0] == digit[1] or digit[1] == digit[2] or digit[2] == digit[0]:
#         identical_nr.append(digit)
#         count = count + 1
# print(count)
# list is not necessary

# Task 4
# The user types in an integer value. Remove all 3s and 6s from this integer and print it.
# while True:
#     # creating an infinite loop that keeps repeating until we tell it to stop using break
#     try:
#         # this block is where we test user input that might cause an error, such as entering text instead of nr
#         integer = input("Provide a integer: ")
#         #    as a string
#         int(integer)
#         # to check if the user actully typed in a nr. If he didn t =>ValueError= caught by the exept block
#         # we don t store the result of int(integer) because we only care about whether it fails or not.
#         if "3" not in integer and "6" not in integer:
#             print("The number is valid. It contains no 3s or 6s.")
#             break
#         #    exit the loop
#         else:
#             # if the number does contain '3' and '6' we go intto this bloc to remove them
#             result = ""
#             # empty string where we build a new string where we ll build a new number without 3s and 6s.
#             for digit in integer:
#                 #    going through every element of the original string (integer string)
#                 if digit != "3" and digit != "6":
#                     # if the digit is not 3 or 6 we add it to our result
#                     result = result + digit
#                 #    this adds valid digits to the result string
#             print("Number wihout 3 s and /or 6s", result)
#             print("Try another number.....\n")
#         # The program will ask again
#     except ValueError:
#         # this runs when the input value is not valid, e.g letters
#         # it print an error messege and continues the loop
#         print("Error")

# or easier and without while:
# integer = input("Provide a number: ")  # Keep it as a string
# result = ""

# for digit in integer:
#     if digit not in ("3", "6"):
#         result += digit

# # Handle case where all digits are removed
# if result == "":
#     print("No digits left after removing 3s and 6s.")
# else:
#     print(int(result))  # Convert to int to remove any leading zeros


# ---------------------------Exercitii cu while-----------------
# x = 1
# while x <= 3:
#     print("x is:'", x)
#     x = x + 1
# starts at x = 1
# prints value of x
# add 1 to x
# keeps looping while x<=3

# while True = code runs forever unless I break it
# True = true=> loop infinit= trebuie sa folosim break
# while True:
#     number = input(": ")
#     if number == "exit":
#         print("You typed", number)
#         break
# keeps asking for input
# stops only if user types 'exit'

# Why use while?
# You want to repeat something until a condition is met
# You don’t know in advance how many times it will need to repeat (unlike for loops)

# ---------------let s try playing around with while in these exercises-----------------

# Task 3
# Count the number of integers in the range from 100 to 9999 that have different digits.
count = 0
digit = 100  # Start from 100

while digit <= 9999:
    digit_str = str(digit)

    # Check if all digits are unique
    if len(set(digit_str)) == len(digit_str):
        count += 1

    digit += 1  # Move to the next number

print("Total numbers with all different digits:", count)
