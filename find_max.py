def find_max(*numbers):
  max = 0
  for num in numbers:
    num = int(num)
    if num > max:
      max = num
  return max


num1 = input('정수 입력 : ')
num2 = input('정수 입력 : ')
num3 = input('정수 입력 : ')
num4 = input('정수 입력 : ')
num5 = input('정수 입력 : ')

print('find_max()=',find_max())
print('find_max('+ num1 + ')=',find_max(num1))
print('find_max('+ num1 + ', ' + num2+ ')' ,find_max(num1,num2))
print('find_max(' + num1 + ', ' + num2 + ', ' + num3 + ')=' ,find_max(num1,num2,num3))
print('find_max(' + num1 + ', ' + num2 + ', ' + num3 + ', ' + num4 + ')=' ,find_max(num1,num2,num3,num4))
print('find_max(' + num1 + ', ' + num2 + ', ' + num3 + ', ' + num4 + ', ' + num5 + ')=', find_max(num1,num2,num3,num4,num5))