from os import times
import math


def readData(fileName):
    departTime = 0
    timestamps = list()
    print("Reading data from: " + fileName)
    with open(fileName, 'r') as dataFile:
        departTime = int(dataFile.readline().rstrip())
        timestamps = dataFile.readline().rstrip().split(',')
    minDiff = -1
    diffId = -1
    minDivVal = -1
    tsCleaned = list()
    for ts in timestamps.copy():
        if ts != 'x':
            tsCleaned.append(int(ts))
    for ts in tsCleaned:
        if ts == 'x':
            continue
        divVal = departTime/int(ts)
        diff = math.ceil(divVal)-divVal

        if minDiff < 0 or diff < minDiff:
            minDiff = diff
            diffId = ts
            minDivVal = divVal

    waitTime = math.ceil(minDivVal)*diffId-departTime
    print(
        f"Part1:answer={diffId*waitTime} bus id: {diffId}, waitTime: {waitTime}, {minDiff}")


def readData2(data):
    timestamps = list()
    timestamps = data.split(',')
    tsCleaned = list()
    tsData = dict({})
    pos = 0
    idx = 0
    for ts in timestamps.copy():
        if ts != 'x':
            ts = int(ts)
            tsCleaned.append(ts)
            tsData[ts] = {'offset': pos, 'idx': idx}
            idx = idx + 1
        pos = pos + 1

    # find higest ts
    tsHigest = max(tsCleaned)
    offsetHighest = tsData[tsHigest]['offset']

    found = False
    testTs = int(100000000000000/tsHigest)*int(tsHigest)+tsHigest
    while not found:
        fail = False
        if testTs == 1068785:
            print('break')

        for ts in tsCleaned:
            offsetAtPos = tsData[ts]['offset']-offsetHighest
            tsAtPos = testTs+offsetAtPos
            test = tsAtPos/ts
            if math.ceil(test)-test > 0:
                fail = True
                break
        if not fail:
            break
        testTs = testTs+tsHigest
    print(f"Answer={testTs-offsetHighest} for {data}", flush=True)


def main():

    readData2("7,13,x,x,59,x,31,19")
    readData2("17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,937,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,397,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19")
    readData2("17,x,13,19")
    readData2("67,7,59,61")
    readData2("67,x,7,59,61")
    readData2("67,7,x,59,61")
    readData2("1789,37,47,1889")
    # readData("input.txt")


if __name__ == "__main__":
    main()
