"""
Python Assignment 9/16/23

Written by Coray Bennett
"""

def problem_1():
    """
    Given the following list 'num_values',
    print every even number in the list 
    """

    # DO NOT EDIT THIS CODE vvvvv
    num_values = [1, 2, 3, 4, 5, 7, 8, 9]

    # YOUR CODE HERE vvvvv

def problem_2(num_values: list[int]):
    """
    Given the 'num_values' list as a parameter,
    print every even number in the list
    (see main() for test cases)
    """

    # YOUR CODE HERE vvvvv

def problem_3(password: str):
    """
    Given the 'password' string as a parameter,
    *return* one of the following values:
    "WEAK" if the password is weak (conains less than 6 characters OR contains no numbers),
    "NORMAL" if the password is normal (contains between 6-10 characters AND at least one number),
    "STRONG" if the password is strong (contains more than 10 characters AND at least one number)
    """

    #YOUR CODE HERE vvvvv

    return ""


def main():

    print("PROBLEM 1: ")
    problem_1()

    print("\nPROBLEM 2: ")
    problem_2([2, 2, 2, 4, 5, 9, 12034])
    
    #uncomment the lines below for more test cases for problem 2:
    #problem_2([1, 1, 1, 1, 1])
    #problem_2([1, 1, 1, 1, 1, 2])
    #problem_2([9, 0, -2, 33, 44, 55])

    print("\nPROBLEM 3: (should state the strength of the password at the end of each line) ")
    print("password 'password' is ", problem_3("password"))
    print("password 'check1' is ", problem_3("check1"))
    print("password 'WrngNumb3r' is ", problem_3("WrngNumb3r"))
    print("password 'VeryVeryStr0ngPassWord' is ", problem_3("VeryVeryStr0ngPassWord"))

if __name__ == "__main__":
    main()


