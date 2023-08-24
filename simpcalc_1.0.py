print('~SimpCalc V1.0~')
a = int(input('Введите первое число: '))
what = input('Выберите действие (+, -, *, /): ')
b = int(input('Введите второе число: '))
if what == '+':
    c = a + b
    print('Результат: ' + str(c))
elif what == '-':
    c = a - b
    print('Результат: ' + str(c))
elif what == '*':
    c = a * b
    print('Результат: ' + str(c))
elif what == '/':
    c = a // b
    print('Результат: ' + str(c))
else:
    print('Выбрана неверная операция!')