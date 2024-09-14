import platform
from io import StringIO
from quiz import play_quiz
from unittest.mock import patch
from file_manager import show_os_info, show_creator
from bank_account import bank_account


def test_bank_account_replenishment(monkeypatch, capsys):
    test_input = StringIO("1\n100\n4\n")
    monkeypatch.setattr("sys.stdin", test_input)
    bank_account()
    captured = capsys.readouterr()
    assert "Счет пополнен на 100.00. Текущий баланс: 100.00" in captured.out

def test_bank_account_purchase(monkeypatch, capsys):
    test_input = StringIO("1\n100\n2\n50\nПокупка\n4\n")
    monkeypatch.setattr("sys.stdin", test_input)
    bank_account()
    captured = capsys.readouterr()
    assert "Покупка Покупка на сумму 50.00 совершена. Текущий баланс: 50.00" in captured.out

def test_bank_account_purchase_insufficient_funds(monkeypatch, capsys):
    test_input = StringIO("2\n100\n4\n")
    monkeypatch.setattr("sys.stdin", test_input)
    bank_account()
    captured = capsys.readouterr()
    assert "Недостаточно средств на счете." in captured.out

def test_bank_account_purchase_history(monkeypatch, capsys):
    test_input = StringIO("1\n100\n2\n50\nПокупка 1\n2\n50\nПокупка 2\n3\n4\n")
    monkeypatch.setattr("sys.stdin", test_input)
    bank_account()
    captured = capsys.readouterr()
    assert "Название: Покупка 1, Сумма: 50.00" in captured.out
    assert "Название: Покупка 2, Сумма: 50.00" in captured.out

def test_bank_account_empty_purchase_history(monkeypatch, capsys):
    test_input = StringIO("3\n4\n")
    monkeypatch.setattr("sys.stdin", test_input)
    bank_account()
    captured = capsys.readouterr()
    assert "История покупок пуста." in captured.out

def test_play_quiz_correct_answer(monkeypatch, capsys):
    test_input = StringIO("9.09.1828\nвыход\n")
    monkeypatch.setattr("sys.stdin", test_input)
    monkeypatch.setattr("random.sample", lambda *args: ['Лев Толстой'])
    play_quiz()
    captured = capsys.readouterr()
    assert "Правильно!" in captured.out


def test_play_quiz_incorrect_answer(monkeypatch, capsys):
    test_input = StringIO("1.01.1800\nвыход\n")
    monkeypatch.setattr("sys.stdin", test_input)
    monkeypatch.setattr("random.sample", lambda *args: ['Лев Толстой'])
    play_quiz()
    captured = capsys.readouterr()
    assert "Неправильно." in captured.out


def test_play_quiz_exit(monkeypatch, capsys):
    test_input = StringIO("выход\n")
    monkeypatch.setattr("sys.stdin", test_input)
    play_quiz()
    captured = capsys.readouterr()
    assert "Вы вышли из викторины." in captured.out


def test_show_os_info(capsys):
    """Тестирует функцию show_os_info."""
    show_os_info()
    captured = capsys.readouterr()

    assert f'Операционная система: {platform.system()}' in captured.out
    assert f'Версия: {platform.release()}' in captured.out
    assert f'Архитектура: {platform.architecture()[0]}' in captured.out


def test_show_creator():
    # Тест на вывод информации о создателе программы функцией show_creator
    expected_output = "Создатель программы: [Ваше имя]"
    with patch('builtins.print') as mock_print:
        show_creator()
        mock_print.assert_called_once_with(expected_output)
