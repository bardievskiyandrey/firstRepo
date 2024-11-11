print("prev code")
try:
    input()
    print(0/0)
    print(value)
except ZeroDivisionError:
    print("Error")
except KeyboardInterrupt:
    print("keyboard error")
except (NameError, KeyError) as error:
    print(error)
print("next code")