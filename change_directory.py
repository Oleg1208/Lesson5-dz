import os
def change_directory():
    """Меняет рабочую директорию."""
    new_path = input('Введите новый путь: ')
    if os.path.exists(new_path):
        os.chdir(new_path)
        print(f'Рабочая директория изменена на: {os.getcwd()}')
    else:
        print(f'Путь {new_path} не существует.')