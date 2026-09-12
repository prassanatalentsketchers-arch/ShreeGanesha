"""
This is demo program to print entered number is even or odd using teh function...
"""


# import sys


# Here we are writing the function to get the valid integer from the user.
def get_valid_integer(prompt: str) -> int:
    """
    This function takes one valid integer as an input from the user and return that valid integer...

    Parameters:
                prompt (str): Message for the input methods display statement

    Returns:
            int: Valid integer
    """

    while True:
        try:
            number = int(input(prompt))
            return number  # Returning the valid integer
        except ValueError as e:
            print(f"Error : {e}")
            print(f"Choice must be the type <class 'int'>")


# Here we are writing the function for finding the given number is 'Even' or 'Odd'.
def find_even_or_odd(number: int) -> str:
    """
    This function finds the entered number is even or odd.
    :param number: int - The entered number.
    :return: str - The entered number is even or odd.
    """
    return "Even" if number % 2 == 0 else "Odd"  # Here we are using single line if-else statement


# Here we define custom user defined exception for the InvalidChoice.
class InvalidChoice(Exception):  # Custom user defined or generated exception
    """
    This is raised when an invalid choice is given.
    """
    # pass


# Here we are making the function to display the dictionary items in proper formate.
def display_dictionary_items(dictionary: dict[int, str]) -> None:
    """
    This function displays all the items in the dictionary.
    :param dictionary: dict - The dictionary to be displayed.
    :return: None - It returns nothing.
    """
    print("\nList of the options : ")
    for key, value in dictionary.items():
        print(f"\t{key}:{value} ")
    # print()


# main() method when we want to run the particulate block of the code.
def main() -> None:
    """
    This is the main function that runs when the program is executed.
    :return: None - It returns nothing
    """
    options = {
        1: "Find the Even or ODD Number.",
        2: "Exit the Program."
    }
    print(f"\n{"*" * 25} Shree Ganesha {"*" * 25}\n")
    while True:
        try:
            display_dictionary_items(options)  # Calling the display_dictiona_items()
            # choice = int(input("\nPlease enter your choice : "))
            choice = get_valid_integer("\nPlease enter your choice : ")
            """
            Here we are writing the logic to get the one valid integer value
            & find its type even otr odd 
            """
            match choice:
                case 1:
                    print("*#*" * 30)
                    print(f"\nNow we are in first case...")
                    number = get_valid_integer("\n\tEnter any integer value : ")
                    print(f"\n\tThe entered integer {number} is {find_even_or_odd(number)} number.\n")
                    print("*#*" * 30)
                case 2:
                    print("*#*" * 30)
                    print(f"\nNow we are in second case...\nGood Buy we are exiting the code...")
                    print("*#*" * 30)
                    # sys.exit(0)
                    return
                case _:
                    print(f"Invalid Choice.")
                    raise InvalidChoice(f"Invalid Choice. Please choose from options.")

        # except ValueError as e:
        #     """
        #     Here we are handle the ValueError.
        #     """
        #     print(f"Error : {e}")
        #     print(f"Choice must be the type <class 'int'>"
        #           f"\nPlease enter the valid integer choice...")

        except InvalidChoice as e:
            """
            Here we are handle the InvalidChoiceError. 
            """
            print(f"Error : {e} ")
        # except Exception as e:
        #     """
        #     Here we are handle the exception.
        #     """
        #     print(f"Error : {e}")


# This block is call only when we directly run the module.
if __name__ == "__main__":
    """
    This block only runs when we are run the specific particular module. 
    """
    main()  # Here we are calling the main function
