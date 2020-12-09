def readData(fileName):
    numbers = list()
    print("Reading numbers from: " + fileName)
    with open(fileName, 'r') as dataFile:
        numbers = [int(line.rstrip()) for line in dataFile]
    return numbers


def isValid(value, numbers):
    for pos in range(0, len(numbers)-1):  # check each number
        first = numbers[pos]
        for second in numbers[pos+1:]:
            if first+second == value:
                return True
    return False


def runPart2(value, numbers):
    for pos in range(0, len(numbers)-1):  # check each number
        first = numbers[pos]
        sumVal = first
        posSecond = pos+1
        for second in numbers[pos+1:]:
            posSecond = posSecond+1
            sumVal = sumVal+second
            if sumVal == value:
                foundRange = numbers[pos:posSecond]
                minInRange = min(foundRange)
                maxInRange = max(foundRange)
                print(
                    f"  Part2: min={minInRange}, max = {maxInRange}, sum = {minInRange+maxInRange}")
                return
            elif sumVal > value:
                break


def runDay9(numbers, preamble):
    pos = preamble
    for p in range(pos, len(numbers)-1):
        if(not isValid(numbers[p], numbers[p-preamble:p])):
            print(f"  Part1: Invalid value {numbers[p]} at index {p}")
            runPart2(numbers[p], numbers[:p-1])
            break


def main():
    runDay9(readData("test.txt"), 5)
    runDay9(readData("input.txt"), 25)


if __name__ == "__main__":
    main()
