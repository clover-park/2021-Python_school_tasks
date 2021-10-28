students = []

for i in range(3):
  name =  input('이름 :')
  tel = input('전화 :')
  students.append({
    'name' : name,
    'tel' : tel
  })

while True:
  menu = int(input('1. 검색  2.종료 :'))
  if menu < 1 or menu > 2:
    print('잘못된 번호를 입력함!!!')

  elif menu == 1:
    search_name = input('검색할 이름 : ')

    found = False
    for student in students:
      if search_name == student['name']:
        print(student['name'], ':', student['tel'])
        found = True
        break
    if not found:
      print(search_name + '의 전화번호는 저장되어 있지 않습니다!')

  else:
    print('리스트 내용')
    print(students[0], students[1], students[2], sep='\n')
    break
