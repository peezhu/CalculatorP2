from src.Calculator.Addition import addition
from src.Calculator.Division import division
from src.Calculator.Subtraction import subtraction


def median(data):

    try:
        lst = sorted(data)
        length = len(data)
        if length % 2 == 0:  # the data set has an even number of elements
            median1 = lst[int(length // 2)]  # this is the first element of the second half)
            median2 = lst[int(subtraction((length // 2), 1))]   # this is the last element of the first half
            actual_median = division(2, addition(median1, median2))
        else:
            actual_median = lst[length // 2]    # this is the middle element if the data has an off number of elements
        return actual_median
    except ZeroDivisionError:
        print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
