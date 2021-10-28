questions = (['3+2', 5, 3], ['6/2', 3, 5],
['10-2', 8,3], ['2의 3승', 8, 4],
['5-2*2', 1, 5])
score = 0
correct = 0

for question in questions:
  print(question[0], ': ',end='')
  num = int(input())
  if num == question[1]:
    score += question[2]
    correct += 1

print('정답수 : ', correct)
print('오답수 : ', 5-correct)
print('점  수 : ', score)