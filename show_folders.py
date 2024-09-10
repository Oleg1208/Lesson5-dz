import os
def show_folders():
    """Выводит список всех папок в рабочей директории."""
    print('Папки в рабочей директории:')
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)