from src.Calculator.Addition import addition
from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Calculator.Subtraction import subtraction
from src.Statistics.Mean import mean


def population_variance(data):
    try:
        length = len(data)
        mean_v = mean(data)
        total = 0
        for x in data:
            x = square(subtraction(mean_v, x))
            total = addition(x, total)
        return division(length, total)
    except ZeroDivisionError:
        print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
