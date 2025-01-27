#Grade 1. Этап 2: Задание 3

# Импортируем необходимые модули для работы с датами
from datetime import datetime
current_date = datetime.now()
formatted_date = "{:%d-%m-%Y}".format(current_date)
print("Текущая дата", formatted_date)

# Основной блок программы
while True:
    try:
        # Запрашиваем дату дедлайна у пользователя

        deadline_str = input("Введите дату дедлайна (в формате день-месяц-год, например 25-12-2024): ")

        # Преобразуем строку с датой в объект datetime
        deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y")

        # Вычисляем разницу между текущей датой и дедлайном
        time_difference = deadline_date - current_date
        days_difference = time_difference.days

        # Проверяем статус дедлайна и выводим соответствующее сообщение
        if days_difference < 0:
            print(f"Внимание! Дедлайн истёк {abs(days_difference):01d} дней назад.")
        elif days_difference == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До дедлайна осталось {days_difference:01d} дней.")

        # Прерываем цикл после успешной обработки даты
        break

    except ValueError:
        # Обработка ошибки неверного формата даты
        print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
        print("Пример: 25-12-2024")

    except Exception as e:
        # Обработка прочих ошибок
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова.")
print(days_difference)