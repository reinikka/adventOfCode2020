def readDataPart1(fileName, posInc, rowInc):
    numOfTrees = 0
    with open(fileName, 'r') as dataFile:
        rowCount = 0
        lineLenght = 0
        pos = posInc
        rowCount = 0
        skipRows = rowInc - 1

        for inLine in dataFile:
            rowCount = rowCount + 1
            inLine = inLine.strip()
            if not lineLenght:
                lineLenght = len(inLine)
                continue
            if(skipRows > 0):
                skipRows = skipRows-1
                continue

            skipRows = rowInc - 1
            charAtPos = inLine[pos]
            if charAtPos == "#":
                numOfTrees = numOfTrees + 1
            pos = pos + posInc
            if pos >= lineLenght:
                pos = pos-lineLenght

    return numOfTrees


def readDataPart2(fileName):
    answer = 1
    answer = answer * readDataPart1(fileName, 1, 1)
    answer = answer * readDataPart1(fileName, 3, 1)
    answer = answer * readDataPart1(fileName, 5, 1)
    answer = answer * readDataPart1(fileName, 7, 1)
    answer = answer * readDataPart1(fileName, 1, 2)
    return answer


def main():
    answer = readDataPart2("input.txt")
    print(f"Answer to part2 = {answer}")
    answer = readDataPart1("input.txt", 3, 1)
    print(f"Answer to part1 = {answer}")


if __name__ == "__main__":
    main()
