#6 May,2020
import random,sys

#To count
win = 0
lose = 0
tie = 0
#for adjustment
w = ' Winner '
L = ' Lose '
D = ' Draw '
I = ' Invalid Input '
while True:
    #Options for player
    player = input("Enter your choice: 'R' = Rock, 'P' = Paper, 'S' = Scissor or 'Q' = Quit: ")
    if player == 'q' or player == 'Q':
        print("\nWin = %s, Lose = %s, Tie = %s" % (win, lose, tie))
        sys.exit('Thank you for playing :)')
    elif player == 'r' or player == 'R':
        print('\nRock VS ', end = '')
    elif player == 'p' or player == 'P':
        print('\nPaper VS ',end = '')
    elif player == 's' or player == 'S':
        print('\nScissor VS ', end = '')
    else:
        print(I.ljust(16,'!'),"\n")
        continue
    #Setting up Random number for Rock Paper and Scissor
    for i in range(1):
        computer = random.randint(1,3)
        if computer == 1:
            print('Rock')
        elif computer == 2:
            print('Paper')
        elif computer == 3:
            print('Scissor')
    #for Draw
        if computer == 1 and (player == 'r' or player == 'R'):
            print(D.center(12,'#'),"\n")
            tie = tie + 1
            break
        elif computer == 2 and (player == 'p' or player == 'P'):
            print(D.center(12,'#'),"\n")
            tie = tie + 1
            break
        elif computer == 3 and (player == 's' or player == 'S'):
            print(D.center(12,'#'),"\n")
            tie = tie + 1
            break
    #for winner and Loser against computer
        if (player == 'p' or player == 'P') and computer == 1:
            print(w.center(12,'*'),"\n")
            win = win + 1
        elif (player == 's' or player == 'S') and computer == 2:
            print(w.center(12,'*'),"\n")
            win = win + 1
        elif (player == 'r' or player == 'R') and computer == 3:
            print(w.center(12,'*'),"\n")
            win = win + 1
        else:
            print(L.center(12,'!'),"\n")
            lose = lose + 1











