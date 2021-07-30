from src.Calculator.Addition import addition
from src.Calculator.Division import division


def mean(data):
    try:
        total = 0
        length = len(data)
        for num in data:
            total = addition(total, num)
        return division(length, total)
    except ZeroDivisionError:
        print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
