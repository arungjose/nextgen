# Keyword Arguments
def stddetails(**args):
    print(args)

stddetails(name="arun", score=67)


def disp(n1,n2,*others):
    print("n1=",n1)
    print("n2=",n2)
    print("others",others)
