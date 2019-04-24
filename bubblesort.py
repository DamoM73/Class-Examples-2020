def bubbleSort(values):
    num = len(values)

    pass_num = 0
    while pass_num < num:
        pointer = 0
        while pointer < num - 1 - pass_num:
            if values[pointer] > values[pointer +1]:
                values[pointer], values[pointer + 1] = values[pointer + 1], values[pointer]
            pointer += 1
        pass_num += 1
    return(values)

example_list = [19,10,8,17,9]
sorted_list = bubbleSort(example_list)
print(sorted_list)