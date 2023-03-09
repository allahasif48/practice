my_list = ["windows", "Linux", "Mac OS", "Unix"]
print(type(my_list))
print('first_element', my_list[0])
print('last_element', my_list[-1])
print('length', len(my_list))
print(my_list[0:2])
print(my_list[0:0])
print(my_list[-1:1])

# [Number_of_ELEMENT][START_POINT:END_POINT]
print(my_list[0:3])
print(my_list[1:1])
print(my_list[-1:-2])
print(my_list[-2:-1])

# [NUMBER_OF_ELEMENT][START_POINT : END_POINT]
print(my_list[0:3:2])
# 0 -->windows
# 0+2=2--> Mac OS
# 2+2=4---> out of range

my_list[2] = 'asif'
# my_list[-4] = 'windows'
print(my_list)

# append --> allows us to add a single element to a list(adds at the end)
my_list.append("c0883873")
print(my_list)
# insert allows us to add a single element to the list given
# a specific position(element)
my_list.insert(-2, "windows")
print(my_list)

# index(element)---->index of the element inside the list
print(my_list.index("windows"))

# count(element)--> counts the occurrence of a certain element
print(my_list.count("windows"))
# remove(element)
print(my_list.remove("Linux"))
print(my_list)

# del list[index]--> removes the elemnet given the index

del my_list[0]
print(my_list)
# pop[index]--> pops the element form the list
# removes the element
print(my_list.pop(0))
print(my_list)

# clear() --> it clears the elements in the list
# my_list.clear()
# print(my_list)

# sort() --> sorts the elements in the list
my_list.sort()
print(my_list)

#reverse() ---> reverse the elements in the list
my_list.reverse()
print(my_list)