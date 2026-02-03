print("Give two word of equal length!")
word1 = input("Enter the first word     :   ")
word2 = input("Enter the second word    :   ")
arr = []

if len(word1) == len(word2):
    for i in range(len(word1)):
        arr.append(word1[i])
        arr.append(word2[i])

else:
    print("Words are not of equal length")

word = "".join(arr)
print(word)