'''

복합 대입연산자
    +=
        ex) x += 3 와 x = x + 3 같다
    -=
        ex) x -= 3 과 x = x - 3 같다
'''

piggy_bank = 0
money = 10000
piggy_bank += money # piggy_bank = piggybank + money
print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
print('지금 저금통에는 용돈 {}원이 있습니다.'.format(piggy_bank))

snack = 2000
piggy_bank -= snack
print('저금통에서 스낵 구입비 {}원을 뺏습니다.'.format(snack))
print('지금 저금통에는 용돈 {}원이 있습니다.'.format(piggy_bank))
