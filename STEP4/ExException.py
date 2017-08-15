#math 모듈에서 pi만 쓰겟다
#from math import pi

num = 1
num2 = 0

#print(num/num2)

#
# try:
#     print(num/num2)
#     print('success')
# except ZeroDivisionError:
#     print('zeroError')
# except :
#     print('except')


# try:
#     print('hi' + num)
# except ZeroDivisionError :
#     print('zeroError')
# except (TypeError, ValueError) :
#     print('typeError or valueError')

#
# try:
#     print('Hello')
#     print(1/0)
# except ZeroDivisionError:
#     print('zeroError')
# finally:
#     print('This code will run no matter what')

#
# try:
#     print(1)
#     print(10/0)
# except ZeroDivisionError :
#     print(unknown_var)
# finally:
#     print('This is executed last')

#
# print(1)
# raise ValueError
# print(2)

#
# try:
#     print(1/0)
# except ZeroDivisionError :
#     raise TypeError


# raise NameError('세부정보')
#
# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)
#
tmp3 = -10
assert tmp3 > 0, 'Colder than absolute zero!'