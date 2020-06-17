"""
Program: string_functions.py
Author: Jacob Sharpe
Last date modified: 6/16/2020

The purpose of this program is to take in a string and an number and output
the string message the amount given
"""


def multiply_string(message, n):
    """ this takes the message string and the number of times to output and returns the string
    :param n, number of times to output
    :param message, message string
    :returns the created string from the for loop
    """
    results = ""
    for x in range(n):
        results = results + message
    return results


if __name__ == '__main__':
    result = multiply_string("Jacob", 3)
    print(result)
