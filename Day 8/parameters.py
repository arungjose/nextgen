def findsum(a=0, b=0, c=0):
    print(a+b+c)


findsum(10,25)
findsum(10,10,10)
findsum(10)

# Special Parameters
def findmult(*nums):
    prod=1
    for n in nums:
        prod=prod*n
    print("Product is    :    ", prod)


findmult(12,23,34,45)
