from day1 import read_one_value_lines

values = read_one_value_lines('ressources/day2.txt')
split_value = ["",0]
depth, horizontal = 0,0

def go_down(change:int):
    global depth
    depth += change

def go_up(change:int):
    global depth
    depth -= change

def go_forward(change:int):
    global horizontal
    horizontal += change

commands = {
            'down' : go_down,
            'up' : go_up,
            'forward' : go_forward
            }

for value in values:
    split_value = value.split()
    commands[split_value[0]](int(split_value[1]))

print('Final Position mult.: ' + str(depth*horizontal))
