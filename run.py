import random


#Character details
races = ['Human', 'Elf', 'Dwarf', 'Orc', 'Goblin', 'Cyborg', 'Werewolf', 'Vampire', 'Giant', 'Dragonborn']
race = random.choice(races)
   
# Start of program
print("Welcome to Fantasy RPG Character Generator!")
new_input = input("Create a new character? Please type 'Yes' or 'No'.\n")
if new_input == "Yes" or new_input == "yes":
    print("Okay! Let's make a new character!")
elif new_input =="No" or new_input == "no":
    print("That's a shame, maybe next time?")
else:
    print("That's not an answer I was expecting, please start again.")


