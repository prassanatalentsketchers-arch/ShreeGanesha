"""
This module demonstrates two different approaches to calculate the sum
of numbers from a given number down to 1.

The first approach uses function recursion, while the second approach
uses Python's built-in range() and sum() functions.
"""


def sum_from_n_to_1(number_: int, total: int = 0) -> int:
    """
    Recursively calculates the sum of all numbers from number_ down to 1.

    :param number_: The starting number from which the summation begins.
    :param total: The current accumulated total.
    :return: The sum of all numbers from number_ down to 1.
    """
    if number_ == 0:
        return total

    total += number_
    return sum_from_n_to_1(number_ - 1, total)


no = int(input("Enter any number: "))

print(
    f"\nImplemented using function recursion"
    f"\nThe sum of the numbers from {no} to 1 is {sum_from_n_to_1(no)}"
)

print(
    f"\nImplemented using range() and sum()"
    f"\nThe sum of the numbers from {no} to 1 is {sum(range(1, no + 1))}"
)
