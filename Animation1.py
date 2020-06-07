import time, sys
spaces = ''
astk = '********'

try:
    while True:
        while len(spaces) < 10:
            spaces = spaces + ' '
            print(spaces + astk)
            time.sleep(0.5)

        while len(spaces) > 1:
            spaces = spaces[:-1]
            print(spaces + astk)
            time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()