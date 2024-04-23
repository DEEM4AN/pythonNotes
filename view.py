# view.py
class NotesView:
    def show_notes(self, notes):
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']} - Created: {note['created_at']}, Updated: {note['updated_at']}")

    def get_note_data(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        return title, body

    def get_note_title(self):
        return input("Введите заголовок заметки: ")

    def get_note_body(self):
        return input("Введите новый текст заметки: ")