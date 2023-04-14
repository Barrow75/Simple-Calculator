# Calculator 1v1.0
# A simple calculator that takes just the simple arithmatic (Add, Subtract, Multiple and Divide)


def Calculator(Number_1, Number_2, operator):
    if operator == "+":
        return Number_1 + Number_2
    elif operator == "-":
        return Number_1 - Number_2

    elif operator == "*":
        return Number_1 * Number_2

    elif operator == "/":

        return Number_1 / Number_2

    else:
        return "Invalid"


Number_1 = float(input("Enter First Number: "))
operator = input("Enter Operator: ")
Number_2 = float(input("Enter Second Number: "))
result = Calculator(Number_1, Number_2, operator)
print(result)

