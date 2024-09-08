# quiz.py
def play_quiz():
    import random

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
        'Алексей Толстой': '10.01.1883'
    }

    def format_birthday(birthday):
        day, month, year = birthday.split('.')
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                  'ноября',
                  'декабря']
        return f'{int(day)} {months[int(month) - 1]} {year} года'

    def quiz():
        random_people = random.sample(list(birthdays.keys()), 5)
        correct_answers = 0
        wrong_answers = 0

        for person in random_people:
            print(f'Введите дату рождения для {person} (или введите "выход" для завершения):')
            user_answer = input()

            if user_answer.lower() == 'выход':
                print('Вы вышли из викторины.')
                return

            if user_answer == birthdays[person]:
                print('Правильно!')
                correct_answers += 1
            else:
                print(f'Неправильно. Правильный ответ: {format_birthday(birthdays[person])}')
                wrong_answers += 1

        print(f'Количество правильных ответов: {correct_answers}')
        print(f'Количество неправильных ответов: {wrong_answers}')

        play_again = input('Хотите сыграть еще раз? (да/нет):')
        if play_again.lower() == 'да':
            quiz()

    quiz()

    # Реализация викторины
    print('Викторина пока недоступна.')