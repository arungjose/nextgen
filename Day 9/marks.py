print("Please enter the marks	:	")
marklist = []

for _ in range(5):
	mark = int(input())
	marklist.append(mark)

print(marklist)

# Updated marklist

marks = [mark + 5 for mark in marklist if mark < 20]

print(marks)