from Python_Practice.Beetroot_Home_Lessons.Calculator.Mods import Standard_Mod, AutoMode

operations = ["addition", "subtraction", "multiplication", "division", "floor_division", "division_by_modulo",
              "exponent",
              "round_off_the_number", "the_square_root_of_the_number", "factorial", "exit"]

name = input("Input your name: ").capitalize()
selector = input("Choose the number of your mode: 1. - Standard or 2. - AutoMode ")
try:
    if selector == '1':
        print("Standard mode is started")
        print(f"{name}, choose required operation from the current list: \n")
        print(f"List of available operations:\n{operations}")
        Standard_Mod.standard_module()
    if selector == '2':
        print("AutoMode is started")
        print(f"{name}, choose required operation from the current list: \n")
        print(f"List of available operations:\n{operations}")
        AutoMode.automode()
    else:
        print("NO such mode")
except AttributeError as a:
    print(a)