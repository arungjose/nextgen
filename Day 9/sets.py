# sets - unordered, no index ,unique

s = set()
s1 = {6, 7, "abc"}
print(s1)

s2 = {6, 7, "abc", 5, 6, 7}
print(s2)

s2.add("xyz")
print(s2)

s2.update({5, 6})
print(s2)

s2.remove("xyz")
print(s2)
s2.pop()
