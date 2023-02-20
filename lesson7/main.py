
# Домашняя работа №7
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        multiplication_table = []
        for j in range(1, num_columns + 1):
            multiplication_table.append(str(operation(i, j)))
        print("\t".join(multiplication_table))


i = int(input('Выберите номер задачи(от 1 до 2): '))
if i == 1:  # Задача №34
    stroka = input('Введите фразу: ').lower().split()
    list_stroka = [sum(x in 'аоуыэеёиюя' for x in str) for str in stroka]
    if len(set(list_stroka)) == 1:
        result = "Парам пам-пам"
    else:
        result = "Пам парам"
    print(result)
elif i == 2:  # Задача №36
    print_operation_table(lambda x, y: x * y)
else:
    print('Неверно введен номер задачи')
