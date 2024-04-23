# main.py
from model import NotesModel
from view import NotesView
from controller import NotesController

def main():
    model = NotesModel()
    view = NotesView()
    controller = NotesController(model, view)

    while True:
        choice = input("1. Создать заметку\n2. Показать заметки\n3. Редактировать заметку\n4. Удалить заметку\n5. Выйти\nВыберите действие: ")

        if choice == "1":
            controller.create_note()
        elif choice == "2":
            controller.read_notes()
        elif choice == "3":
            controller.edit_note()
        elif choice == "4":
            controller.delete_note()
        elif choice == "5":
            break
        elif choice == "6":
            controller.view_note()
        else:
            print("Неправильный выбор")


if __name__ == "__main__":
    main()