
my_list = []

n = 1 # 0이 아닌 초기값을 주면 반복문이 실행됩니다.

while n != 0: # 0아닌 것은 다 True 0만 False라는 뜻
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_list.append(n)

my_list.pop() # my_list의 마지막 요소는 언제나 0이므로 제거합니다.
print(my_list)