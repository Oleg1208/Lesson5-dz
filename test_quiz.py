# test_quiz.py
import unittest
from unittest.mock import patch
from io import StringIO
import quiz  # Импорт вашего модуля quiz.py


class TestQuiz(unittest.TestCase):

    @patch('builtins.input', side_effect=['9.09.1828', '30.10.1821', 'выход'])  # Мокаем ввод
    @patch('sys.stdout', new_callable=StringIO)  # Мокаем вывод
    def test_quiz_correct_answers(self, mock_stdout, mock_input):
        quiz.play_quiz()
        output = mock_stdout.getvalue()

        # Проверяем, что ответы правильно обрабатываются
        self.assertIn('Правильно!', output)
        self.assertIn('Вы вышли из викторины.', output)

    @patch('builtins.input', side_effect=['10.10.1828', '30.10.1821', 'выход'])  # Неправильный и правильный ответ
    @patch('sys.stdout', new_callable=StringIO)
    def test_quiz_incorrect_answer(self, mock_stdout, mock_input):
        quiz.play_quiz()
        output = mock_stdout.getvalue()

        # Проверяем, что выводится правильное сообщение для неправильного ответа
        self.assertIn('Неправильно. Правильный ответ:', output)
        self.assertIn('Вы вышли из викторины.', output)

    @patch('builtins.input', side_effect=['выход'])  # Тестируем выход
    @patch('sys.stdout', new_callable=StringIO)
    def test_quiz_exit(self, mock_stdout, mock_input):
        quiz.play_quiz()
        output = mock_stdout.getvalue()

        # Проверяем, что викторина завершилась после ввода "выход"
        self.assertIn('Вы вышли из викторины.', output)


if __name__ == '__main__':
    unittest.main()
