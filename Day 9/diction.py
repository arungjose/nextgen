# Dictionary
"""{key:value, key:value}, unordered keys
must be unique, immutable type values can
be repeated"""

d1 = {}
d2 = dict()
fruits = {"a": "apple", "b": "banana"}

print(fruits)

# access - dict[key]
print("first ele", fruits["a"])

# adding pairs
fruits["b"] = "berrry"
print(fruits)

# Deletion
del fruits["b"]

fruits2 = {"m": "mango", "p": "papaya"}
fruits.update(fruits2)

print(fruits2)
