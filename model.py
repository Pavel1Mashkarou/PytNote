import json


class Notes:
    def __init__(self, path: str = 'notes.json'):
        self.notes: dict = {}
        self.not_changed = {}
        self.path = path


    def get(self, index: int | None = None):
        if index:
            return self.notes.get(index)
        return self.notes

    def open_file(self):
        try:
            with open(self.path,'r',encoding='UTF-8') as file:
                self.notes = json.load(file)
                self.not_changed = self.notes.copy()
            return True
        except:
            return False


    def search(self, word: str) -> dict[int:dict[str,str]]:
        result = {}
        for index, note in self.notes.items():
            if word.lower() in ' '.join(note.values()).lower():
                result[index] = note
        return result

    def check_id(self):
        if self.notes:
            return max(list(map(int, self.notes))) + 1
        return 1

    def add_note(self, new: dict[str,str]):
        note = {self.check_id(): new}
        self.notes.update(note)

    def remove_note(self, index):
        name = self.notes.pop(int(index))
        return name.get('name_note')

    def check_on_exit(self):
        if self.notes == self.not_changed:
            return False
        return True

    def update_notes(self, index, note: dict[str, str]):
        self.notes[index] = note
        return note.get('name_note')

    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.notes, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False






