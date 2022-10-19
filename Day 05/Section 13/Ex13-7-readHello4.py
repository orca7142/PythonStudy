# line(줄별로 구분됨)
file = open('hello.txt', 'rt')

line_list = file.readlines()
for line in line_list:
    print(line, end='')

file.close()