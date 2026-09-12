"""
Here we are doing practice off indexing and slicing ,negative indexing with builtin data type list[]
"""
# from ShreeGanesha import greater_among_four as g4
# d=g4.get_valid_integer("f")
from ShreeGanesha.greater_among_four import get_valid_integer as g4
demo = [1, 2, 3, 4, 5]

print(demo[::])  # demo[start=0:end=len(demo):step=1] o/p [1,2,3,4,5]

print(demo[-5:5:1])  # demo[start=-5:end=5:step=1] o/p [1,2,3,4,5]

print(demo[-1:-5:-1])  # demo[strart=-1:end=-5:step=-1] o/p [5,4,3,2] here we are reversing
# the list's elements

print(isinstance(5, int))

print(f"The length of the demo = {len(demo)} and it's type is {type(demo)} ")
# print(demo.__name__)

# print(f"{g4.get_valid_integer("Enter the First Number : ")}")
print(f"{g4("Enter the First Number : ")}")

list2=[1,2,3]
l1=[]
print(len(l1))
print(bool(l1))

print(type(l1))
typ=isinstance(2,int)