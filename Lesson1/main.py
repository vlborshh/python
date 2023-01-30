# Домашняя работа №1
i = int(input('Выберите номер задачи(от 1 до 4): '))

# Найдите сумму цифр трехзначного числа.
if i == 1:
    number = int(input('Введите трехзначное число: '))
    i = 3
    sum = 0
    while i > 0:
        number2 = number % 10
        number = number // 10
        sum = sum + number2
        i = i - 1
    print(sum)
elif i == 2:  # задача про детей
    number = int(input('Введите количество журавликов: '))
    if number % 6 == 0:
        result = False
        count = 0
        while result != True:
            count = count + 1
            if (6 * count) == number:
                result = True
                print(
                    f'Сделано журавликов: Петей {count}, Катей {count*4}, Сережей {count} ')
    else:
        print(f'При значении {number} задача не имеет решения')
elif i == 3:  # задача про счастливый билет
    number = int(input('Введите шестизначный номер билета: '))
    i = 3
    sum1 = 0
    sum2 = 0
    while i > 0:
        number2 = number % 10
        number = number // 10
        sum1 = sum1 + number2
        i = i - 1
    i = 3
    while i > 0:
        number2 = number % 10
        number = number // 10
        sum2 = sum2 + number2
        i = i - 1
    if sum1 == sum2:
        print('Билет счасливый!!!')
    else:
        print('Вам не повезло...')
elif i == 4:  # про шоколадку
    n = int(input('Введите количество долек по горизонтали: '))
    m = int(input('Введите количество долек по вертикали: '))
    k = int(input('Введите количество долек которые хотите отломить: '))
    if m * n > k:
        if k % n == 0 or k % m == 0:
            print('Можно')
        else:
            print('Нельзя')
    else:
        print('Долек которые Вы хотите отломить больше общего их количества!!!')
else:
    print('Неверно введен номер задачи')
