# 변수 범위 테스트 공간

# case 1
#
# a = 2
#
# def test():
#     a = 3
#     print('inside test : ', a)
#
# test()
# print('outside test : ', a)



# case 2

# a = 2
#
# def test():
#     print('inside test : ', a)
#
# test()
# print('after test : ', a)

# case 3
#
# a = 2
#
# def test():
#
#     print('inside test : ', a)
#     a = 3
#
# test()
# print('after test : ', a)

# case 4

a = 2

def test():
    global a # 전역변수와 동일한 변수로 취급한다는 의미
    print('inside test : ', a)
    a = 3

test()
print('after test : ', a)
