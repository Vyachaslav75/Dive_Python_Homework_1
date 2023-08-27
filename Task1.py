print('Таблица умножения')
for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(4):
            # print(i+k, '*', j+k, '=', i*j, end=' ')
            print(f'{i+k:2} * {j:2} = {(i+k)*j:3}   ', end=' ')
        print()
    print()
