repeats = 9
divNo = 4
lineNo = 1
startPos = 1
endPos = 1

times = int(input('input Times Number : '))

## Default Times Table
"""for repPos in range(1, repeats + 1):
    for curPos in range(1, times + 1):
        print(str(curPos) + ' X ' + str(repPos) + ' = ' + str(curPos*repPos), end='')
        print('\t', end='')
    print()"""

##

while True:
    endPos = times if lineNo * divNo >= times else lineNo * divNo
    for repPos in range(1, repeats + 1):
        for curPos in range(startPos, endPos + 1):
            print(str(curPos) + ' X ' + str(repPos) + ' = ' + str(curPos * repPos), end='')
            print('\t', end='')
        print()
    lineNo += 1
    startPos = endPos + 1
    print()

    if endPos == times:
        break;

print('Times Table END....')