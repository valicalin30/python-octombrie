# # lesson 1
# # print("To be or")
# # # print("not")
# # # print("to be")
# print("'To be or\nnot\nto be'")

# # print('"Life is what happens')
# # print("    when            ")
# # print(
# #     "        you're busy making other plans \"                                   John Lennon.")
# print(
#     '"Life is what happens\n       when\n       you\'re busy making other plans            John Lennon"'
# )


# # Lesson 2
# # -The user types in the number of meters. Convert meters to centimeters, decimeters, millimeters, miles and display the result.

# # -Write a program that calculates the area of a triangle. The user types in the base and height of a triangle.

# # -The user types in a four-digit number. Flip the number and print the result. If the typed in number is 4512, the will be 2154.

# # Task1
# # meters = int(input("Print the meters: "))
# # cm = meters * 100
# # dm = meters * 10
# # mm = meters * 1000
# # miles = meters / 1609.344
# # choice = input(
# #     "To find the centemeters type 'cm' ,\nto find the decimeters write 'dm' ,\nto find the millimeters type 'mm' \nto find the miles type 'miles': "
# # )
# # if choice == "cm":
# #     print(f"Conversion for meter to cm is {cm}")
# # elif choice == "dm":
# #     print(f"Conversion for meters to dm is {dm}")
# # elif choice == "mm":
# #     print(f"Conversion for meters to millimeters is {mm}")
# # elif choice == "miles":
# #     print(f"Conversion for meters to miles is {miles}")
# # else:
# #     print("Invalid input")

# # Task2
# # Aaria = (a * b) / 2
# # a = int(input("height: "))
# # b = int(input("base: "))
# # Aria = (a * b) / 2
# # print(Aria)

# # Task3
# number = input("Original number: ")
# fliped_number = (number)[::-1]
# print(fliped_number)

# # deci asta este formula y = (x)[::-1]


# # Lesson 3/4

# Task 1
# The user types in a number. Check if it is even or odd. If the number is even, print the number and the text "Even number."
# If the number is odd, print the number and the text "Odd number."

# Task 2
# The user types in a number. Check if it is a multiple of 7. If it is, print
#  the number and the text "Your number is a multiple of 7." If it is not, print the number and the text
# "Your number is not a multiple of 7."

# Task 3
# The user types in two numbers. Find the maximum of two numbers and print it.

# Task 4
# The user types in two numbers. Find the minimum of two numbers and print it.

# Task 5
# The user types in two numbers. Based on the user's choice, print the result of
# the sum, difference, product of these numbers or their arithmetic mean.

# Task 1
# to check if a nr is even or odd we check if it diides perfectly with 2 ot if it s a multible of 2
# number = int(input("Provide a number: "))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# Task 2
# number = int(input("Provide a number: "))
# if number % 7 == 0:
#     print(f"{number} is a multiple of 7")
# else:
#     print(f"{number} is not a multiple of 7")

# task 3
# nr_1 = int(input("Provide the first number: "))
# nr_2 = int(input("Provide the second number: "))
# maximum = max(nr_1, nr_2)
# minimum = min(nr_1, nr_2)
# choice = input("Type 'max' to get the maximum value of the 2 numbers: ")
# if choice == "max":
#     if nr_1 == nr_2:
#         print("Error- the numbers provided are equal")
#     else:
#         print(maximum)

# else:
#     print("ERROR- didn t mention the objective")

# Task 4
# num1 = int(input("Provide the first number: "))
# num2 = int(input("Provide the second number: "))
# maximum = max(num1, num2)
# minimum = min(num1, num2)
# choice = input("Type 'min' to find the minimum number between the 2 provided: ")
# if choice == "min":
#     if num1 == num2:
#         print("Error- the provided numbers are equal")
#     else:
#         print(minimum)
# else:
#     print("Error - didn t mention the objective")

# task 5
# 2 numbers. sum/product/ arithmetic mean
# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))
# sum = num1 + num2
# product = num1 * num2
# arthm = (num1 + num2) / 2
# choice = input(
#     "Type 'sum' to provide the sum of the numbers, type 'product' \nto find the product \nand type'arthm' to provide the arithmetic meana: "
# )
# if choice == "sum":
#     print(sum)
# elif choice == "product":
#     print(product)
# elif choice == "arthm":
#     print(arthm)
# else:
#     print("ERROR")

# Lesson/homework 5
# Task 3
# The user types in a number. If the number is greater than 0, print "Your number is positive"; if it is less than zero,
# print "Your number is negative"; if it is equal to 0, print "Your number is equal to zero."
# number = int(input("Provide a number: "))
# if number > 0:
#     print(f"The provided number {number} is positive")
# elif number < 0:
#     print(f"The provided number {number} is negative")
# elif number == 0:
#     print(f"The provided number is equal to 0")
# else:
#     print("Error")

