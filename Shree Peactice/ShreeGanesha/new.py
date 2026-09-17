"""
Split the entered string using user defined function...
"""

from func_demo import get_valid_integer as get_integer, InvalidChoice


def my_won_split(str1: str, split_char: str = " ") -> list[str]:
    """
     User defined split function
    :param str1: str - The string to be split
    :param split_char: str - The delimiter or the seperator to be split
    :return: list[str] -  The list of the split string
    """
    split_str, word = [], ""
    i = 0

    while i < len(str1):
        # print("\n", "*#*" * 50, "\n")
        # print(f"while loops iteration no : {i} start")
        if str1[i] != split_char:
            word += str1[i]
        elif str1[i] == split_char and i != 0:
            if word:
                split_str.append(word)
                word = ""

        if i == len(str1) - 1:
            if word:
                split_str.append(word)
        # print(f"while loop {i} iteration in end")
        # print("\n", "*#*" * 50, "\n")
        i += 1

        # print(f"The split string is : {split_str}\n")
        #
        # print("Split words of the the string : \n")
        # for words in split_str:
        #     print(words)
    return split_str

    # else:
    #     print("We must be required the delimiter or seperator for splitting operation.")


def get_valid_string(prompt: str) -> str:
    """
    Function to get the valid string from the user
    :param prompt: str - The message displayed on the users screen
    :return: str - The valid string contains at list one element in it.
    """
    # print(f"The entered string is : \"{str1}\" \n")
    #
    # # split_char = input("Enter the delimiter or the seperator : ")
    # # if split_char:
    # print(f"The delimiter is : '{split_char}'\n")
    # print(f"Length of the \"{str1}\" is {len(str1)}\n")
    while True:
        try:
            if str1 := input(prompt):
                return str1
            else:
                raise EmptyString("Please enter a valid string...")
        except EmptyString as e:
            print(f"Error : {e}")
            print("You entered the empty string...")


class EmptyString(Exception):
    """
    Exception raised for empty strings
    """


# class EmptySplitChar(Exception):
#     """
#     Exception raised for empty split_char
#     """

def display_dictionary_items(dictionary1: dict[int, str]) -> None:
    print("The list of options : ")
    for key, val in dictionary1.items():
        print(f"\t{key}: {val}")
    print("\n")


def formatted_line(formate: int = -1) -> str:
    """
    This returns a special formated string of the symbols or special characters.
    :param formate: int - Format number which user want to use.
    :return: str - The formatted string
    """
    match formate:
        case 1:
            return f"\n{"***" * 30}\n"
        case 2:
            return f"\n{"*#*" * 30}\n"
        case _:
            return f"\n{"+#+" * 30}\n"


def get_input(case_number: int, choice: int = 0) -> tuple[str, str]:
    """
    Function to get the input
    :param case_number: int - The case number
    :param choice: int - Choice of the case

    :return: tuple[str, str] -
    """
    print(f"Now you are in the Case No {case_number} : \n")
    string1 = get_valid_string("Please enter the string : ")
    print(f"The entered string is : \"{string1}\" \n")
    split_char = " "
    if not choice:
        split_char = get_valid_string("Please enter the 'Separator' / 'Delimiter' / 'split char' : ")
        print(f"The delimiter is : '{split_char}'\n")

    # return string1,split_char if choice == 0 else string1
    # return [string1,split_char] if choice == 0 else [string1,]
    return string1, split_char


def display_output(split_strings: list[str]) -> None:
    """
    Function to display the output of the split strings.
    :param split_strings: list[str] - The list of the split strings
    """
    print(f"The separated or split  string : {split_strings}")
    for words in split_strings:
        print(f'"{words}"')


def main() -> None:
    list_of_choice = {
        1: "Want to perform split operation with own delimiter or separator.",
        2: "Want to perform split operation with default delimiter or seperator.",
        3: "Exit the code or program."
    }
    print(formatted_line(1))
    print(" " * 35, "|| Shree Ganesha ||", "\t")
    print(formatted_line(1))
    while True:
        try:
            display_dictionary_items(list_of_choice)
            choice = get_integer("Enter the choice : ")
            match choice:
                case 1:
                    print(formatted_line(2))
                    # print("Now you are in the Case First : \n")
                    string1, split_char = get_input(case_number=choice)
                    display_output(my_won_split(string1, split_char))
                    print(formatted_line(2))

                case 2:
                    print(formatted_line(2))
                    # print("Now you are in the Case Second : \n")
                    string1, split_char = get_input(case_number=choice, choice=1)
                    display_output(my_won_split(string1, split_char))
                    print(formatted_line(2))
                case 3:
                    print(formatted_line(2))
                    print("Now you are in the Case Third : \n")
                    print("\n Goodbye! We are Stop Here...")
                    print(formatted_line(2))
                    return
                case _:
                    raise InvalidChoice("Please enter a valid choice.")

        except InvalidChoice as e:
            print(f"Error : {e}")


if __name__ == "__main__":
    main()
