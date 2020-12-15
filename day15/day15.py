def loopNumbers(numbersStr, maxLoops):
    numbers = [int(n) for n in numbersStr.split(',')]
    history = {numbers[i]:(i+1,i+1) for i in range(0,len(numbers))}
    turn = len(numbers)+1
    lastSpoken = numbers[-1]
    
    while turn<=maxLoops:
        spokenNow = 0
        prevTurn = turn
        if lastSpoken in history:
            spokenNow = history[lastSpoken][0]-history[lastSpoken][1]
        if spokenNow in history:
            prevTurn = history[spokenNow][0]
        history[spokenNow] = (turn,prevTurn)
        lastSpoken = spokenNow
        turn = turn+1

    return lastSpoken

def main():

    if True:
        data = "0,13,16,17,1,10,6"
        print(f'Answer to part 1 is {loopNumbers(data,2020)}')
        print(f'Answer to part 2 is {loopNumbers(data,30000000)}')
    else:
        assert loopNumbers("0,3,6",2020) == 436
        assert loopNumbers("1,3,2",2020) == 1
        assert loopNumbers("2,1,3",2020) == 10
        assert loopNumbers("1,2,3",2020) == 27
        assert loopNumbers("2,3,1",2020) == 78
        assert loopNumbers("3,2,1",2020) == 438
        assert loopNumbers("3,1,2",2020) == 1836


if __name__ == "__main__":
    main()
