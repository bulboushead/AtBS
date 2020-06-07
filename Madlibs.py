import os
import re

os.chdir('C:\\Users\\wdavis9013\\PycharmProjects\\ATBS\\')
madlib = open('C:/Users/wdavis9013/PycharmProjects/ATBS/Madlib.txt', 'r')
text = madlib.read()
madlib.close()

regex =  re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)|(ADVERB)')

for i in regex.findall(text):
    for j in i:
        if j != '':
            reg = re.compile(f"{j}")
            inp_text = input(f"Enter the substitute for {j}:")
            text = reg.sub(inp_text, text, 1)

print(text)

newFile = open('MadlibDone.txt','w')
newFile.write(text)
newFile.close()