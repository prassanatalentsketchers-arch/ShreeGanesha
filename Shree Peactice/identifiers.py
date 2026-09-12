"""
This module contains the content about pythons concept like function,typehints,docstrings,etc.
also we are using the methods:
1.help()
2.input()
3.print()

and one user defined method:
1.add_two_integers(int_num1, int_num2)

"""
help(print)


def add_two_integers(int_num1: int, int_num2: int) -> int:
    """
    This method takes two integers as an input and returns the sum of that two integers...
    
    Parameters:
    int_num1 (int): First Integer.
    int_num2 (int): Second Integer.

    Returns:
    int:The sum of the int_num1 and int_num2

    """
    return int_num1 + int_num2


try:
    print(f"The addition of the {(num1 := int(input("Enter the first no : ")))} + "
          f"{(num2 := int(input("Enter the second no : ")))} = {add_two_integers(num1, num2)}")

except ValueError as e:
    print(f"Error: {e}")

help(add_two_integers)
print(f"The docstring of the {add_two_integers.__name__} is :\n  {add_two_integers.__doc__} ")

# try:
#     pass
# finally:
#     pass

