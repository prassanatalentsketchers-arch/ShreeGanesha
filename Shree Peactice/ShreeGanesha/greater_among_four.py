"""
WAP to find the greatest no umang 4 numbers
"""


def get_valid_integer(position_message: str) -> int:
    """
    This method get the valid integer value as input from the user and return that value.

    :param position_message: (str) position of the number
    :return: int : it returns valid integer
    """
    while True:
        try:
            number = int(input(position_message))
            return number
        except ValueError as e:
            print("Error : ", e)
            print("Please enter a valid integer.")


if __name__ == "__main__":
    num1 = get_valid_integer("Enter the first no: ")
    num2 = get_valid_integer("Enter the second no: ")
    num3 = get_valid_integer("Enter the third no: ")
    num4 = get_valid_integer("Enter the fourth no: ")

    # greater_no1, greater_no2 = max(num1,num2),max(num3,num4) # gno=max(num1,num2,num3,num4)
    greater_no1, greater_no2 = 0, 0
    if num1 >= num2:
        greater_no1 = num1
    else:
        greater_no1 = num2

    if num3 >= num4:
        greater_no2 = num3
    else:
        greater_no2 = num4

    if greater_no1 >= greater_no2:
        print("The greatest number is ", greater_no1)
    else:
        print("The greatest number is ", greater_no2)
