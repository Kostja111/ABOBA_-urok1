try:
    print("start code")
    #print(error)
    print("No errors")
except NameError as error:
    print(error)
else:
    print("I am ELSE")
finally:
    print("Finally code")