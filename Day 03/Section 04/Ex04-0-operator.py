'''

https://velog.io/@taeho8822/PythonBasic-연산자

연산자
    특정한 작업을 수행하기 위해서 사용하는 기호를 의미한다.

연산자 종류
    산술연산자 : +, -, *, **, /, //, %
    대입 연산자 : =, +=, -=, *=, **=, /=, %=
    관계 연산자 : >, >=, <, <=, == (같다), != (같지 않다)
    논리 연산자 : and, or, not
    비트 연산자 : &, |, ^, ~, <<, >>
    기타연산자
        조건연산 : 참 if 조건식  else 거짓
        시퀀스연산 : in, +, *


연산자의 우선순위

1   리플, 튜플, 집합, 딕셔너리
    ex) [값...]. (값...), {값...}, {키:값...}
2   인덱싱, 슬라이싱, 객체, 프로퍼티
    ex) a[0], a[0:3], a.name
3   거듭제곱
    ex) **
4   양의부호, 음의부호
    ex)+a, -a
5   곱셈,나눗셈,몫,나머지
    ex) *, /, //, %
6   덧셈, 뺄셈
    ex) +, -
7   관계 연산자
    ex) >, >=, <, <=, ==, !=
8   논리연산자
    ex) not, and, or 순
11  조건 연산자

암기필요 X 먼저 처리하고 싶은 연산 괄호() 이용
'''