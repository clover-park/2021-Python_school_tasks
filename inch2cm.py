input_inch = float(input("inch 입력 : "))
convert2cm = input_inch * 2.54

print("학번 : " + "{:20d}".format(202101318))
print("성명 : " + "{:>20}".format('Clover'))

print('=' * 30)
print(' ' * 5 + "{:08.2f}".format(input_inch),'inch')
print(' ' * 5 + "{:08.2f}".format(convert2cm),'cm')
print('=' * 30)
