import csv

def read_one_value_lines(path:str):
    with open(path) as values_file:
        values = list(value.rstrip() for value in values_file)
        return values

def return_nbr_inc_depth():
    depths = read_one_value_lines('ressources/day1a.txt')
    prev_depth = 0
    depth_counter = 0

    for depth in depths:
        if int(depth) > int(prev_depth) and prev_depth != 0:
            depth_counter += 1

        prev_depth = depth

    return depth_counter


def return_nbr_inc_rollingW():
    depths = read_one_value_lines('ressources/day1a.txt')
    prev_sum_depths = 0
    depth_counter = 0

    for i in range(len(depths)-1):
        temp_sum=0
        for j in range(3):
            if (i+j) < len(depths):
                temp_sum += int(depths[i + j])
        
        if temp_sum > prev_sum_depths and prev_sum_depths != 0:   
            depth_counter += 1 
        
        prev_sum_depths = temp_sum

    return depth_counter
        
print(len(read_one_value_lines('ressources/day1a.txt')))
print('Task 1a: ' + str(return_nbr_inc_depth()))
print('Task 1b: ' + str(return_nbr_inc_rollingW()))


