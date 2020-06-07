import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
loss = 0
tie = 0

while True:
    print('WINS:' + str(wins) + '    LOSSES:' + str(loss) + '    TIES:' + str(tie))

    while True:
        print('Enter your move: (r)ock (p)aper or (s)cissors, or (q)uit:')
        move = raw_input()
        if move in ['r', 'p', 's']:
            break
        elif move == 'q':
            print('Quitting!')
            sys.exit()
        else:
            print('Invalid input!  Try again')

    print('You entered ' + str(move))
    otherMove = random.randint(1,3)
    if otherMove == 1:
        if move == 'r':
            print('Rock vs Rock: TIE')
            tie = tie + 1
        elif move == 'p':
            print('Paper vs Rock:  WIN')
            wins = wins + 1
        else:
            print('Scissors vs Rock:  LOSS')
            loss = loss + 1
    elif otherMove == 2:
        if move == 'r':
            print('Rock vs Paper: LOSS')
            loss = loss + 1
        elif move == 'p':
            print('Paper vs Paper:  TIE')
            tie = tie + 1
        else:
            print('Scissors vs Paper:  WIN')
            wins = wins + 1
    else:
        if move == 'r':
            print('Rock vs Scissors: WIN')
            wins = wins + 1
        elif move == 'p':
            print('Paper vs Scissors:  LOSS')
            loss = loss + 1
        else:
            print('Scissors vs Scissors:  TIE')
            tie = tie + 1



