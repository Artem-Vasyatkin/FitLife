# Проект FitLife - MVP версия 1.0

# Подсказали однокурсники, добавил модуль sys, чтобы последний тест прошел
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# 1. Знакомство
user_name = input('Здравствуйте, как вас зовут?')
user_name_title = user_name.title()
user_age = int(input('Сколько вам лет?'))
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную
# user_age (не забудь преобразовать в число)

user_weigth = float(input('Укажите ваш вес в кг:'))
user_height = float(input('Укажите ваш рост в метрах "Пример: 1.75"'))
# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75)
#  и сохрани в user_height (тип float)

bmi = user_weigth / (user_height ** 2)
bmi_round = round(bmi, 1)
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)

water_needed = user_weigth * 0.03
# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
print("-" * 40)
print(f"Отчет для пользователя: {user_name_title} ({user_age} г.)")
print(f"Ваш индекс массы тела: {bmi_round}")
print(f"Рекомендуемая норма воды {water_needed:.1f} л. в день")
# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести
# приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print("Расчет окончен. Будьте здоровы!")
