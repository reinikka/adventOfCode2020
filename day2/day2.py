from dataclasses import dataclass


@dataclass
class PasswordRowPart1:
    minOccurs: int
    maxOccurs: int
    pwChar: str
    pw: str

    def isValid(self):
        chrCount = self.pw.count(self.pwChar)
        if(chrCount < self.minOccurs or chrCount > self.maxOccurs):
            return False
        return True


@dataclass
class PasswordRowPart2:
    firstPosition: int
    secondPosition: int
    pwChar: str
    pw: str

    def isValid(self):
        posCount = 0
        if(self.pw[self.firstPosition-1] == self.pwChar):
            posCount = posCount + 1
        if(self.pw[self.secondPosition-1] == self.pwChar):
            posCount = posCount + 1
        if(posCount == 1):
            return True
        return False


def readData(fileName, part1):

    # 1-3 a: abcde
    # 1-3 b: cdefg
    # 2-9 c: ccccccccc

    data = list()
    with open(fileName, 'r') as dataFile:
        for inLine in dataFile:
            inLine = inLine.split()
            minMax = inLine[0].split("-")

            if(part1):
                data.append(PasswordRowPart1(
                    int(minMax[0]), int(minMax[1]), inLine[1][:1], inLine[2]))
            else:
                data.append(PasswordRowPart2(
                    int(minMax[0]), int(minMax[1]), inLine[1][:1], inLine[2]))

    return data


def numberValidPasswords(pwList):
    count = 0
    for pwRow in pwList:
        if(pwRow.isValid()):
            count = count + 1
    return count


def main():
    pwsPart1 = readData("input.txt", True)
    print(
        f"Part1: Number of valid passwords: {numberValidPasswords(pwsPart1)}.")

    pwsPart2 = readData("input.txt", False)
    print(
        f"Part2: Number of valid passwords: {numberValidPasswords(pwsPart2)}.")


if __name__ == "__main__":
    main()
