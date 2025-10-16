# # Removing punctuation in Python – Step by Step Examples
# # Example sentence

# import string

# sentence1 = "Hello, world! It's 2025."
# print(sentence1)

# # Step 1: See all punctuation characters
# print(string.punctuation)  # ->  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# # This is Python’s built-in list of punctuation symbols.

# # Step 2: Build a translation table
# table = str.maketrans("", "", string.punctuation)
# print(f"Table: {table}")
# # output:
# # {33: None, 34: None, 35: None, ...}
# # Each punctuation character maps to None → tells .translate() to delete it.

# # Step 3: Apply .translate()
# clean_sentence = sentence1.translate(table)
# print(f"clean_sentence: {clean_sentence}")
# # output:
# # Hello world Its 2025

# # All punctuation removed, spaces remain.

# # Step 4: Explanation of arguments
# # str.maketrans(from_chars, to_chars, delete_chars)
# # from chars -> characters you want to replace
# # to chars -> characters you want them REPLACED WITH
# # delete_chars -> characters you want to comepletely remove

# # DECI IN EXEMPLUL NOSTRU : str.maketrans("", "", string.punction)
# # from char == ""-> ce vreau sa inlocuiesc (nimic)
# # t0 char == "" -> cu ce vreau sa inlocuiesc (nimic)
# # delete chars -> ce vreau sa sterg -> string.punction

# # str.maketrans() by itself just builds a translation table.

# # It doesn’t change any string. It’s like a map or a recipe.

# # .translate(table) actually applies that map to a string, character by character, replacing or deleting characters as the table says.

# # Step 5: Simple examples showing replacements vs deletion
# table = str.maketrans("abc", "123", "")
# print("abc cab".translate(table))
# # Output -> 123 321
# #
# # Deletion:
# table = str.maketrans("", "", "!?")
# print("Hello!? World!".translate(table))
# # Output: -> Hello World

# # Step 6: Full one-liner
# print(sentence1.translate(str.maketrans("", "", string.punctuation)))
# # Output -> Hello world Its 2025

# # Tema 12
# # Task 1
# # The user types in a string. Check if this string is a palindrome.
# # A palindrome is a word or text that reads the same backward as forward.
# # For instance, racecar; "Do geese see God?"; tenet; "Was it a car or a cat I saw?"
# import string

# palindrome = input("pROVIDE A PALINDROME: ")
# palindrome_clean = palindrome.lower().translate(
#     str.maketrans("", "", string.punctuation)
# )
# palindrome_clean = palindrome_clean.replace(" ", "")  # => remove spaces

# if palindrome_clean == palindrome_clean[::-1]:
#     print("It s a palindrome")
# else:
#     print("It s not a palindrome")


# # OOOOR:
# palindrome_clean_2 = palindrome.lower()
# palindrome_clean_2 = "".join(x for x in palindrome_clean_2 if x.isalnum())
# print(f"Version 2: {palindrome_clean_2}")
# if palindrome_clean_2 == palindrome_clean_2[::-1]:
#     print("PALINDROME")
# else:
#     print("Not a palindome")


# # ✅ Key Takeaways

# # Both methods work for words and sentences.

# # isalnum() is simpler if you don’t care about keeping spaces or punctuation.

# # translate() + replace() is faster for long strings and more efficient if you need precise control over which characters to remove.

# # split() breaks a string into words based on spaces.
# # ========================================================
# # EXERCITII CHAT GPT
# # 1. Searching
# # Ask the user for a sentence and a word.
# # Print whether the word is in the sentence or not.
# # 👉 Example: "The cat sleeps" + "cat" → "Found!".
# import string

# sentence_1 = input("Provide a sentence: ")
# word1 = input("Provide a word: ")
# sentence_1 = sentence_1.lower().translate(str.maketrans("", "", string.punctuation))

# sentence_1 = sentence_1.split()
# # sentence_1.replace(" ", "") removes all spaces, so "The cat sleeps" becomes "thecatsleeps".

# # .split() by default splits on spaces, but there are no spaces left, so you end up with a list containing one big string: ["thecatsleeps"].
# # ✅ That means checking if word1 in sentence_1: will only match if word1 is literally "thecatsleeps", which isn’t what you want.
# word1 = word1.lower().translate(str.maketrans("", "", string.punctuation))

# if word1 in sentence_1:
#     print("Word found")
# else:
#     print("That word isn t in the sentence")


# # LESSON 12
# # Task 2
# # The user types in a string.
# # Count the number of letters and digits in the string. Print both results.
# def digits_letters():
#     the_string = input("Provide a string: ")
#     lettercounter = 0
#     digitcounter = 0

#     for char in the_string:
#         if char.isdigit():
#             digitcounter += 1
#         elif char.isalpha():
#             lettercounter += 1

