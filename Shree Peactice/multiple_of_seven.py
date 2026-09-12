"""
WAP to check if a number is a multiple of 7 or not.
"""

num = int(input("Enter the number : "))  # get one integer input from the user

if num % 7 == 0:
    print(f"The {num} is multiple of seven or 7...")
else:
    print(f"The {num} is not a multiple of the seven or 7...")

