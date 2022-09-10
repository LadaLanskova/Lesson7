from message import *
import var
import pandas as pd


def output_all():
    return print_output_select(book_to_list())


def print_output_select(contact_list): # вывод списка контактов
    choice = select_output_format()
    match choice:
        case 1:
            string_format(output_to_string(contact_list))
            log_f = var.log_form[choice]
        case 2:
            column_format(contact_list)
            log_f = var.log_form[choice]
    return log_f


def output_to_string(phone_list): # создание словаря из списка для вывода таблицей
    phone_dict = dict()
    for i in range(len(var.title)):
        key = var.title[i]
        column = []
        for j in range(len(phone_list)):
            column.append(phone_list[j][i])
        value = column
        phone_dict[key] = value
    return phone_dict


def string_format(phone_dict): # вывод таблицей - построчный (из словаря)
    print('\n')
    print(pd.DataFrame(phone_dict))


def column_format(phone_list): # вывод в столбец с разделением пустой строкой (из списка)
    print('\n')
    for i in range(len(phone_list)):
        for j in range(len(var.title)):
            print(f'{var.title[j]}: {phone_list[i][j]}')
        print()
