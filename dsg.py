try:
    print("start code")
    print(10/0)
    print("no errors")
except(NameError, ZeroDivisionError) as error:
    print(error)