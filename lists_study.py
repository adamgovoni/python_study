# testing some python code in sublime 3

a = 5
b = 6

c = a + b

print(a, b, c)

# testing lists: start with empty list
# using append add item to list
a = []
# append only takes 1 argument
a.append(5)
print(a)

# counting how many times 'x' appears in the list using 'index'
a.append(6)
print(a)
print("The number 6 appears " + (str(a.index(6))) + " time/s in list 'a' ")

# appending the integer '1' to the list
a.append(1)
print(a)

# using 'extend' to append more than one item to the list
# you have to provide an iterable item so here I used another list
# extend iterates over list 'b'' and adds b's items to list 'a'
b = [8, 9, 10]
a.extend(b)
print(a)

# using 'sort' to order the items in the list
a.sort()
print(a)

# clearing a list using 'clear'
# before clearing the list it is saved as 'b'
# I print list 'a' after to show it is in fact empty
# notice that printing 'b' shows that it is also empty
# this is because there were never two seperately saved lists
# the data in list 'a' was simply references by list 'b'
# as soon as list 'a' was cleared it cleared the memory location
# that list 'b' pointed two so in effect both lists are cleared
b = []
b = a
print("Before clearing list a, list b = " + str(b))
a.clear()
print("After clearing list a the result is...")
print("List a = " + str(a))
print("List b = " + str(b))

# printing the memory address of both list 'a' and 'b' 
print("The memory address of list a is: " + str(id(a)))
print("The memory address of list b is: " + str(id(b)))

# appending an item to list 'a' while list 'b' still references
# the same memory address will show the items in both lists
a.append(17)
print(b)
print("The memory address of list a is: " + str(id(a)))
print("The memory address of list b is: " + str(id(b)))

# if the list is reinitialized 'a=?' then it receives a new memory address
# 'b' will then be the only variable with 'a's' previous address
a = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(a)
print(b)
print("The memory address of list a is: " + str(id(a)))
print("The memory address of list b is: " + str(id(b)))
