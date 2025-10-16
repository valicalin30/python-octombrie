# lesson 17
# Task 1

# You have a set containing country names. Provide the following features:

# Add a country;

# Delete a country;

# Search for a country by entered characters;

# Check whether the country exists inside the set.

# Initialize a set of countries
countries = {"Brazil", "India", "France", "Serbia"}
print(countries)


def add_country(country):
    while True:
        if country in countries:
            print("This country already exists, try again")
            break
        else:
            countries.add(country)
            print("while adding:", countries)
            break


add_country("Germany")


# countries = {"Brazil", "India", "France", "Serbia", "Germany"}


def delete_country(country):
    try:
        # Ensure input is a string
        if not isinstance(country, str):
            raise ValueError("You must enter a valid string country.")

        country = country.strip().title()  # normalize input

        if country not in countries:
            raise ValueError("This country isn't in the set.")

        countries.remove(country)  # raises KeyError if not found
        print(f"{country} has been deleted successfully.")

    except ValueError as e:
        print("Error:", e)
    except KeyError:
        # only occurs if we use remove() and country not found
        print(f"Error: {country} could not be found.")

    finally:
        # Always show the final set
        print("Current countries:", countries)
        return countries


# remove vs discard = remove ne da error singur si discard nu , discard sare peste eroare daca e nevoie

# Example usage:


# print(delete_country("Brazil"))  # Deletes Brazil
# print(delete_country("Atlantis"))  # Triggers ValueError


# searching


# def search_country(country):
#     try:
#         if not isinstance(country, str):
#             raise ValueError("Non valid country")
#         country = country.strip().title()
#         if country not in countries:
#             raise ValueError("This country isn in the set")
#         else:
#             print(f"The country {country} is in the loop")
#             return True

#     except ValueError as e:
#         print("Error:", e)


# print(search_country("Brazil"))


# Exercitiu chatgpt
# Write a function called safe_divide() that:

# Asks the user to input two numbers: a numerator and a denominator.

# Tries to divide the numerator by the denominator.

# Catches the following exceptions:

# ValueError if the user doesn’t enter a number.

# ZeroDivisionError if the denominator is 0.

# Keeps asking the user for input until a valid division can be performed.

# Returns the result of the division.


# def safe_divide(numerator, denumator):
#     while True:
#         try:

#             if not isinstance(numerator, int):
#                 print("Please try again with a valid numerator")
#                 break
#             if not isinstance(denumator, int):
#                 print("Please provide a valid denumator")
#                 break
#             result = numerator / denumator
#             print("Final result:", result)
#             return result
#         except ValueError as e:
#             print("Error:", e)
#         except ZeroDivisionError:
#             print(f"The denumator is {denumator}")
#             break


# safe_divide(9, 0)


# def safe_divide2():
#     while True:
#         try:
#             numerator = float(input("Enter numerator: "))
#             denominator = float(input("Enter denominator: "))
#             result = numerator / denominator
#             print("Final result:", result)
#             return result
#         except ValueError:
#             print("Oops! You must enter a number. Try again.")
#         except ZeroDivisionError:
#             print("Oops! Cannot divide by zero. Try again.")


# # Example usage
# safe_divide2()

# Step by step in “normal words”

# while True: → “Keep doing the following steps forever, until we manually stop (with return or break).”

# try: block → “Try to do this stuff safely:”

# Ask the user for a numerator and denominator.

# Convert them to numbers (float()).

# Divide numerator by denominator.

# Print the result.

# return result → “If everything worked, return the answer and exit the function.”

# This also stops the loop, because the function ends.

# except ValueError: → “If the user didn’t type a number, print an error and go back to the top of the loop to try again.”

# except ZeroDivisionError: → “If the user typed 0 as the denominator, print an error and go back to the top of the loop to try again.”


# chat gpt ex 2
# Write a function called safe_sqrt() that:

# Asks the user to enter a number.

# Tries to calculate the square root of the number using math.sqrt().

# Catches the following exceptions:

# ValueError if the user enters a negative number (since square root of negative numbers is invalid in real numbers).

# ValueError if the user enters something that is not a number (like a string).

# Keeps asking the user for input until a valid non-negative number is entered.

# Returns the square root of the number.


import math


def safe_sqrt():
    while True:
        try:
            nr = float(input("Enter a number: "))

            # manually check for negative
            if nr < 0:
                raise ValueError("Cannot take the square root of a negative number")

            result = math.sqrt(nr)
            print(f"The square root of {nr} is {result}")
            return result

        except ValueError as e:
            print("Error:", e)


safe_sqrt()
print("hello")
