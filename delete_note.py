#Grade 1. Этап 2: Задание 5

# Список заметок
notebooks = [
    {
        "username": "Роман",
        "title": "Список покупок",
        "content": "Купить продукты на неделю"
    },
    {
        "username": "Антон",
        "title": "Учеба",
        "content": "Подготовиться к экзамену"
    }
]

def display_notebooks(notebooks):
    print("Текущие заметки:")
    for i, note in enumerate(notebooks, start=1):
        print(f"{i}. Имя: {note['username']}")
        print(f"   Заголовок: {note['title']}")
        print(f"   Описание: {note['content']}\n")

def delete_notes(criteria):
    global notebooks
    initial_count = len(notebooks)
    notebooks = [note for note in notebooks if note['username'] != criteria and note['title'] != criteria]
    if len(notebooks) < initial_count:
        print("Заметка успешно удалена.")

    else:
        print("Заметок с таким именем пользователя или заголовком не найдено.")

def main():
    while True:
        display_notebooks(notebooks)
        criteria = input("Для удаления заметки введите имя пользователя или заголовок : ").strip()
        if not criteria:
            print("Вы должны ввести значение для удаления.")
            continue
        delete_notes(criteria)

if __name__ == "__main__":
     main()