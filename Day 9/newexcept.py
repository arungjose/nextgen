try:
    d = {"a": 1}
    print(d["a"])
except Exception as e:
    print("there is an exception")
    print("Exception: ", e)
else:
    print("All good no exception")
finally:
    print("I am finally")
