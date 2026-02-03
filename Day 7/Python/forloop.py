print("0 - > 10")
for i in range (10):
    print(i)


print("Even numbers till 100")
for i in range (2,101, 2):
    print(i)


print("String traversal")
str = "stylishstaralluarjun"
for ch in str:
    print(ch)

print("Reverse Odd")
x = int(input("Enter a number  :  "))

for i in range (x, 0, -1):
    if i%2 != 0:
        print(i)


for i in range (0, x, -1):
    print(i)
