import os
def create_folder():
    """Создает новую папку в рабочей директории."""
    folder_name = input('Введите название папки: ')
    os.mkdir(folder_name)
    print(f'Папка {folder_name} успешно создана.')