# # or
# try:
#     num = float(input("Please enter a number: "))

#     if num > 0:
#         print("Your number is positive")
#     elif num < 0:
#         print("Your number is negative")
#     else:
#         print("Your number is equal to zero")
# except ValueError:
#     print("Error, you didn't enter a number!")
#  try = The try block is used for error handling — it lets your program run safely even
#  something goes wrong (like the user entering text instead of a number).

# What try does:
# It tries to run the code inside the try: block.

# If an error happens (like float("hello")), Python jumps to the except block instead of crashing.

# It's useful when you expect something might go wrong — like converting input to a number.

# Task 1
# The user types in the time in seconds since the beginning of the day.
# Based on the user's choice, calculate how many hours, minutes, and seconds are left until midnight.
# seconds_since_today = float(
#     input("How many seconds have passed since the start of the day: ")
# )
# How many seconds in a day:
# 1 h = 60(min) * 60 sec= 3600
# 2 h = 120(min) * 60 = 7200 <=> 2 * 3600
# 24 h = 24 * 3600 = 86.400 seconds in a day
# # How many minutes in a day:
# 1 h = 60min => 2 * 60 = 120
# 24 h  = 24 * 60min = 1.440 minutes in a day

# day_seconds_total = 24 * 3600
# day_min_total = 24 * 60
# day_hours_total = 24
# choice = input(
#     "To find out how many hours are left in the day type 'hours', to find out how many minutes are left \ntype 'minutes', to find out the seconds left in the day\ntype 'seconds': "
# )
# if choice == "seconds":
#     seconds_remaining = day_seconds_total - seconds_since_today
#     print(f"The number of seconds remaining in the day is {seconds_remaining}")
# elif choice == "minutes":
#     minutes_remaining = day_min_total - (seconds_since_today / 60)
#     print(f"The number of minutes remaining in the day is {minutes_remaining}")
# elif choice == "hours":
#     hours_remaining = day_hours_total - (seconds_since_today / 3600)
#     print(f"The number of hours remaining in the day is {hours_remaining}")

# or
# seconds_since_today = float(
#     input("How many seconds have passed since the start of the day: ")
# )
# day_total_seconds = 1h *60 = 3600 * 24h = 86.400 seconds in a day
# day_total_seconds = 24 * 3600
# day_total_minutes = 1min=60sec => 1h = 60min => 60(adica o ora) * 24= 1440
# day_total_minutes = 24 * 60
# day_total_hours = 24

# seconds_remaining = day_total_seconds - seconds_since_today
# choice = input(
#     "To find out how many hours are left in the day type 'hours', to find out how many minutes are left \ntype 'minutes', to find out the seconds left in the day\ntype 'seconds': "
# )
# if choice == "seconds":
#     print(seconds_remaining)
# elif choice == "minutes":
#     minutes_remaining = seconds_remaining / 60
#     print(minutes_remaining)
# elif choice == "hours":
#     hours_remaining = seconds_remaining / 3600
#     print(hours_remaining)
# magine seconds like small bricks:

# A minute is a wall made of 60 bricks
# An hour is a tower made of 3600 bricks
# If someone gives you 7200 bricks (seconds), and says “how many towers (hours) can I build?”, you'd divide:
# 7200 / 3600 = 2 towers (hours)

# Task 2
# The user types in the diameter of a circle.
#  Based on the user's choice, calculate the area or perimeter of the circle.
# area of the circle = Area  = πr²=> r = radiu = diameter /2
# diameter = float(input("Provide the diameter mesurment:"))
# choice = input(
#     "To get the area of the circle type 'area', to get the perimeter of the circle type'perimeter':"
# )
# if choice == "area":
#     radius = diameter / 2
#     area = 3.14 * radius**2
#     print(area)
# # 3.14= pi
# elif choice == "perimeter":
#     perimeter = 3.14 * diameter
#     print(perimeter)
# else:
#     print("Error- non valid input provided")

# Task 3
# The user types in the cost of one gaming console, their quantity, and a discount. Based on the user's choice,
# calculate the total amount of the order or the cost of one console, including the discount.
cost = int(input("Price of the gaming console is: "))
quantity = int(input("How many condoles: "))
discount = float(input("Discount provided: "))
if discount > 0:
    total_amount_before_discount = cost * quantity
    discount_amount = total_amount_before_discount * (discount / 100)
    total_amount = total_amount_before_discount - discount_amount
    print(total_amount)
else:
    print("Error")
