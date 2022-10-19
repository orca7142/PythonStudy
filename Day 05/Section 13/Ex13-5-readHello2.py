file = open('hello.txt', 'rt')

while True:
    str = file.read(5)
    if not str: # 5자리 글자 계속 읽다보면 아무것도 읽을게 없는데 그럼 0이 나오고 False이나 not이 앞에 붙어 True로 끝남
        break
    print(str, end='')

file.close()