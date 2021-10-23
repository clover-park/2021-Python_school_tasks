int_list = []

while True:
  num = int(input('정수 입력 : '))
  if num == 0:
    print(int_list)
    print()
    break
  else:
      int_list.append(num)

reversed_list = reversed(int_list)
print('역순 : ', reversed_list)
print()

i = len(int_list)
insert_num = int(input('삽입 정수 : '))
insert_index = int(input('삽입할 인덱스 : '))
if insert_index > i:
  print('index의 범위에 맞지 않습니다!!')
else:
  int_list.insert(insert_index, insert_num)
print(int_list)
print()

del_num = int(input('삭제할 정수 : '))
if del_num in int_list:
  int_list.remove(del_num)
else:
  print(del_num, '은 존재하지 않습니다!')
print(int_list)
int_list.reverse()
print('역순 : ', int_list)
int_list.sort()
print('정렬 : ', int_list)