from collections import Counter


def mode(data):
    try:
        length = len(data)  # calculates how many elements in data
        count = Counter(data)   # counts amount of keys and values
        get_mode = dict(count)  # splits count into dictionary
        mode_lst = [k for k, v in get_mode.items() if v == max(list(count.values()))]  # goes through mode_dict
        print(type(mode_lst))
        print(mode_lst)
        if len(mode_lst) == length:
            get_mode = "No mode found"
        else:
            get_mode = mode_lst[0]
        return get_mode
    except ZeroDivisionError:
        print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
