input_number = input('정수 입력 : ')

if not input_number.isdecimal():
  print('숫자를 입력해야 합니다')
else:
  score=int(input_number)
  if score>100:
    print('숫자 범위 오류!!!')
  elif score>=80:
    print('통과!!!')
  elif score>=60:
    print('재시험!!!')
  elif score<60:
    print('과락!!!')