
import os.path as Path
import sys

from app import model

from app import view
def list_fun():
    return  {
    '!m':action_show_menu,
    '1':action_find_all,
    '2':action_add,
    '3':action_update,
    '4':action_status,
    '5':action_status,
    '!q':action_exit
    }
#_____________________________________________________________
get_connection= lambda: model.connect('calendar.sqlite')

#____________________________________________________________

def action_add():
    start_data= view.input_start_data()
    end_data = view.input_end_data()
    text= view.input_text()
    with get_connection() as conn:
        task= model.add_task(conn, start_data, end_data, text)
    if not text:
        return
    return task

def action_find_all():
    with get_connection() as conn:
        rows= model.find_all(conn)
    return rows

def action_update ():
    parametr_tela= view.input_update_parametr
    values = view.input_update_values
    with get_connection() as conn:
        mode = model.update(conn)
    s=mode[parametr_tela](values)# защита нужна продумай !!
    return s

def action_status ():
    parametr_tela= view.input_status_parametr
    #values= view.input_status_values
    with get_connection() as conn:
        mode = model.status(conn)# защиат нужна подумай!!!
    s=mode[parametr_tela]()
    return s

def action_show_menu():
    view.output (""" 
    Ежедневник! выбирити задачу:
    1. Вывесте список задач
    2. Добавить Задачу
    3. Отредеактировать задачу
    4. Завершить задачу
    5. Начать задачу сначала
   !q. Выход   
   !m. Меню
    """)

def action_exit():
    sys.exit(0)
#________________________________________________________________________________________________

def creat_shema():
    creation_schema = Path.join(
        Path.dirname(__file__), 'bd.sql')
    with get_connection() as conn:
        model.initialize(conn, creation_schema)

