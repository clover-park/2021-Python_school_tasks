import datetime
now= datetime.datetime.now()

parking = int(input('차량번호:'))

if now.day % 2 ==0:
  if parking % 2 ==0:
    print('주차 가능')
  elif parking % 2 ==1:
    print('주차 불가능')
#else:

if now.day % 2 ==1:
  if parking % 2 ==1:
    print('주차 가능')
  elif parking % 2 ==0:
    print('주차 불가능')