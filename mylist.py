mylist = []

while True:
  print('1. 이름 추가')
  print('2. 이름 삭제')
  print('3. 이름 수정')
  print('4. 종료')
  menu = int(input('메뉴 선택 : '))
  if menu > 4 or menu < 1:
    print('잘못된 번호입니다.')
  elif menu == 1:
    name = input('이름 : ')
    if name not in mylist:
      mylist.append(name)
      print(mylist)
    else:
      print('이미 있는 이름')
  elif menu == 2:
    name = input('이름 : ')
    if name in mylist:
      mylist.remove(name)
      print(mylist)
    else:
      print('해당 이름 없음')
  elif menu == 3:
    name = input('이름 : ')
    if name in mylist:
      new_name = input('새이름 : ')
      i = mylist.index(name)
      mylist.insert(i,new_name)
      mylist.remove(name)
      print(mylist)
    else:
      print('해당 이름 없음')
  elif menu == 4:
    break