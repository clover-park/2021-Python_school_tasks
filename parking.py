import datetime
now = datetime.datetime.now()

car_number = int(input('차량번호:'))

if now.day % 2 == 0:
  odd_or_even_day = '짝수'
else:
  odd_or_even_day = '홀수'

is_car_number_even = car_number % 2 == 0
is_today_even = now.day % 2 == 0

if is_car_number_even == is_today_even:
  print('오늘은' + ' ' + str(now.day) + '로 ' + odd_or_even_day + '날로 주차 가능합니다.')
else:
  print('오늘은' + ' ' + str(now.day) + '로 ' + odd_or_even_day + '날로 주차 불가능합니다.')