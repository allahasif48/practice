# import function  # import the whole file(or library)
from function import greet   # import the function that I want

print(greet.__code__.co_varnames)   # show the variable name
print(greet.__code__.co_nlocals)   # show the number of local variables
