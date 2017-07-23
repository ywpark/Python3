list1 = [] ##Empty
list2 = [1, 3, 5, 7, 9] ##Default
list3 = ['asdasd', "weqweqwr", '1', 2, 4, [1,4,5,6], list2]

print('list1 = ' + str(list1))
print('list2 = ' + str(list2))
print('list3 = ' + str(list3))

print(list1 + [2,2,2,2])

print()

print('list1 length = ' + str(len(list1)))
print('list2 length = ' + str(len(list2)))
print('list3 length = ' + str(len(list3)))

print()

isExist1 = 1 in list1
isExist2 = 4 in list2
isExist3 = list2 in list3

print('isExist1 = ' + str(isExist1))
print('isExist2 = ' + str(isExist2))
print('isExist3 = ' + str(isExist3))

print(not 4 in list2)
print(4 not in list2)

print()

list4 = [[]] * 3
print(list4)

## Add
list4[0].append(4)
print(list4)


## insert
list2.insert(2, 3)
print(list2)

print(list2.index(3))

## max, min
print(max(list2))
print(min(list2))

listC = ['가', '나', '다', 'Z']
print(max(listC))
print(min(listC))

## count
print(list2.count(11))

## remove
list2.remove(3)
list2.remove(3)
print(list2)

## reverse
list2.reverse()
print(list2)
