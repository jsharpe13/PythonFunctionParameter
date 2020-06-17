"""
Program: inner_functions.py
Author: Jacob Sharpe
Last date modified: 6/16/2020

The purpose of this program is to take in a list of numbers and output
both the perimeter and the area
"""


def measurements(a_list):
    """ measurements uses inner functions to return the perimeter and area of a shape
    :param a_list, a list of numbers
    :returns a string of the perimeter and area
    """

    def area():
        length = a_list[0]
        if len(a_list) == 1:
            width = a_list[0]
        elif len(a_list) >= 2:
            width = a_list[1]
        return length * width

    def perimeter():
        length = a_list[0]
        if len(a_list) == 1:
            width = a_list[0]
        elif len(a_list) >= 2:
            width = a_list[1]
        return (length * 2) + (width * 2)

    result = "Perimeter = " + str(perimeter()) + " Area = " + str(area())
    return result


if __name__ == '__main__':
    print(measurements([2.1, 3.4]))
    print(measurements([3.5]))
