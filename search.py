from message import *
from output import *
import var


def select_position_title(): # возврат номера позиции поиска в списке title
    select_list = ''
    for item in range(len(var.sel_position)):
        select_list = select_list + str(var.sel_position[item]) + '. '
        select_list = select_list + var.title[item] +'\n'
    return select_sign(select_list)


def check_availability_data(num, value): # проверка наличия контактов по запросу
    list_name = name_to_list(num)
    count = 0
    for item in range(len(list_name)):
        if value.lower() in list_name[item].lower() or value.lower() == list_name[item].lower():
            count += 1
    return count


def name_to_list(num):  # формирование списка неповторяющихся значений в тлф.книге
# по заданной позиции поиска из title
    phone_list = book_to_list()
    name_list = [phone_list[0][num]]
    for i in range(1, len(phone_list)):
        if not phone_list[i][num] in name_list:
            name_list.append(phone_list[i][num])
    return name_list


def contact_to_list(num, value):  # список контактов по значению позиции сортировки
        with open(var.book_file, 'r', encoding='utf-8') as book:
            str_list = book.read().split('\n')[:-1]
            contact_list = []
            for item in str_list:
                entry = item.split(var.s_symb)
                if value.lower() == entry[num].lower() or value.lower() in entry[num].lower():
                    contact_list.append(entry)
        return contact_list


def choice_by_id(id): # вывод контакта в список по заданному id
    phone_list = book_to_list()
    for item in range(len(phone_list)):
        if int(phone_list[item][0]) == id:
            contact_list = phone_list[item]
    return contact_list


def output_select():
    sel_pos = select_position_title()
    log_s = var.title[sel_pos] + var.s_symb
    if sel_pos == 0:
        value = str(id_choice())
        log_s = log_s + value + var.s_symb
        log_s = log_s + print_output_select(contact_to_list(0, value)) + var.s_symb
    else:
        av_data = 0
        while av_data == 0:
            value = search_by_input(sel_pos)
            log_s = log_s + value + var.s_symb
            av_data = check_availability_data(sel_pos, value)
            if av_data != 0:
                log_s = log_s + print_output_select(contact_to_list(sel_pos, value)) + var.s_symb
            else:
                act = when_no_search_results()
                if act == 1:
                    av_data = 0
                elif act == 2:
                    name_to_list(sel_pos)
                    next_action = continue_or_exit()
                    if next_action == '1':
                        av_data = 0
                    else:
                        log_s += 'invalid value, the operation was interrupted by the user'
                        av_data = -1
                elif act == 3:
                    log_s += 'invalid value, the operation was interrupted by the user'
                    av_data = -1
    return log_s
