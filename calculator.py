def mul(x: float, y: float):
    c = x*y
    return c


def sub(x, y):
    c = x-y
    return c


def calculator(a, b):
    print("multiplication result:", mul(x=a, y=b))
    print("subtraction result:", sub(x=a, y=b))


calculator(4, 3)

my_list = ["1", "2", "3"]
my_tuple = ("1", "2", "3")
my_set = {"1", "2", "3"}
my_dictionary = {"key1": "1","key2": "2", "key3": "3" }
b= "john"
for key, value in my_dictionary.items():
    print(key)
    print(value)


for num in range(4):
    print(num)

for char in b:
    print(char)
for i in my_set:
    print(i)
