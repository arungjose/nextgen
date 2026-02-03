my_str = input("Enter a string :   ")

doobly = []
doobly2 = []
rev = my_str[::-1]

for i in range(len(my_str)):
    doobly.append(rev[i] * 2)

    doobly2.append(rev[i] + str(i))

print(doobly)
print(doobly2)
