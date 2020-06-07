def listToString(theList):

    for i in range(len(theList) - 2):
        print(theList[i] + ","),
    print(theList[-2] + ', and ' + theList[-1])

listToString(['apples', 'bananas', 'tofu', 'cats'])