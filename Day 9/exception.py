# Exceptions - Runtime Errors
# Exception Handling


try:
    L = []
    print(L[0])
except IndexError:
    print("I handle Index error haha")
except Exception as e:
    print(f"I am the main error handler{e}")


try:
    print(1 / 0)
except Exception as e:
    print(f"I am the main error handler --> {e}")
finally:
    print("I am finally")
