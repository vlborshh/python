import os

os.chdir("lesson8")

print('Телефонный справочник, возможные действия:\n 1. Добавить запись\n 2. Найти запись\n 3. Удалить запись\n 4. Изменить запись\n 5. Выход из программы')


def read_file_for_delete(name_file, number):
    with open(name_file, 'rt', encoding='utf-8') as id_file:
        list_d = id_file.readlines()
        i = number - 1
        k = len(list_d) - 1
        while i < k:
            list_d[i] = list_d[i + 1]
            i += 1
        list_d = list_d[:-1]
    with open(name_file, 'w', encoding='utf-8') as id_file:
        for line in list_d:
            id_file.write(line)


def read_file_for_edit(name_file, number, str_new):
    with open(name_file, 'rt', encoding='utf-8') as id_file:
        list_d = id_file.readlines()
        str_new = str_new + '\n'
        list_d[number - 1] = str_new
    with open(name_file, 'w', encoding='utf-8') as id_file:
        for line in list_d:
            id_file.write(line)


key_exit = True
while key_exit == True:
    i = int(input('Выберите действие: '))
    if i == 1:
        str = input('Введите ФИО: ')
        with open('FIO.txt', 'a', encoding='utf-8') as fio:
            fio.write('\n' + str)
        str = input('Введите адрес прописки: ')
        with open('adress.txt', 'a', encoding='utf-8') as adress:
            adress.write('\n' + str)
        str = input('Введите телефон: ')
        with open('telef.txt', 'a', encoding='utf-8') as telef:
            telef.write('\n' + str)
    elif i == 2:
        str = input('Введите ФИО: ')
        with open('FIO.txt', 'rt', encoding='utf-8') as fio:
            for num, line in enumerate(fio, 1):
                if str in line:
                    number_str = num
                    result_fio = 'ФИО: ' + line.rstrip('\n')
        with open('adress.txt', 'rt', encoding='utf-8') as adress:
            for i, line in enumerate(adress, 1):
                if i == number_str:
                    result_adress = 'Адрес: ' + line.rstrip('\n')
        with open('telef.txt', 'rt', encoding='utf-8') as telef:
            for i, line in enumerate(telef, 1):
                if i == number_str:
                    result_telef = 'Телефон: ' + line.rstrip('\n')
        print(result_fio)
        print(result_telef)
        print(result_adress)
    elif i == 3:
        str = input('Введите ФИО: ')
        with open('FIO.txt', 'rt', encoding='utf-8') as fio:
            for num, line in enumerate(fio, 1):
                if str in line:
                    number_str = num
        read_file_for_delete('FIO.txt', number_str)
        read_file_for_delete('telef.txt', number_str)
        read_file_for_delete('adress.txt', number_str)

        print(f'Запись с фИО {str} удалена')
    elif i == 4:
        str = input('Для нахождения записи введите ФИО: ')

        with open('FIO.txt', 'rt', encoding='utf-8') as fio:
            for num, line in enumerate(fio, 1):
                if str in line:
                    number_str = num

        print('Для изменения записи введите данные:')

        str = input('Введите ФИО: ')
        read_file_for_edit('FIO.txt', number_str, str)
        str = input('Введите адрес прописки: ')
        read_file_for_edit('adress.txt', number_str, str)
        str = input('Введите телефон: ')
        read_file_for_edit('telef.txt', number_str, str)

        print('Запись была изменена')
    elif i == 5:
        key_exit = False
