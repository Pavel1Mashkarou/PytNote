import model
import view
import text


def start():
    notes = model.Notes()
    while True:
        select = view.menu()
        match select:
            case 1:
                if notes.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if notes.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_notes(notes.get(),text.empty_notes)
            case 4:
                new_note = view.add_note()
                notes.add_note(new_note)
                view.print_message(text.add_successful(new_note.get('name_note')))
            case 5:
                word = view.view_input(text.search_word)
                result = notes.search(word)
                view.show_notes(result, text.empty_search(word))
            case 6:
                word = view.view_input(text.search_word)
                result = notes.search(word)
                view.show_notes(result, text.empty_search(word))
                index = view.view_input(text.index_update)
                name = notes.update_notes(index,view.update_notes())
                view.print_message(text.update_note(name))
            case 7:
                word = view.view_input(text.search_word)
                result = notes.search(word)
                view.show_notes(result, text.empty_search(word))
                index = view.view_input(text.index_remove)
                name = notes.remove_note(index)
                view.print_message(text.remove_note(name))
            case 8:
                if notes.check_on_exit():
                    answer = view.view_input(text.change_confirm)
                    if answer!= 'n':
                        notes.save_file()
                view.print_message(text.goodbay)
                break
