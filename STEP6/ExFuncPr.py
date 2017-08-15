
# #function Programming
# def apply_twice(func, arg):
#     return func(func(arg))
#
# def add_five(x):
#     return x + 5
#
# print(apply_twice(add_five,10))
#
# #pure function
# #memoization
# def pure_function(x,y):
#     temp = x + 2*y
#     return temp/(2*x+y)
#
# #impure function
# some_list = []
# def impure(arg):
#     some_list.append(arg)

# # Lambdas
# def my_func(f, arg):
#     return f(arg)
#
# print(my_func(lambda x: 2*x*x, 5))
#
# def polynomial(x):
#     return x**2 + 5*x + 4
# print(polynomial(-4))
#
# print((lambda x:x**2 + 5*x + 4)(-4))
#
# double = lambda x: x*2
# print(double(7))

# # map & filter
# # iterable : 멤버를 하나씩 반환할 수 있는 object
# # iterator : next() 함수로 데이터를 순차적으로 호출하는 object
# def add_five(x):
#     return x+5
#
# nums = [11,22,33,44,55]
# #result = list(map(add_five, nums))
# result = list(map(lambda x: x+ 5, nums))
# print(result)
#
# #filter는 return a Boolean
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)

# #Generators
# #yield : iterable type
# def countdown():
#     i = 5
#     while i > 0:
#         print('**')
#         yield i
#         print('>', i)
#         i -= 1
#
# for i in countdown():
#     print(i)
#
# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
#
# print(list(numbers(11)))

# # Decorators
# def decor(func):
#     def wrap():
#         print('==========')
#         func()
#         print('==========')
#     return wrap
#
# @decor
# def print_text():
#     print('Hello world!')
#
# #decorated = decor(print_text)
# #decorated()
#
# print_text()

# # Recursion 재귀
#
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
#
# print(factorial(5))
#
# def is_even(x):
#     if x == 0:
#         return True
#     else:
#         return is_odd(x-1)
#
# def is_odd(x):
#     return not is_even(x)
#
# print(is_odd(17))
# print(is_even(23))
#
# def fib(x):
#     if x == 0 or x == 1:
#         return 1
#     else :
#         return fib(x-1) + fib(x-2)
#
# print(fib(4))

# # Sets
#
# num_set = {1,2,3,4,5}
# word_set = set(['spam','eggs','sausage'])
#
# print(3 in num_set)
# print('spam' not in word_set)
#
# num_set.add(-7)
# num_set.remove(3)
# print(num_set)
#
# nums = {1,2,1,3,1,4,5,6}
# print(nums)
#
# first = {1,2,3,4,5,6}
# second = {4,5,6,7,8,9}
#
# print(first | second) # union
# print(first & second) # intersection
# print(first - second) # difference
# print(first ^ second) # symmetric difference


# itertools

from itertools import count, cycle, repeat, accumulate, takewhile, product, permutations

for i in count(3):
    print(i)
    if i >= 11:
        break

for i in cycle('abcde'):
    print(i)
    if i == 'e':
        break

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x:x<=6, nums)))

letters = ('A','B', 'c')
print(list(product(letters,range(5))))
print(list(permutations(letters)))


