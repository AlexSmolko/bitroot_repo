from Python_Practice.Beetroot_Home_Lessons.Calculator import Main

#result = 0

signs = ["+", "-", "*", "/", "%", "//", "**"]


def expression_result(sign, result):
    if sign in signs:
        expression2 = sign
        print(f"{operand1} {expression2} {operand3} = {result}")
    return result


while True:
    operation = input("Enter the command from loaded list: ")
    if operation == "exit":
        break
    if operation == "factorial":
        number = int(input("Enter a number which you would wish to handle: "))
        factorial = 1
        for n in list(range(2, number + 1)):
            factorial *= n
        print(f'Output of factorial of the number: {number} \n \t \t \t \tis \n'
              f'\t \t \t \t{factorial}')
        continue

    if operation == "the_square_root_of_the_number":
        number = (input("Enter a number which you would wish to handle:"))
        if int(number) < 0:
            print("Operation impossible, because impossible to get the square root of a negative number")
        sqrt_op = int(number) ** (1 / 2)
        print(f'Output of square root of the number: {number} \n \t \t \t \tis \n'
              f'\t \t \t \t{sqrt_op}')
        continue

    if operation == "round_off_the_number":
        number = input("Enter a number which you would wish to handle:")
        print(f'Output of the round_off_the_number operation with number {float(number)}:  \n \t \t \t \tis')
        print(f"\t \t \t \t{round(float(number))}")
        continue
    #
    # if operation not in Main.operations:
    #     print("You entered incorrect operation")

    operand1, operand2, operand3 = input("Enter your expression here across blank line: ").split(" ")

    addition = int(operand1) + int(operand3)
    subtraction = int(operand1) - int(operand3)
    multiplication = int(operand1) * int(operand3)
    division = int(operand1) / int(operand3)
    floor_division = int(operand1) // int(operand3)
    division_by_modulo = int(operand1) % int(operand3)
    exponent = int(operand1) ** int(operand3)

    if operation == "addition":
        expression_result("+", addition)
    elif operation == "subtraction":
        expression_result("-", subtraction)
    elif operation == "multiplication":
        expression_result("*", multiplication)
    elif operation == "division":
        expression_result("/", division)
    elif operation == "division_by_modulo":
        expression_result("%", division_by_modulo)
    elif operation == "floor_division":
        expression_result("//", floor_division)
    elif operation == "exponent":
        expression_result("**", exponent)
