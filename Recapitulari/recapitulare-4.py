# # # lesson5
# # # Task 2
# # # The user types in the diameter of a circle.
# # #  Based on the user's choice, calculate the area or perimeter of the circle.
# # # area = 3.14 * radius**2
# # # rarius = diameter  /2
# # # perimeter = 3.14 * diameter
# # # let s try using the while function so what it keeps asking me to enter a new diameter until i type 'guit':
# # # while True:
# # #     diameter_input = input("Provide a diameter, or type 'quit' to exit:  ")
# # #     if diameter_input.lower() == "quit":
# # #         print("goodbye")
# # #         break
# # #     diameter = float(diameter_input)
# # #     # diameter input = is the text that then we convert to float

# # #     choice = input("'area', 'parimeter', 'quit':")
# # #     if choice == "area":
# # #         radius = diameter / 2
# # #         area = 3.14 * radius**2
# # #         print(f"The area is:{area}")
# # #     elif choice == "perimeter":
# # #         perimeter = 3.14 * diameter
# # #         print(f"The perimeter is: {perimeter}")
# # #     elif choice == "quit":
# # #         print("goodbye")
# # #         break

# # #     print("Care for a new diameter?")
# # # -----------------------------------------------------------------

# # # My exercise:
# # # Vreau sa cumpar 5 chitari a cate 1 costa 100 de lei. Eu am 400 de lei.
# # # Trebuie sa ii spun calculatorului asta si sa imi spuna cate chitari as putea sa cumpar.
# # # Daca introduc numar de chitari care va fi peste buget atunci trebuie sa imi spuna asta
# # # si sa ma roage sa introduc alt numar de chitari:

# # # while True:
# # #     chitara = 100
# # #     buget = 400
# # #     nr_chitari_dorite = input("Scrie cate chitari doresti sau scrie 'quit': ")

# # #     if nr_chitari_dorite == "quit":
# # #         print("Cu bine!")
# # #         break

# # #     nr_chitari = int(nr_chitari_dorite)
# # #     cost_total = chitara * nr_chitari  # 3 * 100 = 300
# # #     print(f"Cost total: {cost_total} lei")  # DEBUG LINE (poți șterge apoi)

# # #     if cost_total > buget:
# # #         print(f"Nu ai destui bani pentru {nr_chitari} chitari, introdu alta cantitate.")
# # #         continue
# # #     else:
# # #         rest = buget - cost_total  # 400 - 300 = 100
# # #         print(f"Ai destui bani pentru {nr_chitari} chitari și îți rămân {rest} lei.")
# # #         break


# # # sau:
while True:
    chitara = 100
    buget = 400
    nr_chitari_dorite = input("Scrie cate chitari doresti sau scrie 'quit': ")

    if nr_chitari_dorite.lower() == "quit":
        print("Cu bine!")
        break

    if not nr_chitari_dorite.isdigit():
        print("Te rog introdu un număr valid.")
        continue
    # pentru a verifica ca ceea ce tastam este un nr
    nr_chitari = int(nr_chitari_dorite)
    cost_total = chitara * nr_chitari

    if cost_total > buget:
        print(
            f"Nu ai destui bani pentru {nr_chitari} chitari. Încearcă altă cantitate."
        )
    else:
        rest = buget - cost_total
        print(f"Poți cumpăra {nr_chitari} chitari și îți rămân {rest} lei.")


# # # -------------------------------------------------
# # # Ex chatgpt:
# # Vrei să strângi bani pentru o excursie care costă 1000 de lei.
# # În fiecare zi pui deoparte o sumă diferită.
# # Programul trebuie să te întrebe în fiecare zi câți bani vrei să pui deoparte.
# while True:
#     excursie = input("Cat costa excursia ta?( sau scrie 'quit'): ")
#     if excursie.lower() == "quit":
#         print("Cu bine!")
#         break
#     if not excursie.isdigit():
#         print("Te rog introdu un nr valid:")
#         continue
#     excursie = int(excursie)

#     zile = input("In cate zile vrei sa strangi banii?")
#     if not zile.isdigit():
#         print("Introdu un nr valid!")
#         continue
#     zile = int(zile)

#     buget = 0
#     for zi in range(1, zile + 1):
#         suma_zi = input(f"Ziua {zi} - Cat vrei sa depui? ")
#         if not suma_zi.isdigit():
#             print("Valoare invalida, zi ignorata. ")
#             continue
#         buget = buget + int(suma_zi)

#     if buget >= excursie:
#         print(f"Felicitari! Ai strans {buget} lei pentru excursie")
#         break
#     else:
#         print(f"Din pacate ai strans doar {buget} lei. Mai incearca!\n")
# deci:
# excursie = input string care daca nu este scris in cifre se ia de la capat prin continue dar daca e in cifre se continua prin a fi transformat in int
# zile la fel ca si excursie

