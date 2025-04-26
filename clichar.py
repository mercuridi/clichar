
def input_stat(stat_name):
    return input_int(f"\nPlease input your {stat_name} score: ", 20, 8)

def input_int(request: str, upper=float("inf"), lower=float("-inf")):
    while True:
        try:
            value = int(input(request))
            if check_bounds(value, upper, lower): 
                return value
            else: 
                print("The value failed its bounds check.")
        except TypeError:
            print("Please enter an integer value.")

def check_bounds(value: int, upper, lower):
    if value > upper:
        check = out_of_bounds_check(value, "high", upper)
    elif value < lower:
        check = out_of_bounds_check(value, "low", lower)
    else: 
        check = True
    return check

def out_of_bounds_check(value: int, hi_lo: str, exceeded_bound: int):
    if hi_lo == "high":
        maxmin_str = "max"
    else:
        maxmin_str = "min"
    print(f"\nThe value ({value}) is {hi_lo}er than expected.")
    print(f"The {maxmin_str}imum expected value was {exceeded_bound}.")
    if input_bool("Would you like to continue anyway? "):
        return True
    else:
        return False

def input_bool(request: str):
    while True:
        ans = input(request).lower()
        if ans in ["y", "yes", "t", "true"]:
            return True
        elif ans in ["", "n", "no", "f", "false"]:
            return False
        else:
            print("Please enter an affirmative or negative reply.")
            print("Empty replies are assumed negative.")

class Stat:
    def __init__(self, name, value):
        self.name = name
        self.abbreviation = name[:3].upper()
        self.value = value
        self.modifier = (value - 10) // 2
    
    def __str__(self):
        if self.modifier > 0:
            mod_string = f"+{self.modifier}"
        else:
            mod_string = str(self.modifier)
        return f"{self.name} " + \
            f"({self.abbreviation}): " + \
            f"{self.value} " + \
            f"({mod_string}) "

class Skill:
    def __init__(self, name: str, parent_stat: Stat):
        self.name = name
        self.parent_stat = parent_stat

class Skills:
    def __init__(self):
        pass
        
class Character:
    def __init__(self):
        print("Character creator initialised...\n")
        self.name = input("Please enter your character's name: ").title()
        
        print("\nNext, we will define your character's stats.")
        print("This number typically ranges from 8 to 20, ")
        print("but can be as low as 1 and as high as 30")
        print("when magic items and story events are involved.")
        
        # character race
        
        # character stats
        self.strength       = Stat("Strength"    , input_stat("Strength"))
        self.dexterity      = Stat("Dexterity"   , input_stat("Dexterity"))
        self.constitution   = Stat("Constitution", input_stat("Constitution"))
        self.intelligence   = Stat("Intelligence", input_stat("Intelligence"))
        self.wisdom         = Stat("Wisdom"      , input_stat("Wisdom"))
        self.charisma       = Stat("Charisma"    , input_stat("Charisma"))

    def print_name(self):
        print(f"Character name: {self.name}\n")

    def print_stats(self):
        print(f"{self.strength}")
        print(f"{self.dexterity}")
        print(f"{self.constitution}")
        print(f"{self.intelligence}")
        print(f"{self.wisdom}")
        print(f"{self.charisma}")
        
def print_char(char: Character):
    print()
    char.print_name()
    char.print_stats()

def main():
    new_char = Character()
    print_char(new_char)

if __name__ == "__main__":
    main()

# TODO justify the text printouts so they're easier to read
