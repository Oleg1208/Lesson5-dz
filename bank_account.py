import os
import json


def save_to_file(file_name, data, mode='w'):
    """Декоратор для сохранения данных в файл."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, mode) as f:
                if isinstance(data, dict):
                    json.dump(data, f)
                else:
                    f.write(str(data))
            return result

        return wrapper

    return decorator


@save_to_file('balance.txt', 0)
@save_to_file('purchases.json', [])
def load_data():
    balance = load_balance()
    purchases = load_purchases()
    return balance, purchases


def load_balance():
    try:
        with open('balance.txt', 'r') as f:
            return float(f.read())
    except (FileNotFoundError, ValueError) as e:
        print(f'Ошибка загрузки баланса: {e}')
        return 0


def load_purchases():
    try:
        with open('purchases.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Ошибка загрузки покупок: {e}')
        return []


def bank_account():
    balance, purchases = load_data()

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
            history = (f'Название: {purchase["name"]}, Сумма: {purchase["amount"]:.2f}' for purchase in purchases)
            print('История покупок:')
            print('\n'.join(history) if purchases else 'История покупок пуста.')

        elif choice == '4':
            break

        else:
            print('Неверный пункт меню')

    # Сохранение баланса и истории покупок перед выходом
    try:
        with open('balance.txt', 'w') as f:
            f.write(str(balance))
        with open('purchases.json', 'w') as f:
            json.dump(purchases, f)
    except Exception as e:
        print(f'Ошибка при сохранении данных: {e}')

    print('До свидания!')


if __name__ == '__main__':
    bank_account()
