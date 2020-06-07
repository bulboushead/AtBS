def CoinFlipStreaks():
    import random, sys

    trials = 100000
    numberOfStreaks = 0
    minStreak = 6

    for experimentNumber in range(trials):
        #Create 100 HT values
        flips = 100
        flipList = []
        for i in range(flips):
            if random.randint(0,1) == 0:
                flipList += 'H'
            else:
                flipList += 'T'
        #print(flipList)

        #Check for streaks and incr numberOfStreaks
        counter = 0
        done = False
        for i in range(len(flipList)):
            while i < len(flipList)-1:
                if done:
                    break

                if flipList[i] == flipList[i+1]:
                    counter += 1
                    if counter == 5:
                        numberOfStreaks += 1
                        done = True
                else:
                    counter = 0
                break

    print('\n\n')
    print('Number of streaks = ' + str(numberOfStreaks))
    trials = float(trials)
    print('Chance of streak: %s%%' % ((numberOfStreaks / (trials / 100))))

CoinFlipStreaks()