# Imports practice // Module_2

from Python_Practice.Beetroot_Home_Lessons.Lesson17_Modules_and_stand_lib.Task1_Module1 import weather


def answers():
    answer = " "
    while answer != "Exit":
        answer = input("Select your variant of analytics. \n Food. \n Weather. \n "
                       "Sport. \n or \n Exit for exit of the program: ").capitalize()
        if answer == "Weather":
            weather()
        elif answer == "Exit":
            print("Program finished")
            break
        else:
            print("Sorry, I can not give you any information. Try another variant of input")
    return

answers()