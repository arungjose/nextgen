inp = input("Enter a string :   ")
arr = []
mid = len(inp)//2
arr.append(inp[mid-1::-1])
arr.append(inp[len(inp):mid-1:-1])
print("".join(arr))