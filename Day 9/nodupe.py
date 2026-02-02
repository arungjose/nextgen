x = int(input("Enter range	:	"))
my_list=[]
for i in range(x):
	inp = input()
	my_list.append(inp)

set_list = set(my_list)
new_list = list(set_list)
print(new_list)