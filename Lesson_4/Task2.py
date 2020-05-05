import random

indx = 0
f_list = list(range(1, 10))
s_list = list(range(1, 10))
var_list1 = random.choices(f_list, k=10)
var_list2 = random.choices(s_list, k=10)
var_list3 = []

while indx < 10:
    indx += 1

indx = 0
while indx in range(0, 10):
    item1 = var_list1[indx]
    item2 = var_list2[indx]
    indx += 1
    if item1 in var_list2:
        var_list3.append(item1)
    print(f'Third list:{list(set(var_list3))}')

print(f'First{var_list1}')
print()
print(f'Second{var_list2}')
