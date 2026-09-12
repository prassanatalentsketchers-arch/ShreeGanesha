# from email import generator

For = 10
_for = "ram"
print("Hi")
if 19 >= 18: print("hi")
# else: print("hi")

# if
# no_type="Even" if (no:=int(input("Enter any no : "))) % 2 == 0 else "odd"

# no = int(input("Enter any no : "))
# print(f"The entered {no} is type of the {"Even" if no % 2 == 0 else "odd"} number... ")
# print(f"The entered is type of the {"Even" if (no1 := int(input("Enter any no : "))) % 2 == 0 else "odd"} number... ")

l = [1, 2, 3, 4, 5]
i = iter(l)
ele = next(i)
for ele in i:
    print(ele)

print(f"{type(i), type(ele)}")

table = [lambda x: 2 * x for x in range(1, 11)]
val = iter(table)
for i in range(1, len(table)):
    print(f"{next(val)}")

l = [2 * x for x in range(1, 11)]
print(l)


def gen():
    pass


even_2_to_100 = [x for x in range(1, 100) if x % 2 == 0]
print(even_2_to_100, sep="\n")


var = [2,4,6,8,10,12,14,16,18,20]
