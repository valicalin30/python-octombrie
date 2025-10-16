# Lesson 13
# Task 1
# There is some text. Implement the following features:
# Change the text so that each sentence starts with a capital letter;
# Count how many times numbers appear in the text;
# Count how many times punctuation marks appear in the text;
# Count the number of exclamation marks in the text.
import re
import string

text = "helLo 2! th1is. 11is a test? hi."
word_to_remove = "test"

# 1. Remove digits
digitscount = sum(c.isdigit() for c in text)
markcounter = sum(1 for m in text if m in string.punctuation)
exclamationcounter = sum(1 for e in text if e is "!")
# for char in text if char in string.punctuation
# Loops over each character in text
# Only keeps characters that are punctuation
# 1 for char in ...
# For each punctuation character, we yield 1
# Think of it like saying: “For each punctuation, add 1 to the total.”
# sum(...)
# Adds up all the 1s
# Result = total number of punctuation characters
# text = re.sub(r"\d", "", text)
print(digitscount)
print(markcounter)
print(exclamationcounter)
# 2. Remove the target word (case-insensitive, ignoring punctuation)
# version1:
# text = re.sub(rf"\b{re.escape(word_to_remove)}\b", "", text, flags=re.IGNORECASE)
# or: version2
# Remove target word, ignoring punctuation and case
# words = text.split()
# filtered_words = [
#     w
#     for w in words
#     if w.lower().translate(str.maketrans("", "", string.punctuation))
#     != word_to_remove.lower()
# ]
# or: version 3
words = text.split()
filtered_words = [
    w for w in words if w.lower().strip(string.punctuation) != word_to_remove.lower()
]

text = " ".join(filtered_words)
print(text)
# orrr: version 4(keeping the punctuation)
words = text.split()
filtered_words = []

for w in words:
    # Separate the "core" word from trailing punctuation
    core = w.lower().rstrip(string.punctuation)
    trailing = w[len(core) :]  # whatever is left (punctuation)
    # .lstrip(chars)

    # Removes characters only from the start (left) of the string.
    # .rstrip(chars)

    # Removes characters only from the end (right) of the string.

    if core != word_to_remove.lower():
        filtered_words.append(w)  # keep the whole original word including punctuation

text = " ".join(filtered_words)
print(text)
# # 3. Fix extra spaces
# text = " ".join(text.split())

# # 4. Capitalize sentences while keeping punctuation
# # Split by punctuation, but keep it
# parts = re.split(f"([.!?])", text)
# new_text = ""
# for i in range(0, len(parts) - 1, 2):
#     sentence = parts[i].strip().capitalize() + parts[i + 1]  # add punctuation back
#     new_text += sentence + " "

# new_text = new_text.strip()

# print(new_text)


# Split text on punctuation marks
# re.split(pattern, string, maxsplit=0)
# pattern → the regex rule you want to split by.

# if s.strip()
# This filters out empty sentences (like ''), after trimming spaces.
# That means it ignores the last blank piece created after the final ".".
# s.strip()
# This removes leading and trailing spaces inside each sentence.
# For example:

# ===============================================================================
# Original text
#    │
#    │  "helLo 2! th1is. 11is a test? hi."
#    ▼
# Split into words
#    │
#    │  text.split() → ['helLo', '2!', 'th1is.', '11is', 'a', 'test?', 'hi.']
#    ▼
# Filter / process words
#    │
#    │  [w for w in words if w.lower().strip(string.punctuation) != "test"]
#    │
#    │  → Check each word:
#    │      "helLo"  → keep
#    │      "2!"     → keep
#    │      "th1is." → keep
#    │      "11is"   → keep
#    │      "a"      → keep
#    │      "test?"  → remove
#    │      "hi."    → keep
#    ▼
# Filtered list
#    │
#    │  ['helLo', '2!', 'th1is.', '11is', 'a', '?', 'hi.']
#    ▼
# Join back into string
#    │
#    │  " ".join(filtered_words)
#    ▼
# Final text
#    │
#    │  "helLo 2! th1is. 11is a ? hi."
