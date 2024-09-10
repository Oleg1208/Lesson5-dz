import os
def show_files():
    """Выводит список всех файлов в рабочей директории."""
    print('Файлы в рабочей директории:')
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)