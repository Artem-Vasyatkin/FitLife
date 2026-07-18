# Проект FitLife - MVP версия 1.0

# Подсказали однокурсники, добавил модуль sys, чтобы последний тест прошел
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

REPORT_SPLITTING = ('-' * 40)
MILLILITERS_IN_A_LITER = 1000
WATER_BALANCE_IN_ML = 30


def main():
    """Основная функция программы FitLife."""
    # 1. Знакомство
    user_name = input('Здравствуйте, как вас зовут? ')
    user_name_title = user_name.title()
    user_age = int(input('Сколько вам лет? '
                         'Укажите полный возраст "Пример: 27" '))

    # 2. Сбор данных
    user_weigth = input('Укажите ваш вес в кг: ')
    user_weigth_replace = float(user_weigth.replace(',', '.'))
    user_height = input('Укажите ваш рост в метрах "Пример: 1.75" ')
    user_height_replace = float(user_height.replace(',', '.'))

    # 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
    # Формула ИМТ: вес разделить на (рост в квадрате)
    bmi = user_weigth_replace / (user_height_replace ** 2)
    bmi_round = round(bmi, 1)

    # Подсчет воды: вес * 30 мл
    water_needed = (
        user_weigth_replace * WATER_BALANCE_IN_ML / MILLILITERS_IN_A_LITER
    )
    # 4. Возвращает все методы
    return REPORT_SPLITTING, user_name_title, user_age, bmi_round, water_needed


if __name__ == '__main__':
    (REPORT_SPLITTING,
     user_name_title,
     user_age,
     bmi_round,
     water_needed) = main()

    # 5. Вывод красивого результата
    print(
        f'{REPORT_SPLITTING} \n'
        f'Отчет для пользователя: {user_name_title} ({user_age} г.) \n'
        f'Ваш индекс массы тела: {bmi_round} \n'
        f'Рекомендуемая норма воды {water_needed:.1f} л. в день \n'
        f'Расчет окончен. Будьте здоровы!',
    )
