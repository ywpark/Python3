# Python이 추구하는 철학 ( The Zen of Python )
#import this

# Python Enhancement Proposals (PEP) : 파이선을 개선하기 위한 제안

# Function Arguments
# *args = 기본 파라미터 외에 다른 파라미터를 tuple로 return

# def function(named_arg, *args):
#     print(named_arg)
#     print(args)
#
# function(1,2,3,4,5)

# Default Value
# def function(x,y,food='spam'):
#     print(food)
#
# function(1,2)
# function(3,4,'egg')

# **kwargs = keyword arguments return dictionary
# def my_func(x,y=7,*args,**kwargs):
#     print(x)
#     print(y)
#     print(args[0])
#     print(kwargs['a'])
#
# my_func(2,3,4,5,6,a=7, b=8)


# Tuple Unpacking

# numbers = 1,2,3
# a,b,c = numbers
# print(a)
# print(b)
# print(c)
#
# a,b = b,a
# print(a)
# print(b)
# print(c)

# # *변수는 나머지를 다가져간다
# a,b,*c,d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(d)


#ternary operator ( 삼항연산자 )

# a = 7
# b = 1 if a >= 10 else 42
# print(b)


# else 구문 관련
# # for or while loop 에서는  break 문이 아닌 정상적으로 loop 구문이 종료됐을때 이후 실행되는 로직
# for i in range(10):
#     if i == 999:
#         break
# else:
#     print('Unbroken 1')
#
# for i in range(10):
#     if i == 5:
#         break
# else:
#     print('Unbroken 2')


# try/except 에서도 다른의미 부여
# try 구문에서 에러없이 정상 실행될때만 else 로직이 실행된다
# try:
#     print(1)
# except ZeroDivisionError:
#     print(2)
# else:
#     print(3)
#
#
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(4)
# else:
#     print(5)


# __main__
# module 마다 name 이 존재하며 해당 변수는 __name__ 이다.


def function():
    print('This is a module function')

print(__name__)
if __name__ == '__main__':
    print('This is a script')


# Major 3rd-Party Libraries

# 1. Django : web framework
# CherryPy , Flask : web framework
# matplotlib : graphs based on data
# NumPy : 다차원 배열에 최적화 네이티브보다 성능이 좋다
# SciPy : contains numerous extensions to the functionality
# Panda3D : 3d game , pygame : 2d game




