import random

r_list = list(range(1, 101))
rand_list = random.choices(r_list, k = 10)

indx = 0
maximum_value = 0

while indx in range(0, len(rand_list)):
    item = rand_list[indx]
    if item > maximum_value:
        maximum_value = item
    indx += 1
    #print(f'Printed list of random values: {rand_list}\n', end="\n")
    # print(f'Printed current item which compares with maximum and if it greater, then becomes maximum: {item}\n', end='\n')
    # print(f'Current Maximum value: {maximum_value}\n')
print(f'Printed list of random values: {rand_list}\n', end="\n")
print(f'\t\t\tFinally maximum value: {maximum_value}')






