from day1 import read_one_value_lines

values = read_one_value_lines('ressources/day4.txt')
bingo_nbrs = [value for value in values[0].split(',')]
bingo_boards_raw = [values[i] for i in range(1, len(values)-1) if values[i].strip() != ""]
bingo_boards = []

# i could just have regexed instead of breaking everything and putting it back
# together afterwards
for i in range(0,len(bingo_boards_raw)-6, 5): #-1 bcz length, -5 bcz inner for loop
    single_board = []
    for row in range(5):
        single_board.append([])
        for value in bingo_boards_raw[i+row].split(' '):
            if value != '':
                single_board[row].append((value, False))
    bingo_boards.append(single_board)

winners_in_order = []
board_and_nbr = {}

def update_rows(board, nbr, index):
    if index not in winners_in_order:
        for row in board:
            if (nbr, False) in row:
                row[row.index((nbr, False))] = (nbr, True)
            bingo = True
            for position in row:
                if position[1] == False:
                    bingo = position[1]
            if bingo:
                winners_in_order.append(index)
                board_and_nbr[index]=nbr
    return

def update_cols(board, nbr, index):
    if index not in winners_in_order:
        columns = []
        for col in range(5):
            column = []
            for row in board:
                column.append(row[col])
            columns.append(column)
        update_rows(columns, nbr, index)
    return

for nbr in bingo_nbrs:
    for board in bingo_boards:
        update_rows(board, nbr, bingo_boards.index(board))
        update_cols(board, nbr, bingo_boards.index(board))

sum = 0

for row in bingo_boards[winners_in_order[0]]:
    for element in row:
        if element[1] == False:
            sum += int(element[0])
winner_nbr = board_and_nbr[winners_in_order[0]]
print('result: ' + str(int(sum)*int(winner_nbr)))

sum_looser = 0
looser_nbr = board_and_nbr[winners_in_order[-1]]

for row in bingo_boards[winners_in_order[-1]]:
    for element in row:
        if element[1] == False:
            sum_looser += int(element[0])
print('result: ' + str(int(sum_looser)*int(looser_nbr)))
