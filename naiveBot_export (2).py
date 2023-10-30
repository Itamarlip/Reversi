# Example reversi bot.

# A function to return your next move.
# 'board' is a 8x8 int array, with 0 being an empty cell and 1,2 being you and the opponent,
# determained by the input 'me'.
def get_move(me : int, board : list[list[int]]) -> tuple[int,int]:
    for i in range(8): 
        for j in range(8): 
            if valid_move(i, j, me, board):
                return i, j 
    
    # if there is no valid move, the bot will never be called in the first place. For safety, we return an invalid result.
    return -1, -1


def valid_move(i, j, me, board):
    if board[i][j] != 0:
        return False

    for x in range(max(0, i - 1), min(7,i + 1)):
        for y in range(max(0, j - 1), min(7,j + 1)):
            if x == i and y == j:
                continue

            if board[x][y] == 3 - me:
                k = x - i
                l = y - j
                n = 1
                while 0<= i + n * k <8 and 0<= j + n * l <8:
                    if board[i + n * k, j + n * l] == me:
                        return True
                    n += 1
    return False

lst=[[0 for i in range(8)] for j in range(8)]
lst[4][4] = 1
lst[4][5] = 2
lst[5][4] = 2
lst[5][5] = 1

print(valid_move(5,3,1,lst))
