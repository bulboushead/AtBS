#! python2
# Date format replacer, takes any date and formats it correctly.

import re, pyperclip

# DD/MM/YYYY, 01-31, 01-12, 1000-2999, if single digit, will have leading zero
# regEx will accept right format, wrong days
dateRegex = re.compile(r'''(

    ([0-9]{2})
    /
    ([0-9]{2})
    /
    ([0-9]{4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

# store strings into variables 'month', 'day', 'year' in a dictionary
dateDict = {}
for groups in dateRegex.findall(text):
    dateDict[groups[0]] = [groups[1],groups[2],groups[3]]

for date in dateDict.values():
    check = True
    # detect if valid date
    if date[0] > '31':
        check = False
    if date[1] > '12':
        check = False
    if date[2] < '1000' or date[2] > '2499':
        check = False

    #   April, June, Sept, Nov  30 days
    if date[1] in ['04','06','09','11']:
        if date[0] > '30':
            check = False

    #   Feb                     28 days
    if date[1] in ['02']:
        if date[1] > '29':
            check = False
        # leap year?
        if date[1] == '29':
            if not ((date[2] % 400 == 0) or ((date[2] % 4 == 0) and (date[2] % 100 != 0))):
                check = False

    #   Rest                    31 days
    if date[1] not in ['02','04','06','09','11']:
        if date[0] > '31':
            check = False

    if check == True:
        matches.append('%s/%s/%s' % (date[0],date[1],date[2]))

pyperclip.copy('\n'.join(matches))