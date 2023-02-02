

# Домашняя работа №2
i = int(input('Выберите номер задачи(от 1 до 3): '))

# Задача с монетами.
if i == 1:
    numbers = int(input("Введите количесто монеток: "))
    count = 0
    for i in range(numbers):
        v = int(input("Выберите как лежит монета: орел - 1, решка - 0:"))
        if v == 0:
            count += 1
    if count < numbers/2:
        print(f'Mинимальное количество монет {count}')
    else:
        print(f'Mинимальное количество монет {numbers-count}')
elif i == 2:  # задача про детей
    number_s = int(input("Введите сумму чисел: "))
    number_p = int(input("Введите произведение чисел: "))
    # теорема Виета
    x = (number_s-(number_s**2-4*number_p)**0.5)//2
    y = (number_s+(number_s**2-4*number_p)**0.5)//2
    print(f'Числа равны: {int(x)} и {int(y)}')
    # перебором:
    # count = False
    # i = 0
    # j = 0
    # while i < number_p:
    #     while j < number_p:
    #         if (i * j == number_p) and (i + j == number_s):
    #             print(f'Числа равны {i} и {j}')
    #             count = True
    #             i = number_p + 1
    #             j = number_p + 1
    #         else:
    #             j += 1
    #     i += 1
    #     j = 0
    # if count == False:
    #     print('Задача не имеет решения')

elif i == 3:  # задача про степень двойки
    number = int(input('Введите число "N": '))
    for i in range(number):
        if 2**i <= number:
            print(f'Степень двойки равна {2**i}')
        else:
            i = number + 1
else:
    print('Неверно введен номер задачи')
