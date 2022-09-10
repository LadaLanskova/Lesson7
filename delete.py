from search import *
import var

def del_contact():
    log_d = delete_contact(id_choice())
    contact_deletion_message()
    return log_d

def delete_contact(id):
    cont = var.s_symb.join(choice_by_id(id)) + '\n'
    result_file = ''
    with open(var.book_file, 'r', encoding='utf-8') as book:
        source_file = book.read()
        result_file = source_file.replace(cont, '')
    with open(var.book_file, 'w', encoding='utf-8') as book:
        book.write(result_file)
    return cont[:-2]