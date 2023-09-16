main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать все заметки',
             'Добавить заметку',
             'Найти заметку',
             'Изменить заметку',
             'Удалить заметку',
             'Выход']

select_menu = 'Выберите пункт меню: '
input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu) - 1}: '

load_successful = 'Заметки успешно загружены'
save_successful = 'Заметки успешно сохранены'
error_load = 'Ошибка загрузки заметок'
error_save = 'Ошибка сохранения заметок'

new_note = {'name_note': 'Введите заголовок: ',
               'text_note': 'Введите текст заметки: ',
               'date_note': 'Введите комментарий: '}
search_word = 'Введите строку для поиска: '
def add_successful(name_note: str) -> str:
    return f'Заметка с заголовком {name_note} успешно добавлена!'

empty_notes = 'Заметок нет или они не открыты'

def empty_search(word: str) -> str:
    return f'Заметки содержащие {word} не найдены'

index_update = 'Введите ID заметки, которую хотите изменить: '

def update_note(name_note: str) -> str:
    return f'Заметка с заголовком {name_note} успешна изменена'

index_remove = 'Введите ID контакта, который хотите удалить: '

def remove_note(name_note: str) -> str:
    return f'Заметка с заголовком {name_note} успешно удалена!'

change_confirm = 'У вас есть не сохраненые изменения. Сохранить перед выходом? (y/n)'
goodbay = 'До новых встреч!'
