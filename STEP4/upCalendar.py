import datetime, calendar

custDaysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
currentColPos = 0

def printCalendar(year, month):
    "달력 그리기"
    # index[0] : ( 0 ~ 6 , Mon ~ Sun ), index[1] : lastDays
    totalDays = calendar.monthrange(userSearchYear, userSearchMonth)
    currentColPos = totalDays[0] + 1 if totalDays[0] != 6 else 0

    for cDaysText in custDaysOfWeek:
        print(cDaysText + '\t\t', end='')

    print()

    if (currentColPos != 0):
        # 시작지점 세팅
        print('  \t\t' * (int(totalDays[0]) + 1), end='')

    while True:
        for dayNum in range(1, totalDays[1] + 1):
            preStr = ' ' if dayNum > 9 else '  '
            print(preStr + str(dayNum) + '     ', end='')
            currentColPos += 1
            if (currentColPos > 6):
                currentColPos = 0
                print()
        print()
        break

while True:
    try:
        userSearchYear = int(input('Search Year : '))
        userSearchMonth = int(input('Search Month : '))

        assert userSearchMonth > 0 and userSearchMonth < 13

        printCalendar(userSearchYear, userSearchMonth)

        print('============== END ==============')
        break
    except ValueError:
        print('숫자형식으로 입력해주세용')
        print()
    except AssertionError:
        print('1 ~ 12월을 넘을 수 없습니다.')
        print()