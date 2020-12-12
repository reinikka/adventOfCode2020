def readData(fileName):
    numbers = list()
    print("Reading layout from: " + fileName)
    layout = {}
    row = 1
    with open(fileName, 'r') as dataFile:
        for line in dataFile:
            col = 1
            for c in line.strip():
                layout[row, col] = c
                col = col + 1
            row = row + 1
    return layout


def getNumAdjacentCells(cell, layout, marker):
    # print('----')
    nAdj = 0
    for row in range(cell[0]-1, cell[0]+2):
        for col in range(cell[1]-1, cell[1]+2):
            if (row, col) == cell:
                continue
            if (row, col) in layout:
                if layout[row, col] == marker:
                    nAdj = nAdj+1
                # print(row, col, layout[row, col])
    return nAdj
    # print('||||')


def getNumVisibleSeatsCells(cell, layout, marker):
    # print('----')
    nAdj = 0
    seatRow = cell[0]
    seatCol = cell[1]
    seats = {'n': (seatRow-1, seatCol), 'ne': (seatRow-1, seatCol+1), 'e': (seatRow, seatCol+1), 'se': (seatRow+1, seatCol+1),
             's': (seatRow+1, seatCol), 'sw': (seatRow+1, seatCol-1), 'w': (seatRow, seatCol-1), 'nw': (seatRow-1, seatCol-1)}

    ready = False
    while not ready:
        for d in seats.copy():
            if seats[d] != '#' and seats[d] != 'L':
                if seats[d] not in layout:
                    del seats[d]

        ready = True
        for d in seats:
            if seats[d] == 'L':
                continue
            if seats[d] == '#':
                continue
            ready = False
            if layout[seats[d]] == '#':
                seats[d] = '#'
            elif layout[seats[d]] == 'L':
                seats[d] = 'L'
            else:
                if seats[d][0] < seatRow:
                    seats[d] = (seats[d][0]-1, seats[d][1])
                if seats[d][0] > seatRow:
                    seats[d] = (seats[d][0]+1, seats[d][1])
                if seats[d][1] < seatCol:
                    seats[d] = (seats[d][0], seats[d][1]-1)
                if seats[d][1] > seatCol:
                    seats[d] = (seats[d][0], seats[d][1]+1)

    # print(seats)
    return sum(value == marker for value in seats.values())


def areAdjacentCells(cell, layout, marker):

    for row in range(cell[0]-1, cell[0]+2):
        for col in range(cell[1]-1, cell[1]+2):
            if (row, col) == cell:
                continue
            if (row, col) in layout:
                if layout[row, col] == marker:
                    return False

    return True


def part1(layout):
    while True:
        newLayout = layout.copy()
        for cell in layout:
            if layout[cell] == 'L':
                if areAdjacentCells(cell, layout, '#'):
                    newLayout[cell] = '#'
            elif layout[cell] == '#':
                numOccupied = getNumAdjacentCells(cell, layout, '#')
                if(numOccupied) >= 4:
                    newLayout[cell] = 'L'
        if newLayout == layout:
            break
        layout = newLayout.copy()
    print(
        f"Part1: Number of occupied seats = {sum(value == '#' for value in layout.values())}")


def part2(layout):
    while True:
        newLayout = layout.copy()
        for cell in layout:
            if layout[cell] == 'L':
                numFree = getNumVisibleSeatsCells(cell, layout, '#')
                if numFree == 0:
                    newLayout[cell] = '#'
            elif layout[cell] == '#':
                numOccupied = getNumVisibleSeatsCells(cell, layout, '#')
                if(numOccupied) >= 5:
                    newLayout[cell] = 'L'
        if newLayout == layout:
            break
        # print(newLayout)
        layout = newLayout.copy()
    print(
        f"Part2: Number of occupied seats = {sum(value == '#' for value in layout.values())}")


def main():
    layout = readData("input.txt")
    part1(layout)
    part2(layout)


if __name__ == "__main__":
    main()
