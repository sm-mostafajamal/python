# 18, may 2020

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


def TTT(value):
# Player Choosing Option
    while True:
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
        print(f"{board[7]} | {board[8]} | {board[9]} \n")

# For Player1 Functionality
        move = int(input("what is your move: "))
        # checking in between (1-9)
        if move == 1 or move == 2 or move == 3 or move == 4 or move == 5 or move == 6 or move == 7 or move == 8 or move == 9:
            pass
        else:
            print('invalid')
            break

        for k,v in board.items():
            # If key match then it will proceed
            if move == k:
                # If the move is already inserted by the player then it will go inside
                if v == 'X' or v == 'O':
                    # print(f"choose another value: {v} and key: {k}")
                    # This will ask again
                    _move = int(input("'WARNING!' Choose anther position: "))
                    for k,v in board.items():
                        if _move == k: 
                            if v == 'X' or v == 'O':
                                print('You Missed The Chance!')
                                break
                            else: 
                                v = player.upper()  # This will replace the board value
                                board[k] = v        # This will check the key and replace the actual value
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

# For Computer Functionality
        computer = randint(1,9)
        for ck,cv in board.items():
            if computer == ck:
                # print(f"The Bot choosed: {computer}")
                if cv == 'X' or cv == 'O':
                    # print('MATCHED')
                    # theBoard = sample(board.items(), k=9)   # To shuffle the board dictionary key inside the sample K means key
                    # print(f"theBoard choosed: {theBoard}")
                    for ck2,cv2 in board.items():              # loop through the keys to check any value is empty
                        if cv2 == 'X' or cv2 == 'O':           # If the inserted value is 'X' or 'O' then it will skip
                            # print(f"After the match {ck2}")
                            continue
                            cv2 = com.upper()
                            board[ck2] = cv2
                        else:
                            # print(f'after continue the comouter choosed: {ck2}')
                            cv2 = com.upper()
                            board[ck2] = cv2
                        break           # after replacing  the value or all value are filledup  it will break through the loop
                else:
                    # print(f"'Else' The computer choosed {computer}")
                    computer = com
                    cv = com.upper()
                    board[ck] = cv         
# For Computer win and lose
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

    

   



        
    




