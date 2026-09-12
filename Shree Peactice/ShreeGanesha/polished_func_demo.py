"""
This module demonstrates how to determine whether a number is even or odd.

It also demonstrates user input validation, exception handling,
a custom exception, dictionary-based menu options, and pattern matching.
"""


def get_valid_integer(prompt: str) -> int:
    """
    Get a valid integer from the user.

    :param prompt: The message displayed when requesting input.
    :return: A valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def find_even_or_odd(number: int) -> str:
    """
    Determine whether the given number is even or odd.

    :param number: The number to check.
    :return: "Even" if the number is even; otherwise, "Odd".
    """
    return "Even" if number % 2 == 0 else "Odd"


class InvalidChoice(Exception):
    """Raised when the user selects an invalid menu option."""


def display_dictionary_items(dictionary: dict[int, str]) -> None:
    """
    Display all menu options stored in the dictionary.

    :param dictionary: A dictionary containing menu options.
    """
    print("\nList of options:")
    for key, value in dictionary.items():
        print(f"\t{key}: {value}")


def main() -> None:
    """
    Run the main menu and handle user selections.
    """
    options = {
        1: "Find the Even or Odd Number.",
        2: "Exit the Program."
    }

    print(f"\n{'*' * 25} Shree Ganesha {'*' * 25}\n")

    while True:
        try:
            display_dictionary_items(options)
            choice = get_valid_integer("\nPlease enter your choice: ")

            match choice:
                case 1:
                    print("*#*" * 30)
                    number = get_valid_integer("\n\tEnter any integer value: ")
                    result = find_even_or_odd(number)
                    print(f"\n\tThe entered number {number} is {result}.\n")
                    print("*#*" * 30)

                case 2:
                    print("*#*" * 30)
                    print("\nGoodbye! The program is exiting.")
                    print("*#*" * 30)
                    return

                case _:
                    raise InvalidChoice(
                        "Invalid choice. Please choose from the available options."
                    )

        except InvalidChoice as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
