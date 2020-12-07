

# 0     1   2    3       4 5      6     7    8 9     10     11
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# 0      1     2    3       4 5     6    7
# bright white bags contain 1 shiny gold bag.
# 0      1     2    3       4  5     6
# dotted black bags contain no other bags.
bagRules = {}


def readData(fileName):
    print("Reading rules from: " + fileName)
    with open(fileName, 'r') as dataFile:
        for inLine in dataFile:
            lineParts = inLine.strip().split()
            bagColor = lineParts[0] + lineParts[1]
            numOfBags = inLine.count(',')+1
            if lineParts[4] == 'no':
                numOfBags = 0

            bagRules[bagColor] = list({})
            if numOfBags > 0:
                readPos = 4
                for i in range(0, numOfBags):
                    numOfBagsInside = lineParts[readPos]
                    insideBagColor = lineParts[readPos +
                                               1] + lineParts[readPos+2]
                    bagRules[bagColor].append(
                        {'color': insideBagColor, 'num': numOfBagsInside})
                    readPos = readPos + 4
    return bagRules


def countPart1(bagColor, indent, searchColor, num):
    if(bagColor == searchColor):
        return num + 1

    #print(indent + bagColor)
    for bag in bagRules[bagColor]:
        num = countPart1(bag['color'], indent + '   ', searchColor, num)
    return num


def countBagPart1(searchColor):
    numOfSearchColor = 0
    for bagColor in bagRules:
        if(bagColor == searchColor):
            continue
        num = countPart1(bagColor, '   ', searchColor, 0)
        #print(f"Bag {bagColor} contains {num} {searchColor} bags.")
        if(num > 0):
            numOfSearchColor = numOfSearchColor + 1
    return numOfSearchColor


def countBagPart2(color, indent):
    #print(f"{indent}Bag {color} contains:")
    numberBags = 0
    for e in bagRules[color]:
        num = countBagPart2(e['color'], indent+'   ')
        numberBags = numberBags + (1+num)*int(e['num'])
        # print(
        #    f"{indent}{e['num']} bags of {e['color']} which has {num} bags. Total now {numberBags}")
    return numberBags


def main():
    data = readData("input.txt")
    color = "shinygold"
    print(f"Part1: bag {color} can be in {countBagPart1(color)} bags.")
    print(f"Part2: number of bags in {color} is {countBagPart2(color,'')}.")


if __name__ == "__main__":
    main()
