from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'
        '3. Поиск контакта\n'
        '4. Копирование строки из файла\n'
        '5. Выход из программы')
        command = input('Введите номер действия: ')
        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число команды')
            command = input('Введите номер действия: ')
        if command == '1':
            add_contact()
        if command == '2':
            show_info()
        if command == '3':
            search_contact()
        if command == '4':
            import_data()
        if command == '5':
            print('Всего хорошего!')

