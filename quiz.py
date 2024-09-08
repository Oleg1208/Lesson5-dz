def play_quiz():
    # Реализация викторины
    def check_input(prompt, correct_answer):
        """
        Функция для проверки ввода пользователя.

        Args:
            prompt: Текст подсказки для ввода.
            correct_answer: Правильный ответ.

        Returns:
            True, если ввод пользователя верен, иначе False.
        """
        answer = input(prompt)
        return answer == correct_answer

    # Проверка года рождения
    while not check_input('Ввведите год рождения А.С.Пушкина: ', '1799'):
        print("Не верно")

    # Проверка дня рождения
    while not check_input('В какой день июня родился Пушкин? ', '6'):
        print("Не верно")

    print('Верно')