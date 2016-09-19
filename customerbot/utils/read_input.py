import sys


def input_function():
    """
    :return: Normalize reading input bewteen python 2 and python 3
    'raw_input' is just input in python 3
    """
    if sys.version_info[0] < 3:
        user_input  = str(raw_input())

        # Avoid problems using format strings with unicode characters
        if user_input:
            user_input = user_input.decode('utf-8')
    else:
        user_input = input()

    return user_input
