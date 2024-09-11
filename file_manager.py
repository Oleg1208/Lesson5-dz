from change_directory import change_directory
from copy_item import copy_item
from create_folder import create_folder
from delete_item import delete_item
from show_creator import show_creator
from show_directory import show_directory
from show_files import show_files
from show_folders import show_folders
from show_os_info import show_os_info
from bank_account import bank_account
from quiz import play_quiz
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
        print('9. Играть в викторину')
        print('10. Мой банковский счет')
        print('11. Смена рабочей директории')
        print('12. Выход')
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
            play_quiz()
        elif choice == '10':
            bank_account()
        elif choice == '11':
            change_directory()
        elif choice == '12':
            break
        else:
            print('Неверный пункт меню.')

if __name__ == '__main__':
    main()