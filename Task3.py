print('Введите число от 0 до 100000')
num = input('Введите число: ')
if num.isdigit() and int(num) < 100000:
    num = int(num)

    if num % 2 != 0 and num != 2:
        i = 3
        while i <= num**0.5:
            if num % i == 0:
                print(f'Число составное, делитель: {i}')
                break

            i += 2
        else:
            print('Число простое')
    else:
        if num == 2:
            print('Число простое')
        else:
            print('Число составное, делитель 2')

else:
    print('Число введено не верно')
