# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных 
# в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны 
# находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной з
# аписи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Этапы работы:
# 1) Создать телефонный справочник:
# - Открыть файл в режиме добавления (a)
# 2) Добавить контакт:
# - Запросить информацию у пользователя
# - Подготовить данные в необходимом формате
# - Открыть файл в режиме добавления (a)
# - Добавить контакт в файл
# 3) Вывести данные из файла на экран:
# - Открыть файл в режиме чтения (r)
# - Вывести информацию на экран
# 4) Поиск данных:
# - Запросить вариант поиска
# - Запросить данные поиска
# - Открыть файл в режиме чтения (r)
# - Осуществить поиск по файлу
# - Вывести нужную информацию на экран
# 5) Реализовать UI:
# - Вывести варианты меню
# - Получение запроса пользователя
# - Реализация запроса пользователя
# - Выход из программы


def input_name():
    return input('Введите имя: ')


def input_surname():
    return input('Введите фамилию: ')


def input_patronymic():
    return input('Введите отчество: ')


def input_phone():
    return input('Введите номер телефона: ')


def input_address():
    return input('Введите адрес: ')


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)


def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print(file.read().rstrip())


def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    var_search = input('Выберите вариант поиска: ')

    while var_search not in ('1', '2', '3', '4', '5'):
        print('Некорректные данные, нужно ввести число команды')
        var_search = input('Введите вариант поиска: ')
        
    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)
            
def import_data():
    import os
    
    print('выберите команду:\n'
        '1. Cмотреть общий список контактов\n'
        '2. Копировать строку'  )
    
    var_import = input('Выберите вариант поиска: ')

    while var_import not in ('1', '2'):
        com = '-1'
        print('Некорректные данные, нужно ввести число команды')
        var_import = input('Введите вариант поиска: ')
    if com == '1':
            show_contacts()
    if com == '2':
            copy_string()
            
def show_contacts():            
    with open ('contacts.txt') as inf:
        for line in inf:
            line=line.strip()
            print(line)
        
def copy_string():
    print('введите номер строки, которую необходимо перенести\n')
    n = int(input())
    
    with open('contacts.txt', 'r', encoding='UTF-8') as file:
        s1=a.readline()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(a)


def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'
        '3. Поиск контакта\n'
        '4. Копирование из общего списка контактов\n'
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
            
interface()
