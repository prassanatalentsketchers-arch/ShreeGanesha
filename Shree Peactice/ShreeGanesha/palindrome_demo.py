"""

"""

l1 = [1, 2, 1]
l2 = l1.copy()
l2.reverse()
if l1 == l2:
    print(f"The lists {l1} and {l2} are palindrome")
else:
    print(f"The lists {l1} and {l2} are not palindrome")

l3 = [int(input(f"Enter the {i} th index & {i+1} position's ele of list l3 : ")) for i in range(5)]
print(l3)
