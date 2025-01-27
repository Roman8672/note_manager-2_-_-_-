#Grade 1. Этап 2: Задание 4

from datetime import datetime
current_date = datetime.now()
formatted_date = "{:%d-%m-%Y}".format(current_date)
def main():
    notes = []

    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

    while True:
        note = {}
        note['name'] = input("Введите имя пользователя: ")
        note['title'] = input("Введите заголовок заметки: ")
        note['contend'] = input("Введите описание заметки: ")
        note['status'] = input("Введите статус заметки (новая, в процессе, выполнено): ")
        note['created_date'] = formatted_date
        note['deadline'] = input("Введите дедлайн (день-месяц-год): ")

        notes.append(note)

        new_note = input("Хотите добавить ещё одну заметку? (да/нет): ")
        if new_note.lower() != 'да':
            break
# вывод информации
    print("\nВаши заметки сохранены:")
    for i, note in enumerate(notes, start=1):
        print(f"\nЗаметка {i}:")
        for key, value in note.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()