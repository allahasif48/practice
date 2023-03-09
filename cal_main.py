
def calculate(a, b, operator):
    if operator == "addition":
        return addition(a,b)
    elif operator == "subtraction":
        return subtraction(a,b)
    elif operator == "multiplication":
        return multiplication(a,b)
    elif operator == " division":
        return division(a,b)


def addition(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    if b != 0:
        return a/b
    else:
        print("Base cannot be zero for division operation")


a = input("Enter first input value")
b = input("Enter second input value")
operation = input("Enter the operation to be performed")

print("result is:", calculate(a=a, b=b, operator=operation))


