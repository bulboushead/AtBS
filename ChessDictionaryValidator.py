import random, pprint, sys

def isValidChessBoard(boardInput):

    testFail =  False
    spots = {}
    pieces = {}
    #build possible pieces
    pcs = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    clrs = ['b', 'w']
    final = [x + y for y in pcs for x in clrs]
    for i in range(len(final)):
        pieces.setdefault(final[i],0)

    # Build the spot and piece dictionaries
    for i in boardInput.keys():
        spots.setdefault(i,0)
        spots[i] = spots[i]+1

    for i in boardInput.values():
        pieces.setdefault(i,0)
        pieces[i] = pieces[i]+1

    # 1 each b/w king
    if (pieces['bking'] != 1) or (pieces['wking'] != 1) == True:
        print('INVALID ' + str(pieces['bking']) + ' black kings, and ' + str(pieces['wking']) + ' white kings!')
        testFail = True
    else:
        print('Valid number of ' + str(pieces['bking']) + ' black kings, and ' + str(pieces['wking']) + ' white kings!')

    # confirm player has <= 16 pieces
    bPieces = 0
    wPieces = 0
    for j in pieces.keys():
        if j[0] == 'b':
            bPieces += pieces[j]
        else:
            wPieces += pieces[j]
    if bPieces > 16 or wPieces > 16:
        print('INVALID ' + str(bPieces) + ' black pieces, and ' + str(wPieces) + ' white pieces!')
        testFail = True
    else:
        print('Valid number of ' + str(bPieces) + ' black pieces, and ' + str(wPieces) + ' white pieces!')

    # If pawns exist, and does Player have <= 8 pawns

    if pieces['bpawn'] > 8 or pieces['wpawn'] > 8:
        print('INVALID ' + str(pieces['bpawn']) + ' black pawns, and ' + str(pieces['wpawn']) + ' white pawns!')
        testFail = True
    else:
        print('Valid number of ' + str(pieces['bpawn']) + ' black pawns, and ' + str(pieces['wpawn']) + ' white pawns!')

    # make sure no double spaces
    for k in spots.keys():
        if spots[k] == 1:
            continue
        else:
            print('One spot has more than one piece on it!  Exiting...')
            testFail = True

    # make sure the space is valid, 1a to 8h
    for m in range(len(spots)):
        # Verify length of spot is 2
        if len(spots.items()[m][0]) != 2:
            print('Length of spot does not equal two, invalid!')
            testFail = True

        if int(spots.items()[m][0][0]) not in range(1,9):
            print('First char of spot name out of range!')
            testFail = True
            break
        if spots.items()[m][0][1] not in ['a','b','c','d','e','f','g','h']:
            print('Second char of spot name out of alphabetical range!')
            testFail = True
            break

    # pieces start w/ 'w' or 'b'
    for m in range(len(pieces)):
        if str(pieces.items()[m][0])[0] not in ['b','w']:
            print('Piece does not start with w or b!')
            testFail = True
            break
        # followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
        if str(pieces.items()[m][0])[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            print('Piece is not a valid piece!')
            testFail = True
            break

    # Finish loop
    if testFail == False:
        # The test didn't fail!
        print('testFail = ' + str(testFail) + ', great success!')
        print(checker)
    else:
        print('testFail = ' + str(testFail) + ', failure!')

# Build random board and test
def generate_random_board(num):
    xAxis = ['a','b','c','d','e','f','g','h']
    yAxis = range(1,9)
    valid_spaces = [str(yspace)+xspace for xspace in xAxis for yspace in yAxis]
    colors = ['b', 'w']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']


    board = {}
    for num in range(0,num):
        board.update({random.choice(valid_spaces) : random.choice(colors)+random.choice(pieces)})

    print(board)
    return board

# Test function
iterations = 1000
for i in range(iterations):
    checker = random.randint(1,64)
    boardInput = generate_random_board(checker)
    isValidChessBoard(boardInput)


