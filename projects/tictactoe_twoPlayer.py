# 21, may 2020

from random import *
import sys


board = { 
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9"
    }


# Tictactoe board functionality
def TTT(value):
    while True:
# To choose Option
        player = input("what is your choice 'X' or 'O' or 'Q' to exit the game: ")
        print("You are Player({})".format(player.upper()))       
        # Player choosing value
        if player.upper() == 'X':
            com = "o".upper()
            print(f"Your opponent is Player({com})")
            break
        elif player.upper() == 'O':
            com = "X".upper()
            print(f"Your Opponent is Player({com})")
            break
        elif player.upper() == 'Q':
            sys.exit()
        else:
            print('Wrong Input!!!')
            
   
    while True: 

# <--------------------------------------Player1 TicTacToe Board---------------------------------------->
        print(f"\n{board[1]} | {board[2]} | {board[3]}")
        print("--|---|--")
        print(f"{board[4]} | {board[5]} | {board[6]}")
        print("--|---|--")
        print(f"{board[7]} | {board[8]} | {board[9]}\n")
            
# For Player1 Functionality
        move = int(input("Player({}) move: ".format(player.upper())))
        if move == 1 or move == 2 or move == 3 or move == 4 or move == 5 or move == 6 or move == 7 or move == 8 or move == 9:
            pass
        else:
            print('invalid')
            break

        for k,v in board.items():
            if move == k:
                if v == 'X' or v == 'O':
                    # print(f"choose another value: {v} and key: {k}")
                    _move = int(input("'WARNING!' Choose anther position: "))
                    for k,v in board.items():
                        if _move == k: 
                            if v == 'X' or v == 'O':
                                print('You Missed The Chance!')
                                break
                            else: 
                                v = player.upper()
                                board[k] = v
                else:
                    v = player.upper()
                    board[k] = v
# For Player1 win and lose
        if board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
            print('Player(X) is WINNER!')
            sys.exit()
        elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            print('Player(X) is WINNER!') 
            sys.exit()
        elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
            print('Player(X) is WINNER!') 
            sys.exit()
        elif board[3] == 'X' and board[6] == 'X' and board[9] == 'X':
            print('Player(X) is WINNER!') 
            sys.exit()
        elif board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
            print('Player(X) is WINNER!')
            sys.exit()
        elif board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
            print('Player(X) is WINNER!')
            sys.exit()
        elif board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
            print('Player(X) is WINNER!')
            sys.exit()
        elif board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
            print('Player(X) is WINNER!')
            sys.exit() 
                      
# <--------------------------------------player2 TicTacToe Board---------------------------------------->
        print(f"\n{board[1]} | {board[2]} | {board[3]}")
        print("--|---|--")
        print(f"{board[4]} | {board[5]} | {board[6]}")
        print("--|---|--")
        print(f"{board[7]} | {board[8]} | {board[9]}\n")

# For Player2 Functionality
        pmove = int(input("Player({}) move: ".format(com.upper())))
        if pmove == 1 or pmove == 2 or pmove == 3 or pmove == 4 or pmove == 5 or pmove == 6 or pmove == 7 or pmove == 8 or pmove == 9:
            pass
        else:
            print('invalid')
            break
        for pk,pv in board.items():
            if pmove == pk:
                if pv == 'X' or pv == 'O':
                    # print(f"choose another value: {v} and key: {k}")
                    _pmove = int(input("'WARNING!' Choose anther position: "))
                    for pk,pv in board.items():
                        if _pmove == pk: 
                            if pv == 'X' or pv == 'O':
                                print('You Missed The Chance!')
                                break
                            else: 
                                pv = com.upper()
                                board[pk] = pv
                else:
                    pv = com.upper()
                    board[pk] = pv  
# For Player2 win and lose
        if board[1] == 'O' and board[2] == 'O' and board[3] == 'O':
            print('Player(O) is WINNER!')
            sys.exit()
        elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
            print('Player(O) is WINNER!') 
            sys.exit()
        elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
            print('Player(O) is WINNER!') 
            sys.exit()
        elif board[3] == 'O' and board[6] == 'O' and board[9] == 'O':
            print('Player(O) is WINNER!') 
            sys.exit()
        elif board[4] == 'O' and board[5] == 'O' and board[6] == 'O':
            print('Player(O) is WINNER!')
            sys.exit()
        elif board[7] == 'O' and board[8] == 'O' and board[9] == 'O':
            print('Player(O) is WINNER!')
            sys.exit()
        elif board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
            print('Player(O) is WINNER!')
            sys.exit()
        elif board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
            print('Player(O) is WINNER!')
            sys.exit()     
        
TTT(board)

    

   



        
    




