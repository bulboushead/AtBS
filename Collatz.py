import time, sys

def collatz(ans):

    counter = 0
    while True:
        #time.sleep(0.01)
        if ans == 1:
            print('You have arrived at 1 after ' + str(counter) + ' iterations.')
            break
        elif (ans % 2 == 0):
            ans = ans // 2
            counter += 1
            print(ans)
        else:
            counter +=1
            ans = 3 * ans + 1
            print(ans)

test = True
while test:

    try:
        number = raw_input('Enter a number, I will reduce it to 1: ')
        number = int(number)
        #if isinstance(number, (int, long)):
        collatz(number)
        sys.exit()
    except (ValueError, NameError):
        print('ENTER AN INTENGER!')
        continue





