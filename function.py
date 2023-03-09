# def <FUNCTION_NAME>(INPUT):
# CALCULATIONS
# <return Result>
p = 10  # global variable


def fun1(x):
    return x * x


# more preferred compared to fun1
def fun2(x):
    z = 1  # private variable
    print("Step 1: initial step")
    y = x * x + p + z
    print("step 2: calculating y")
    return y


result = fun2(x=8)
print(result)
# print(z) z is local or private variable cannot be used outside of function

zx = "A+"


def show():
    zx = "B+"
    print("Highest grade:", zx)


show()


# first name is default parameter
# last name optional parameter
def greet(first_name: str, last_name: str = None):
    """
    A function to print the first and last name
    :param first_name: the first name of the person (str)
    :param last_name: the last name of the person (str)
    :return:none
    """
    print("hello", first_name, last_name)


greet(first_name="Asif", last_name="Shaikh")
greet(first_name="Asif")
# greet(first_name=1, last_name=2)  # Incorrect parameter type
