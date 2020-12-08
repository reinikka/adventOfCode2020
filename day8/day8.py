cmds = list({})


def readData(fileName):
    print("Reading commands from: " + fileName)
    with open(fileName, 'r') as dataFile:
        lineNo = 0
        for inLine in dataFile:
            parts = inLine.split()
            cmds.append(
                {'oper': parts[0], 'arg': parts[1], 'visited': False})
            lineNo = lineNo + 1


def runPart1():
    global gAccumulator
    gAccumulator = 0
    line = 0
    lastLine = len(cmds)-1
    while cmds[line]['visited'] == False:
        cmds[line]['visited'] = True
        oper = cmds[line]['oper']
        arg = int(cmds[line]['arg'])
        if oper == 'acc':
            gAccumulator = gAccumulator + arg
            line = line + 1
        elif oper == 'jmp':
            line = line + arg
        elif oper == 'nop':
            line = line + 1
        else:
            print(f"Invalid operator {oper} at line {line}")
            return
        if(line > lastLine):
            #print(f"Reached end, gAccumulator={gAccumulator}")
            break
    #print(f"Accumulator: {gAccumulator} at line {line}")
    return line


def runPart2():
    global gAccumulator
    lastCmd = len(cmds)
    for c in cmds:
        for c2 in cmds:
            c2['visited'] = False
        origOper = c['oper']
        if c['oper'] == 'jmp':
            c['oper'] = 'nop'
        elif c['oper'] == 'nop':
            c['oper'] = 'jmp'
        else:
            continue
        if runPart1() >= lastCmd:
            break
        c['oper'] = origOper


def main():
    readData("input.txt")
    runPart1()
    print(f"Part1: {gAccumulator}")
    runPart2()
    print(f"Part2: {gAccumulator}")


if __name__ == "__main__":
    main()
