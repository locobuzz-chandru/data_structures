# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

d = {1: 'a', 2: [1, 'b']}

d1 = d[1]

d[1] = 'c'

d1 = d.get(1)

di = list(d.items())
dv = list(d.values())
dk = list(d.keys())

a = {3: 'c'}
d.update(a)

print(d)

x = ('key1', 'key2', 'key3')
y = 0

dic = dict.fromkeys(x, y)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")

