import random


#Character details
races = ['Human', 'human', 'Elf', 'elf', 'Dwarf', 'dwarf', 'Orc', 'orc', 'Goblin', 'goblin', 
         'Cyborg', 'cyborg', 'Werewolf', 'werewolf', 'Vampire', 'vampire', 'Giant', 'giant', 'Dragonborn', 'dragonborn']
race = random.choice(races)

  
# Start of program
def start_program():
    print("Welcome to Fantasy RPG Character Generator!")
    new_input = input("Create a new character? Please type 'Yes' or 'No'.\n")
    if new_input == "Yes" or new_input == "yes":
        print("Okay! Let's make a new character!")
    elif new_input =="No" or new_input == "no":
        print("That's a shame, maybe next time?")
    else:
        print("That's not an answer I was expecting, please start again.\n")
        start_program()


start_program()


def create_new_char():
    print("""
        Lets start with your characters race...
        Please choose one from the list and enter it below or
        choose 'Random' to be assigned one.
        *Human        *Elf        *Dwarf
        *Orc          *Goblin     *Cyborg
        *Werewolf     *Vampire    *Giant
        *Dragonborn   *Random
        """)
    new_input = input("Please enter your choice...\n")
    if new_input == "Random" or new_input == "random":
        race = random.choice(races)
        print("Race:", race)
    else:
        if new_input in races:
            print(f"You have chosen: {new_input.capitalize()}\n")
        elif new_input not in races:
            print("""
                That's a new one! Never heard of that!
                But do please choose from the list... 
                """)
            create_new_char()


create_new_char()

def assign_random_name():
    vowels = "aeiou"
    cons = "bbbcdddfghhklmnprrrsssttty"
    num_vowels = random.randint(2, 3)
    num_cons = random.randint(2, 3)
    name = ''.join([random.choice(vowels) for i in range(num_vowels)] +
                   [random.choice(cons) for i in range(num_cons)]) 
    return name.capitalize() 
    
    
new_name = assign_random_name()
print("Let me randomly choose your new name! Welcome:", new_name)






