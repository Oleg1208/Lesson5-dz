import os


def save_directory_content():
    """Сохраняет содержимое рабочей директории в файл listdir.txt."""
    files = []
    dirs = []
    for item in os.listdir():
        if os.path.isfile(item):
            files.append(item)
        elif os.path.isdir(item):
            dirs.append(item)

    with open('listdir.txt', 'w') as f:
        f.write('files: ')
        f.write(', '.join(files))
        f.write('dirs: ')
        f.write(', '.join(dirs))