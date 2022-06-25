my_list = [[1, 2], [3], [4, 5, 6], [7]]

flat_list = [x for temp in my_list for x in temp]

print(flat_list)


flat_list = []

for temp in my_list:
    for x in temp:
        flat_list.append(x)

print(flat_list)
