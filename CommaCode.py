def listToString ():
    import sys

    while True:
        try:
            inputList = raw_input('Please enter a list: ')
            if inputList == []:
                print('Your list is empty!')
                continue
        except SyntaxError:
            print('You did not format your input as a list, please try again')
            continue

        finalString = ''
        for i in range(len(inputList)):
            if i == 0:
                finalString = (finalString) + inputList[i]
            elif i < len(inputList) - 1:
                finalString = (finalString) + ', ' + inputList[i]
            else:
                finalString = (finalString) + ', and ' + inputList[i]

        print(finalString)
        sys.exit()

listToString()