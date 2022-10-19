'''
format
    {}를 활용하여 데이터의 종류에 상관없이  print문으로 표현이 가능
'''

print("올해는 {}년 입니다. ".format(2022))
print("올해는 {}년, 내년은 {}년 입니다.".format(2022,2023))
print("나는 {}을 공부합니다.".format('지하철'))
print("나는 {}과 {}를 탑니다.".format('지하철', '버스'))
print("나는 %s %s를 탑니다." % ('지하철', '버스'))
print("제가 듣는 수업인 Python은 %c로 시작해서 %c로 끝납니다." %('P', 'c'))

address = '''서울특별시 강남구
테헤란로 123'''
print('주소 : {addr}' .format(addr=address))