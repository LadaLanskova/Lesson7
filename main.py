import os.path

from delete import *
from input import *
from output import *
from logger import *
from message import *
import var

def init_book(): # создание файла тлф.книги при отсутствии
    with open(var.book_file, 'w', encoding='utf-8') as book:
        book.write('')

def get_key(dict, value): # возврат ключа по содержимому значения словаря
    for k, v in dict.items():
        if v == value:
            return k

write_log('program start, ')

if not os.path.isfile(var.log_file): # проверка наличия файла логов (из glv)
    init_log()
    write_log('init_log_file' + var.s_symb + var.log_file + var.s_symb)

if not os.path.isfile(var.book_file): # проверка наличия файла тлф.книги (из glv)
    init_book()
    write_log('init_phone_book_file' + var.s_symb + var.book_file + var.s_symb)

next_action = greetings()

while next_action == '1':
    if number_of_lines(var.book_file) == 0: # проверка на наличие записей в тлф.книге
        message_on_empty_book()
        if continue_or_exit() == '1':
            opers = get_key(var.log_oper, 'add_contact')
        else:
            break
    else:
        opers = operation_selection()
    match opers:
        case 1:
            log_op = var.log_oper[opers] + var.s_symb
            log_op = log_op + output_all() + var.s_symb
            write_log(log_op)
        case 2:
            log_op = var.log_oper[opers] + var.s_symb
            log_op += output_select()
            write_log(log_op)
        case 3:
            log_op = var.log_oper[opers] + var.s_symb
            log_op += add_contact()
            write_log(log_op)
        case 4:
            log_op = var.log_oper[opers] + var.s_symb
            log_op += del_contact()
            write_log(log_op)
    next_action = continue_or_exit()

farewell()

write_log('program shutdown, ')
