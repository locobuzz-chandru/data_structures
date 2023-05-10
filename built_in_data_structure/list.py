# Lists are one of 4 built-in data types in Python used to store collections of data

# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

lst = [1, 2, 3, 'a', {1: 'x'}]

lst.append(4)

l = lst[2]

lst = lst + ['m', 'p']

lst.extend([5, 9])

lst.insert(0, 'z')

x = lst.copy()

lst.pop()

lst.remove('p')

lst.reverse()

print(lst)
