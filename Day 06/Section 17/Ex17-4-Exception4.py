'''

try:
    코드 작성영역
except:
    예외 발생시 처리영역
else:
    예외가 발생하지 않으면 처리되는 영역
finally:
    언제나 실행되는 영역
'''


try:
    a = int(input('제수를 입력하세요>>> '))
    b = int(input('파제수를 입력하세요>>> '))

    result = a/b

    print('예외 발생해도 실행됩니까?')

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except ValueError:
    print('정수만 입력할 수 있습니다.')
except:
    print('예외가 발생했습니다.')
else: # 예외가 발생하지 않을 때 처리되는 구문
    pritn('{}/ {} = {}'.format(a, b, result))
finally: # 반드시 나오게 해야 할 때만
    print('프로그램을 종료합니다.')

