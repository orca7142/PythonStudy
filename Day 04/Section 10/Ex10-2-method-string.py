# join() 메쏘드
s = '-'.join('python')
print(s)

s= '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s= ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join({'a': 'appple', 'b': 'banna'})
print(s)

# split()메쏘드 , 문자열을 나눠서 list로 반환을 해준다.
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)
print(result[2]) # 뒷자리 전화번호만 구할때

# replace()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(). rstrip() - (양쪽, 왼쪽, 오른쪽)공백제거
s = '     apple'
print(s)
result = s.lstrip()
print(result)

s = 'apple     '
print(s)
result = s.rstrip()
print(result)

s = '     apple      '
print(s)
result = s.strip()
print(result)

s = ' a p p l e '
print(s)
result = s.replace(' ', '') #양쪽과 사이사이 공백 지우기
print(result)

# 확장
thislist = ['apple', 'banana']
thislist.extend(['cherry', 'mango'])
print(thislist)