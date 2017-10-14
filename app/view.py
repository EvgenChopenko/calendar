# получение данных от пользователя и интерпритация ответа с субд
import os
from datetime import datetime
import sys

from app import modelview


def view():
    modelview.creat_shema()
    #modelview.action_show_menu()
    modelview.action_find_statusfalse()

    list_funs =modelview.list_fun()
    while True:

        s=input("Выберете значение : ")
        #print(sys.platform)
        # if sys.platform == 'win32':
        #     os.system('cls')
        # else:
        #     os.system('clear')#!!!! не знаю рабатоет или нет не успел проверить

        fun=(list_funs.get(s))

        if fun:
            fun()
        else:
            print('неизвестная команда')



# ________________________________________________________________________________________
def output_update_parametr():
    return {
    0: 'Изменить текст',
    1: 'Изменить дату начала',
    2: 'Изменить дату окончания'
    }
def output_update_fun():
    return {
        0:input_text,
        1:input_start_data,
        2:input_end_data

    }
def output_status_parametr():
    return {
    0: 'решен',
    1: 'не решен'
    }

def output_param(param):
    params= '{0}. : {1}'

    for row in param:
        print(params.format(row,param[row]))


#__________________________________________________________________________
def input_status_parametr():
    s=output_status_parametr()
    while True:
        output_param(output_status_parametr())
        pram =input('Выберете действие: ')
        try:
            pram = int(pram)
            if pram < s.__len__():
                return pram
            else:
                print("Выберете команду из списка")

        except ValueError:
            print("Введите целое число занчение")

        except:
            print("Выберете команду из списка")



def input_start_data():
    while True:
        pram = input('Введите дату начала события в формате YYYY-MM-DD: ')
        try:
            deadline = datetime.strptime(pram, "%Y-%m-%d")
            if deadline:
                return deadline
        except:
            print("не правильный формат времни смотри внемательно! YYYY-MM-DD")


def input_end_data():
    while True:
        pram = input('Введите дату завершения события в формате YYYY-MM-DD: ')
        try:
            deadline = datetime.strptime(pram, "%Y-%m-%d")
            if deadline:
                return deadline
        except:
            print("не правильный формат времни смотри внемательно! YYYY-MM-DD")

def input_text():
    while True:
        pram= input("Введите текс на Заметку*: ")
        if pram:
            return pram


def input_update_parametr():
    s =output_update_parametr()
    while True:
        output_param(output_update_parametr())
        pram = input('Выберете действие: ')
        try:
            pram = int(pram)
            if pram < s.__len__():
                return pram
            else:
                print("Выберете команду из списка")

        except ValueError:
            print("Введите целое число занчение")

        except:
            print("Выберете команду из списка")




def input_update_values(parametr_tela):
    func = output_update_fun()
    fun = func.get(parametr_tela)
    return fun()

def input_id():
    while True:
        id = input('Введите номер задачи: ')
        if id == "!m":
            return None
        elif id == '!q':
            modelview.action_exit()
        try:
            id = int(id)
            if id <= modelview.action_find_id() and id >0:
                return int(id)
            else:
                modelview.action_find_all()
                print('Изучити список задач внимательно ! и ведите задачу в которую нужно изменить ')
        except ValueError:
            print("Введите целое число занчение")
        except:
            print("Введите коректный № задачи")

#__________________________________________________________


def output(param):
    print(param)

def output_find_all(param):
    template = '\nЗаметка № {row[id]}. Статус задачи : {row[STATUS]}  \nДата создания : {row[data_create]}\nДата начала : {row[start_data]}\nДата окончания : {row[end_data]}\nПримечание: {row[text]}'

    for row in param:
        if row['STATUS'] == 0:
            row['STATUS'] = "Выполнена"
        elif row['STATUS'] == 1:
            row['STATUS'] = "не выполнена"
        else:
            row['STATUS'] = "не определена"
        print(template.format(row=row ),'\n')
    print("Для отображаения меню введите : '!m'\nДля Выхода введите : '!q'\n" )

#________________________________________________________________________________________________________________________

def error_print():
    print("ошибка выбора функции измения данных БД")
