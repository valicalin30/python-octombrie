# STRINGS------


# Let s first understand while
# If condition is True, it runs the block.

# After finishing, it checks the condition again.

# If still True, it repeats.

# # If False, the loop stops.
# x = 0
# while x < 5:
#     print("x is:", x)
#     x += 1
# # When x becomes 5, the condition x < 5 is False, so the loop ends.

# # re asking for input until correct
# password = ""

# while password != "secret":
#     password = input("Enter password: ")

# print("Access granted!")
# If you type something wrong, the loop continues (condition is still True).
# When you finally type "secret", the condition password != "secret" becomes False, so the loop stops.

# Example 3: using break to exit manually
# while True:  # infinite loop
#     number = int(input("Enter a number between 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Good, in range!")
#         break  # stop the loop if condition met
#     else:
#         print("Try again!")
# Here we use while True: to loop forever.

# break is the "emergency exit" when the user gives correct input.

# EXERCITII CHAT GPT
# 1. Searching
# Ask the user for a sentence and a word.
# Print whether the word is in the sentence or not.
# 👉 Example: "The cat sleeps" + "cat" → "Found!".


# sentence1 = input("Provide a sentence: ")
# word1 = input("Provide a word that s in the sentence: ")
# while word1 not in sentence1.split():
#     print("The word is not in the sentence , try again:")
#     word1 = input("Provide a word that s in the sentence: ")
# print("The word is in the sentence")
# print(word1)
# print(sentence1)
# Let s harden this:
# daca avem litere mari sau mici:
# sentence1_lower = sentence1.lower()
# word1_lower = word1.lower()

# daca avem semne de punctuatie:
# If the sentence has . , ? etc., .split() will leave them attached to words.
# de exemplu punctul de la sfarsit lipit de cuvant
# import string
# sentence_clean = sentence1.translate(str.maketrans("", "", string.punctuation))
# string.punctuation -> contains all punctuation characters
# .translate --> REMOVES THE FROM THE STRING.

# Daca cerem mai multe cuvinte:
# words_to_search = word1.split()  # list of words


# So in summary:

# string.punctuation = all punctuation symbols

# str.maketrans("", "", string.punctuation) = “delete all punctuation” rule

# .translate(...) = apply that rule to the sentence


# str.maketrans(from_chars, to_chars, delete_chars)
# from_chars → characters you want to replace.

# to_chars → characters you want them replaced with.

# delete_chars → characters you want to completely remove.

# table = str.maketrans("abc", "123", "")
# print("abc cab".translate(table)) -> 123 321


# SOOO:
# import string

# sentence1 = input("Provide a sentence: ")
# # Cleaning it:
# sentence1_clean = sentence1.translate(str.maketrans("", "", string.punctuation))
# # This is the trickiest line — it removes punctuation.
# # string.punctuation = list of all punctuation characters.
# # str.maketrans('', '', string.punctuation) = builds a “translation table” that says:
# # For every punctuation character, remove it.
# # sentence1.translate(...) = applies that rule to sentence1.
# sentence1_words = sentence1_clean.lower().split
# # This does two operations:

# # .lower() → makes everything lowercase.
# # "The cat sleeps" → "the cat sleeps".
# # This makes comparisons case-insensitive.
# # .split() → splits the sentence into words (default: split on spaces).
# #  "the cat sleeps" → ["the", "cat", "sleeps"].
# # # That list is stored in sentence_words.

# while True:
#     word1 = input("Provide a word or more : ")
#     words_to_search = word1.lower().split()  # lowercase and split
#     if all(word in sentence1_words for word in words_to_search):
#         print("The words ar valid")
#         #         This is the check.

#         # word in sentence_words → checks if each word exists in the list sentence_words.
#         # Example: "cat" in ["the", "cat", "sleeps"] → True.
#         # (word in sentence_words for word in words_to_search) → creates checks for each word the user entered.
#         # # Example: ["cat", "sleeps"] → checks "cat" in ... and "sleeps" in ....
#         # all(...) → returns True only if all checks are True.
#         # Example:
#         # all([True, True]) → True
#         # all([True, False]) → False
#         # So this line means:
#         # # 👉 "If all the words the user entered are inside the sentence..."
#         break
#     else:
#         print("Some words were not found , try again: ")
# print("Original sentence", sentence1)
# print("Words found", words_to_search)


# 👉 Task:
# Write a program that:

# Asks the user to enter a sentence.

# Asks the user to enter a word.

# Counts how many times that word appears in the sentence (case-insensitive, ignoring punctuation).

# Prints the count.
# import string

# sentence2 = input("Sentence: ")
# sentence2_clean = sentence2.translate(str.maketrans("", "", string.punctuation))
# sentence2_lower = sentence2_clean.lower().split()


# TEMA 17
# Task 3
# Create an app Company. Store the following information about a person:
# full name, phone number, corporate email, job title, room number, skype.
# Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.
# personal_data = {}


# def add_person(first_name, last_name, phone, email, title, room_number, skype):
#     key = first_name, last_name
#     if key in personal_data:
#         print("This name was already added")
#     else:
#         personal_data[key] = {
#             "phone": phone,
#             "email": email,
#             "title": title,
#             "room": room_number,
#             "skype": skype,
#         }


# def find(name):
#     key_list = list(personal_data.keys())
#     result = []

#     for idx, (first, last) in enumerate(key_list):
#         if name.lower() in (first.lower(), last.lower()):
#             result.append((idx, (first, last), personal_data[(first, last)]))

#     if result:
#         print(f"Found {len(result)} match(es) for {name}:")
#         for idx2, (first2, last2), details in result:
#             print(f"[{idx2}] {first2} {last2}: {details}")
#     else:
#         print(f"No matches found for '{name}'.")


# add_person(
#     "John", "Smith", "1212", "john@smith.corp", "manager", "23", "johnskypesmith"
# )
# find("John")


# ✅ TL;DR of the loop flow

# Convert dictionary keys to a list (key_list).

# Loop over key_list with enumerate to get both index (idx) and tuple key (first, last).

# Check if the name matches first or last.

# If yes, append (idx, (first, last), personal_data[(first, last)]) to result.

# After the loop, check if result is empty or not.

# If not empty, loop over result again to print all matches.

# Tema 12
# Task 1
# The user types in a string. Check if this string is a palindrome.
# A palindrome is a word or text that reads the same backward as forward.
# For instance, racecar; "Do geese see God?"; tenet; "Was it a car or a cat I saw?"
# import string

# palindrome = input("Provide a palindrome: ")
# clean = palindrome.lower()
# clean = "".join(x for x in clean if x.isalnum())
# # islanum = ia numai numere si litere , ignora spatii si punctuatie
# # AIici aceeasi chestie dar loop normal si bagam fiecare caracter isalnum in stringul temp
# # temp = ""
# # for char in clean:
# #     if char.isalnum():
# #         temp = temp + char
# # cleaned = temp
# # print(temp)
# if clean == clean[::-1]:
#     print("It s a palindrome")

# else:
#     print("It s not a palindrome")
