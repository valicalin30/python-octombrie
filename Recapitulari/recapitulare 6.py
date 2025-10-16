# # -----------------------------------------------------------------------------------------------------------------------------------------------------

# # # lesson 11
# # # Task 3
# # # Write a program that tests users for their multiplication table skills.
# # # The program prints two numbers, and the user must enter their product.
# # # Develop several levels of difficulty (they should differ in complexity and number of questions).
# # #  Print the points that represent the user's skills.
import random

score = 0
levels = {
    1: {"range": (1, 5), "questions": 5},
    2: {"range": (5, 10), "questions": 7},
    3: {"range": (10, 15), "questions": 8},
}

for level, data in levels.items():
    print(f"This is level {level}, and we have {data}")
    for _ in range(data["questions"]):
        a = random.randint(*data["range"])
        b = random.randint(*data["range"])
        total = a * b
        print(a, "*", b)
        # print(total)
        answer = int(input("Your answer: "))
        if answer == total:
            print("Goodjob!")
            score += 1
        else:
            print("WRONG!")
            score -= 1
print(score)
# Looping over levels without .items() gives only the keys: 1, 2, 3
# Python tries to unpack each key (like 1) into level,
# data → impossible, because 1 is not a pair, it’s a single number.


# score = 0
# levels = {
#     1: {"range": (1, 5), "questions": 5},
#     2: {"range": (5, 10), "question": 7},
#     3: {"range": (10, 20), "question": 10},
# }
# # # deci-> range/questions valorile cheii 1/ 2/ 3 = level. Putem spune ca range si question sunt data pentru levels(valori si cheie)
# # #  si levels
# # # este valoarea cheii levels
# # # range si questions mai bine sspus sunt string KEYS a carora le am acordat valori(min, max)-> VALOARE TUPLE/
# # # 5 nr de intrebari-> valoare de un singur nr
# for level, data in levels.items():
#     print(
#         f"This is level {level}, and we re gonr have questions from{data['range'][0]} to {data['range'][1]},"
#     )
#     for _ in range(data["question"]):

#         a = random.randint(*data["range"])
#         # b = data["range"[1]] -> this only gets the characters of the string so 1 = a(rAnge)
#         # b = data["range"][1]
#         b = random.radiant(*data["range"])
#         # this is unpacking -> basically range is a string as we said, but also a key -> we need to turn it s Tuple value
#         # into min and max parameter, rignt now they re just 2 numbers, so with this radiant(*data['range]) we re doing just that
#         total = a + b
#         print(a, "+", b)
#         print(total)

#         try:
#             answer = int(input("Your answer: "))
#             if answer == total:
#                 score = score + 1
#                 print("correct")
#             else:
#                 print(f"WRONG! The correct answer was {total}, so -1 score")
#                 score = score - 1
#         except ValueError:
#             print("⚠️ Please enter a number!")
#             score -= 1
# print("\n=== Quiz Finished ===")
# print(f"Your final score: {score}")

# # # thislst = [("Comedy", "Rabbit", "Fish")]
# # # for level, data, flower in thislst:
# # #     print(level, data, flower)
# # # a list of 3 tuples
# # # thislst = ["Com"]
# # # for level, data, flower in thislst:
# # #     print(level, data, flower)
# # # thislst is a list with one element, and that element is the string 'com'.
# # # ✅ So thislst itself is a list, not a tuple.
# # # Python tries to unpack each element of the list into a, b, c.
# # # The element 'com' is a string, which is iterable, like a list of characters: ['c', 'o', 'm'].
# # Python can unpack this string into 3 variables: a='c', b='o', c='m'


# # --------------------------------------------------
# # TEMA 13
# # Task 1
# # The user types in an arithmetic expression. For example, 23+12.
# # Print its result. In our example, the output is 35.
# # The arithmetic expression can have only three parts: number, operation, number. Possible operations: +, -, *, /.

# operation = input("Provide an arithmetic expression: ")
# if "+" in operation:
#     a, b = operation.split("+")
#     result = int(a) + int(b)
#     print(result)
# if "-" in operation:
#     a, b = operation.split("-")
#     result = int(a) - int(b)
#     print(result)
# if "*" in operation:
#     a, b = operation.split("*")
#     result = int(a) * int(b)
#     print(result)
# if "/" in operation:
#     a, b = operation.split("/")
#     result = int(a) / int(b)
#     print(result)