# apoi avem un for loop ce va lua fiecare element 'zi' din range pe rand si va face urmatoarele:
# zi = elementul din range ul dintre 1 si variabila zile care a fost transformata in int
# suma_zi = input string ce se refera la suma depusa pe fiecare zi , adica elementul zi din range
# dupa ce ne asiguram ca suma_zi este in cifre cum am facut si cu 'excursie' si' si 'zile' convertim 'suma-zile' in , daca nu e in cifre inseamna ca sarim peste zi
# dupa ce convertim vom aduna fiecare suma_zi cu variabila buget care este 0 la inceput . Asta se intampla in bucla for pentru a se aduna la
# fiecare suma_zi care se intampla in fiecare elementzi

# NOtice THIS:
# Comparativ: ce face diferența?
# Situație	      ai while pentru validare?	 Ce se întâmplă la input greșit?
# excursie, zile etc.	    ✅ Da	               Reîncepe întrebarea
# suma_zi (în buclă for)	❌ Nu	               Sare peste zi

# Soluție dacă vrei ca o zi greșită să se repete (să nu o pierzi):
# Trebuie să pui input-ul într-un while în interiorul buclei for, așa:
# for zi in range(1, zile + 1):
#     while True:
#         suma_zi = input(f"Ziua {zi} - Cât vrei să depui azi? ")
#         if not suma_zi.isdigit():
#             print("Valoare invalidă. Încearcă din nou.")
#             continue  # rămânem la aceeași zi
#         buget += int(suma_zi)
#         break  # ieșim din while, trecem la următoarea zi


# apoi iesim din loop ulu for si stabilim niste conditii:
# daca la final bugetul este mai mare sau = cu variabila excursie atunci am indeplinit strangerea de bani si dam break
# daca nu (else) nu dam break si o luam de la capat

# -----------------------
# while True:
#     x = int(input("Introdu un nr: "))
#     if x > 100:
#         # while x > 100:
#         print("Incearca din nou")
#         # x = int(input("Introdu un nr: "))
#         # sau continue
#         continue
#     else:
#         print("Bine!")
#     break

# # --------------------------------------------SA EXPLICAM MAI BINE WHILE:
# . Ce face o buclă while?
# Repetă blocul de cod din interiorul său atât timp cât condiția este adevărată.

# Dacă condiția devine falsă, bucla se oprește.

# Dacă condiția nu se schimbă niciodată în fals, atunci bucla devine infinita.

# 2. Unde trebuie să fie codul care se repetă?
# Doar codul indentat în interiorul buclei se execută de mai multe ori.

# Codul aflat în afara buclei se execută o singură dată, la început (sau după ce bucla s-a terminat).

# 3. Exemple pentru a înțelege mai bine:
# 3.1. Input în afara buclei (problematic)
# python
# Copy code
# x = int(input("Introdu un număr: "))  # inputul se cere o singură dată

# while x > 100:
#     print("Încearcă din nou")
#     # NU mai cerem input în interiorul buclei -> valoarea lui x NU se schimbă
# print("Bine!")
# Ce se întâmplă?

# Dacă x > 100 de la început, bucla se va executa la infinit (loop infinit).
# Pt a evita asta cerem input din nou in bucla sau (mai jos) tot codul este in block

# Pentru că x nu se schimbă și condiția rămâne adevărată.

# Dacă x <= 100 de la început, bucla nici măcar nu se execută.

# 3.2. Input în interior buclei (corect)
# python
# Copy code
# while True:
#     x = int(input("Introdu un număr: "))  # inputul se cere de fiecare dată când începe o iterație
#     if x > 100:
#         print("Încearcă din nou")
#         continue  # sari la începutul buclei să ceri input din nou
#     else:
#         print("Bine!")
#         break  # ieși din buclă
# Ce se întâmplă?

# Inputul se cere mereu.

# Dacă x e prea mare, te roagă să încerci iar (prin continue).
# so to put the final nail in the coffin: we use 'continue' in a
# while loop so that  if the condition is true , it will start the loop again , but if the condition is fals , we can move on

# Dacă e OK, bucla se oprește cu break.

# 4. Cum evit un loop infinit?
# Trebuie să actualizezi valoarea pe baza căreia verifici condiția (ex: ceri input nou).

# Sau să folosești o instrucțiune care să scoată programul din buclă (break).

# Dacă uiți să schimbi condiția, bucla rulează la infinit.

# 5. Ce face continue?
# Sari imediat la începutul buclei, fără să execuți codul rămas după continue.

