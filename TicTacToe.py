import random

board = [' ' for x in range(10)]

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def place_marker(board, marker, position):
    board[position] = marker

def space_check(board, position):
    return board[position] == ' '

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def player_move():
    run =  True
    while run:
        move = input('Please, select a possition to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_check(board, move):
                    run = False
                    place_marker(board, 'X', move)
                else:
                    print('Sorry, this place is occupied.')
            else:
                print('Please, enter a number within the range (1-9).')
        except:
            print('Please type a number!')

def comp_move():
    # list of possible moves
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # Checking for possible moves to make, either block or take best possible possition
    for let in ['O','X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if win_check(board_copy, let):
                move = i
                return move
    
    # Try taking one of the corners
    open_conners = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            open_conners.append(i)
    if len(open_conners) > 0:
        move = select_random(open_conners)
        return move

    # Try to take the center
    if 5 in possible_moves:
        move = 5
        return move
    
    # Take an edge
    open_edges = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            open_edges.append(i)

    if len(open_edges) > 0:
        move = select_random(open_edges)

    return move

def select_random(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def main():
    print('Welcome to Tic Tac Toe!')
    display_board(board)

    while not(full_board_check(board)):
        if not (win_check(board, 'O')):
            player_move()
            display_board(board)
        else:
            print('Sorry, O\'s won this game!')
            break
        if not(win_check(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
            else:
                place_marker(board, 'O', move)
                print('Computer placed an \'O\' in position', move, ':')
                display_board(board)
        else:
            print('X\'s won this time! Great Work!')
            break
    if full_board_check(board):
        return 'Tie Game'  

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

while True:
    main()
    if replay():
        board = [' ' for x in range(10)]
        print('---------------------------------')
        main()
    else:
        break  
