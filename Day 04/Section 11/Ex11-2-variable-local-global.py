'''
지역변수(local)
    함수 내부 선언
    함수 내부에서만 사용가능


전역변수(global)
    함수 외부 선언
    함수 내부 외부 모두 사용가능
'''

gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    print(gVar, '변수 입니다.')  # 전역변수 참조만 하고 있다., 값을 안넣어서
    print(lVar, '변수 입니다.')

globalAndLocal() #함수 출력할 떄는 이렇게 해야하며 , print는 X
# print(lvar) 출력이 안된다.
print(gVar)

gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역' #글로벌을 안썻기 떄문에 지역변수로 바뀜
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndLocal()

print()

# 전역변수 선언
total = 0

def gift(dic, who, money):
    global total # 전역변수 total을 사용하겠다., global을 써야지만 전역변수로 계속 써줄수 있다.
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희', 5) # {'영희': 5}
gift(wedding, '철수', 3) # {'영희': 5, '철수': 3}
gift(wedding, '이모', 10) # {'영희': 5, '철수': 3, '이모', 10}
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))



