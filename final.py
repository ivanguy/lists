"""Использовано: списки, словари, модуль random, модуль pickle, модуль
 time, работа с файлами. Создание случайой базы, удаление записи и гибкий поиск
"""
import random
import os
import pickle
import time


def search_hard(type_req):
    k = 0
    i = 0
    req = input('Enter {}: '.format(type_req))
    print('='*76)
    for element in base:
        if req in base[i][type_req]:
            print('| № {n:<4}| Name: {name:^11} | Telephone: {number:7} | \
                  Address: {address:^15} |'.format(**base[i]))
            k += 1
            print('='*76)
        i += 1
    print('Results founded:', k)
    print ('='*76)
    back()


def search_gibkiy():
    k = 0
    i = 0
    req = input('Enter information: ')
    print ('='*76)
    for element in base:
        if req in base[i]['name'] or req in base[i]['address'] or \
           req in base[i]['number']:
            print('| № {n:<4}| Name: {name:^11} | Telephone: {number:7} | \
                  Address: {address:^15} |'.format(**base[i]))
            k += 1
            print ('='*76)
        i += 1
    print('Results founded:', k)
    print ('='*76)
    back()


def delete_note(num):
    """Функция удаления записи по номеру"""
    n = len(base) - 1
    if n < 0:
        print('Base is empty')
    else:
        for i in range(num-1, n):
            base[i] = base[i+1]
            base[i]['n'] -= 1
        print('Note successfully deleted!')
    del base[int(len(base))-1]
    back()
    return(n)


def create_new_base(n):
    """Создание случайной базы"""
    tmp_base = []
    i = 1
    for i in range(1, n+1):
        tmp_name = (random.choice (__List_name))
        tmp_street = (random.choice (__List_street)) + ' str.'
        tmp_number = '555' + str(random.randint (123, 900))
        tmp_base.append({'n': i, 'name': tmp_name,
                         'address': tmp_street, 'number': tmp_number})
        i += 1
    print('RANDOM BASE CREATED')
    return tmp_base
    back()


def back():
    """Функция возврата в меню"""
    input('press Enter to back')
    os.system("cls")


random.seed()
base = []
if os.path.exists('DATABASE'):
    file = open('DATABASE', 'rb')
    try:
        base = pickle.load(file)
    except pickle.UnpicklingError:
        print('ERROR! FILE IS DAMAGED! Base is empty!')
        base = []
    finally:
        _kol = len(base)
else:
    file = open('DATABASE', 'wb')
file.close()
empty_file = (len(base) == 0)
__List_name = ('Jacob',	'Emily', 'Michael', 'Emma', 'Joshua', 'Madison',
               'Matthew', 'Olivia', 'Ethan', 'Hannah', 'Andrew', 'Abigail',
               'Daniel', 'Isabella', 'William', 'Ashley', 'Joseph', 'Samantha',
               'Christopher', 'Elizabeth', 'Anthony', 'Alexis', 'Ryan',
               'Sarah', 'Nicholas', 'Grace', 'David', 'Alyssa', 'Alexander',
               'Sophia', 'Tyler', 'Lauren', 'James', 'Brianna', 'John',
               'Kayla', 'Dylan', 'Natalie')
__List_street = ('Green', 'Yellow', 'Seven', 'Central', 'Old')
print("{:$^76}".format(" Hello! It's our DATABASE! "))
if empty_file:
    print('Base is empty!')
    answ = input('Create random base? Yes or No: ')
    answ = answ.upper()
    while answ != 'YES' and answ != 'NO':  # Проверка ввода
        print ('Uncorectable enter')
        answ = input('Create random base? Yes or No:  ')
        answ = answ.upper()
    if answ == 'YES':  # Создание случайной базы
        _kol = int(input('Enter number of notes: '))
        base = create_new_base(_kol)
    elif answ == 'NO':  # Создание пустой базы
        _kol = 0
else:
    file = open('DATABASE', 'rb')
    try:
        base = pickle.load(file)
    except:
        print('ERROR! FILE IS DAMAGER! Base is empty!')
        base = []
    finally:
        _kol = len(base)
        file.close()
answ = 0
Smenu = '{:*^76} \n \
        1 - SHOW ALL NOTES \n \
        2 - ADD NOTE \n \
        3 - DELETE NOTE \n \
        4 - SEARCH \n 5 - CREATE NEW RANDOM TELEPHONE BASE \n \
        6 - EXIT'.format('TELEPHONE DATABASE MENU:')
while answ != 6:
    print(Smenu)
    answ = input('Enter the number: ')
    if answ in ['1', '2', '3', '4', '5', '6']:
        answ = int(answ)
        if answ == 1:  # Просмотр всех записей
            i = 0
            print ('='*76)
            for element in base:
                print('| № {n:<4}| Name: {name:^11} | Telephone: {number:7} | \
                      Address: {address:^15} |'.format(**base[i]))
                print('='*76)
                i += 1
            print('Notes in base: ', _kol)
            print('='*76)
            back()
        elif answ == 2:  # Добавление записи
            _kol += 1
            tmp_name = input('Enter name: ')[:11]
            tmp_number = input('Enter telephone number: ')[:7]
            tmp_street = input('Enter address: ')[:15]
            base.append({'n': _kol, 'name': tmp_name, 'address': tmp_street +
                         ' str.', 'number': tmp_number})
            print('Note successfully added!')
            back()
        elif answ == 3:
            num_del = input('Enter the number of the note you want to delete: ')
            if num_del.isdigit():
                _kol = delete_note(int(num_del))
            else:
                print ('Uncorectable enter')
                back()
        elif answ == 4:  # Поиск
            print ('{:*^76}\n 1 - Search by name\n \
                   2 - Search by telephone number\n \
                   3 - Search by address\n \
                   4 - Search by all categories\n \
                   5 - Back to main menu'.format('SEARCH'))
            variantiPoiska = input('Select operation: ')
            if variantiPoiska == '1':
                search_hard('name')
            elif variantiPoiska == '2':
                search_hard('number')
            elif variantiPoiska == '3':
                search_hard('address')
            elif variantiPoiska == '4':
                search_gibkiy()
            elif variantiPoiska == '5':
                os.system("cls")
            else:
                print('Uncorectable enter')
        elif answ == 5:
            _kol = int(input('Enter number of notes: '))
            base = create_new_base(_kol)
        elif answ == 6:
            print('EXIT')
    else:
        print('Uncorectable enter')
        time.sleep(1)
        os.system("cls")
file = open('DATABASE', 'wb')
pickle.dump(base, file)
file.close()
