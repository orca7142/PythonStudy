'''

논리 연산자
    관계 연산자와 함게 사용되는 연산자로
    2개 이상의 항을 논리적으로 연결할 때 사용한다.
'''

a = 10
b = 0
print('{} > 0 and {} > 0 : {}'.format(a, b, a > 0 and b>0))
print('{} > 0 or {} > 0 : {}'.format(a, b, a > 0 or b>0))
# 0을 False로 인식 1이상을 True로 인식 (not 이니까 그 반대로 출력됨)
print('not {} :" {}'.format(a, not a))
print('not {} :" {}'.format(b, not b))