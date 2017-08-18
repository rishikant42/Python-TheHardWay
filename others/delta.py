raw_input = [
    ["Pakistan", 23],
    ["Pakistan", 127],
    ["India", 3],
    ["India", 71],
    ["Australia", 31],
    ["India", 22],
    ["Pakistan", 81]
]


def convert_to_dict(input):
    result = {}
    for item in input:
        if item[0] in result:
            result[item[0]].append(item[1])
        else:
            result[item[0]] = [item[1]]
    return result


def calculate_avg(input):
    result = {}
    for key in input:
        result[key] = sum(input[key]) / float(len(input[key]))
    return result


def get_key_with_max_value(input):
    res = input.keys()[0]
    for key in input:
        if input[key] > input[res]:
            res = input[key]
    return res


def highest_avg(str):
    dict_data = convert_to_dict(str)
    avg_data = calculate_avg(dict_data)
    get_key = get_key_with_max_value(avg_data)
    return get_key


print highest_avg(raw_input)

############################ TEST ##########################
#
# $ python code.py
# Pakistan
#
############################################################

######################### Running Time #####################
# convert_to_dict() is of O(n)
# calculate_avg() is of O(n^2)
# get_key_with_max_value() is of O(n)
#
# Total running time is of O(n^2)
