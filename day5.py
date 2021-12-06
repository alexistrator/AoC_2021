from day1 import read_one_value_lines

values = read_one_value_lines('ressources/day5.txt')

def vertical_lines(values):
    vertical = []
    for value in values:
        tuples = []
        single_vs = value.split(' -> ')
        for sv in single_vs:
            coords = sv.split(',')
            tuples.append(tuple(coords))
        #if tuples[0][0] == tuples[1][0] or tuples[0][1] == tuples[1][1]:
        vertical.append(tuples)
    return vertical

def playing_field():
    field = []
    for i in range(1000):
        row = []
        for i in range(1000):
            row.append(0)
        field.append(row)
    return field

def count_overlapping(field, vertical_lines):
    for line in vertical_lines:
        max_y = 0
        min_y = 0
        max_x = 0
        min_x = 0
        if int(line[0][0]) <= int(line[1][0]):
            max_x = line[1][0]
            min_x = line[0][0]
            direct_x = 1
        else:
            max_x = line[0][0]
            min_x = line[1][0]
            direct_x = -1
        if int(line[0][1]) <= int(line[1][1]):
            max_y = line[1][1]
            min_y = line[0][1]
            direct_y = 1
        else:
            max_y = line[0][1]
            min_y = line[1][1]
            direct_y = -1


        # THERE ARE ASTRONOMICAL AMOUNTS OF REFACTORING TO DO AROUND HERE
        # - REMOVE UNGODLY AMOUNT OF CODE REPLICATION
        # - DIRECTION CAN DIRECTLY BE IMPLEMENTED BY MULTIPLYING IT INSTEAD
        #   OF DOING ALL THOSE IF-STATEMENTS
        #vertical lines
        if int(line[0][0]) == int(line[1][0]):
            #print('0')
            for i in range(int(min_y), int(max_y) + 1):
                field[int(line[1][0])][i] += 1
        # horizontal lines
        elif int(line[0][1]) == int(line[1][1]):
            #print('1')
            for i in range(int(min_x), int(max_x) + 1):
                field[i][int(line[1][1])] += 1
        # diagonal lines
        else:
            if direct_x == 1:
                y_counter = 0
                for i in range(int(min_x), int(max_x) + 1):
                    if direct_y == 1:
                        field[i][int(min_y) + y_counter] += 1
                        y_counter += 1                       
                    else:
                        field[i][int(max_y) + y_counter] += 1
                        y_counter -= 1
            else:
                y_counter = 0
                for i in range(int(max_x), int(min_x)-1, -1):
                    if direct_y == 1:
                        field[i][int(min_y) + y_counter] += 1
                        y_counter += 1
                    else:
                        field[i][int(max_y) + y_counter] += 1
                        y_counter -= 1 
    counter = 0
    for row in field:
        for element in row:
            if element > 1:
                counter += 1
    return counter 

def main():
    field = playing_field()
    verticals = vertical_lines(values)
    overlaps = count_overlapping(field, verticals)
    print(overlaps)

main()
