#Grade 1. Этап 2: Задание 2
print("        Заметки           ")
note = {}
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")

# создание списка заголовков
note["titles"] = []
# Создание заголовков
while True:
    title = input("Введите заголовок (для завершения напишите стоп или оставьте поле пустым): ")
# Завершение сбора заметок и проверка на повторения
    if title.strip() == "стоп" or title == "":
        break
    if title in note["titles"]:
            print(f"Заголовок '{title}' уже существует. Введите другой заголовок.")
            continue

    note["titles"].append(title)


note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
current_status = input("Введите статус заметки. например: 'Активна', 'Выполнена', 'Отложено' - ")
note["created_status"] = [current_status]
print(f"Текущий статус: {current_status}")
print("Для изменения статуса введите число из списка предложенных вариантов")

# Создаём словарь для статусов
statuses = {
    1: "Выполнено",
    2: "Активна",
    3: "Отложено"
}

# Выводим доступные статусы
for key, value in statuses.items():
    print(f"{key}. {value}")

# Создаем список возможных статусов для проверки
status_options = list(statuses.keys())

# Ввод нового статуса
while True:
    try:
        new_status = int(input("Введите число - "))
        if new_status in status_options:
            current_status = statuses[new_status]  # Изменяем статус
            print(f"Статус заметки изменён на: {current_status}")
            break  # Выход из цикла после успешного изменения статуса
        else:
            print("Некорректный статус. Выберите число из списка.")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите число.")


# Вывод информации
print("      Собранная информация о заметке:      ",
      f"Имя пользователя: {note["username"]}",
      sep='\n')
print("Заголовки заметки:")
for title in note["titles"]:
    print("*", title)
print(f"Описание заметки: {note["content"]} ",
      f"Обновлённый статус заметки: {current_status}.",
      #f"Статус заметки: {note["status"]}",
      f"Дата создания заметки: {note["created_date"][0:5]}",
      f"Дата истечения заметки: {note["issue_date"][0:5]}",
      sep='\n')