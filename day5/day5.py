def readDataPart1(fileName):
    count = 0
    seatIds = list()
    with open(fileName, 'r') as dataFile:
        maxId = 0
        for inLine in dataFile:
            inLine = inLine.strip()
            rowPart = inLine[:6]
            colPart = inLine[7:]
            row = parseData(rowPart, 128, 'B')
            col = parseData(colPart, 8, 'R')
            print(f"Row:  {row}")
            seatId = row*8+col
            seatIds.append(seatId)
            print(f"Row:  {row} Col: {col} Id: {seatId}")
            maxId = max(maxId, seatId)
            count = count + 1
    print(f"Parsed {count} rows")
    return maxId


def readDataPart2(fileName):
    count = 0
    seatIds = list()
    with open(fileName, 'r') as dataFile:
        for inLine in dataFile:
            inLine = inLine.strip()
            rowPart = inLine[:7]
            colPart = inLine[7:]
            row = parseData(rowPart, 128, 'B')
            col = parseData(colPart, 8, 'R')
            seatId = row*8+col
            seatIds.append(seatId)
            print(f"Row:  {row} Col: {col} Id: {seatId} data:{inLine}")
            count = count + 1
    print(f"Parsed {count} rows")
    prevPrev = 0
    prev = 0
    seatIds.sort()
    myId = 0
    for i in range(1, len(seatIds)-1):
        if(seatIds[i] == seatIds[i-1]+1 and seatIds[i] == seatIds[i+1]-1):
            continue
        return seatIds[i]+1


def parseData(inStr, range, inChr):
    pos = 0

    for c in inStr:
        range = range/2
        if c == inChr:
            pos = pos + range
    return pos


def main():
    myId = readDataPart2("input.txt")

    maxId = readDataPart1("input.txt")
    print(f"maxId : {maxId}.")
    print(f"myId : {myId}.")


if __name__ == "__main__":
    main()
