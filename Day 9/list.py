L1 = [5,6,7,8,9]
L2 = ["abc","xyz", "pqr"]
L3 = ['a','b','c','d','e']

del L3[0]
print("L3 after update!	:	", L3)

L3.pop()
print("L3 after update!	:	", L3)

L3.pop(1)
print("L3 after update!	:	", L3)

print("L2 Status			:	", L2)

L2.clear()
print("L2 after update!	:	", L2)

print("L1 status			:	", L1)

L1.remove(6)
print("L1 after update!	:	", L1)