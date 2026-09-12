"""

"""
from num2words import num2words

d1 = {
    "jay": [1, 2, 3, 4, 5]
}
print(d1)
# print(type(d1))

d1["jay"].append(6)
print(d1["jay"])
print(d1)

# new_dict=dict((key for key in range(1,11)),[val for val in range(1,11)])
# new_dict=dict((key,val for key,val in range(1,11)))
# print(new_dict)

# result = {
#     number: alphabet
#     for number, alphabet in zip([number for number  in range(1,11)], [alphabet for alphabet in "ABCDEFGHIJ"])
# }
#
# print(result)

# numbers_to_words = {
#     numbers: words
#     for numbers, words in zip([numbers for numbers in range(1, 11)], [num2words(numbers).capitalize() for numbers in range(1, 11)])
# }

# numbers_to_words = {
#     numbers: words
#     for numbers, words in zip(range(1,11), [num2words(numbers).capitalize() for numbers in range(1, 11)])
# }

numbers_to_words = {
    numbers: num2words(numbers).capitalize()
    for numbers in range(1, 11)
}

print(numbers_to_words)
# print(numbers_to_words)

list1 = [number for number in range(1, 11)]
list2 = list(range(1, 11))

print(list1)
print(list2)
num1, num2 = int(input("Enter Num1 : ")), int(input("Enter Num2 : "))
add = lambda no1, no2: no1 + no2  # Not allowed (no1:=int(input(""))) + (no2:=int(input("")))
print(f"tThe addition of the {num1} and {num2} = {add(num1, num2)}")

# add = lambda no1, no2: (int(input(""))) + (int(input("")))
# print(f"tThe addition of the number= {add(1,2)}")
