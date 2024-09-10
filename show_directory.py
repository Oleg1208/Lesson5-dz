import os
def show_directory():
    """Выводит список всех файлов и папок в рабочей директории."""
    print('Содержимое рабочей директории:')
    for item in os.listdir():
        print(item)
