inp = int(input("Enter the number to find   :   "))

def fact(n):
    if n < 0:
        exit()
    elif n <= 0 or n <= 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(inp))