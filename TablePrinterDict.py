def printTable(tableData):
    import pprint
    colWidths = [0]*len(tableData)
    finalTable = {0:[],1:[],2:[],3:[]}

    for listt in tableData:
        for item in range(len(listt)):
            finalTable[item].append(listt[item])
            colWidths.append(len(listt[item]))
    #pprint.pprint(finalTable)

    maxWidth = max(colWidths)

    finalString = ''
    for row in finalTable.values():
        for word in row:
            finalString += word.rjust(maxWidth) + ' '
        finalString += '\n'
    print(finalString)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'pickled']]

printTable(tableData)