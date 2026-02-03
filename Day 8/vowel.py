vowels = "aeiouAEIOU"
flag = 0
c = input("Enter a character    :   ")

# for ch in vowels:
#     if c == ch:
#         flag = 1

# if flag == 1:
#     print("Vowel")
# else:
#     print("Consonant")


if c in vowels:
    print("vowel")
else:
    print("consonant")