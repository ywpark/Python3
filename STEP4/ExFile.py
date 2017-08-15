
#기본적인 파일 오픈
# myfile = open('test.txt')

#write mode
#새로작성
# open('test.txt', 'w')
#마지막 부분에 추가적으로 작성
#open('test.txt', 'a')

#read mode
# open('test.txt', 'r')

#binary write mode
# open('test.txt', 'wb')

#마직막은 항상 닫기
# myfile.close()
#
# file = open('test.txt', 'r')
# cont = file.read()
# print(cont)
# file.close()

#
# file = open('test.txt', 'r')
# #print(file.read(1))
# print(file.read(2))
# print(file.read(3))
# print(file.read(10))
# print(file.read(10))
# file.close()

file = open('test.txt', 'r')
#print(file.readlines())
for line in file.readlines():
    print(line)
file.close()


# # w 모드는 없으면 create 한다
# file = open('test1.txt', 'w')
# file.write('This has been written to a file')
# file.close()
#
# file = open('test1.txt', 'r')
# print(file.read())
# file.close()

msg = 'Hello world!!!!'
file = open('test2.txt', 'w')
amount_written = file.write(msg)
print(amount_written)
file.close()

try:
    f = open('test2.txt')
    print(f.read())
finally:
    f.close()