import json
from datetime import datetime

# model.py
class NotesModel:
    def __init__(self):
        self.notes = []
        self.file_name = "notes.json"

    def load_notes(self):
        try:
            with open(self.file_name, 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        try:
            with open(self.file_name, 'w') as file:
                json.dump(self.notes, file, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении заметок: {e}")

    def create_note(self, title, body):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "body": body,
            "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.notes.append(note)
        self.save_notes()


    def read_notes(self):
        self.load_notes()
        return [note for note in self.notes]  


    def get_note_by_title(self, title):
        for note in self.notes:
            if note["title"] == title:
                return note
        print("Заметка не найдена.")
        return None

    def edit_note(self, title, new_body):
        note = self.get_note_by_title(title)
        if note:
            note["body"] = new_body
            note["updated_at"] = datetime.now().isoformat()
            self.save_notes()

    def delete_note(self, title):
        note = self.get_note_by_title(title)
        if note:
            self.notes.remove(note)
            self.save_notes()