import random


#Character details
races = ['Human', 'human', 'Elf', 'elf', 'Dwarf', 'dwarf', 'Orc', 'orc', 'Goblin', 'goblin', 
         'Cyborg', 'cyborg', 'Werewolf', 'werewolf', 'Vampire', 'vampire', 'Giant', 'giant', 'Dragonborn', 'dragonborn']
race = random.choice(races)

char_classes = ['Barbarian','Cleric','Druid','Fighter', 'Ranger', 'Wizard', 'Rogue']


  
# Start of program
def start_program():
    print("Welcome to Fantasy RPG Character Generator!\n")
    new_input = input("Create a new character? Please type 'Yes' or 'No'.\n")
    if new_input == "Yes" or new_input == "yes":
        print("Okay! Let's make a new character!")
    elif new_input =="No" or new_input == "no":
        print("That's a shame, maybe next time?")
        start_program()
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


create_new_char()


user_input_race = input("Please enter your choice...\n")
if user_input_race == "Random" or user_input_race == "random":
    race = random.choice(races)
    print("Race:", race)
else:
    if user_input_race in races:
        print(f"You have chosen: {user_input_race.capitalize()}\n")
    elif user_input_race not in races:
        print("""
            That's a new one! Never heard of that!
            But do please choose from the list... 
            """)
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
print("Let me bestow upon you a new name! Welcome:", new_name,"!\n")


print(f"Ok {new_name}, let me choose a class for you...\n")
print("Pondering...\n")

char_class = random.choice(char_classes)
print("Class:", char_class)

print(f"Ah... a {char_class}", user_input_race.capitalize(), "... I haven't seen one of those before.")


