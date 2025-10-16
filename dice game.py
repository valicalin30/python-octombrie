import random

# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│ ●       │", "│         │", "│       ● │", "└─────────┘"),
    3: ("┌─────────┐", "│ ●       │", "│    ●    │", "│       ● │", "└─────────┘"),
    4: ("┌─────────┐", "│ ●     ● │", "│         │", "│ ●     ● │", "└─────────┘"),
    5: ("┌─────────┐", "│ ●     ● │", "│    ●    │", "│ ●     ● │", "└─────────┘"),
    6: ("┌─────────┐", "│ ●     ● │", "│ ●     ● │", "│ ●     ● │", "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
print(dice)
for die in range(num_of_dice):  # -> outter for loop-> number of dices
    for line in dice_art.get(dice[die]):  # -> inner loop -> printing every tuple
        print(line)

for die in dice:
    total += die
print(f"Total = {total}")
for die in dice_art[3]:
    print(die)
