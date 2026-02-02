try:
    raise KeyError("Key Not found")
except Exception as e:
    print("There is an exception")
    print("Exception    :   ", e)
