import os
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