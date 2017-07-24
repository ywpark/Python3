testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for 문 index 사용법

# 이렇게는 사용못합
"""for idx, val in testArray:
    print('idx = ' + str(idx) + ' , val = ' + str(val))"""

# 배열을 enumerate 를 해야한다.
for idx, val in enumerate(testArray):
    print('idx = ' + str(idx) + ' , val = ' + str(val))

"""for idx, val in enumerate(range(10)):
    print('idx = ' + str(idx) + ' , val = ' + str(val))"""


ex1 = not 4 in testArray
ex2 = 4 in testArray

print(ex1)
print(ex2)


