# Домашняя работа №4
i = int(input('Выберите номер задачи(от 1 до 2): '))


def stepen(step, count):
    if count == 1:
        return step
    else:
        return step * stepen(step, count - 1)


def result(step, count):
    if step == 0:
        return count
    return result(step - 1, count + 1)


if i == 1:  # Задача №26
    number_a = int(input("Введите первое число: "))
    number_b = int(input("Введите второе число: "))
    print(f'{number_a} в степени {number_b} равно {stepen(number_a, number_b)}')
elif i == 2:  # Задача №28
    number_a = int(input("Введите первое число: "))
    number_b = int(input("Введите второе число: "))
    print(
        f'Сумма чисел {number_a} и {number_b} равна: {result(number_a, number_b)}')
else:
    print('Неверно введен номер задачи')
