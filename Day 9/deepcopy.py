import copy

lst1 = [1, [2, 2], 3, 4]
lst2 = lst1.copy()
lst2[0] = 10

print("list 1   :   ", lst1)
print("list 2   :   ", lst2)

# lst1 2nd values is affected!!
lst2[1][0] = 20
print("list 1   :   ", lst1)
print("list 2   :   ", lst2)

# deepcopy
lst3 = copy.deepcopy(lst1)
print("list 3   :   ", lst3)
lst3[1][0] = 40
lst3[0] = 300
print("list 1   :   ", lst1)
print("list 3   :   ", lst3)
