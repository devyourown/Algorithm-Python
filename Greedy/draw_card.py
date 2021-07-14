row, col = map(int, input().split())

card_board = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    card_board[i] = list(map(int, input().split()))
    card_board[i].sort()

which_column = 0
for i in range(1, row):
    if(card_board[which_column][0] < card_board[i][0]):
        which_column = i

print(card_board[which_column][0])
