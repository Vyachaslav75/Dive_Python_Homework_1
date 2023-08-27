from random import randint
print('Отгадывание чисел от 0 до 1000 за 10 ходов')
print('Хотите загадывать число введите 1')
print('Хотите отгадывать число введите 2')
num = input('Введите вариант: ')
if num.isdigit():
    num = int(num)
    if num == 1:
        print('Загадайте число от 0 до 1000')
        num1=0
        num2=1000
        for i in range(10):
            print(f'Это число  {(num2+num1)//2}')
            print('Если да введите Y')
            print('Если загаданное число меньше введите   <')
            print('Если загаданное число больше введите   >')
            user_in = input('Введите вариант: ')
            if user_in =='Y':
                print('Победа компьютера')
                break
            elif user_in == '<':
                num2=(num2+num1)//2
            elif user_in == '>':
                num1=(num2+num1)//2
            print(f'num1  {num1},  num2  {num2}')
        else:
            print('Вы победили')
    elif num == 2:
        num1=randint(0, 1000)
        print('Компьютер загадал число')
        for i in range(10):
            num2 =  input('Введите свой вариант: ')
            if num2.isdigit():
                num2 = int(num2)
                if num2==num1:
                    print('Вы победили')
                    break
                elif num2>num1:
                    print('Ваше число больше')
                elif num2<num1:
                    print('Ваше число меньше')
            else:
                print('Неверный ввод')
        else:
            print('Ходы закончились')
else:
    print('Число введено не верно')