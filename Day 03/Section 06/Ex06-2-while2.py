'''


'''

my_list = []
n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

while n != 0: # 0아닌 것은 다 True 0만 False라는 뜻 (False가 되면 다음으로 넘어감)
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

print(my_list)