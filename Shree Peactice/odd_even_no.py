"""
WAP to check if number entered by the user is odd or even.
"""

num = int(input("Enter the number: "))  # Taking integer numbers as an input from the user

# check num is even or odd
if num % 2 == 0:  # print("The ",num," is even") if num%2==0 else print("The ",num," is odd number")
    print("The", num, " is even number")
else:
    print("The", num, "is odd number")
