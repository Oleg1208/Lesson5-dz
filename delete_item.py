import os
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
