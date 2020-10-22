import random

class Die:
    '''
    Define the Die class, name of the die and number of sides.
    '''
    def __init__(self, name, sides=1):
        self.name = name
        self.sides = sides
    def __str__(self):
        return f"This is a {self.name}."

d4 = Die("D4", 4)
d6 = Die("D6", 6)
d8 = Die("D8", 8)
d10 = Die("D10", 10)
d12 = Die("D12", 12)
d20 = Die("D20", 20)
d100 = Die("D100", 100)

def roll_dice(die_type, number_of_dice):
    '''
    Main Function that rolls dice for us.
    Choose a die type (d4,d6,d20 ecc.) and the number of dice to roll.
    Returns the total rolled.
    '''
    roll_total = 0
    for _ in range(number_of_dice):
        roll = random.randint(1,die_type.sides)
        roll_total += roll
        print(roll)
    return roll_total

def check_average(die_type):
    '''
    Function for checking the average roll of a 1000 rolls (used only in development)
    '''
    total = 0
    for _ in range(1000):
        roll = roll_dice(die_type)
        total += roll
    average = total / 1000
    return average

def game_on():
    '''
    Ask if player is ready to play.
    '''
    g = input("Are You ready to play? Y or N").upper()
    if g == "Y":
        return True
    else:
        return False

def choose_a_die():
    '''
    Associate integer input to a die class
    '''
    while True:
        try:
            m = int(input("What die would You like to roll? Write the number of sides. "))
        except:
            print("Sorry, that's not a number.")
        else:
            if m == 4:
                return d4
                break
            elif m == 6:
                return d6
                break
            elif m == 8:
                return d8
                break
            elif m == 10:
                return d10
                break
            elif m == 12:
                return d12
                break
            elif m == 20:
                return d20
                break
            elif m == 100:
                return d100
                break
            else:
                print("Sorry, we don't have this type of dice.")
                continue

def roll_same():
    '''
    Ask player if he wants to roll the same combination of dice again.
    '''
    s = input("Roll the same? Y or N. ").upper()
    if s == 'Y':
        return True
    else:
        return False

def roll_another():
    '''
    Asks if you want to roll another set of dice
    '''
    r = input("Would you like to roll another die? Y or N").upper()
    if r == "Y":
        return True
    else:
        return False
if __name__ == "__main__":
    while True:
        print("\n")
        print("Welcome to the Dice Roller")
        print("At the moment, this app allows you to roll the following dice:")
        print("D4, D6, D8, D10, D12, D20, D100")
        print("\n")
        gaming = game_on()
        while gaming:
            my_die = choose_a_die()
            dice_number = int(input("And how many dice would You like to roll? "))
            my_roll = roll_dice(my_die,dice_number)
            print(f"You rolled {my_roll}")
            loop = roll_same()
            while loop:
                my_roll = roll_dice(my_die,dice_number)
                print(f"You rolled {my_roll}")
                loop = roll_same()
                continue
            gaming = roll_another()
        print("Thank You for rolling with us!")
        break
