
# # Data Hiding
# # _ => weakly private method , attributes
# # __ => strongly private method, attributes
# # __ 변수에 접근할 떄는 _className__privateMethod
#
# class Queue:
#
#     a = 10
#     _b_ = 20
#
#     def __init__(self, content):
#         self._hiddenlist = list(content)
#
#     def push(self, value):
#         self._hiddenlist.insert(0,value)
#
#     def pop(self):
#         return self._hiddenlist.pop(-1)
#
#     def __repr__(self):
#         return 'Queue({})'.format(self._hiddenlist)
#
# queue = Queue([1,2,3])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue._hiddenlist)
# print(queue.__repr__())


# class Spam:
#     __egg = 7
#     def print_egg(self):
#         print(self.__egg)
#
# spam = Spam()
# spam.print_egg()
# print(spam._Spam__egg)
# #print(spam.__egg)

# Class Method , Static Method

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     @classmethod
#     def new_square(cls, side_length):
#         return cls(side_length, side_length)
#
# square = Rectangle.new_square(5)
# print(square.calculate_area())


# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @staticmethod
#     def validate_topping(topping):
#         if topping == 'pineapple':
#             raise ValueError('No pineapples!')
#         else:
#             return True
#
# ingredients = ['cheese', 'onions', 'spam', 'pineapple']
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)


# Properties
# 메소드를 attribute 처럼 접근할 수 있다. 대신 read-only 이다
#
# class Pizza:
#
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @property
#     def pineapple_allowed(self):
#         return False
#
# pizza = Pizza(['cheese', 'tomato'])
# print(pizza.pineapple_allowed)
# #pizza.pineapple_allowed = True

class Pizza2:

    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input('Enter the password: ')
            if password == 'SwOrdf1sh!':
                self._pineapple_allowed = value
            else:
                raise ValueError('Alert! Intruder!')

pizza2 = Pizza2(['cheese', 'tomato'])
print(pizza2.pineapple_allowed)
pizza2.pineapple_allowed = True
#print(pizza.pineapple_allowed)


# # Simple Game
#
# def get_input():
#     command = input(': ').split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dict[verb_word]
#     else:
#         print('Unknown verb {}'.format(verb_word))
#         return
#
#     if len(command) >= 2:
#         noun_word = command[1]
#         print(verb(noun_word))
#     else:
#         print(verb('nothing'))
#
# def say(noun):
#     return 'You said "{}"'.format(noun)
#
# verb_dict = {
#     "say": say,
# }
#
# while True:
#     get_input()

