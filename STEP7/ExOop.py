
# #Classes
# # __init__ 메소드는 중요하다. this is called when an instance of the class is created, using the class name as a function
# # self.attribute (__init__ method) : set the initial value of an instance's attributes
# class Cat:
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs
#
# felix = Cat('ginger', 4)
# rover = Cat('dog-colored', 4)
# stumpy = Cat('brown', 3)
#
# print(felix)
# print(felix.color)

#
# # legs -> class attributes are shared by all instances of the class
# class Dog:
#     legs = 4
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def bark(self):
#         print('Woof!!!')
#
# fido = Dog('Fido', 'brown')
# print(fido.name)
# fido.bark()
#
# print(fido.legs)
# print(Dog.legs)
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# rect = Rectangle(7,8)
# print(rect.color)

# #Inheritance(인히어턴스)
#
# class Animal:
#     def __init__(self, name, color):
#         #print('__init__ method call')
#         self.name = name
#         self.color = color
#
# class Cat(Animal):
#     def purr(self):
#         print('Purr....')
#
# class Dog(Animal):
#     def bark(self):
#         print('Woof!')
#
# fido = Dog('Fido', 'brown')
# print(fido.color)
# fido.bark()

# class Wolf:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def bark(self):
#         print('Grr....')
#
# class Dog(Wolf):
#     def bark(self):
#         print('Woof')
#
# husky = Dog('Max', 'grey')
# husky.bark()
#
# circular inheritance is not possible
# class A:
#     def method(self):
#         print('A method')
#
# class B(A):
#     def another_method(self):
#         print('B method')
#
# class C(B):
#     def third_method(self):
#         print('C method')
#
# c = C()
# c.method()
# c.another_method()
# c.third_method()
# #
# class D:
#     def spam(self):
#         print(1)
#
# class E(D):
#     def spam(self):
#         print(2)
#         super().spam() # super. error
#
# E().spam()


# Magic Methods
#__method__ 형태  => double underscores => dunders 메소드

# # __sub__ for -
# # __mul__ for *
# # __truediv__ for /
# # __floordiv__ for //
# # __mod__ for %
# # __pow__ for **
# # __and__ for &
# # __xor__ for ^
# # __or__  for |
# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # + operator 를 위한 __add__ 함수
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
#
# first = Vector2D(5,7)
# second = Vector2D(3,9)
# result = first + second
# print(result.x)
# print(result.y)

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __truediv__(self, other):
#         line = '=' * len(other.cont)
#         return '\n'.join([self.cont, line, other.cont])
#
# spam = SpecialString('spam')
# hello = SpecialString('Hello world!!')
#
# print(spam/hello)
#
# # __lt__ for <
# # __le__ for <=
# # __eq__ for ==
# # __ne__ for !=
# # __gt__ for >
# # __ge__ for >=
#
# class SpecialString2:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __gt__(self, other):
#         for index in range(len(other.cont) + 1):
#             result = other.cont[:index] + '>' + self.cont
#             result += '>' + other.cont[index:]
#             print(result)
#
# spam = SpecialString('spam')
# eggs = SpecialString2('eggs')
#
# print(eggs + spam)
#
#
# # __len__ for len()
# # __getitem__ for indexing
# # __setitem__ for assigning to indexed values
# # __delitem__ for deleting indexed values
# # __iter__ for iteration over objects
# # __contains__ for in

#
# import random
#
# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1,1)]
#
#     def __len__(self):
#         return random.randint(0, len(self.cont)*2)
#
# vague_list = VagueList(['A','B','C','D','E'])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])


# Object Lifecycle
# an object's reference count increases when it is assigned a new name or placed in a container
# When an object's reference count reaches zero, Python automatically deletes it.
import sys

a = 42 # Create object <42>
b = a  # Increase ref. count of <42>
c = [a] # Increase ref. count of <42>

del a # Decrease ref.count of <42>
b = 100 # Decrease ref.count of <42>
c[0] = -1 # Decrease ref.count of <42>
print('a = ', sys.getrefcount(42))