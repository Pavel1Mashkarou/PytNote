import datetime

import text

def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0<int(select) <= int(len(text.select_menu)):
            return int(select)
        print(text.input_error)

def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message)+'\n')

def add_note():
    new_note = {}
    for key, value in text.new_note.items():
        if key != 'date_note':
            new_note[key] = input(value)
        else:
            new_note[key] = str(datetime.datetime.now(tz=None))
    return new_note

def show_notes(notes: dict[int:dict[str, str]], message):
    if notes:
        max_name_note = []
        max_text_note = []
        max_date_note = []
        for note in notes.values():
            max_name_note.append(len(note.get("name_note")))
            max_text_note.append(len(note.get("text_note")))
            max_date_note.append(len(note.get("date_note")))
        size_name_note = max(max_name_note)
        size_text_note = max(max_text_note)
        size_date_note = max(max_date_note)
        print('\n'+'='*(size_name_note+size_text_note+size_date_note+7))
        notes = dict(sorted(notes.items(), key=lambda item:datetime.datetime.strptime(item[1]['date_note'], '%Y-%m-%d %H:%M:%S.%f'), reverse= True))
        # sorted(d.items(), key=lambda item: item[1]['x'])
        for index, note in notes.items():
            print(f'{index:>3}. Заголовок: {note.get("name_note"):<{size_name_note}}'
                  f' Текст: {note.get("text_note"):<{size_text_note}} '
                  f' Дата создания/изменения: {note.get("date_note"):<{size_date_note}}')
        print('='*(size_name_note+size_text_note+size_date_note+7)+'\n')
    else:
        print_message(message)




def view_input(message: str) -> str:
    return input(message)

def update_notes():
    note = {}
    for key, value in text.new_note.items():
        if key != 'date_note':
            note[key] = input(value)
        else:
            note[key] = str(datetime.datetime.now(tz=None))
    return note

