# A set is a collection which is unordered, unchangeable*, and un-indexed and do not allow duplicate values.
import argparse

# Once a set is created, we cannot change its items, but you can remove items and add new items.

s = {1, 2, 'a'}

s.add(4)

s.discard('a')

s.remove(4)

s1 = {3, 2}

z = s.difference(s1)

# s.difference_update(s1)

x = s.intersection(s1)

x1 = s.isdisjoint(s1)

s2 = {1}

z1 = s2.issubset(s)

z2 = s.issuperset(s2)

z3 = s.symmetric_difference(s1)

s = s.union({5, 6})

s.update({7, 8})

print(s)
