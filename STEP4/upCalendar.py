import datetime, calendar, sys

custDaysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
currentColPos = 0

def addEnterString(orgin):
    return orgin + '\n'

def printConsoleCalendar(year, month):
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

def printFileCalendar(year, month):

    try:
        # 파일 미존재 시 생성
        outputFile = open('Calendar.txt', 'w')

        # index[0] : ( 0 ~ 6 , Mon ~ Sun ), index[1] : lastDays
        totalDays = calendar.monthrange(userSearchYear, userSearchMonth)
        currentColPos = totalDays[0] + 1 if totalDays[0] != 6 else 0
        totalStr = ''

        for cDaysText in custDaysOfWeek:
            totalStr += cDaysText + '\t\t'

        totalStr = addEnterString(totalStr)

        if (currentColPos != 0):
            # 시작지점 세팅
            totalStr += '  \t\t' * (int(totalDays[0]) + 1)

        while True:
            for dayNum in range(1, totalDays[1] + 1):
                preStr = ' ' if dayNum > 9 else '  '
                totalStr +=  preStr + str(dayNum) + '     '
                currentColPos += 1
                if (currentColPos > 6):
                    currentColPos = 0
                    totalStr = addEnterString(totalStr)
            totalStr = addEnterString(totalStr)
            break

        outputFile.write(totalStr)
    except:
        raise
    finally:
        outputFile.close()

while True:
    try:

        # 출력 결정 ( 1. console , 2. file )
        userOutput = input('Output ? ( 1. CONSOLE , 2. FILE , 3. END PROGRAM ) : ')

        if not  userOutput in ('1', '2'):
            if userOutput == '3':
                print('프로그램 종료')
                break
            else:
                print('다시 입력해주세요 (유효 입력값이 아닙니다)')
                continue

        userSearchYear = int(input('Search Year : '))
        userSearchMonth = int(input('Search Month : '))

        # Month 입력 체크
        assert userSearchMonth > 0 and userSearchMonth < 13

        if userOutput == '1':
            printConsoleCalendar(userSearchYear, userSearchMonth)
        elif userOutput == '2':
            printFileCalendar(userSearchYear, userSearchMonth)

        print('============== END ==============')
        break
    except ValueError:
        print('숫자형식으로 입력해주세용')
        print()
    except AssertionError:
        print('1 ~ 12월을 넘을 수 없습니다.')
        print()
    except:
        print('에러 발생 :', sys.exc_info())
        break
