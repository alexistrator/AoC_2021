from day1 import read_one_value_lines

values = read_one_value_lines('ressources/day2.txt')
split_value = ["",0]
aim, depth, horizontal = 0,0,0

def aim_down(change:int):
    global aim
    aim += change

def aim_up(change:int):
    global aim
    aim -= change

def go_forward(change:int):
    global horizontal, aim, depth
    horizontal += change
    depth += (aim * change)

commands = {
            'down' : aim_down,
            'up' : aim_up,
            'forward' : go_forward
            }

for value in values:
    split_value = value.split()
    commands[split_value[0]](int(split_value[1]))

print('Final Position mult.: ' + str(depth*horizontal))
