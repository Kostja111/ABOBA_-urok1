try:

    try:
        print("start code")
        print(10/0)
        print("no errors")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)