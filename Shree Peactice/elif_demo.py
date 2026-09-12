"""
Demo program on the elif conditional statement...
"""


def get_valid_percentage() -> float:
    """
    This function returns the valid percentage...
    :return: float: the valid percentage
    """

    while True:  # this loop will iterate till we got valid percentage as input
        try:
            percentage = float(input("\nEnter the percentage : "))
            if 0 <= percentage <= 100:  # if percentage >= 90 and percentage <= 100
                return percentage  # Here we got percentage entered are valid so we can return that validated percentage...
            print("Please enter a percentage between 0 and 100")

        except ValueError as e:
            print("Error : ", e)
            print("\nPlease enter the valid percentage...")

        # except Exception as e:
        #     print("Error : ",e)


final_percentage = get_valid_percentage()

# if 90 <= final_percentage <= 100:
#     print("The student got the A Garde")
# elif 80 <= final_percentage <= 89:
#     print("The student got the B Grade")
# elif 70 <= final_percentage <= 79:
#     print("The student got the C Grade")
# elif 60 <= final_percentage <= 69:
#     print("The student got the D Grade")
# else:
#     print("The student got the E Grade")

if final_percentage >= 90:
    print("The student got the A Grade")
elif final_percentage >= 80:
    print("The student got the B Grade")
elif final_percentage >= 70:
    print("The student got the C Grade")
elif final_percentage >= 60:
    print("The student got the D Grade")
else:
    print("The student got the E Grade")
