'''
# import 없이 실행할 수 있는 함수
eval
    매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
'''

expr = input('계산식을 입력하세요 >>> ')
# expr = '2*3'
result = eval(expr)
print(expr + '=' + str(result))