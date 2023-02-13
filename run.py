import random


# Character details
races = ['Human', 'human', 'Elf', 'elf', 'Dwarf', 'dwarf', 'Orc', 'orc',
         'Goblin', 'goblin', 'Cyborg', 'cyborg', 'Werewolf', 'werewolf',
         'Vampire', 'vampire', 'Giant', 'giant', 'Dragonborn', 'dragonborn']

race = random.choice(races)

char_classes = ['Barbarian', 'Cleric', 'Druid', 'Fighter',
                'Ranger', 'Wizard', 'Rogue', 'Paladin', 'Warlock', 'Bard']

hair_colour = ['black', 'red', 'green', 'blonde', 'mousy brown', 'purple',
              'silver']
hair_style = ['straight', 'curly', 'wavy', 'braided', 'frazzled', 'slicked back']
hair_length = ['short', 'shoulder length', 'long']

char_alignment = ['Lawful good', 'Neutral good', 'Chaotic good', 'Lawful neutral',
                  'Neutral', 'Chaotic neutral', 'Lawful evil', 'Neutral evil', 'Chaotic evil']

eye_colour = ['wistful blue', 'cavernous green', 'piercing black', 'honest brown', 'mysterious p']

char_height = ['short', 'regular', 'tall', 'towering']
char_build = ['stocky', 'thin', 'wirey', 'imposing', 'muscular', 'soft']



# Start of program
def start_program():
    print("*********************************************\n")
    print("         Welcome to Fablefinder\n")
    print("*********************************************\n")
    new_input = input("Create a new character? Please type 'Yes' or 'No'.\n")
    if new_input == "Yes" or new_input == "yes":
        print("Okay! Let's make a new character!")
    elif new_input == "No" or new_input == "no":
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

while True:
    user_input_race = input("Please enter your choice...\n")
    if user_input_race == "Random" or user_input_race == "random":
        random_race = random.choice(races)
        print("Race:", random_race.capitalize())
        break
    else:
        if user_input_race in races:
            print(f"You have chosen: {user_input_race.capitalize()}\n")
            break
        elif user_input_race not in races:
            print("""
                That's a new one! Never heard of that!
                But do please choose from the list...
                """)
            continue
        

def assign_random_name():
    vowels = "aeiou"
    cons = "bbbcdddfghhklmnprrrsssttty"
    num_vowels = random.randint(2, 3)
    num_cons = random.randint(2, 3)
    name = ''.join([random.choice(vowels) for i in range(num_vowels)] +
                   [random.choice(cons) for i in range(num_cons)])
    return name.capitalize()


new_name = assign_random_name()
print("Let me bestow upon you a new name! Welcome:", new_name, "!\n")


print(f"Ok {new_name}, let me choose a class for you...\n")
print("Pondering...\n")

char_class = random.choice(char_classes)
print("Your class is:", char_class)



if user_input_race == "Random" or user_input_race == "random":
    print(f"Ah... {random_race.capitalize()}", char_class, 
      "... I haven't seen one of those before.")
elif user_input_race in races:
    print(f"Ah... {user_input_race.capitalize()}", char_class,
           "... I haven't seen one of those before.")


user_input_looks = input(f"Ok {new_name}, would you like to see what you look like?\n"
                           "Please choose 'yes' or 'no'.\n")
if user_input_looks == 'Yes' or user_input_looks == 'yes':
    char_hair = random.choice(hair_length) + ', ' + random.choice(hair_style) + ', ' + random.choice(hair_colour)
    print(f"It looks like you have {char_hair} hair.\n")

    char_eyes = random.choice(eye_colour)
    print(f"You have eyes that are {char_eyes}.\n")

    char_body = random.choice(char_height) + ', ' + random.choice(char_build)
    print(f"What a {char_body} body you have!\n")
elif user_input_looks == 'No' or user_input_looks == 'no':
    print("I suppose it's nice to feel mysterious.\n")


print("Next, it is important to discover your Alignment in this world.")
print(f"{new_name}, we must channel energy from a crystal for answers.\n")
user_input_align = input("Are you holding out your hand? Yes or no?\n")                         
if user_input_align == 'Yes' or user_input_align == 'yes':
    char_align = random.choice(char_alignment)
    print(f"It would look like, {new_name}, that you are {char_align}!\n")

#align_explain = input(f"{new_name}, would you like me to explain this more?\n")
#if align_explain == 'Yes' or align_explain == 'yes':
    #print(f"{align_def}")
# create dictionary of key value pairs for alignment


# Dice rolling function using 4, 6 sided dice. 
# Add the 3 highest numbers to get stats values.
def roll_dice():
    dice = []
    for i in range(4):
        dice.append(random.randrange(1, 7))

    total = 0
    lowest = dice[0]

    for num in dice:
        if num < lowest:
            lowest = num

    for num in dice:
        total += num

    return total - lowest


print("Moving on, let us discover your Ability scores...\n")

user_input_dice = input(f"{new_name}, before we roll, please choose your dice colour.\n"
                        "Would you like to choose Green or Blue?\n")
def dice_colour():
    if user_input_dice == "Green" or user_input_dice == "green":
        print("Green it is, let's roll for your Strength.")
        char_strength = roll_dice()
        if char_strength >= 13:
            print(f"You have rolled {char_strength}, this will work in your favour.\n")
        else:
            print(f"You have rolled {char_strength}, you may need to work harder.\n")
    elif user_input_dice == "Blue" or user_input_dice == "blue":
        print("Blue, a good choice, let's roll for your Strength.")
        char_strength = roll_dice()
        if char_strength >= 13:
            print(f"You have rolled {char_strength}, not a bad roll.\n")
        else:
            print(f"You have rolled {char_strength}, I would suggest good armour.\n")
    else:
        print("That was not an option, please be more careful. I will now choose the Blue dice for you...\n")
        char_strength = roll_dice()
        if char_strength >= 13:
            print(f"{char_strength}, you have luck in your favour.\n")
        else:
            print(f"{char_strength}, quite low, you should choose more wisely next time.\n")                            

          
dice_colour()


print("Next we roll for your Dexterity...\n")
char_dex = roll_dice()
if char_dex >= 13:
    print(f"You have rolled {char_dex}, what an advantage.\n")
else:
    print(f"you have rolled {char_dex}, you must stay alert at all times.\n")


print("On to your roll for Constitution...\n")
char_con = roll_dice()
if char_con >= 13:
    print(f"You have rolled {char_con}, you will endure.\n")
else:
    print(f"you have rolled {char_con}, take heed of your energy.\n")


print(f"{new_name}, what think you of your Intelligence..?\n")
char_intel = roll_dice()
if char_intel >= 13:
    print(f"You have rolled {char_intel}, you will not be outsmarted.\n")
else:
    print(f"you have rolled {char_intel}, be sure in your answers.\n")


print("The penultimate, we roll for Wisdom...\n")
char_wis = roll_dice()
if char_wis >= 13:
    print(f"You have rolled {char_wis}, others will look to you.\n")
else:
    print(f"you have rolled {char_wis}, best to always take stock of the situation.\n")


print("Finally, we roll for Charisma...\n")
char_car = roll_dice()
if char_car >= 13:
    print(f"You have rolled {char_car}, a natural way about you, there is.\n")
else:
    print(f"you have rolled {char_car}, good luck with that.\n")





