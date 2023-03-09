def my_calculator(a, b, operator_type: str):
    """
    This is my simple calculator
    :param a: is the first input
    :param b: in the second input
    :param operator_type: can be addition, subtraction, multiplication, division, and exponent
    :return: the result of the requested operation
    """
    # if both a AND b belong to the class float at the same type
    if isinstance(a, float) and isinstance(b, float):
        if operator_type == 'addition':
            return find_addition(x=a, y=b)
        elif operator_type == 'subtraction':
            return find_subtraction(x=a, y=b)
        elif operator_type == 'multiplication':
            return find_multiplication(x=a, y=b)
        elif operator_type == 'division':
            return find_division(x=a, y=b)
        elif operator_type == 'exponent':
            return find_exponent(x=a, y=b)
        else:
            print("The operator_type either has typos or is not defined")
    # either a OR b does not belong to the class float
    else:
        print("Invalid input type for either a or b")


def find_addition(x, y):
    return x + y

def find_subtraction(x, y):
    return x - y

def find_multiplication(x, y):
    return x * y

def find_division(x, y):
    if y == 0:
        print("The denominator must not be zero")
    else:
        return x / y

    # if y != 0:
    #     return x / y
    # else:
    #     print("The denominator must not be zero")

def find_exponent(x, y):
    return x ** y

user_input_a = input("Enter the value of a:")
user_input_b = input("Enter the value of b:")
user_input_operator_type = input("Enter the operator type:")
# print("The result is: ", my_calculator(a=2, b=4, operator_type="addittion"))
# print("The result is: ", my_calculator(a=2, b=4, operator_type="subtraction"))
print("The result is: ", my_calculator(a=user_input_a, b=user_input_b, operator_type=user_input_operator_type))


# isinstance(variable_type, expected_type) -> it checks if the variable_type is the same as the expected_type
# print(type(2))
# print(isinstance(2, int))
# print(isinstance(2.5, float))

# A Conditional Statement
# 1) if    (required) -> one instance
# 2) elif  (optional) -> one or more instance
# 3) else  (optional) -> one instance
# Criteria:
# greater ">"
# greater than or equal ">="
# less "<"
# less than or equal "<="
# equal (the same) "=="
# not equal "!="
# a = -7
# print('criteria (if):', a >= 1)
# print('criteria (elif):', a < -5)
# print('criteria (elif 2):', a < -7)
# --------------------------
# if a >= 1:
#     print("a is greater than or equal 1")
# elif a < -5:  # this means that a can be -6, -7, -8, -9, ...
#     print("a is less than -5 (elif)")
# elif a < -7:  # this means that a can be -8, -9, -10, -11, ...
#     print("a is less than -7 (elif 2)")
# else:
#     print("none of the conditions have return true")
# --------------------------
# a = "-7"  # assign -7 to a
# # object 1 == object 2 -> this means the two objects have the same value AND the same type (same class)
# print(type(a))
# print(type(-7))
# if a == -7:  # if a is -7 or not
#     print("a is equal -7 (new if)")
# else:
#     print("none of the above")