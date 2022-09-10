from search import *
import var

def number_of_lines(user_file): # подсчёт количества записей в тлф.книге
    with open(user_file, 'r', encoding='utf-8') as book:
        return sum(1 for _ in book)


def last_line(user_file): # вывод последней строки из файла тлф.книги
    with open(user_file, 'r', encoding='utf-8') as book:
        lines = book.read().splitlines()
        return lines[-1]


def add_new_contact(new_contact): # добавление нового контакта в файл тлф.книги
    if number_of_lines(var.book_file) == 0:
        num = 1
    else:
        num = int(last_line(var.book_file).split(var.s_symb)[0]) + 1
    with open(var.book_file, 'a', encoding='utf-8') as book:
        new_contact = str(num) + var.s_symb + new_contact + '\n'
        book.write(new_contact)
    contact_addition_message()
    return new_contact


def add_contact(): # ввод нового контакта -> только через терминал с диалогом
    return add_new_contact(input_contact())[:-2]