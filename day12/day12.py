def readData(fileName):
    commands = list()
    print("Reading data from: " + fileName)
    with open(fileName, 'r') as dataFile:
        commands = [line.rstrip() for line in dataFile]
    return commands


def runPart1(commands):
    x = 0
    y = 0
    dx = 1
    dy = 0
    dir = 'e'
    for cmdArg in commands:
        cmd = cmdArg[:1]
        arg = int(cmdArg[1:])
        if cmd == 'F':
            if dir == 'e':
                dx = 1
                dy = 0
            if dir == 's':
                dx = 0
                dy = 1
            if dir == 'w':
                dx = -1
                dy = 0
            if dir == 'n':
                dx = 0
                dy = -1
            x = x + dx*arg
            y = y + dy*arg
        elif cmd == 'L' or cmd == 'R':
            for s in range(0, int(arg/90)):
                if dir == 'e':
                    dir = 's' if cmd == 'R' else 'n'
                elif dir == 'w':
                    dir = 's' if cmd == 'L' else 'n'
                elif dir == 'n':
                    dir = 'e' if cmd == 'R' else 'w'
                elif dir == 's':
                    dir = 'e' if cmd == 'L' else 'w'
        elif cmd == 'N':
            y = y - arg
        elif cmd == 'S':
            y = y + arg
        elif cmd == 'E':
            x = x + arg
        elif cmd == 'W':
            x = x - arg
    print(f"Part1 = {abs(x)+abs(y)} x = {x}, y={y}, dir = {dir}")


def runPart2(commands):
    x = 0
    y = 0
    wayX = 10
    wayY = -1
    for cmdArg in commands:
        cmd = cmdArg[:1]
        arg = int(cmdArg[1:])
        if cmd == 'F':
            x = x + wayX*arg
            y = y + wayY*arg
        elif cmd == 'L' or cmd == 'R':
            for s in range(0, int(arg/90)):
                xMul = 1 if cmd == 'L' else -1
                yMul = -1 if cmd == 'L' else 1
                oldX = wayX
                wayX = xMul*wayY
                wayY = yMul*oldX
        elif cmd == 'N':
            wayY = wayY - arg
        elif cmd == 'S':
            wayY = wayY + arg
        elif cmd == 'E':
            wayX = wayX + arg
        elif cmd == 'W':
            wayX = wayX - arg
    print(f"Part2 = {abs(x)+abs(y)} x = {x}, y={y}, wayX,Y = {wayX,wayY}")


def main():
    commands = readData("input.txt")
    runPart1(commands)
    runPart2(commands)


if __name__ == "__main__":
    main()
