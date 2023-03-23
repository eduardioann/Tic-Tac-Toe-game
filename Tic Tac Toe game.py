import random
import os


def display_board(board):
    print('\n' * 100)
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n')


def start_printing_1():
    print('Hello! Welcome to my TIC-TAC-TOE game\n')



def player_input():
    marker = ''
    while (marker != 'X' and marker != '0'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        print("Great! You play with X and your mate plays with 0 \nLet's play!")
        print('Note that the board is created like this: ')
        print('1 | 2 | 3')
        print('---------')
        print('4 | 5 | 6')
        print('---------')
        print('7 | 8 | 9')
        print('\n')
        return ('X', 'O')

    else:
        print("Great! You play with 0 and your mate plays with X \nLet's play!")
        print('Note that the board is created like this: ')
        print('1 | 2 | 3')
        print('-------')
        print('4 | 5 | 6')
        print('-------')
        print('7 | 8 | 9')
        print('\n')
        return ('O', 'X')



def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))



def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    if board[position] == ' ':
        return True
    return False


def full_board_check(board):
    for x in range(1, 10):
        if space_check(board, x):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a free position between 1-9: "))

    return position



def replay():
    response = input('Do you want to play again? Yes or No?')
    if response == 'y':
        return True
    return False


# RUN THE GAME


start_printing_1()

while True:

    # SETTING UP THE GAME

    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()

    play_game = input('Ready to play? Yes or No?')
    # It is y for yes and anything else for no
    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    # GAME PLAY


    while game_on:

        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break


