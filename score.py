num = input('점수: ')

if num.isdecimal():
  score=int(num)
  if score>100:
    print('입력오류')
  if score>=80:
    print('통과')
  if score>=60:
    print('재시험')
  if score<60:
    print('과락')
else:
  print('숫자를 입력해야합니다')
  
  #if not num.isdecimal():
  #print('숫자를 입력해야 합니다')