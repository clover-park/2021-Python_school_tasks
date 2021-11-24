with open('students.txt','w') as file:
  for i in range(5):
    name = input('이름 입력 : ')
    mid_score = input('중간고사 점수 :')
    fin_score = input('기말고사 점수 : ')
    file.write('%s, %s, %s \n'%(name, mid_score, fin_score))

print('이름   중간   기말   총점   평균   학점')
file = open('students.txt','r')
while True:
  line = file.readline()
  if not line:
    break
  total_score = int(mid_score) + int(fin_score)
  average = total_score/2
  if average >= 90:
    result = 'A'
  elif average >= 80:
    result = 'B'
  elif average >= 70:
    result = 'C'
  elif average >= 60:
    result = 'D'
  else:
    result = 'F'
  print('%s   %s     %s    %s   %.1f      %s'%(name, mid_score,fin_score, total_score, average, result))
file.close()