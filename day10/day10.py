def readData(fileName):
    numbers = list()
    print("Reading joltages from: " + fileName)
    with open(fileName, 'r') as dataFile:
        numbers = [int(line.rstrip()) for line in dataFile]
    numbers.sort()
    return numbers


def runDay10(joltages):
    joltageNow = 0
    diffs = {}
    joltages.append(joltages[-1]+3)

    for j in joltages:
        diff = j-joltageNow
        if diff in diffs:
            diffs[diff] = diffs[diff]+1
        else:
            diffs[diff] = 1
        joltageNow = joltageNow + diff

    print(f"   {diffs}={diffs[1]*diffs[3]}")


def runDay10Part2(joltages):
    joltageNow = 0
    diffs = {}
    joltages.insert(0, 0)
    pathCount = {}
    pathCount[joltages[0]] = 1

    for j in joltages[:len(joltages)-1]:
        for nextJ in range(j+1, j+4):
            if nextJ in joltages:
                found = True
                prevCount = 0
                if nextJ in pathCount:
                    prevCount = pathCount[nextJ]
                pathCount[nextJ] = prevCount + pathCount[j]
        del pathCount[j]
    print(pathCount)


def main():
    # runDay10(readData("test1.txt"))
    # runDay10(readData("test2.txt"))
    runDay10(readData("input.txt"))
    # runDay10Part2(readData("test1.txt"))
    # runDay10Part2(readData("test2.txt"))
    runDay10Part2(readData("input.txt"))


if __name__ == "__main__":
    main()
