def binary(n):
    a, b = divmod(n, 2)
    binary_list.append(str(b))
    global count
    count += 1
    if a > 0 :
      binary(a)

while True:
  num = int(input('양의 정수 입력(음수입력시 종료): '))
  if num >= 0:
    count = 0
    binary_list = []
    binary(num)
    real_binary = binary_list[::-1]
    print(str(num) +'의 이진수:',''.join(real_binary), end=' ')
    print('binary()함수 반복횟수:', count)
    print()
  else:
    break
