
def input_stat(stat_name):
    
    
def input_string(request):
    pass

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
    else: check == True
    return check

def out_of_bounds_check(value: int, hi_lo: str, exceeded_bound: int):
    if hi_lo == "high":
        maxmin_str = "max"
    print(f"The value ({value}) is {hi_lo}er than expected.")
    print(f"The {maxmin_str}imum expected value was {exceeded_bound}.")
    if input_bool("Would you like to continue anyway? "):
        return True
    else:
        False

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
        self.abbreviation = name[:2].upper()
        self.value = value
        self.modifier = (value - 10) // 2

class Skill:
    def __init__(self, name: str, parent_stat: Stat):
        self.name = name
        self.parent_stat = parent_stat

class Skills:
    def __init__(self):
        self.acrobatics = Skill("Acrobatics")
        
class Character:
    def __init__(self):
        print("Character creator initialised...")
        name = input("Please enter your character's name: ")
        print("Next, we will define your character's stats.")
        print("This number typically ranges from 8 to 18, ")
        print("but can be as low as 1 and as high as 30.")
        

        # character stats
        self.strength = Stat("Strength",
            input_int(f"Please enter your character's Strength score: ", 
                        upper = 30, lower = 1)
        self.dexterity
        self.constitution
        self.intelligence
        self.wisdom
        self.charisma
        
    def __str__(self):
        pass
    
    def set_str(self, value: int):
        self.str = value




def main():
    new_char = Character()

if __name__ == "__main__":
    main()