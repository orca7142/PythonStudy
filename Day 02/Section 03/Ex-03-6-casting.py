'''

Casting
    변수에 유형을 지정하려는 경우 캐스팅으로 가능.
'''
# 정수형(정수로만 나오고 실수로 나오진 않음)
x = int(1)
print(x)
y = int(2.8)
print(y)
z = int("3")
print(z)
print(type(z))

# 실수형
x= float(1)
print(x)
z = float("3")
print(z)

# 문자형(문자형이기에 1+2가 3이 아닌 12로 나옴)
x = str(1)
y = str(2)
print(x)
print(type(x))
print(x+y)