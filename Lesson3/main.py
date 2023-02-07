# Домашняя работа №3
i = int(input('Выберите номер задачи(от 1 до 3): '))

# Задача №16
if i == 1:
    number = int(input("Введите количество элементов в массиве: "))
    mass = []
    count = 0
    for i in range(number):
        mass.append(int(input("Введите элемент массива: ")))
    number_x = int(input("Введите число для поиска: "))
    print(
        f'Число: {number_x} встречается в массиве {mass.count(number_x)} раз(а)')
    # решение через цикл
    # for i in range(number):
    #     if mass[i] == number_x:
    #         count += 1
    # print(f'Число: {number_x} встречается в массиве {count} раз(а)')
elif i == 2:  # Задача №18
    number = int(input("Введите количество элементов в массиве: "))
    mass = []

    for i in range(number):
        mass.append(int(input("Введите элемент массива: ")))
    number_x = int(
        input("Введите число для поиска самого близкого по величине элемента: "))
    result = mass[0]
    for i in mass:
        if abs(i - number_x) < abs(result - number_x):
            result = i
    print(result)
elif i == 3:  # Задача №20
    import re
    dict_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
               4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
    dict_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
               4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
    str = input("Введите слово для поиска: ")
    str = str.upper()
    sum = 0
    if re.search('[a-zA-Z]', str):
        for i in str:
            for j in dict_en.keys():
                if i in dict_en[j]:
                    sum += j
    else:
        for i in str:
            for j in dict_ru.keys():
                if i in dict_ru[j]:
                    sum += j
    print(sum)
else:
    print('Неверно введен номер задачи')
