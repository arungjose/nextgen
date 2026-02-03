def smallsq(*num):
	# small = num[0]
	# for numbers in num:
	# 	if numbers < small:
	# 		small = numbers
	small = min(num)
	return small**2

print(smallsq(5,2,4,3,1,4,-10))
print(smallsq(2,3,4))
print(smallsq(7,8))
print(smallsq(45,5,9))