# Lesson10
# Task 3
# The user types in the size of the square's sides. Print an empty square (only its sides are displayed).
# The side is equal to the typed in size.
# size = int(input("Size: "))
# print("*" * size)
# for _ in range(size - 2):
#     print("*" + " " * (size) + "*")
# print("*" * size)

# Lesson 7
# 4
# The user types in two numbers.
#  Print all numbers in the specified range in descending order.
# import random

# nr1 = int(random.randint(1, 100))
# nr2 = int(random.randint(1, 100))
# rng = range(nr1, nr2)
# print(rng)
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# lst = []
# for num in range(start, end + 1):
#     lst.append(num)
# print(lst[::-1])

# LESSON 5
# Task 1
# # Print the multiplication table for the user-defined number. If the user typed in 7, the output should be as follows:
# # 7 * 1 = 7
# # 7 * 2 = 14
# # 7 * 3 = 21
# # …
# import random

# number = random.randint(1, 10)
# print(number)
# for num in range(1, 11):
#     for _ in range(1, 11):
#         total = number * num
#     print(f"{number} * {num} = {total}")
# # or
# number = int(input("Provide a nr: "))
# for num in range(1, 11):
#     total = number * num
#     print(f"{number} * {num} = {total}")

# Lesson 5
# Task 3
# # The user types in the start and end points of the range and a number.
# # If the number is not in the range, the program asks the user to re-enter the number,
# # and so on until the user enters the number correctly. The program displays all numbers in the range,
# # highlighting the number with exclamation marks. For instance: 1 2 3 !4! 5 6 7.
# nr1 = int(input("Write the first number: "))
# nr2 = int(input("Provide the last number: "))
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# specialnr = int(input("Number in the range: "))
# while specialnr not in range(start, end + 1):
#     print(f"Please provide a number within this range: {range(start, end + 1)}")
#     continue
# for num in range(start, end + 1):
#     if num == specialnr:
#         print("!", num, "!", end=" ")
#     else:
#         print(num, end=" ")

# tema 10
# Task 2
# Print the multiplication table for all numbers from 1 to 10. For example:
# 1*1 = 1 1*2 = 2 ….. 1*10 = 10
# ..................................
# 10*1 = 10 10*2 = 20 …. 10*10 = 100
# for num in range(1, 11):
#     for nr in range(1, 11):
#         total = num * nr
#         print(f"{num} * {nr} = {total}")


# TEMA 12
# Task 1
# The user types in a string. Check if this string is a palindrome.
# A palindrome is a word or text that reads the same backward as forward.
# For instance, racecar; "Do geese see God?"; tenet; "Was it a car or a cat I saw?"
# text1 = input("Enter a text: ")
# if text1 == text1[::-1]:
#     print("It s a palindrone")
# else:
#     print("No")
# import string

# text1 = input("Provide a string: ")
# clean = text1.lower()
# clean = "".join(x for x in clean if clean.isalnum())
# if clean == clean[::-1]:
#     print("It s a palindrome")
# else:
#     print("It s not a palindrome")

# MAI CLEAN:
# import string

# # lowercase:

# clean = text1.lower()

# # Step B: remove punctuation and spaces
# clean = "".join(char for char in clean if char.isalnum())

# # Step C: check palindrome
# if clean == clean[::-1]:
#     print("Yes, it's a palindrome")
# else:
#     print("No, it's not a palindrome")


# Task 2
# The user types in text followed by a list of reserved words.
# Find all reserved words in the text and change lowercase to uppercase there. Print the modified text.
text2 = input("Enter a text: ")
reserved_input = input("Reserved words (separate by space): ").split()
# split()-> imparte fiecare cuvant atunci cand intalneste Space in acel string. daca vrem specificam cand sa imparta caracterele
# punand split("," sau ce caracter vrem noi)

# Replace reserved words with uppercase versions
for word in reserved_input:
    text2 = text2.replace(word, word.upper())

print("Modified text:", text2)
