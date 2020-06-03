from Python_Practice.Beetroot_Home_Lessons.Calculator.Mods import Standard_Mod
from Python_Practice.Beetroot_Home_Lessons.Calculator.Mods import AutoMode

operations = ["addition", "subtraction", "multiplication", "division", "floor_division", "division_by_modulo",
              "exponent",
              "round_off_the_number", "the_square_root_of_the_number", "factorial", "exit"]

name = input("Input your name: ").capitalize()
selector = input("Choose the name of your mode: Standard or Auto_mode ").capitalize()


def standard():
    print("Standard mode is started")
    print(f"{name}, choose required operation from the current list: \n")
    print("For exit type 'exit'")
    print(f"List of available operations:\n{operations}")
    Standard_Mod.standard_module(operations, name)
    alternative()
    exit()


def auto_mode():
    print("AutoMode is started")
    print(f"{name}, choose required operation from the current list: \n")
    print(f"List of available operations:\n{operations}\n")
    print("For exit type 'exit'")
    AutoMode.auto_module(operations, name)
    alternative()
    exit()


def alternative():
    choosing = input("Do you wish change your mode? Yes/No: ").capitalize()
    if choosing == "Yes":
        selector = input("Choose the name of your mode: Standard or Auto_mode ").capitalize()
        while True:
            if selector == "Auto_mode":
                auto_mode()
            elif selector == "Standard":
                standard()
    if choosing == "No":
        exit()
    else:
        print("No such mode")


if selector == "Standard":
    standard()
elif selector == "Auto_mode":
    auto_mode()
else:
    print("No such mode")

alternative()


