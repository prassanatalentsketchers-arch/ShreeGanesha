"""In the module we are finding teh second largest no form the list """

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("New Logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

file_handler = logging.FileHandler("second_largest_no.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# logger.addHandler(file_handler)
logger.addHandler(file_handler)

input_list = [int(input("Enter the no : ")) for x in range(0, 5)]

no_of_iteration = len(input_list)
first_greater_no = input_list[0]
# second_greater_no = int | None
second_greater_no = 0
for i in range(1, no_of_iteration):
    if first_greater_no == input_list[i]:
        continue
    else:
        second_greater_no = input_list[i]

for i in range(1, no_of_iteration):

    if first_greater_no < input_list[i]:
        first_greater_no = input_list[i]
    elif first_greater_no == input_list[i]:
        continue

ind_of_first_gn = input_list.index(first_greater_no)
logger.info("First Greater No : %d located on the index no %d ", first_greater_no, ind_of_first_gn)
print(f"The largest no is : {first_greater_no} on the index no {ind_of_first_gn} ")

temp = input_list[0]
input_list[0] = input_list[ind_of_first_gn]
input_list[ind_of_first_gn] = temp

for j in range(1, no_of_iteration):
    if j == ind_of_first_gn or first_greater_no == input_list[j]:
        continue
    if second_greater_no < first_greater_no and second_greater_no < input_list[j]:
        second_greater_no = input_list[j]
    elif second_greater_no == input_list[j]:
        continue

ind_of_second_gn = input_list.index(second_greater_no)
logger.info("Second Greater No : %d ", second_greater_no)
print(f"The second largest No is : {second_greater_no} on the index no {ind_of_second_gn} ")
