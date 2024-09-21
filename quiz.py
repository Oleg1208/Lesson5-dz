# quiz.py

import random


def error_handler(func):
    """Декоратор для обработки исключений."""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Произошла ошибка: {e}')

    return wrapper


def format_birthday(birthday):
    """Форматирует дату рождения."""
    day, month, year = birthday.split('.')
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
              'декабря']
    return f'{int(day)} {months[int(month) - 1]} {year} года'


@error_handler
def quiz(birthdays):
    """Запускает викторину."""
    random_people = random.sample(list(birthdays.keys()), 5)

    correct_answers = 0
    wrong_answers = 0

    for person in random_people:
        user_answer = input(f'Введите дату рождения для {person} (или "выход" для завершения): ').strip()

        if user_answer.lower() == 'выход':
            print('Вы вышли из викторины.')
            return

        correct_answer = birthdays[person]
        correct_answers += (user_answer == correct_answer)
        wrong_answers += (user_answer != correct_answer)

        print(
            'Правильно!' if user_answer == correct_answer else f'Неправильно. Правильный ответ: {format_birthday(correct_answer)}')

    print(f'Количество правильных ответов: {correct_answers}')
    print(f'Количество неправильных ответов: {wrong_answers}')

    # Генератор для повторного запроса
    play_again = (input('Хотите сыграть еще раз? (да/нет): ').lower() == 'да')
    if play_again:
        quiz(birthdays)


@error_handler
def play_quiz():
    """Главная функция для запуска викторины."""
    birthdays = {
        'Лев Толстой': '9.09.1828',
        'Фёдор Достоевский': '30.10.1821',
        'Александр Пушкин': '6.06.1799',
        'Иван Тургенев': '28.10.1818',
        'Антон Чехов': '29.01.1860',
        'Михаил Булгаков': '15.05.1891',
        'Николай Гоголь': '31.03.1809',
        'Владимир Набоков': '22.04.1899',
        'Михаил Лермонтов': '15.10.1814',
        'Алексей Толстой': '10.01.1883',
    }

    # Запускаем викторину
    quiz(birthdays)


if __name__ == '__main__':
    play_quiz()
