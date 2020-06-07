def printTable(tableData):
    import pprint
    colWidths = [0]*len(tableData)
    finalTable = []

    for row in range(len(tableData[0])):
        columnList = []
        for column in range(len(tableData)):
            colWidths.append(len(tableData[column][row]))
            columnList.append(tableData[column][row])
        finalTable.append(columnList)

    maxWidth = max(colWidths)

    finalString = ''
    for row in finalTable:
        for word in row:
            finalString += word.rjust(maxWidth)
        finalString += '\n'
    print(finalString)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'pickled']]

printTable(tableData)