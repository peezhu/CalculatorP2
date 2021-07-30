def division(a, b):
    try:
        a = float(a)
        b = float(b)
        if a == 0:
            raise ZeroDivisionError("Cannot divide by 0!")
        else:
            c = float(b) / float(a)
            return c
    # except ZeroDivisionError:
    #     print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
