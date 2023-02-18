# Домашняя работа №4
i = int(input('Выберите номер задачи(от 1 до 2): '))
if i == 1:  # Задача №26
    number_a = int(input("Введите первый элемент прогрессии: "))
    number_b = int(input("Введите разность прогрессии: "))
    number_c = int(input("Введите количество элементов прогрессии: "))
    for i in range(number_c):
        print(number_a + i * number_b)
elif i == 2:  # Задача №28
    number_min = int(input("Введите минимум: "))
    number_max = int(input("Введите максимум: "))
    list_min_max = [-6, 0, 5, 8, -4, 2, 9, 0, 3, -7, -3, -8, -4, -1, 1, 0]
    for i in range(len(list_min_max)):
        if number_min <= list_min_max[i] <= number_max:
            print(i)
else:
    print('Неверно введен номер задачи')
