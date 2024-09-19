import os
import json

def bank_account():
    # Реализация работы с банковским счетом
    balance = 0  # Начальный баланс
    purchases = []  # Список покупок

    # Проверка наличия файла с балансом
    if os.path.exists('balance.txt'):
        with open('balance.txt', 'r') as f:
            balance = float(f.read())

    # Проверка наличия файла с историей покупок
    if os.path.exists('purchases.json'):
        with open('purchases.json', 'r') as f:
            purchases = json.load(f)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            amount = float(input('Введите сумму пополнения: '))
            balance += amount
            print(f'Счет пополнен на {amount:.2f}. Текущий баланс: {balance:.2f}')

        elif choice == '2':
            amount = float(input('Введите сумму покупки: '))
            if amount > balance:
                print('Недостаточно средств на счете.')
            else:
                name = input('Введите название покупки: ')
                balance -= amount
                purchases.append({'name': name, 'amount': amount})
                print(f'Покупка {name} на сумму {amount:.2f} совершена. Текущий баланс: {balance:.2f}')

        elif choice == '3':
            if purchases:
                print('История покупок:')
                for purchase in purchases:
                    print(f'Название: {purchase["name"]}, Сумма: {purchase["amount"]:.2f}')
            else:
                print('История покупок пуста.')

        elif choice == '4':
            # Сохранение баланса в файл
            with open('balance.txt', 'w') as f:
                f.write(str(balance))
            # Сохранение истории покупок в файл
            with open('purchases.json', 'w') as f:
                json.dump(purchases, f)
            break

        else:
            print('Неверный пункт меню')

    print('До свидания!')