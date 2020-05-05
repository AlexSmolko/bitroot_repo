big_list = list(range(1, 101))
indx = 1
list_deployment = []

while indx in range(len(big_list)):
    item = big_list[indx]
    indx += 1
    if item % 7 == 0 and item % 5 != 0:
        list_deployment.append(item)
print(list_deployment)

