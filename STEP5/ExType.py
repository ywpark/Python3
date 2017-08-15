#None
#absence of a value
print(None == None)

#Dictionary
#Key = immutable object
ages = {'Dave':24, 'Mary':42, 'John':58}
print(ages['Dave'])
print(ages['Mary'])

squares = {1:1, 2:4, 3:'error', 4:16}
print(squares)

squares[8] = 64
squares[3] = 9
print(squares)

print(3 in squares) # key 만 검색

print(ages.get('Dave'))
print(ages.get('test'))


#Tuple
# immutable
# Tuples are faster than lists

words = ('spam', 'eggs', 'sausages')
print(words[0])
#words[1] = 'cheese'

my_tuple = 'one', 'two', 'three'

print(my_tuple[0])
print(my_tuple[1:])

#List Slices

exList = [0,1,4,9,16,25,36,49,64,81]
print(exList[2:6]) # range(6)
print(exList[3:8])
print(exList[0:1])

print(exList[:7])
print(exList[7:])

print(exList[::2])
print(exList[2:8:3])

print(exList[1:-1])
print(exList[::-1])

# List Comprehensions

cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)


# String Formatting

nums = [4,5,6]
msg = 'Numbers: {0} {1} {2}'.format(nums[0], nums[1], nums[2])
print(msg)

a = '{x},,,,{y}'.format(x=5,y=12)
print(a)

nums2 = [ 55, 44, 33, 22, 11]

if all([i > 12 for i in nums2]):
    print('All larger than 5')

if any([i% 2 == 0 for i in nums2]):
    print('At least one is even')

for v in enumerate(nums2):
    print(v)

# File Open 변형
with open('test.txt') as f:
    b = f.read()

print(b)