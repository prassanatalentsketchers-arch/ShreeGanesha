str1 = input("Enter the string which you want to process : ")

print(f"The entered string is : \"{str1}\" \n")

# split_string = list(str1.split(" "))

# print(f"The string after split : {split_string}")
#
# # print(split_string)
#
# print("The all the split strings :  \n")
# for strs in split_string:
#     print(strs)

split_char = input("Enter the delimiter or the seperator : ")

print(f"The delimiter is : '{split_char}'\n")
print(f"Length of the {str1} is {len(str1)}\n")
split_str, word = [], ""

"""

"""
# for i in range(0,len(str1)):
i = 0
while i < len(str1):
    print(f"while loops iteration no : {i} start")
    if str1[i] != split_char:
        word += str1[i]
        # i+=1
    if str1[i] == split_char:
        split_str.append(word)
        word = ""
        # i+=1
    if i == len(str1) - 1:
        split_str.append(word)
    print(f"while loop {i} iteration in end")
    i += 1

print(f"The split string is : {split_str}\n")
print("")
for words in split_str:
    print(words)


# for char in str1:
#     word=[]
#     if char == split_char:
#         word.append(char)

# def my_won_split(str1: str, split_char: str) -> list[str]:
#     """
#
#     :param str1: str - The string to be split
#     :param split_char: str - The delimiter or the seperator to be split
#     :return: list[str] -  The list of the split string
#     """

