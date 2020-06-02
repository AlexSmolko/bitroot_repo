#from Python_Practice.Beetroot_Home_Lessons.Calculator import Main


def operations(operation):
    while True:
        if operation not in operations:
            print("You entered incorrect operation")
            continue
        if operation == 'exit':
            print("You finished the program.")
            print("Good buy, Dear user!")
            break
        if operation == "round_off_the_number":
            number = input("Please enter the number: ")
            print(f'Output of the round_off_the_number operation with number {float(number)}:  \n \t \t \t \tis')
            print(f"\t \t \t \t{round(float(number))}")
            continue
        if operation == "factorial":
            number = int(input("Please enter the number: "))
            factorial = 1
            for n in list(range(2, number + 1)):
                factorial *= n
            print(f'Output of factorial of the number: {number} \n \t \t \t \tis \n'
                  f'\t \t \t \t{factorial}')
            continue
        if operation == "the_square_root_of_the_number":
            number = (input("Please enter the number: "))
            if int(number) < 0:
                print("Operation impossible, because impossible to get the square root of a negative number")
            sqrt_op = int(number) ** (1 / 2)
            print(f'Output of square root of the number: {number} \n \t \t \t \tis \n'
                  f'\t \t \t \t{sqrt_op}')
            continue
        number1, number2 = input("Please enter two numbers separated by space: \n").split(" ")
        if operation == "addition":
            addition = int(number1) + int(number2)
            print(f'Output of the addition operation: {number1} + {number2} \n \t \t \t \tis \n'
                  f'\t \t \t \t{addition}')
        elif operation == "subtraction":
            subtraction = int(number1) - int(number2)
            print(f'Output of the subtraction operation: {number1} - {number2} \n \t \t \t \tis')
            if number2 > number1:
                print(f"\t \t \t \t{subtraction}")
            else:
                print(f"\t \t \t \t{{subtraction}}")
        elif operation == "multiplication":
            multiplication = int(number1) * int(number2)
            print(f'Output of the multiplication operation: {number1} * {number2} \n \t \t \t \tis')
            print(f"\t \t \t \t{multiplication}")
        elif operation == "division":
            if int(number2) == 0:
                print("Division by zero is forbidden")
                continue
            else:
                division = int(number1) / int(number2)
                print(f'Output of the subtraction operation: {number1} / {number2} \n \t \t \t \tis')
                print(f"\t \t \t \t{division}")

        elif operation == "floor_division":
            floor_division = int(number1) // int(number2)
            print(f'Output of the floor_division operation: {number1} // {number2} \n \t \t \t \tis')
            print(f"\t \t \t \t{floor_division}")
        elif operation == "division_by_modulo":
            division_by_modulo = int(number1) % int(number2)
            print(f'Output of the division_by_modulo operation: {number1} % {number2} \n \t \t \t \tis')
            print(f"\t \t \t \t{division_by_modulo}")
        elif operation == 'exponent':
            exponent = int(number1) ** int(number2)
            print(f'Output of the exponent operation: {number1} in power of {number2} \n \t \t \t \tis')
            print(f"\t \t \t \t{exponent}")