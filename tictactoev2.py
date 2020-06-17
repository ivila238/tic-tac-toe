from sys import exit
from textwrap import dedent
from copy import deepcopy

# Creates empty array to model game-board
the_board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
             'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
             'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' '}

win = ""


# prints the game board
def print_board(board):
    print('\n\n')
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])


# list of lists that checks every possible win combination
def win_logic(board):
    global win

    top_row = [board['top-l'], board['top-m'], board['top-r']]
    mid_row = [board['mid-l'], board['mid-m'], board['mid-r']]
    bot_row = [board['bot-l'], board['bot-m'], board['bot-r']]
    l_col = [board['top-l'], board['mid-l'], board['bot-l']]
    m_col = [board['top-m'], board['mid-m'], board['bot-m']]
    r_col = [board['top-r'], board['mid-r'], board['bot-r']]
    ur_diag = [board['top-l'], board['mid-m'], board['bot-r']]
    br_diag = [board['bot-l'], board['mid-m'], board['top-r']]
    x_win = ['X', 'X', 'X']
    o_win = ['O', 'O', 'O']
    # breaks if there is a win condition, otherwise returns to game
    if x_win in [top_row, mid_row, bot_row, l_col, m_col, r_col, ur_diag, br_diag]:
        win = 'X win!'
    elif o_win in [top_row, mid_row, bot_row, l_col, m_col, r_col, ur_diag, br_diag]:
        win = 'O win!'

    else:
        return


# main game loop
def game(board):
    global win
    win = ""
    current_board = deepcopy(board)
    print("Who wants to go first? X or O?")
    turn = input("> ").upper()
    if turn == 'QUIT':
        exit_game()

    while not win:
        win_logic(current_board)
        print_board(current_board)
        print(f"It is {turn}'s turn.")
        print("Make your move.")
        move = input('> ').lower()
        if move == 'quit':
            exit_game()
        valid_move = True
        while valid_move:
            # loop to ensure valid move
            if move in current_board and current_board[move] == ' ':
                current_board[move] = turn
                win_logic(current_board)
                break
            elif move in current_board and current_board[move] in ['X', 'O']:
                print("There is already a move there!\nMake a different move.")
                move = input('> ').lower()
                if move == 'quit':
                    exit_game()
            else:
                print("Please make a valid move")
                move = input('> ').lower()
                if move == 'quit':
                    exit_game()
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    print_board(current_board)
    print(win)
    play_again()


# initial game start text, how-to, or quit
def start_game():
    print("Welcome to Tic Tac Toe")
    print("To play the game, type game")
    print('For info, type info')
    print("To quit, type quit")
    prompt = input('> ')

    if prompt.lower() == 'game':
        game(the_board)
    elif prompt.lower() == "info":
        info()
    elif prompt.lower() == "quit":
        exit_game()
    else:
        start_game()


# ask if user wants to play again
def play_again():
    print("Do you want to play again?")
    response = input('y/n').lower()

    if response == 'y':
        game(the_board)
    elif response == 'n':
        exit_game()
    else:
        play_again()


# automatic stalemate detection
def stalemate(board):
    pass


def info():
    print(dedent("""
        This game is written by Isaac V. He is still very much
        a beginner at python and is using this as practice to
        become a better programmer as well as how to think differently.
        If you are even reading this that means that he decided to show
        his code off to the world and get some feedback (Woo! Progress)

        This is version 2 of tic-tac-toe, this seeks to change the function
        of the code to be more reliant on functions to allow feature
        additions such as repeatability, more user control, and stalemate
        detection. This is also an attempt to work on including more comments
        and supporting documentation.

        Future additions (hopefully) include a computer AI to play against
        with different levels of difficulty, a GUI, and a game counter.
        """))

    print("\nContinue to game or quit?")

    # creates quasi menu
    response = (input("> ")).lower()
    if response == 'game' or response == 'continue':
        game(the_board)
    elif response == "quit":
        exit_game()
    else:
        info()


def exit_game():
    print("Thanks for playing!")
    exit()


start_game()
