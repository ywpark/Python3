

def testFunc2(arg1):
    print('testFunc2 = ' + arg1)

def testFunc(funcName, str1, str2):
    funcName(str1)
    print('testFunc = ' + str2)

a = '안녕'
b = '하세요'

testFunc(testFunc2, a, b)