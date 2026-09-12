"""
WAP to find the greatest of 3 numbers entered by the user.
"""


def get_valid_integer(position: str) -> int:
    """
    This function returns the valid integer inputted by the user :

    Parameters:
          position (str): Position of the number (Ex.First,Second,Third,etc.).

    Returns:
         int: Valid integer inputted by the user.
    """
    while True:
        try:
            number = int(input("Please enter the " + position + " number: "))
            # if isinstance(number, int):  # isinstance(obj,data_type) -> boolean value
            return number  # returning the valid integer
        except ValueError as e:
            print("Error : ", e)
            print("Please enter a valid input...")


num1 = get_valid_integer("First")
num2 = get_valid_integer("Second")
num3 = get_valid_integer("Third")

# Method Number 1
if num1 >= num2:
    if num1 >= num3:
        print("The greatest number is ", num1)
    else:
        print("The greatest number is ", num3)

else:
    if num2 >= num3:
        print("The greatest number is ", num2)
    else:
        print("The greatest number is ", num3)

# Method no 2:

# num_type=("Odd","Even")[num1%2==0]

if num2 <= num1 >= num3:
    print("The greatest number is ", num1)
elif num1 <= num2 >= num3:
    print("The greatest number is ", num2)
else:
    print("The greatest number is ", num3)

# Method no 3:
if num1 >= num2 and num1 >= num3:
    print("The greatest number is ", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is ", num2)
else:
    print("The greatest number is ", num3)

# Method No 4:
print("The greatest number is ", max(num1, num2, num3))  # it returns biggest values among 3

# Method No 5:
if num1 >= num2 and num1 >= num3:
    print("The greatest number is ", num1)

elif num2 >= num3:
    print("The greatest number is ", num2)
else:
    print("The greatest number is ", num3)
