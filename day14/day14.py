def readData(fileName):
    print("Reading data from: " + fileName)
    maskResult = {}
    sumOfAllVals = 0

    with open(fileName, 'r') as dataFile:
        mask = ''
        for line in dataFile:
            lineParts = [x.strip() for x in line.rstrip().split("=")]
            if lineParts[0] == 'mask':
                mask = lineParts[1]
            else:
                answ = getVal(mask, int(lineParts[1]))
                maskResult[lineParts[0]] = answ
    for v in maskResult:
        sumOfAllVals = sumOfAllVals+maskResult[v]
    return sumOfAllVals


def getVal(mask, val):
    andmask = mask.replace('1', '0')
    andmask = int(andmask.replace('X', '1'), 2)
    answ = val & andmask
    ormask = int(mask.replace('X', '0'), 2)
    answ = answ | ormask
    return answ


def readData2(fileName):
    print("Reading data from: " + fileName)
    maskResult = {}
    sumOfAllVals = 0

    with open(fileName, 'r') as dataFile:
        mask = ''
        for line in dataFile:
            lineParts = [x.strip() for x in line.rstrip().split("=")]
            if lineParts[0] == 'mask':
                mask = lineParts[1]
            else:
                addr = int(lineParts[0].replace('mem[', '').replace(']', ''))
                newMask = getMask(mask, addr)
                calcResults(newMask, int(lineParts[1]), maskResult)

    for v in maskResult:
        sumOfAllVals = sumOfAllVals+maskResult[v]
    return sumOfAllVals


def getMask(mask, val):
    ormask = int(mask.replace('X', '0'), 2)
    res = bin(val | ormask)
    res = res.replace('0b', '')
    while len(res) < len(mask):
        res = '0' + res
    i = -1
    while True:
        i = mask.find('X', i+1)
        if(i < 0):
            break
        res = res[:i] + 'X' + res[i+1:]
    return res


def calcResults(mask, val, maskResult):
    if 'X' in mask:
        i = mask.find('X')
        res = mask[:i] + '0' + mask[i+1:]
        calcResults(res, val, maskResult)
        res = mask[:i] + '1' + mask[i+1:]
        calcResults(res, val, maskResult)
    else:
        addr = int(mask, 2)
        maskResult[addr] = val


def main():
    print(f"Answer to part 1 is {readData('input.txt')}")
    print(f"Answer to part 2 is {readData2('input.txt')}")


if __name__ == "__main__":
    main()
