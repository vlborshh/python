# Домашняя работа №4
i = int(input('Выберите номер задачи(от 1 до 3): '))

# Задача №22
if i == 1:
    n = int(input("Введите количество элементов в первом множестве: "))
    m = int(input("Введите количество элементов во втором множестве: "))
    set_1 = set()
    set_2 = set()
    for i in range(n):
        set_1.add(input("Введите элемент первого множества: "))
    for i in range(m):
        set_2.add(input("Введите элемент второго множества: "))
    set_1_2 = set_1 & set_2
    result = list(set_1_2)
    result.sort()
    for i in result:
        print(i, end=' ')
elif i == 2:  # Задача №24
    number = int(input("Введите количество кустов: "))
    list_1 = list()
    for i in range(number):
        list_1.append(int(input("Введите количество ягод: ")))
    list_result = list()
    for i in range(len(list_1) - 1):
        list_result.append(list_1[i - 1] + list_1[i] + list_1[i + 1])
    list_result.append(list_1[-2] + list_1[-1] + list_1[0])
    print(f'Результат: {max(list_result)}')
else:
    print('Неверно введен номер задачи')
