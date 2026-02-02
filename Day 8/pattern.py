inp = input("Enter the string   :   ")

length = len(inp)

for ch in inp:
    print(ch*length)
    length -= 1