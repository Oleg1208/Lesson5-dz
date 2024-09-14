import os
import pytest
import shutil
from change_directory import change_directory
from create_folder import create_folder
from copy_item import copy_item


@pytest.fixture
def setup_and_teardown(tmp_path):
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    yield tmp_path
    os.chdir(original_dir)


def test_change_directory_success(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr('builtins.input', lambda _: str(tmp_path))
    change_directory()
    captured = capsys.readouterr()
    assert os.getcwd() == str(tmp_path)
    assert f"Рабочая директория изменена на: {tmp_path}" in captured.out


def test_change_directory_failure(monkeypatch, capsys):
    nonexistent_path = '/nonexistent_path'
    monkeypatch.setattr('builtins.input', lambda _: nonexistent_path)
    original_dir = os.getcwd()
    change_directory()
    captured = capsys.readouterr()
    assert os.getcwd() == original_dir
    assert f"Путь {nonexistent_path} не существует." in captured.out


def test_create_folder(monkeypatch, setup_and_teardown, capsys):
    tmp_path = setup_and_teardown
    folder_name = 'test_folder'
    monkeypatch.setattr('builtins.input', lambda _: folder_name)
    create_folder()
    captured = capsys.readouterr()
    assert os.path.exists(tmp_path / folder_name)
    assert f"Папка {folder_name} успешно создана." in captured.out


def test_copy_item_file(monkeypatch, setup_and_teardown, capsys):
    tmp_path = setup_and_teardown
    with open('test.txt', 'w') as f:
        f.write('Test file')
    monkeypatch.setattr('builtins.input',
                        lambda _: 'test.txt' if _ == 'Введите название файла или папки: ' else 'test_copy.txt')

    # Заменяем os.system на shutil.copy
    monkeypatch.setattr('os.system', lambda _: shutil.copy('test.txt', 'test_copy.txt'))

    copy_item()
    captured = capsys.readouterr()
    assert os.path.exists(tmp_path / 'test_copy.txt')
    assert "Файл test.txt скопирован как test_copy.txt." in captured.out


def test_copy_item_folder(monkeypatch, setup_and_teardown, capsys):
    tmp_path = setup_and_teardown
    os.mkdir('test_folder')
    monkeypatch.setattr('builtins.input',
                        lambda _: 'test_folder' if _ == 'Введите название файла или папки: ' else 'test_folder_copy')

    # Заменяем os.system на shutil.copytree
    monkeypatch.setattr('os.system', lambda _: shutil.copytree('test_folder', 'test_folder_copy'))

    copy_item()
    captured = capsys.readouterr()
    assert os.path.exists(tmp_path / 'test_folder_copy')
    assert "Папка test_folder скопирована как test_folder_copy." in captured.out


def test_copy_item_not_found(monkeypatch, setup_and_teardown, capsys):
    monkeypatch.setattr('builtins.input',
                        lambda _: 'nonexistent_item' if _ == 'Введите название файла или папки: ' else 'new_name')
    copy_item()
    captured = capsys.readouterr()
    assert "Файл или папка nonexistent_item не найдены." in captured.out
