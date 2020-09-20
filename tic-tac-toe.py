
import random

#function to display the board
def display_board(board):
    print("\n ")
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
    print("\n ")

#function to player's input
def input_player():
    marker=""

    while not( marker=="X"or marker=="O"):
        marker= input("\n Player 1. Do you want to be X or O ?").upper()

        if marker=="X":
            return("X","O")
        else:
            return("O","X")

# function to place x/y on the board
def place_marker(board,position,marker):
    board[position]=(marker)

#to check the winner
def check_winner(board,mark):
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 
    

# choose first player
def choose_player():
    if random.randint(0,1) ==0:
        return "Player 2"
    else:
        return "Player 1"

# check if board has space left
def space_check(board,position):
    return(board[position]==" ")


# check if board is full
def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True


# take player's next input
def player_choice(board,turn):
    position=0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("\n "+turn +" Choose Your next Position:1-9 "))

        return position


# restart game
def play_again():
    return input("\n Do you want to play again?(Y/N)").lower().startswith('y')

print("\n ----WELCOME TO  TIC-TAC-TOE----")


while True:
    # Reset the board
    main_board = [' '] * 10
    player1_marker, player2_marker = input_player()
    turn = choose_player()
    print("\n "+str(turn) + ' will go first.')
    
    play_game = input('\n Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(main_board)
            position = player_choice(main_board,turn)
            place_marker(main_board, position,player1_marker)

            if check_winner(main_board, player1_marker):
                display_board(main_board)
                print('\n Player 1 has won!')
                game_on = False
            else:
                if full_board(main_board):
                    display_board(main_board)
                    print('\n The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(main_board)
            position = player_choice(main_board,turn)
            place_marker(main_board,position,player2_marker)

            if check_winner(main_board, player2_marker):
                display_board(main_board)
                print('\n Player 2 has won!')
                game_on = False
            else:
                if full_board(main_board):
                    display_board(main_board)
                    print('\n The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break

#END