"""
Program: validate_input_in_functions.py
Author: Jacob Sharpe
Last date modified: 6/16/2020

validates input and prints out an invalid message if the number
does not meet the criteria
"""

"""score_input takes the name and test score and if it is in a valid
range will output the test name and score
:param test name, and test score between 1 and 100
:returns string of combined test name and score
"""


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    result = ""
    try:
        test_score = int(test_score)
    except ValueError:
        return invalid_message

    if test_score < 0 or test_score > 100:
        result = invalid_message
    else:
        result = test_name + ": " + str(test_score)
    # return{test_name: test_score}
    return result


if __name__ == '__main__':
    name = input("What is the test name")
    result = "Invalid test score, try again!"
    while result == "Invalid test score, try again!":
        number = input("What is the score")
        result = score_input(name, number)
        print(result)
