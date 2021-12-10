import score1

ban = []

for i in range(5):
  name = input('성명 : ')
  korean = int(input('국어점수 : '))
  english = int(input('영어점수 : '))
  math = int(input('수학점수 : '))
  student = [name, korean, english, math]
  ban.append(student)

for indiv in ban:
  total_score = score1.total(indiv)
  indiv.append(total_score)
  average_score = score1.ave(indiv)
  indiv.append(average_score)
  result = score1.grade(indiv)
  indiv.append(result)
  score1.output(indiv)

print('2명 성적 비교하여 더 좋은 점수의 학생 찾기')
score1.output(score1.max_student(ban[2]))
score1.output(score1.max_student(ban[4]))
print('성적이 더 좋은 학생')
score1.output(score1.max_student(ban[2], ban[4]))

print('3명 성적 비교하여 가장 좋은 점수의 학생 찾기')
score1.output(ban[1])
score1.output(ban[2])
score1.output(ban[3])

print('성적이 가장 좋은 학생')

score1.output(score1.max_student(ban[1], ban[2], ban[3]))