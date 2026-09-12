"""
Split the entered string using user defined function...
"""

str1 = input("Enter the string which you want to process : ")

if str1:
    print(f"The entered string is : \"{str1}\" \n")

    split_char = input("Enter the delimiter or the seperator : ")
    if split_char:
        print(f"The delimiter is : '{split_char}'\n")
        print(f"Length of the \"{str1}\" is {len(str1)}\n")
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

        print(f"The split string is : {split_str}\n")

        print("Split words of the the string : \n")
        for words in split_str:
            print(words)

    else:
        print("We must required the delimiter or seperator for splitting operation..")

else:
    "Can not perform the split operation on the empty string..."
