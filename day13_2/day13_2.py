from os import times
import math

def readData2_fast(data):
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
            tsData[ts] = {'offset': pos, 'loopadd': idx}
            idx = idx + 1
        pos = pos + 1

    # find higest ts
    tsHigest = max(tsCleaned)
    offsetHighest = tsData[tsHigest]['offset']

    found = False
    testTs = tsHigest
    matched = {}
    round = 1
    while not found:
        for ts in tsCleaned:
            if ts in matched:
                continue
            offsetAtPos = tsData[ts]['offset']-offsetHighest
            tsAtPos = testTs+offsetAtPos
            test = tsAtPos/ts
            if math.ceil(test)-test == 0:
                matched[ts] = round
        if len(matched) == len(tsCleaned):
            break

        testTs = testTs+tsHigest
        round = round +1

    # eliminate first, loop rest
    oldTsTable = tsCleaned.copy()
    oldTsTable.remove(tsHigest)
    tsCleaned.clear()
    tsData.clear()
    for ts in oldTsTable:
        tsCleaned.append(ts*tsHigest)
        tsData[ts*tsHigest] = {'offset': matched[ts]*tsHigest, 'loopadd':ts*tsHigest}
    
    foundTs = 0
    startLargest = 100000000000000
    while not found:
        smallesTs = -1
        largestTs = -1
        allTheSame = True
        tsPrev = -1
        for ts in tsCleaned:
            if tsPrev> 0 and tsData[ts]['offset'] != tsPrev:
                allTheSame = False
            if smallesTs < 0:
                smallesTs = ts
            elif tsData[ts]['offset'] < tsData[smallesTs]['offset']:
                smallesTs = ts
            if largestTs < 0:
                largestTs = ts
            elif tsData[ts]['offset'] > tsData[largestTs]['offset']:
                largestTs = ts
            tsPrev = tsData[ts]['offset']
        if allTheSame:
            foundTs = tsData[smallesTs]['offset']-offsetHighest
            break
        for ts in tsCleaned:
            if startLargest<0:
                if ts == largestTs:
                    continue
                difftolargest = tsData[largestTs]['offset'] - tsData[ts]['offset']
            else:
                difftolargest = startLargest-tsData[ts]['offset']
            
            addToOffset = int(difftolargest/tsData[ts]['loopadd'])*tsData[ts]['loopadd']
            if addToOffset == 0:
                addToOffset = tsData[ts]['loopadd']

            tsData[ts]['offset'] = tsData[ts]['offset'] + addToOffset
        startLargest = -1
                
        continue

    print(f"Answer part 2 ={foundTs}")


def main():
    readData2_fast("17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,937,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,397,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19")

if __name__ == "__main__":
    main()