#     print(f"Letters: {lettercounter}")
#     print(f"Digits: {digitcounter}")


# # digits_letters()


# # Task 5
# # The user types in a string, a search word, and a replacement word.
# # Replace one word with another one in the string. Print the resulting string.
import string


# string_5 = input("Provide a new string: ")
# search_word = input("Provide a search word: ")
# replacement = input("Provide a replacement word: ")

# # Clean search and replacement for comparison
# clean_search = search_word.lower().translate(str.maketrans("", "", string.punctuation))
# clean_replacement = replacement.lower().translate(
#     str.maketrans("", "", string.punctuation)
# )

# words = string_5.split()
# new_words = []

# for word in words:
#     # Clean each word in the string
#     clean_word = word.lower().translate(str.maketrans("", "", string.punctuation))

#     if clean_word == clean_search:
#         # Replace the whole word with the cleaned replacement
#         word = clean_replacement
#     new_words.append(word)

# new_string = " ".join(new_words)
# print("This is the new string:", new_string)


# tema 12
# Task 2
# The user types in text followed by a list of reserved words.
# Find all reserved words in the text and change lowercase to uppercase there. Print the modified text.
# import re


# def highlight_reserved_words(text, reserved_words):
#     # Step 1: Normalize spaces
#     text = re.sub(r"\s+", " ", text.strip())

#     # Step 2: Create regex pattern for reserved words (ignore case)
#     pattern = r"\b(" + "|".join(map(re.escape, reserved_words)) + r")\b"

#     # Step 3: Replace matches with uppercase form
#     def replacer(match):
#         return match.group(0).upper()

#     modified_text = re.sub(pattern, replacer, text, flags=re.IGNORECASE)

#     return modified_text


# # Example usage
# text = "  this is a sample text,   with  Select   and join as reserved words. "
# reserved = ["select", "join", "from"]

# result = highlight_reserved_words(text, reserved)
# print(result)

# orrrr:

# text = input("Provide a text: ")
# reserved_input = input("Provide the words in the text: ")
# reserved_words = reserved_input.split()
# # Split the text into words
# words = text.split()

# # Go through each word and convert reserved words to uppercase
# # modified_words = [word.upper() if word in reserved_words else word for word in words]
# # or we do a normal loop instead of a list comprehension
# modified_words = []
# for word in words:
#     if word == reserved_words:
#         modified_words.append(word.upper())
#     else:
#         modified_words.append(word)


# # Join the words back into a string
# modified_text = " ".join(modified_words)

# print("Modified text:")
# print(modified_text)


# EXERCITII CHATGPT
# =========================================================================================================================================
# 1 Check if a word exists in text
text1 = "Python is powerful and Python is easy."
# Find out if the word "easy" exists in text
word1 = text1.find("easy")
if not word1 == -1:
    print("The word is in the text")
else:
    print("Not found")
# oh so we re saying if that word doesen t == -1 it mean it is in the string
# 2 Count occurrences of a word
sentence2 = "cat bat mat cat rat cat"
# Count how many times "cat" appears
word2 = sentence2.count("cat")
print(word2)

# 3 Find position of first and last occurrence
story = "once upon a time, there was a time traveler."
# Find first and last index of "time"
first_index = story.find("time")  # first occurrence
last_index = story.rfind("time")  # last occurrence

print("First occurrence:", first_index)
print("Last occurrence:", last_index)

# 4 Remove extra spaces
messy = "   Python   is   fun   "
# Clean it to: "Python is fun"
new_messy4 = messy.strip().split()
new_messy4 = " ".join(new_messy4)
print(new_messy4)
# strip() removes spaces at the beginning and end before splitting.
# By default, .split() splits on any whitespace (spaces, tabs, newlines), and removes extra spaces automatically.

# 5 Remove punctuation
import string

text5 = "Hello!!! How, are... you???"
# Result: "Hello How are you"
string5 = text5.translate(str.maketrans("", "", string.punctuation))
print(string5)

# 6 Normalize capitalization
sentence6 = "pYTHON is AweSOME"
# Result: "Python is awesome"
sentence6 = sentence6.lower()
new_sentence6 = sentence6.capitalize()
print(new_sentence6)

# 7 Simple replace
text7 = "I like Java. Java is cool."
# Replace "Java" with "Python"
result7 = text7.replace("Java", "Python")
print(result7)

# 8 Replace only the first occurrence
text8 = "red green blue red"
# Replace only the first "red" with "yellow"
result8 = text8.replace("red", "yellow", 1)
print(result8)

# 9 Remove digits from a string
data = "a1b2c3d4"

result9 = "".join([ch for ch in data if not ch.isdigit()])

print(result9)

# 10 Check for palindrome
word10 = "Madam"
# Check if it reads the same forwards and backwards
word10 = word10.lower()
if word10 == word10[::-1]:
    print("Palindrome")
