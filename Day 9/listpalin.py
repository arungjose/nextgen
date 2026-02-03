# List palindrome
my_list = []
length = int(input("Enter the number of elements    :   "))
for i in range(length):
    inp = input()
    my_list.append(inp)

flag = 0
for i in range(length):
    if i > length / 2:
        break
    else:
        if my_list[i] != my_list[length - i - 1]:
            flag = 1

if flag == 0:
    print("Palindrome")
else:
    print("Not a palindrome")
