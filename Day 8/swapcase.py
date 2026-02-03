inp = input("Enter a word   :   ")

arr = []

for ch in inp:
    if ch.islower():
        arr.append(ch.upper())
    else:
        arr.append(ch.lower())
    
word = "".join(arr)
print(word)