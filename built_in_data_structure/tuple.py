# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

tup = (1, 2, 3, 4)

tup = tuple(list(tup) + [5, 6])

a, b, *c, d = tup
print(*c)

tup = tup + (7, 8)

print(tup)

