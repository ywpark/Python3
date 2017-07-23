floors = int(input('input Floors Number : '))
shape = input('Shapes( 1 character ) : ')
curFloor = floors

## Default Draw
for floor in range(1, floors + 1):
    print(shape * floor)

print()

## Reverse Draw
for floor in range(floors, 0, -1):
    print(shape * floor)

for floor in range(1, floors + 1):
    print(' ' * (2 * (curFloor - 1)), end='')
    print((shape + '   ') * floor)
    curFloor += -1
