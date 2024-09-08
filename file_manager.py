import os
import platform

from quiz import play_quiz
from bank_account import bank_account

def create_folder():
    """Создает новую папку в рабочей директории."""
    folder_name = input('Введите название папки: ')
    os.mkdir(folder_name)
    print(f'Папка {folder_name} успешно создана.')

def delete_item():
    """Удаляет файл или папку в рабочей директории."""
    item_name = input('Введите название файла или папки: ')
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            os.rmdir(item_name)
            print(f'Папка {item_name} успешно удалена.')
        else:
            os.remove(item_name)
            print(f'Файл {item_name} успешно удален.')
    else:
        print(f'Файл или папка {item_name} не найдены.')



def copy_item():
    """Копирует файл или папку в рабочей директории."""
    item_name = input('Введите название файла или папки: ')
    new_name = input('Введите новое название: ')
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            os.system(f'cp -r {item_name} {new_name}')
            print(f'Папка {item_name} скопирована как {new_name}.')
        else:
            os.system(f'cp {item_name} {new_name}')
            print(f'Файл {item_name} скопирован как {new_name}.')
    else:
        print(f'Файл или папка {item_name} не найдены.')

def show_directory():
    """Выводит список всех файлов и папок в рабочей директории."""
    print('Содержимое рабочей директории:')
    for item in os.listdir():
        print(item)

def show_folders():
    """Выводит список всех папок в рабочей директории."""
    print('Папки в рабочей директории:')
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

def show_files():
    """Выводит список всех файлов в рабочей директории."""
    print('Файлы в рабочей директории:')
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)

def show_os_info():
    """Выводит информацию об операционной системе."""
    print(f'Операционная система: {platform.system()}')
    print(f'Версия: {platform.release()}')
    print(f'Архитектура: {platform.architecture()[0]}')

def show_creator():
    """Выводит информацию о создателе программы."""
    print('Создатель программы: [Ваше имя]')

def change_directory():
    """Меняет рабочую директорию."""
    new_path = input('Введите новый путь: ')
    if os.path.exists(new_path):
        os.chdir(new_path)
        print(f'Рабочая директория изменена на: {os.getcwd()}')
    else:
        print(f'Путь {new_path} не существует.')

def main():
    """Основная функция программы."""
    while True:
        print('1. Создать папку')
        print('2. Удалить (файл/папку)')
        print('3. Копировать (файл/папку)')
        print('4. Просмотр содержимого рабочей директории')
        print('5. Посмотреть только папки')
        print('6. Посмотреть только файлы')
        print('7. Просмотр информации об операционной системе')
        print('8. Создатель программы')
        print('9. Смена рабочей директории')
        print('10. Выход')
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            create_folder()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            copy_item()
        elif choice == '4':
            show_directory()
        elif choice == '5':
            show_folders()
        elif choice == '6':
            show_files()
        elif choice == '7':
            show_os_info()
        elif choice == '8':
            show_creator()
        elif choice == '9':
            change_directory()
        elif choice == '10':
            break
        else:
            print('Неверный пункт меню.')

if __name__ == '__main__':
    main()