# Ideal când vrei să reiei testul/cererea input-ului fără să execuți restul codului.

# 6. Ce face break?
# Întrerupe bucla imediat, programul continuă după blocul de while.

# Ideal când ai atins un scop (ex: input valid, sau s-a terminat treaba).

# 7. De ce uneori pui toată logica în while True?
# Pentru flexibilitate: poți controla când să ieși cu break.

# Poți repeta inputul și validarea fără să te complici cu condiții lungi.

# Ex:

# python
# Copy code
# while True:
#     x = input("Scrie un număr: ")
#     if not x.isdigit():
#         print("Nu e un număr. Mai încearcă.")
#         continue
#     x = int(x)
#     if x > 100:
#         print("Numărul e prea mare.")
#         continue
#     print("Numărul e bun!")
#     break


# ----------------------------------------------HAI SA MAI EXERSAM TEMA 9
# Task 2
# Count the number of integers in the range from 100 to 999 that have two identical digits.
# number_list = []
# for num in range(100, 999 + 1):
#     digit = str(num)

#     if digit[0] == digit[1] or digit[1] == digit[2] or digit[0] == digit[2]:
#         number_list.append(num)

# print(len(number_list))


# Task 4
# The user types in an integer value. Remove all 3s and 6s from this integer and print it.
# while True:
#     integer = input(
#         "Provide a integer with a 3s and 6s so we can remove the or 'quit': "
#     )
#     if integer == "quit":
#         print("bye")
#         break
#     if "3" in integer or "6" in integer:
#         print("The number has 3 and 6 s so it s valid!")
#         filtered = integer.replace("3", "").replace("6", "")
#         print(f"The resullt is {filtered}")

#     else:
#         print("There is nothing to do , there are no 3s or 6s")


# z.replace('what to replace', 'with which to replace').replace(another)

# Take any range and display it in a descending order
# for num in range(1, 11):
#     print(num, end="")

# for num in reversed(range(1, 11)):
#     print(num, end=" ")


# or:
# nr1 = int(input("First number: "))
# nr2 = int(input("Second number: "))
# start = min(nr1, nr2)
# end = max(nr1, nr2)
# numbers = list(range(start, end + 1))
# print(numbers[::-1])

# nr = list(range(1, 11))
# print(nr[::-1])


# 3
# The user types in two numbers.
# Print all even numbers in the specified range.
# for num in range(1, 13):
#     if num % 2 == 0:
#         print(num, end=" ")


# Task 3
# # The user types in the start and end points of the range and a number.
# # If the number is not in the range, the program asks the user to re-enter the number,
# # and so on until the user enters the number correctly. The program displays all numbers in the range,
# # highlighting the number with exclamation marks. For instance: 1 2 3 !4! 5 6 7.
# while True:
#     nr1 = int(input("First nr: "))
#     nr2 = int(input("Last nr: "))
#     start = min(nr1, nr2)
#     end = max(nr1, nr2)
#     while True:
#         nr_input = input("Your number in the range, or type 'quit': ")
#         if nr_input == "quit":
#             print("Bye")
#             break

#         nr_input = int(nr_input)

#         if nr_input not in range(start, end + 1):
#             print("Please type a number withing the respective range")
#             continue
#         for num in range(start, end + 1):
#             if num == nr_input:
#                 print(f"!{num}!", end=" ")
#             else:
#                 print(num, end=" ")
# exit() => this results in the loop exiting the moment num !=nr input so we re not gone use it

# Now, with else, the loop always prints something for every number in the range.

# If it matches → prints !number!

# If it doesn’t match → prints the number normally.

# Result: You see the entire range, with your chosen number highlighted.

# break


# # Task 1
# # Print the multiplication table for the user-defined number. If the user typed in 7, the output should be as follows:
# # 7 * 1 = 7
# # 7 * 2 = 14
# # 7 * 3 = 21
# # …
# nr = int(input("Type a number: "))
# for num in range(1, 11):
#     total = nr * num
#     print(f"{nr} * {num} = {total}")


# Task 2-Vali
# The user types in a number from 1 to 12 that represents a month.
# Print its name. For example, if the number is 1, display "January"; if 2, display "February," etc.
while True:
    month_nr = input("Provide a nuber from 1 to 12 or 'quit': ")
    if month_nr == "quit":
        print("bye")
        break
    if not month_nr.isdigit():
        print("Please provide a valid input")
        continue
    month_nr = int(month_nr)
    if month_nr < 1 or month_nr > 12:
        print("Please provide a number between 1 and 12")
        continue
    months_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    if month_nr >= 1 and month_nr <= 12:
        print(months_list[month_nr - 1])
