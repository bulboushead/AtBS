#! python2
""" bulletPointAdder.py - Adds '* ' to the first line of each entry copied to
 the clipboard from Wikipedia """

import sys, os, pprint
print(os.getcwd())
print()
print(sys.executable)
pprint.pprint(sys.path)
sys.path.append('C:\Users\wdavis9013\PycharmProjects\ATBS\\venv\Lib\site-packages')
print('\n')
pprint.pprint(sys.path)
import pyperclip

text = pyperclip.paste()
text =  text.split('\n')
for i in range(len(text)):
    text[i] = str('* ') + text[i]

text = '\n'.join(text)

pyperclip.copy(text)