else:
    print("not a palindrome")
#  TO ENHANCE
# text10 = input("Provide a palindromw string: ")
# text10 = text10.lower().translate(str.maketrans("", "", string.punctuation))
# if text10 == text10[::-1]:
#     print("THIS IS A PALINDROME")
# else:
#     print("THSI IS NOT A PALINDROME")

# 11 Find all unique words (ignore case & punctuation)
import string

text11 = "Hello, hello! World world..."
# 1. Convert to lowercase
text11 = text11.lower()

# 2. Remove punctuation
text11 = text11.translate(str.maketrans("", "", string.punctuation))

# 3. Split into words
words = text11.split()

# 4. Get unique words
result11 = set(words)

print(result11)

# 12 Mask part of a string
card = "1234 5678 9012 3456"
# Mask it to: "**** **** **** 3456"


# Keep the last 4 digits, mask the rest
masked_card = "**** **** **** " + card[-4:]

print(masked_card)

# Explanation:

# card[-4:] → takes the last 4 characters of the string.

# "**** **** **** " → manually adds the masked blocks for the first 12 digits.

# Combine them with + to get the final masked string.


# EXERCITIU FINAL:
# Your tasks (in order):
# Trim spaces → remove leading/trailing spaces.
# Remove digits (123, 42, …).
# Replace multiple spaces with a single space.
# Remove all occurrences of word_to_remove (case-insensitive).
# Capitalize the first letter of each sentence, make the rest lowercase.
import string

textfinal = "   HELLO123   world!! this is  a  tESt.  42python is fun.  "
word_to_remove = "test"
textfinal = textfinal.strip()
textfinal = textfinal.lower().translate(str.maketrans("", "", string.digits))
textfinal = " ".join(textfinal.split())

# REMOVINGWORD:
words = textfinal.split()
new_final = []

for word in words:
    # strip punctuation only for comparison
    clean_word = word.lower().strip(string.punctuation)

    if clean_word == word_to_remove.lower():
        # keep any trailing punctuation (like ".", "!", "?")
        trailing = (
            word[len(clean_word) :] if word.endswith((".", "!", "?", ",")) else ""
        )
        if trailing:
            new_final.append(trailing)
    else:
        new_final.append(word)

textfinal = " ".join(new_final)

# textfinal = textfinal.split()
# new_final = []
# for word in textfinal:
#     if word.lower().strip(string.punctuation) != word_to_remove.lower():
#         new_final.append(word)

new_final = " ".join(new_final)
# capitalize:


print(new_final)

# BETTER VERSION:
textfinal = "   HELLO123   world!! this is  a  tESt.  42python is fun.  "
word_to_remove = "test"

# 1. Trim spaces
textfinal = textfinal.strip()

# 2. Remove digits
textfinal = textfinal.translate(str.maketrans("", "", string.digits))

# 3. Replace multiple spaces with a single space
textfinal = " ".join(textfinal.split())

# 4. Remove word_to_remove (case-insensitive, ignoring punctuation)
words = textfinal.split()
words = [
    w for w in words if w.strip(string.punctuation).lower() != word_to_remove.lower()
]
textfinal = " ".join(words)

# 5. Capitalize sentences
sentences = [
    s.strip().capitalize() for s in textfinal.split(string.punctuation) if s.strip()
]
textfinal = ". ".join(sentences) + "."

print(textfinal)

import re
import string

# # 1. Get text from user
# txt = input("Type something: ")

# # 2. Split text on punctuation
# parts = re.split(f"[{re.escape(string.punctuation)}]+", txt)

# # 3. Clean and capitalize each piece
# parts = [part.strip().capitalize() for part in parts if part.strip()]

# # 4. Join it back into one string
# new_text = ". ".join(parts) + "."

# # 5. Show result
# print(new_text)


# Step-by-step:

# txt = input(...)

# txt is just a variable to store whatever the user types.

# We could call it anything (text, user_input), but txt is short and clear.

# re.split(...)

# Splits the string wherever punctuation appears.

# Produces a list of pieces.

# [part.strip().capitalize() for part in parts if part.strip()]

# Clean spaces around each piece.

# Make the first letter uppercase.

# Skip empty strings.

# ". ".join(parts) + "."

# Join the cleaned pieces with a period + space.

# Add a final period at the end.

# print(new_text)

# Show the cleaned-up, sentence-like version.


# MIC TEST
import string

test = input("Un test de impartire: ")
test = "".join(test.split())  # remove spaces
new_text = "".join(ch for ch in test if not ch.isdigit())
print(new_text)

# or:
import re

test = input("Un test de impartire: ")
test = "".join(test.split())
new_text = re.sub(r"\d", "", test)
print(new_text)
