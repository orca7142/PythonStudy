# 파일 읽기
file = open('hello.txt', 'rt')

str = file.read()
print(str, end='')

file.close()