# controller.py
class NotesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_note(self):
        title, body = self.view.get_note_data()
        self.model.create_note(title, body)

    def read_notes(self):
        self.model.load_notes()
        notes = self.model.read_notes()
        self.view.show_notes(notes)

    def edit_note(self):
        title = self.view.get_note_title()
        new_body = self.view.get_note_body()
        self.model.edit_note(title, new_body)

    def delete_note(self):
        title = self.view.get_note_title()
        self.model.delete_note(title)
        

    def view_note(self):
        title = self.view.get_note_title()
        note = self.model.get_note_by_title(title)
        if note:
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Created at: {note['created_at']}")
            print(f"Updated at: {note['updated_at']}")
        else:
            print("Заметка не найдена.")