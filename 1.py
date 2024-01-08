def add_contact():
    pass

def show_info():
    pass

def search_contact():
    pass

def interface():
    command = '-1'
    while command != '4':
        print('Возможные варианты взаимодействия:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'
        '3. Поиск контакта\n'
        '4. Выход из программы')
        command = input('Введите номер действия: ')
        while command not in ('1', '2', '3', '4'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')
        if command == '1':
            add_contact()
        if command == '2':
            show_info()
        if command == '3':
            search_contact()
        if command == '4':
            print('Всего хорошего!')

interface()
