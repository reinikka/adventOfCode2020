def readDataPart1(fileName):
    count = 0
    with open(fileName, 'r') as dataFile:
        answers = ""
        for inLine in dataFile:
            inLine = inLine.strip()
            if inLine:
                for c in inLine:
                    if answers.count(c) == 0:
                        answers = answers + c
            else:
                count = count + len(answers)
                answers = ""

        count = count + len(answers)

    return count


def readDataPart2(fileName):
    count = 0
    with open(fileName, 'r') as dataFile:
        answers = ""
        newGroup = True
        for inLine in dataFile:
            inLine = inLine.strip()
            if inLine:
                if(newGroup):
                    answers = inLine
                    newGroup = False
                else:
                    for c in answers:
                        if(inLine.count(c) == 0):
                            answers = answers.replace(c, "")
            else:
                count = count + len(answers)
                newGroup = True

        count = count + len(answers)

    return count


def main():
    countPart1 = readDataPart1("input.txt")
    countPart2 = readDataPart2("input.txt")
    print(
        f"Part1: Number of answers: {countPart1}.")
    print(
        f"Part2: Number of answers: {countPart2}.")


if __name__ == "__main__":
    main()
